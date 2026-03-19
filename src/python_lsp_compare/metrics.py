from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


def _truncate(value: Any, limit: int = 160) -> str | None:
    if value is None:
        return None
    text = repr(value)
    if len(text) <= limit:
        return text
    return f"{text[: limit - 3]}..."


@dataclass(slots=True)
class CallMetric:
    kind: str
    method: str
    duration_ms: float
    success: bool
    started_at_unix: float
    bytes_sent: int
    bytes_received: int
    request_id: int | str | None = None
    error_code: int | None = None
    error_message: str | None = None
    result_preview: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ScenarioReport:
    name: str
    description: str
    success: bool
    total_duration_ms: float
    metrics: list[CallMetric] = field(default_factory=list)
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "success": self.success,
            "total_duration_ms": self.total_duration_ms,
            "error_message": self.error_message,
            "metrics": [metric.to_dict() for metric in self.metrics],
        }


@dataclass(slots=True)
class RunReport:
    server_command: list[str]
    requested_scenarios: list[str]
    started_at_unix: float
    finished_at_unix: float
    scenario_reports: list[ScenarioReport]

    def to_dict(self) -> dict[str, Any]:
        return {
            "server_command": self.server_command,
            "requested_scenarios": self.requested_scenarios,
            "started_at_unix": self.started_at_unix,
            "finished_at_unix": self.finished_at_unix,
            "scenario_reports": [report.to_dict() for report in self.scenario_reports],
        }


def build_call_metric(
    *,
    kind: str,
    method: str,
    duration_ms: float,
    success: bool,
    started_at_unix: float,
    bytes_sent: int,
    bytes_received: int,
    request_id: int | str | None = None,
    error: dict[str, Any] | None = None,
    result: Any = None,
) -> CallMetric:
    return CallMetric(
        kind=kind,
        method=method,
        duration_ms=duration_ms,
        success=success,
        started_at_unix=started_at_unix,
        bytes_sent=bytes_sent,
        bytes_received=bytes_received,
        request_id=request_id,
        error_code=None if error is None else error.get("code"),
        error_message=None if error is None else error.get("message"),
        result_preview=_truncate(result),
    )
