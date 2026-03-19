from __future__ import annotations

import json
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Sequence

from .benchmark_suites import BenchmarkPoint, BenchmarkSuite, discover_benchmark_suites
from .lsp_client import LspClient
from .metrics import BenchmarkPointReport, BenchmarkSuiteReport, CallMetric, RunReport, ScenarioReport
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
        requested_benchmarks=[],
        started_at_unix=started_at,
        finished_at_unix=time.time(),
        scenario_reports=scenario_reports,
        benchmark_reports=[],
    )


def run_benchmarks(
    command: Sequence[str],
    benchmark_names: Sequence[str] | None = None,
    timeout_seconds: float = 10.0,
    benchmark_root: Path | None = None,
    install_requirements: bool = False,
    python_executable: str | None = None,
) -> RunReport:
    suites = discover_benchmark_suites(benchmark_root)
    selected_names = list(benchmark_names or suites.keys())
    unknown = [name for name in selected_names if name not in suites]
    if unknown:
        raise ValueError(f"Unknown benchmarks: {', '.join(unknown)}")

    started_at = time.time()
    benchmark_reports = [
        _run_single_benchmark_suite(
            command=command,
            suite=suites[name],
            timeout_seconds=timeout_seconds,
            install_requirements=install_requirements,
            python_executable=python_executable or sys.executable,
        )
        for name in selected_names
    ]
    return RunReport(
        server_command=list(command),
        requested_scenarios=[],
        requested_benchmarks=selected_names,
        started_at_unix=started_at,
        finished_at_unix=time.time(),
        scenario_reports=[],
        benchmark_reports=benchmark_reports,
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
            summary=_summarize_metrics(client.metrics),
        )


def _run_single_benchmark_suite(
    *,
    command: Sequence[str],
    suite: BenchmarkSuite,
    timeout_seconds: float,
    install_requirements: bool,
    python_executable: str,
) -> BenchmarkSuiteReport:
    started_perf = time.perf_counter()
    if install_requirements:
        _install_suite_requirements(suite, python_executable)

    client = LspClient(command, timeout_seconds=timeout_seconds)
    client.start()
    error_message: str | None = None
    point_reports: list[BenchmarkPointReport] = []
    success = True
    try:
        client.initialize(suite.workspace_dir)
        client.initialized()
        opened = _open_benchmark_documents(client, suite)
        try:
            for method, points in suite.points_by_method.items():
                for point in points:
                    point_reports.append(
                        _run_benchmark_point(
                            client=client,
                            suite=suite,
                            method=method,
                            point=point,
                        )
                    )
        finally:
            for uri in reversed(opened):
                client.did_close(uri,)
        client.shutdown()
        success = all(point.success for point in point_reports)
    except Exception as exc:
        success = False
        error_message = str(exc)
    finally:
        try:
            client.exit()
        except Exception:
            pass
        client.close()
    if client.stderr_lines and error_message is not None:
        error_message = f"{error_message}\n--- server stderr ---\n" + "\n".join(client.stderr_lines)
    return BenchmarkSuiteReport(
        name=suite.name,
        description=suite.description,
        workspace_dir=str(suite.workspace_dir),
        requirements_file=None if suite.requirements_file is None else str(suite.requirements_file),
        install_packages=suite.install_packages,
        success=success,
        total_duration_ms=(time.perf_counter() - started_perf) * 1000,
        points=point_reports,
        metrics=client.metrics,
        error_message=error_message,
        summary=_summarize_benchmark_suite(point_reports, client.metrics),
    )


def _run_benchmark_point(
    *,
    client: LspClient,
    suite: BenchmarkSuite,
    method: str,
    point: BenchmarkPoint,
) -> BenchmarkPointReport:
    metrics: list[CallMetric] = []
    error_message: str | None = None
    success = True
    uri = point.file_path.as_uri()
    for iteration in range(suite.warmup_iterations + suite.iterations):
        is_warmup = iteration < suite.warmup_iterations
        before = len(client.metrics)
        context = {
            "suite": suite.name,
            "label": point.label,
            "file_path": str(point.file_path),
            "line": point.line,
            "character": point.character,
            "phase": "warmup" if is_warmup else "measured",
            "iteration": iteration + 1 if is_warmup else iteration - suite.warmup_iterations + 1,
        }
        try:
            _dispatch_benchmark_request(client, method, uri, point.line, point.character, context)
        except Exception as exc:
            success = False
            error_message = str(exc)
            break
        metrics.extend(client.metrics[before:])

    measured_metrics = [metric for metric in metrics if metric.context.get("phase") == "measured" and metric.kind == "request"]
    return BenchmarkPointReport(
        label=point.label,
        method=method,
        file_path=str(point.file_path),
        line=point.line,
        character=point.character,
        success=success,
        warmup_iterations=suite.warmup_iterations,
        measured_iterations=suite.iterations,
        metrics=metrics,
        summary=_summarize_metrics(measured_metrics),
        error_message=error_message,
    )


def _dispatch_benchmark_request(
    client: LspClient,
    method: str,
    uri: str,
    line: int,
    character: int,
    context: dict[str, object],
) -> object:
    if method == "textDocument/hover":
        return client.hover(uri, line, character, context=context)
    if method == "textDocument/completion":
        return client.completion(uri, line, character, context=context)
    if method == "textDocument/documentSymbol":
        return client.document_symbols(uri, context=context)
    if method == "textDocument/definition":
        return client.definition(uri, line, character, context=context)
    if method == "textDocument/references":
        return client.references(uri, line, character, context=context)
    raise ValueError(f"Unsupported benchmark method: {method}")


def _open_benchmark_documents(client: LspClient, suite: BenchmarkSuite) -> list[str]:
    opened: list[str] = []
    seen: set[str] = set()
    for points in suite.points_by_method.values():
        for point in points:
            uri = point.file_path.as_uri()
            if uri in seen:
                continue
            seen.add(uri)
            client.did_open(uri, point.file_path.read_text(encoding="utf-8"), context={"suite": suite.name, "phase": "setup"})
            opened.append(uri)
    return opened


def _install_suite_requirements(suite: BenchmarkSuite, python_executable: str) -> None:
    commands: list[list[str]] = []
    if suite.requirements_file is not None and suite.requirements_file.exists():
        commands.append([python_executable, "-m", "pip", "install", "-r", str(suite.requirements_file)])
    if suite.install_packages:
        commands.append([python_executable, "-m", "pip", "install", *suite.install_packages])
    for command in commands:
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or f"pip install failed for {suite.name}")


def _summarize_benchmark_suite(points: Sequence[BenchmarkPointReport], metrics: Sequence[CallMetric]) -> dict[str, object]:
    summary = _summarize_metrics(metrics)
    by_method: dict[str, dict[str, object]] = {}
    for point in points:
        current = by_method.setdefault(point.method, {"point_count": 0, "durations_ms": []})
        current["point_count"] = int(current["point_count"]) + 1
        current["durations_ms"].extend(metric.duration_ms for metric in point.metrics if metric.context.get("phase") == "measured")
    summary["by_method"] = {
        method: _summarize_values(value["durations_ms"], extra={"point_count": value["point_count"]})
        for method, value in by_method.items()
    }
    return summary


def _summarize_metrics(metrics: Sequence[CallMetric]) -> dict[str, object]:
    request_metrics = [metric for metric in metrics if metric.kind == "request"]
    durations = [metric.duration_ms for metric in request_metrics]
    return _summarize_values(
        durations,
        extra={
            "request_count": len(request_metrics),
            "notification_count": len([metric for metric in metrics if metric.kind == "notification"]),
            "success_count": len([metric for metric in request_metrics if metric.success]),
            "failure_count": len([metric for metric in request_metrics if not metric.success]),
            "bytes_sent": sum(metric.bytes_sent for metric in metrics),
            "bytes_received": sum(metric.bytes_received for metric in metrics),
        },
    )


def _summarize_values(values: Sequence[float], extra: dict[str, object] | None = None) -> dict[str, object]:
    summary: dict[str, object] = dict(extra or {})
    if not values:
        summary.update({"min_ms": None, "max_ms": None, "mean_ms": None, "median_ms": None, "p95_ms": None})
        return summary
    sorted_values = sorted(values)
    summary.update(
        {
            "min_ms": min(sorted_values),
            "max_ms": max(sorted_values),
            "mean_ms": statistics.fmean(sorted_values),
            "median_ms": statistics.median(sorted_values),
            "p95_ms": _percentile(sorted_values, 0.95),
        }
    )
    return summary


def _percentile(sorted_values: Sequence[float], percentile: float) -> float:
    if len(sorted_values) == 1:
        return sorted_values[0]
    index = (len(sorted_values) - 1) * percentile
    lower = int(index)
    upper = min(lower + 1, len(sorted_values) - 1)
    if lower == upper:
        return sorted_values[lower]
    remainder = index - lower
    return sorted_values[lower] * (1 - remainder) + sorted_values[upper] * remainder
