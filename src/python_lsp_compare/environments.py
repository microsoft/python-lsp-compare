from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .benchmark_suites import BenchmarkSuite


@dataclass(slots=True)
class BenchmarkEnvironment:
    mode: str
    root_path: Path | None
    python_executable: str
    process_env: dict[str, str]
    launch_command: list[str]


def prepare_benchmark_environment(
    *,
    suite: BenchmarkSuite,
    command: Sequence[str],
    environment_mode: str,
    base_python_executable: str,
    install_requirements: bool,
    environment_root: Path | None = None,
) -> BenchmarkEnvironment:
    if environment_mode not in {"current", "isolated"}:
        raise ValueError(f"Unsupported environment mode: {environment_mode}")

    base_env = dict(os.environ)
    if environment_mode == "current":
        if install_requirements:
            _install_suite_requirements(suite, base_python_executable)
        return BenchmarkEnvironment(
            mode="current",
            root_path=None,
            python_executable=base_python_executable,
            process_env=base_env,
            launch_command=list(command),
        )

    venv_root = (environment_root / suite.name if environment_root is not None else suite.root_path / ".venv").resolve()
    env_python = _ensure_virtual_environment(venv_root, base_python_executable)
    process_env = _build_isolated_process_env(base_env, venv_root)
    if install_requirements:
        _install_suite_requirements(suite, env_python)
    return BenchmarkEnvironment(
        mode="isolated",
        root_path=venv_root,
        python_executable=env_python,
        process_env=process_env,
        launch_command=_adapt_command_for_environment(command, env_python),
    )


def _ensure_virtual_environment(venv_root: Path, base_python_executable: str) -> str:
    python_path = _venv_python_path(venv_root)
    if python_path.exists():
        return str(python_path)
    venv_root.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        [base_python_executable, "-m", "venv", str(venv_root)],
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or f"failed to create virtual environment at {venv_root}")
    return str(python_path)


def _build_isolated_process_env(base_env: dict[str, str], venv_root: Path) -> dict[str, str]:
    process_env = dict(base_env)
    scripts_dir = str(_venv_scripts_path(venv_root))
    original_path = base_env.get("PATH", "")
    process_env["PATH"] = scripts_dir if not original_path else os.pathsep.join([scripts_dir, original_path])
    process_env["VIRTUAL_ENV"] = str(venv_root)
    process_env["PYTHONNOUSERSITE"] = "1"
    process_env.pop("PYTHONHOME", None)
    process_env.pop("PYTHONPATH", None)
    return process_env


def _adapt_command_for_environment(command: Sequence[str], env_python: str) -> list[str]:
    if not command:
        raise ValueError("command must not be empty")
    adapted = list(command)
    if _looks_like_python_command(adapted[0]):
        adapted[0] = env_python
    return adapted


def _looks_like_python_command(command_part: str) -> bool:
    name = Path(command_part).name.lower()
    return name in {"python", "python.exe", "py", "py.exe"} or Path(command_part).resolve() == Path(sys.executable).resolve()


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


def _venv_python_path(venv_root: Path) -> Path:
    if os.name == "nt":
        return venv_root / "Scripts" / "python.exe"
    return venv_root / "bin" / "python"


def _venv_scripts_path(venv_root: Path) -> Path:
    if os.name == "nt":
        return venv_root / "Scripts"
    return venv_root / "bin"