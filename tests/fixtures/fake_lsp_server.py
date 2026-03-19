from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--write-env")
    return parser.parse_args()


def read_message() -> dict[str, Any] | None:
    headers: list[bytes] = []
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        headers.append(line)
        if line == b"\r\n":
            break
    content_length = None
    for line in headers:
        if line.lower().startswith(b"content-length:"):
            content_length = int(line.split(b":", 1)[1].strip())
            break
    if content_length is None:
        raise RuntimeError("missing content length")
    body = sys.stdin.buffer.read(content_length)
    return json.loads(body.decode("utf-8"))


def write_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    sys.stdout.buffer.write(header + body)
    sys.stdout.buffer.flush()


def handle_request(message: dict[str, Any]) -> dict[str, Any] | None:
    request_id = message.get("id")
    method = message.get("method")
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "capabilities": {
                    "hoverProvider": True,
                    "completionProvider": {"resolveProvider": False, "triggerCharacters": ["."]},
                    "documentSymbolProvider": True,
                }
            },
        }
    if method == "shutdown":
        return {"jsonrpc": "2.0", "id": request_id, "result": None}
    if method == "textDocument/hover":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {"contents": {"kind": "plaintext", "value": "Fake hover"}},
        }
    if method == "textDocument/completion":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {"isIncomplete": False, "items": [{"label": "greet", "kind": 2}]},
        }
    if method == "textDocument/documentSymbol":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": [
                {
                    "name": "Greeter",
                    "kind": 5,
                    "range": {
                        "start": {"line": 0, "character": 0},
                        "end": {"line": 2, "character": 0},
                    },
                    "selectionRange": {
                        "start": {"line": 0, "character": 0},
                        "end": {"line": 0, "character": 7},
                    },
                }
            ],
        }
    if method == "textDocument/definition":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "uri": message["params"]["textDocument"]["uri"],
                "range": {
                    "start": {"line": 0, "character": 0},
                    "end": {"line": 0, "character": 7},
                },
            },
        }
    if method == "textDocument/references":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": [
                {
                    "uri": message["params"]["textDocument"]["uri"],
                    "range": {
                        "start": {"line": 0, "character": 0},
                        "end": {"line": 0, "character": 7},
                    },
                }
            ],
        }
    return {"jsonrpc": "2.0", "id": request_id, "result": None}


def main() -> int:
    args = parse_args()
    if args.write_env:
        with open(args.write_env, "w", encoding="utf-8") as handle:
            json.dump(
                {
                    "sys_executable": sys.executable,
                    "virtual_env": os.environ.get("VIRTUAL_ENV"),
                    "path": os.environ.get("PATH", ""),
                },
                handle,
                indent=2,
            )
    while True:
        message = read_message()
        if message is None:
            return 0
        response = handle_request(message)
        if response is not None:
            write_message(response)
        if message.get("method") == "exit":
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
