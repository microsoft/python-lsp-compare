from __future__ import annotations

import json
import subprocess
import threading
from dataclasses import dataclass
from queue import Queue
from typing import Any, Sequence


class JsonRpcTransportError(RuntimeError):
    """Raised when the stdio JSON-RPC transport fails."""


@dataclass(slots=True)
class JsonRpcResponse:
    payload: dict[str, Any]
    raw_size: int
    request_size: int


class StdioJsonRpcTransport:
    def __init__(self, command: Sequence[str]) -> None:
        if not command:
            raise ValueError("command must not be empty")
        self._command = list(command)
        self._process: subprocess.Popen[bytes] | None = None
        self._pending: dict[int | str, Queue[JsonRpcResponse]] = {}
        self._pending_lock = threading.Lock()
        self._reader_thread: threading.Thread | None = None
        self._stderr_thread: threading.Thread | None = None
        self._closed = threading.Event()
        self._stderr_lines: list[str] = []

    @property
    def stderr_lines(self) -> list[str]:
        return list(self._stderr_lines)

    def start(self) -> None:
        if self._process is not None:
            return
        self._process = subprocess.Popen(
            self._command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self._reader_thread = threading.Thread(target=self._read_stdout_loop, daemon=True)
        self._reader_thread.start()
        self._stderr_thread = threading.Thread(target=self._read_stderr_loop, daemon=True)
        self._stderr_thread.start()

    def close(self) -> None:
        self._closed.set()
        process = self._process
        if process is None:
            return
        if process.stdin is not None and not process.stdin.closed:
            process.stdin.close()
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)
        if process.stdout is not None and not process.stdout.closed:
            process.stdout.close()
        if process.stderr is not None and not process.stderr.closed:
            process.stderr.close()
        self._process = None

    def send_request(self, request_id: int, method: str, params: dict[str, Any], timeout_seconds: float) -> JsonRpcResponse:
        payload = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
            "params": params,
        }
        response_queue: Queue[JsonRpcResponse] = Queue(maxsize=1)
        with self._pending_lock:
            self._pending[request_id] = response_queue
        try:
            request_size = self.send_message(payload)
            try:
                response = response_queue.get(timeout=timeout_seconds)
                response.request_size = request_size
                return response
            except Exception as exc:
                raise TimeoutError(f"Timed out waiting for response to {method}") from exc
        finally:
            with self._pending_lock:
                self._pending.pop(request_id, None)

    def send_notification(self, method: str, params: dict[str, Any]) -> int:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
        }
        return self.send_message(payload)

    def send_message(self, payload: dict[str, Any]) -> int:
        process = self._require_process()
        if process.stdin is None:
            raise JsonRpcTransportError("process stdin is unavailable")
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
        raw = header + body
        process.stdin.write(raw)
        process.stdin.flush()
        return len(raw)

    def _require_process(self) -> subprocess.Popen[bytes]:
        process = self._process
        if process is None:
            raise JsonRpcTransportError("transport has not been started")
        return process

    def _read_stdout_loop(self) -> None:
        process = self._require_process()
        if process.stdout is None:
            return
        try:
            while not self._closed.is_set():
                headers: list[bytes] = []
                while True:
                    line = process.stdout.readline()
                    if not line:
                        return
                    headers.append(line)
                    if line == b"\r\n":
                        break
                content_length = self._parse_content_length(headers)
                body = process.stdout.read(content_length)
                if len(body) != content_length:
                    return
                payload = json.loads(body.decode("utf-8"))
                raw_size = sum(len(item) for item in headers) + len(body)
                if "id" in payload and ("result" in payload or "error" in payload):
                    self._dispatch_response(payload, raw_size)
        finally:
            self._closed.set()

    def _read_stderr_loop(self) -> None:
        process = self._require_process()
        if process.stderr is None:
            return
        while not self._closed.is_set():
            line = process.stderr.readline()
            if not line:
                return
            self._stderr_lines.append(line.decode("utf-8", errors="replace").rstrip())

    def _dispatch_response(self, payload: dict[str, Any], raw_size: int) -> None:
        with self._pending_lock:
            queue = self._pending.get(payload["id"])
        if queue is not None:
            queue.put(JsonRpcResponse(payload=payload, raw_size=raw_size, request_size=0))

    @staticmethod
    def _parse_content_length(header_lines: list[bytes]) -> int:
        for line in header_lines:
            if line.lower().startswith(b"content-length:"):
                _, value = line.split(b":", 1)
                return int(value.strip())
        raise JsonRpcTransportError("missing Content-Length header")
