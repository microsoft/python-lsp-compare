from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .runner import BUILTIN_SCENARIOS, run_scenarios, write_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m python_lsp_compare")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list-scenarios", help="List bundled scenarios.")
    list_parser.set_defaults(func=handle_list_scenarios)

    run_parser = subparsers.add_parser("run", help="Run scenarios against an LSP server.")
    run_parser.add_argument("--server-command", required=True, help="Executable to launch.")
    run_parser.add_argument("--server-arg", action="append", default=[], help="Additional executable argument. Repeatable.")
    run_parser.add_argument("--scenario", action="append", default=[], help="Scenario to run. Repeatable.")
    run_parser.add_argument("--timeout-seconds", type=float, default=10.0, help="Per-request timeout in seconds.")
    run_parser.add_argument("--output", type=Path, help="Write the JSON report to this path.")
    run_parser.set_defaults(func=handle_run)
    return parser


def handle_list_scenarios(_: argparse.Namespace) -> int:
    for scenario in BUILTIN_SCENARIOS.values():
        print(f"{scenario.name}: {scenario.description}")
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def _default_output_path(executable_name: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path("results") / f"{executable_name}-{timestamp}.json"
