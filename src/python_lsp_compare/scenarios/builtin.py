from __future__ import annotations

from dataclasses import dataclass

from .base import Scenario, ScenarioContext


@dataclass(slots=True)
class HoverScenario:
    name: str = "hover"
    description: str = "Open a Python document and request hover info for a method call."

    def run(self, client, context: ScenarioContext) -> None:
        client.did_open(context.document_uri, context.document_text)
        client.hover(context.document_uri, 7, 19)
        client.did_close(context.document_uri)


@dataclass(slots=True)
class CompletionScenario:
    name: str = "completion"
    description: str = "Open a Python document and request completions on an instance."

    def run(self, client, context: ScenarioContext) -> None:
        client.did_open(context.document_uri, context.document_text)
        client.completion(context.document_uri, 7, 18)
        client.did_close(context.document_uri)


@dataclass(slots=True)
class DocumentSymbolsScenario:
    name: str = "document_symbols"
    description: str = "Open a Python document and request document symbols."

    def run(self, client, context: ScenarioContext) -> None:
        client.did_open(context.document_uri, context.document_text)
        client.document_symbols(context.document_uri)
        client.did_close(context.document_uri)


BUILTIN_SCENARIOS: dict[str, Scenario] = {
    "hover": HoverScenario(),
    "completion": CompletionScenario(),
    "document_symbols": DocumentSymbolsScenario(),
}
