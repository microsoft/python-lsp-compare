from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from python_lsp_compare.lsp_client import LspClient


SAMPLE_SOURCE = '''class Greeter:
    def greet(self, name: str) -> str:
        return f"Hello, {name}!"


def build_message() -> str:
    greeter = Greeter()
    return greeter.greet("world")


build_message()
'''


@dataclass(slots=True)
class ScenarioContext:
    workspace_path: Path
    document_path: Path
    document_uri: str
    document_text: str = SAMPLE_SOURCE


class Scenario(Protocol):
    name: str
    description: str

    def run(self, client: LspClient, context: ScenarioContext) -> None:
        ...
