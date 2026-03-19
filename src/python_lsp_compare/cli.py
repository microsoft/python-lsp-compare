from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .benchmark_suites import discover_benchmark_suites
from .runner import BUILTIN_SCENARIOS, run_benchmarks, run_scenarios, write_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m python_lsp_compare")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list-scenarios", help="List bundled scenarios.")
    list_parser.set_defaults(func=handle_list_scenarios)

    list_benchmarks_parser = subparsers.add_parser("list-benchmarks", help="List config-driven benchmark suites.")
    list_benchmarks_parser.add_argument("--benchmark-root", type=Path, help="Directory containing benchmark suite folders.")
    list_benchmarks_parser.set_defaults(func=handle_list_benchmarks)

    run_parser = subparsers.add_parser("run", help="Run scenarios against an LSP server.")
    run_parser.add_argument("--server-command", required=True, help="Executable to launch.")
    run_parser.add_argument("--server-arg", action="append", default=[], help="Additional executable argument. Repeatable.")
    run_parser.add_argument("--scenario", action="append", default=[], help="Scenario to run. Repeatable.")
    run_parser.add_argument("--timeout-seconds", type=float, default=10.0, help="Per-request timeout in seconds.")
    run_parser.add_argument("--output", type=Path, help="Write the JSON report to this path.")
    run_parser.set_defaults(func=handle_run)

    run_benchmark_parser = subparsers.add_parser("run-benchmark", help="Run config-driven benchmark suites against an LSP server.")
    run_benchmark_parser.add_argument("--server-command", required=True, help="Executable to launch.")
    run_benchmark_parser.add_argument("--server-arg", action="append", default=[], help="Additional executable argument. Repeatable.")
    run_benchmark_parser.add_argument("--benchmark", action="append", default=[], help="Benchmark suite to run. Repeatable.")
    run_benchmark_parser.add_argument("--benchmark-root", type=Path, help="Directory containing benchmark suite folders.")
    run_benchmark_parser.add_argument("--install-requirements", action="store_true", help="Install suite requirements with pip before running.")
    run_benchmark_parser.add_argument("--python-executable", default=None, help="Python executable to use for pip installs.")
    run_benchmark_parser.add_argument("--timeout-seconds", type=float, default=10.0, help="Per-request timeout in seconds.")
    run_benchmark_parser.add_argument("--output", type=Path, help="Write the JSON report to this path.")
    run_benchmark_parser.set_defaults(func=handle_run_benchmark)
    return parser


def handle_list_scenarios(_: argparse.Namespace) -> int:
    for scenario in BUILTIN_SCENARIOS.values():
        print(f"{scenario.name}: {scenario.description}")
    return 0


def handle_list_benchmarks(args: argparse.Namespace) -> int:
    suites = discover_benchmark_suites(args.benchmark_root)
    for suite in suites.values():
        point_count = sum(len(points) for points in suite.points_by_method.values())
        requirements = suite.requirements_file.name if suite.requirements_file is not None else "none"
        print(f"{suite.name}: {suite.description} ({point_count} points, requirements={requirements})")
    return 0


def handle_run(args: argparse.Namespace) -> int:
    command = [args.server_command, *args.server_arg]
    requested = args.scenario or list(BUILTIN_SCENARIOS.keys())
    report = run_scenarios(command=command, scenario_names=requested, timeout_seconds=args.timeout_seconds)
    output_path = args.output or _default_output_path(command[0])
    write_report(report, output_path)
    print(f"Wrote report to {output_path}")
    for scenario in report.scenario_reports:
        status = "ok" if scenario.success else "failed"
        print(f"{scenario.name}: {status} ({scenario.total_duration_ms:.2f} ms, {len(scenario.metrics)} calls)")
        if scenario.error_message:
            print(f"  error: {scenario.error_message}")
    return 0 if all(item.success for item in report.scenario_reports) else 1


def handle_run_benchmark(args: argparse.Namespace) -> int:
    command = [args.server_command, *args.server_arg]
    requested = args.benchmark or None
    report = run_benchmarks(
        command=command,
        benchmark_names=requested,
        timeout_seconds=args.timeout_seconds,
        benchmark_root=args.benchmark_root,
        install_requirements=args.install_requirements,
        python_executable=args.python_executable,
    )
    output_path = args.output or _default_output_path(f"{command[0]}-benchmarks")
    write_report(report, output_path)
    print(f"Wrote report to {output_path}")
    for benchmark in report.benchmark_reports:
        status = "ok" if benchmark.success else "failed"
        print(f"{benchmark.name}: {status} ({benchmark.total_duration_ms:.2f} ms, {len(benchmark.points)} points)")
        if benchmark.error_message:
            print(f"  error: {benchmark.error_message}")
        for point in benchmark.points:
            point_status = "ok" if point.success else "failed"
            mean_ms = point.summary.get("mean_ms")
            mean_text = f"{mean_ms:.2f} ms" if isinstance(mean_ms, (float, int)) else "n/a"
            print(f"  {point.label}: {point_status} ({point.measured_iterations} measured, mean={mean_text})")
            if point.error_message:
                print(f"    error: {point.error_message}")
    return 0 if all(item.success for item in report.benchmark_reports) else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def _default_output_path(executable_name: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path("results") / f"{executable_name}-{timestamp}.json"
