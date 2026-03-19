from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Sequence

from .metrics import CallMetric, build_call_metric
from .transport import StdioJsonRpcTransport


class LspClient:
    def __init__(self, command: Sequence[str], timeout_seconds: float = 10.0) -> None:
        self._transport = StdioJsonRpcTransport(command)
        self._timeout_seconds = timeout_seconds
        self._next_request_id = 1
        self._metrics: list[CallMetric] = []

    @property
    def metrics(self) -> list[CallMetric]:
        return list(self._metrics)

    @property
    def stderr_lines(self) -> list[str]:
        return self._transport.stderr_lines

    def start(self) -> None:
        self._transport.start()

    def close(self) -> None:
        self._transport.close()

    def initialize(self, workspace_path: Path) -> dict[str, Any] | None:
        return self.request(
            "initialize",
            {
                "processId": None,
                "clientInfo": {"name": "python-lsp-compare", "version": "0.1.0"},
                "rootUri": workspace_path.as_uri(),
                "capabilities": {
                    "textDocument": {
                        "hover": {"dynamicRegistration": False},
                        "completion": {"dynamicRegistration": False},
                        "documentSymbol": {"dynamicRegistration": False},
                    }
                },
                "workspaceFolders": [
                    {"uri": workspace_path.as_uri(), "name": workspace_path.name}
                ],
            },
        )

    def initialized(self) -> None:
        self.notify("initialized", {})

    def shutdown(self) -> dict[str, Any] | None:
        return self.request("shutdown", {})

    def exit(self) -> None:
        self.notify("exit", {})

    def did_open(
        self,
        uri: str,
        text: str,
        language_id: str = "python",
        version: int = 1,
        context: dict[str, Any] | None = None,
    ) -> None:
        self.notify(
            "textDocument/didOpen",
            {
                "textDocument": {
                    "uri": uri,
                    "languageId": language_id,
                    "version": version,
                    "text": text,
                }
            },
            context=context,
        )

    def did_close(self, uri: str, context: dict[str, Any] | None = None) -> None:
        self.notify("textDocument/didClose", {"textDocument": {"uri": uri}}, context=context)

    def hover(self, uri: str, line: int, character: int, context: dict[str, Any] | None = None) -> Any:
        return self.request(
            "textDocument/hover",
            {"textDocument": {"uri": uri}, "position": {"line": line, "character": character}},
            context=context,
        )

    def completion(self, uri: str, line: int, character: int, context: dict[str, Any] | None = None) -> Any:
        return self.request(
            "textDocument/completion",
            {
                "textDocument": {"uri": uri},
                "position": {"line": line, "character": character},
                "context": {"triggerKind": 1},
            },
            context=context,
        )

    def document_symbols(self, uri: str, context: dict[str, Any] | None = None) -> Any:
        return self.request("textDocument/documentSymbol", {"textDocument": {"uri": uri}}, context=context)

    def definition(self, uri: str, line: int, character: int, context: dict[str, Any] | None = None) -> Any:
        return self.request(
            "textDocument/definition",
            {"textDocument": {"uri": uri}, "position": {"line": line, "character": character}},
            context=context,
        )

    def references(self, uri: str, line: int, character: int, context: dict[str, Any] | None = None) -> Any:
        return self.request(
            "textDocument/references",
            {
                "textDocument": {"uri": uri},
                "position": {"line": line, "character": character},
                "context": {"includeDeclaration": True},
            },
            context=context,
        )

    def request(self, method: str, params: dict[str, Any], context: dict[str, Any] | None = None) -> Any:
        request_id = self._next_request_id
        self._next_request_id += 1
        started_at = time.time()
        started_perf = time.perf_counter()
        response = self._transport.send_request(request_id, method, params, timeout_seconds=self._timeout_seconds)
        duration_ms = (time.perf_counter() - started_perf) * 1000
        payload = response.payload
        bytes_sent = response.request_size
        if "error" in payload:
            self._metrics.append(
                build_call_metric(
                    kind="request",
                    method=method,
                    duration_ms=duration_ms,
                    success=False,
                    started_at_unix=started_at,
                    bytes_sent=bytes_sent,
                    bytes_received=response.raw_size,
                    request_id=request_id,
                    error=payload["error"],
                    context=context,
                )
            )
            raise RuntimeError(f"{method} failed: {payload['error']}")
        self._metrics.append(
            build_call_metric(
                kind="request",
                method=method,
                duration_ms=duration_ms,
                success=True,
                started_at_unix=started_at,
                bytes_sent=bytes_sent,
                bytes_received=response.raw_size,
                request_id=request_id,
                result=payload.get("result"),
                context=context,
            )
        )
        return payload.get("result")

    def notify(self, method: str, params: dict[str, Any], context: dict[str, Any] | None = None) -> None:
        started_at = time.time()
        started_perf = time.perf_counter()
        bytes_sent = self._transport.send_notification(method, params)
        duration_ms = (time.perf_counter() - started_perf) * 1000
        self._metrics.append(
            build_call_metric(
                kind="notification",
                method=method,
                duration_ms=duration_ms,
                success=True,
                started_at_unix=started_at,
                bytes_sent=bytes_sent,
                bytes_received=0,
                context=context,
            )
        )
