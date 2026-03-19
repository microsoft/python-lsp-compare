from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from python_lsp_compare.cli import main


class CliTests(unittest.TestCase):
    def test_list_scenarios(self) -> None:
        exit_code = main(["list-scenarios"])
        self.assertEqual(exit_code, 0)

    def test_run_writes_report(self) -> None:
        server_script = Path(__file__).parent / "fixtures" / "fake_lsp_server.py"
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "report.json"
            exit_code = main(
                [
                    "run",
                    "--server-command",
                    sys.executable,
                    "--server-arg",
                    str(server_script),
                    "--scenario",
                    "hover",
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(exit_code, 0)
            report = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(report["requested_scenarios"], ["hover"])
            self.assertEqual(report["scenario_reports"][0]["name"], "hover")
            self.assertTrue(report["scenario_reports"][0]["success"])

    def test_list_benchmarks(self) -> None:
        exit_code = main(["list-benchmarks", "--benchmark-root", str(Path(__file__).parent / "fixtures")])
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
