from __future__ import annotations

import json
import sys
import threading
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from python_lsp_compare.transport import StdioJsonRpcTransport


class _InterleavingPipe:
    def __init__(self) -> None:
        self._buffer = bytearray()

    def write(self, data: bytes) -> int:
        for byte in data:
            self._buffer.append(byte)
            time.sleep(0.00001)
        return len(data)

    def flush(self) -> None:
        return None

    def getvalue(self) -> bytes:
        return bytes(self._buffer)


class _FakeProcess:
    def __init__(self) -> None:
        self.stdin = _InterleavingPipe()
        self.stdout = None
        self.stderr = None


class TransportTests(unittest.TestCase):
    def test_send_message_serializes_concurrent_writes(self) -> None:
        transport = StdioJsonRpcTransport([sys.executable])
        transport._process = _FakeProcess()
        barrier = threading.Barrier(3)

        def send(method: str, request_id: int) -> None:
            barrier.wait()
            transport.send_message({"jsonrpc": "2.0", "id": request_id, "method": method})

        first = threading.Thread(target=send, args=("alpha", 1))
        second = threading.Thread(target=send, args=("beta", 2))
        first.start()
        second.start()
        barrier.wait()
        first.join(timeout=2)
        second.join(timeout=2)

        self.assertFalse(first.is_alive())
        self.assertFalse(second.is_alive())

        payloads = self._parse_payloads(transport._process.stdin.getvalue())
        self.assertEqual(len(payloads), 2)
        self.assertEqual({payload["method"] for payload in payloads}, {"alpha", "beta"})

    def _parse_payloads(self, raw: bytes) -> list[dict[str, object]]:
        payloads: list[dict[str, object]] = []
        remaining = raw
        while remaining:
            header, separator, rest = remaining.partition(b"\r\n\r\n")
            self.assertEqual(separator, b"\r\n\r\n")
            content_length = None
            for line in header.split(b"\r\n"):
                if line.lower().startswith(b"content-length:"):
                    _, value = line.split(b":", 1)
                    content_length = int(value.strip())
                    break
            self.assertIsNotNone(content_length)
            assert content_length is not None
            body = rest[:content_length]
            self.assertEqual(len(body), content_length)
            payloads.append(json.loads(body.decode("utf-8")))
            remaining = rest[content_length:]
        return payloads


if __name__ == "__main__":
    unittest.main()
