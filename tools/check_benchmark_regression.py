"""Compare benchmark results against the latest-results baseline.

Exits with code 1 if any server has more failed points than the baseline.

Usage:
    python tools/check_benchmark_regression.py <new-summary-json>

The baseline is read from latest-results/summary-*.json (committed snapshot).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_report_path(summary_path: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute() and path.exists():
        return path
    for candidate in [Path.cwd() / path, summary_path.parent / path, summary_path.parent / path.name]:
        if candidate.exists():
            return candidate.resolve()
    return path.resolve()


def _count_failed_points(summary_path: Path) -> dict[str, int]:
    """Return {server_id: failed_point_count} for each server in a summary."""
    summary = _read_json(summary_path)
    counts: dict[str, int] = {}
    for entry in summary.get("servers", []):
        server_id = entry["id"]
        report_path = _resolve_report_path(summary_path, entry["output_path"])
        if not report_path.exists():
            print(f"  Warning: report not found for {server_id}: {report_path}")
            counts[server_id] = 0
            continue
        report = _read_json(report_path)
        failed = 0
        for benchmark in report.get("benchmark_reports", []):
            for point in benchmark.get("points", []):
                passed = point.get("summary", {}).get("validation", {}).get("passed", True)
                if not passed:
                    failed += 1
        counts[server_id] = failed
    return counts


def _find_baseline_summary() -> Path | None:
    latest_dir = Path("latest-results")
    if not latest_dir.is_dir():
        return None
    summaries = sorted(latest_dir.glob("summary-*.json"))
    return summaries[-1] if summaries else None


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <new-summary-json>")
        return 2

    new_summary_path = Path(sys.argv[1])
    if not new_summary_path.exists():
        print(f"Error: new summary not found: {new_summary_path}")
        return 2

    baseline_path = _find_baseline_summary()
    if baseline_path is None:
        print("No baseline found in latest-results/. Skipping regression check.")
        return 0

    print(f"Baseline: {baseline_path}")
    print(f"New:      {new_summary_path}")
    print()

    baseline_counts = _count_failed_points(baseline_path)
    new_counts = _count_failed_points(new_summary_path)

    print("Failed points per server:")
    print(f"  {'Server':<20} {'Baseline':>10} {'New':>10} {'Status'}")
    print(f"  {'-' * 20} {'-' * 10} {'-' * 10} {'-' * 10}")

    regressions = []
    for server_id in sorted(set(baseline_counts) | set(new_counts)):
        baseline_val = baseline_counts.get(server_id, 0)
        new_val = new_counts.get(server_id, 0)
        if new_val > baseline_val:
            status = "REGRESSION"
            regressions.append((server_id, baseline_val, new_val))
        elif new_val < baseline_val:
            status = "improved"
        else:
            status = "ok"
        print(f"  {server_id:<20} {baseline_val:>10} {new_val:>10} {status}")

    print()
    if regressions:
        print("FAILED: Regressions detected:")
        for server_id, baseline_val, new_val in regressions:
            print(f"  {server_id}: {baseline_val} -> {new_val} (+{new_val - baseline_val})")
        return 1

    print("PASSED: No regressions detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
