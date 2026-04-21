from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ServerConfigFile:
    baseline_server: str | None = None
    servers: list[ConfiguredServer] = field(default_factory=list)


@dataclass(slots=True)
class ConfiguredServer:
    id: str
    display_name: str
    command: str
    args: list[str] = field(default_factory=list)
    benchmark_args: list[str] = field(default_factory=list)
    enabled: bool = True
    kind: str | None = None
    notes: list[str] = field(default_factory=list)
    protocols: list[str] = field(default_factory=lambda: ["lsp"])
    protocol_launch_args: dict[str, list[str]] = field(default_factory=dict)
    source_path: str | None = None
    version_label: str | None = None

    def launch_command_for_protocol(self, protocol: str | None = None) -> list[str]:
        args = self.args if protocol is None else self.protocol_launch_args.get(protocol, self.args)
        return [self.command, *args]

    @property
    def launch_command(self) -> list[str]:
        return self.launch_command_for_protocol()

    def benchmark_launch_command_for_protocol(self, protocol: str | None = None) -> list[str]:
        return [*self.launch_command_for_protocol(protocol), *self.benchmark_args]

    @property
    def benchmark_launch_command(self) -> list[str]:
        return self.benchmark_launch_command_for_protocol()


def default_local_server_config_path() -> Path:
    return Path(__file__).resolve().parents[2] / ".python-lsp-compare" / "lsp_servers.json"


def example_server_config_path() -> Path:
    return Path(__file__).resolve().parents[2] / "configs" / "lsp_servers.example.json"


def load_server_configs(config_path: Path | None = None) -> list[ConfiguredServer]:
    return load_server_config_file(config_path).servers


def load_server_config_file(config_path: Path | None = None) -> ServerConfigFile:
    if config_path is None:
        resolved = _resolve_default_server_config_path()
    else:
        resolved = config_path.resolve()
    if not resolved.exists():
        raise FileNotFoundError(
            f"Server config file not found: {resolved}. Copy {example_server_config_path()} to that path and fill in local server commands."
        )
    data = json.loads(resolved.read_text(encoding="utf-8"))
    servers = [
        ConfiguredServer(
            id=item["id"],
            display_name=item.get("displayName", item["id"]),
            command=_resolve_value(item["launch"]["command"], resolved.parent),
            args=[_resolve_value(arg, resolved.parent) for arg in item["launch"].get("args", [])],
            benchmark_args=_load_benchmark_args(item, resolved.parent),
            enabled=bool(item.get("enabled", True)),
            kind=item.get("kind"),
            notes=list(item.get("notes", [])),
            protocols=list(item.get("protocols", ["lsp"])),
            protocol_launch_args=_load_protocol_launch_args(item, resolved.parent),
            source_path=item.get("sourcePath"),
        )
        for item in data.get("servers", [])
    ]
    return ServerConfigFile(
        baseline_server=data.get("baselineServer"),
        servers=servers,
    )


def _resolve_value(value: str, base_dir: Path) -> str:
    if value.startswith("./") or value.startswith("../"):
        return str((base_dir / value).resolve())
    return value


def _resolve_default_server_config_path() -> Path:
    return default_local_server_config_path().resolve()


def _load_benchmark_args(item: dict[str, Any], base_dir: Path) -> list[str]:
    launch = item.get("launch", {})
    return [_resolve_value(arg, base_dir) for arg in launch.get("benchmarkArgs", [])]


def _load_protocol_launch_args(item: dict[str, Any], base_dir: Path) -> dict[str, list[str]]:
    launch = item.get("launch", {})
    raw = launch.get("protocolArgs", {})
    if not isinstance(raw, dict):
        return {}
    return {
        str(protocol): [_resolve_value(arg, base_dir) for arg in args]
        for protocol, args in raw.items()
        if isinstance(args, list)
    }


def write_summary(summary_path: Path, payload: dict[str, Any]) -> None:
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
