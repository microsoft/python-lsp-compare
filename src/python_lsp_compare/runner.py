from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path
from typing import Sequence

from .lsp_client import LspClient
from .metrics import RunReport, ScenarioReport
from .scenarios.base import SAMPLE_SOURCE, ScenarioContext
from .scenarios.builtin import BUILTIN_SCENARIOS


def run_scenarios(
    command: Sequence[str],
    scenario_names: Sequence[str] | None = None,
    timeout_seconds: float = 10.0,
) -> RunReport:
    selected_names = list(scenario_names or BUILTIN_SCENARIOS.keys())
    unknown = [name for name in selected_names if name not in BUILTIN_SCENARIOS]
    if unknown:
        raise ValueError(f"Unknown scenarios: {', '.join(unknown)}")

    started_at = time.time()
    scenario_reports: list[ScenarioReport] = []
    for name in selected_names:
        scenario = BUILTIN_SCENARIOS[name]
        scenario_reports.append(_run_single_scenario(command, scenario, timeout_seconds))

    return RunReport(
        server_command=list(command),
        requested_scenarios=selected_names,
        started_at_unix=started_at,
        finished_at_unix=time.time(),
        scenario_reports=scenario_reports,
    )


def write_report(report: RunReport, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")


def _run_single_scenario(command: Sequence[str], scenario, timeout_seconds: float) -> ScenarioReport:
    started_perf = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="python-lsp-compare-") as temp_dir:
        workspace_path = Path(temp_dir)
        document_path = workspace_path / "sample.py"
        document_path.write_text(SAMPLE_SOURCE, encoding="utf-8")
        context = ScenarioContext(
            workspace_path=workspace_path,
            document_path=document_path,
            document_uri=document_path.as_uri(),
        )
        client = LspClient(command, timeout_seconds=timeout_seconds)
        client.start()
        error_message: str | None = None
        success = False
        try:
            client.initialize(workspace_path)
            client.initialized()
            scenario.run(client, context)
            client.shutdown()
            success = True
        except Exception as exc:
            error_message = str(exc)
        finally:
            try:
                client.exit()
            except Exception:
                pass
            client.close()
        if client.stderr_lines and error_message is not None:
            error_message = f"{error_message}\n--- server stderr ---\n" + "\n".join(client.stderr_lines)
        return ScenarioReport(
            name=scenario.name,
            description=scenario.description,
            success=success,
            total_duration_ms=(time.perf_counter() - started_perf) * 1000,
            metrics=client.metrics,
            error_message=error_message,
        )
