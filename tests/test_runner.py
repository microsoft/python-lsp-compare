from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from python_lsp_compare.runner import run_scenarios


class RunnerTests(unittest.TestCase):
    def test_run_all_builtin_scenarios(self) -> None:
        server_script = Path(__file__).parent / "fixtures" / "fake_lsp_server.py"
        report = run_scenarios([sys.executable, str(server_script)], timeout_seconds=2.0)
        self.assertEqual(len(report.scenario_reports), 3)
        self.assertTrue(all(item.success for item in report.scenario_reports))
        self.assertTrue(all(item.metrics for item in report.scenario_reports))

    def test_unknown_scenario_fails_fast(self) -> None:
        with self.assertRaises(ValueError):
            run_scenarios(["python", "fake.py"], scenario_names=["missing"])


if __name__ == "__main__":
    unittest.main()