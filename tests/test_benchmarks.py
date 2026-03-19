from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from python_lsp_compare.benchmark_suites import discover_benchmark_suites
from python_lsp_compare.cli import main
from python_lsp_compare.runner import run_benchmarks


class BenchmarkSuiteTests(unittest.TestCase):
    def test_discover_benchmark_suite(self) -> None:
        suites = discover_benchmark_suites(Path(__file__).parent / "fixtures")
        self.assertIn("fixture_suite", suites)
        suite = suites["fixture_suite"]
        self.assertEqual(suite.iterations, 2)
        self.assertEqual(suite.warmup_iterations, 1)
        self.assertIn("textDocument/hover", suite.points_by_method)
        self.assertIn("textDocument/references", suite.points_by_method)

    def test_run_benchmark_suite(self) -> None:
        server_script = Path(__file__).parent / "fixtures" / "fake_lsp_server.py"
        report = run_benchmarks(
            command=[sys.executable, str(server_script)],
            benchmark_names=["fixture_suite"],
            benchmark_root=Path(__file__).parent / "fixtures",
            timeout_seconds=2.0,
        )
        self.assertEqual(report.requested_benchmarks, ["fixture_suite"])
        self.assertEqual(len(report.benchmark_reports), 1)
        suite_report = report.benchmark_reports[0]
        self.assertTrue(suite_report.success)
        self.assertEqual(len(suite_report.points), 5)
        self.assertIn("textDocument/hover", suite_report.summary["by_method"])
        hover_point = next(point for point in suite_report.points if point.method == "textDocument/hover")
        self.assertEqual(hover_point.measured_iterations, 2)
        self.assertEqual(hover_point.warmup_iterations, 1)
        self.assertEqual(hover_point.summary["request_count"], 2)

    def test_run_benchmark_cli_writes_report(self) -> None:
        server_script = Path(__file__).parent / "fixtures" / "fake_lsp_server.py"
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "benchmarks.json"
            exit_code = main(
                [
                    "run-benchmark",
                    "--server-command",
                    sys.executable,
                    "--server-arg",
                    str(server_script),
                    "--benchmark-root",
                    str(Path(__file__).parent / "fixtures"),
                    "--benchmark",
                    "fixture_suite",
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(exit_code, 0)
            report = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(report["requested_benchmarks"], ["fixture_suite"])
            self.assertEqual(report["benchmark_reports"][0]["name"], "fixture_suite")
            self.assertTrue(report["benchmark_reports"][0]["success"])

    def test_isolated_environment_creates_suite_venv_and_rewrites_python_command(self) -> None:
        server_script = Path(__file__).parent / "fixtures" / "fake_lsp_server.py"
        with tempfile.TemporaryDirectory() as temp_dir:
            env_capture = Path(temp_dir) / "env.json"
            report = run_benchmarks(
                command=[sys.executable, str(server_script), "--write-env", str(env_capture)],
                benchmark_names=["fixture_suite"],
                benchmark_root=Path(__file__).parent / "fixtures",
                timeout_seconds=2.0,
                environment_mode="isolated",
                environment_root=Path(temp_dir) / "envs",
            )
            suite_report = report.benchmark_reports[0]
            self.assertTrue(suite_report.success)
            self.assertEqual(suite_report.environment_mode, "isolated")
            self.assertIsNotNone(suite_report.environment_path)
            self.assertTrue(Path(suite_report.environment_path).exists())

            env_data = json.loads(env_capture.read_text(encoding="utf-8"))
            self.assertEqual(Path(env_data["virtual_env"]), Path(suite_report.environment_path))
            self.assertEqual(Path(env_data["sys_executable"]), Path(suite_report.python_executable))
            self.assertTrue(env_data["path"].startswith(str(Path(suite_report.environment_path) / "Scripts")))


if __name__ == "__main__":
    unittest.main()