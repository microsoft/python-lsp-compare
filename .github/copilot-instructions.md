# Project Guidelines

## Overview

`python-lsp-compare` is a benchmark and regression harness for Python LSP servers.
It downloads servers, runs LSP scenarios over stdio JSON-RPC, captures timing/payload
metrics, and produces comparison reports. Pure Python, zero external dependencies.

## Architecture

All source lives under `src/python_lsp_compare/`. Key modules and data flow:

```
server_download.py  →  server_configs.py  →  runner.py  →  report_markdown.py
  (download/cache)     (ConfiguredServer)    (LSP I/O)     report_csv.py
                       server_versions.py
```

- **server_download.py** — Downloads servers from GitHub releases (`ServerSpec`) or
  installs into isolated venvs from PyPI (`PypiServerSpec`). Caches binaries under
  `.python-lsp-compare/servers/`. Version checks cached 24h in `versions.json`.
  Functions return `tuple[Path, str]` (executable path + version label).
- **server_configs.py** — `ConfiguredServer` dataclass wraps a server binary with
  its launch command, args, and optional `version_label`.
- **server_versions.py** — Detects version info for reports. Uses `version_label`
  when present (downloaded servers), falls back to git for local dev builds.
- **runner.py** — Starts LSP server processes, sends JSON-RPC over stdio, measures
  latency. Sends `workspace/didChangeConfiguration` after `initialized` (required
  by Pyright).
- **lsp_client.py / transport.py** — Low-level LSP framing and JSON-RPC protocol.
- **cli.py** — Entry point. Subcommands: `run`, `run-servers`, `bench-servers`,
  `run-benchmark`, `render-report`, `list-scenarios`, `list-benchmarks`,
  `list-servers`, `download-servers`.
- **report_markdown.py / report_csv.py** — Render comparison tables from JSON results.
- **environments.py** — Creates per-benchmark-suite `.venv` with suite requirements.
- **benchmark_suites.py** — Discovers suites under `benchmarks/` with config.json.
- **scenarios/** — Individual LSP test scenarios (hover, completion, etc.).

## Servers

Four servers are benchmarked by default (defined in `server_download.py`):

| Server | Type | Notes |
|--------|------|-------|
| Pyright | `ServerSpec` (GitHub release, Node.js) | Needs `node` on PATH |
| Ty | `ServerSpec` (GitHub release, native) | |
| Pyrefly | `ServerSpec` (GitHub release, native) | Uses `--indexing-mode lazy-blocking --build-system-blocking` |
| pylsp-mypy | `PypiServerSpec` (PyPI venv) | Installs `python-lsp-server` + `pylsp-mypy`; hover/completion come from Jedi, only diagnostics from mypy |

## Build & Test

```bash
python -m venv .venv
pip install -e .                          # install in editable mode
python -m pytest tests/ -x -q            # run all tests (26 tests, ~15s)
python -m python_lsp_compare bench-servers  # full benchmark run (downloads servers if needed)
```

No dev dependencies are required — tests use only stdlib `unittest` and `pytest`.

## Key Conventions

- **Zero external dependencies.** All HTTP downloads use `urllib.request`. Do not
  add packages to `dependencies` in pyproject.toml.
- **Python 3.11+.** Uses `match` statements, `str | None` unions, `dataclasses`.
- **Return tuples consistently.** `download_server()` and `install_pypi_server()`
  return `(path, version_label)`. All code paths (including cache-hit early returns)
  must return the same shape.
- **Server failures are informational.** `handle_run_servers` and `handle_bench_servers`
  always return exit code 0. Individual server failures are logged but don't fail
  the overall run.
- **Benchmark results go to `results/`.** The `_update_latest_results()` function
  also copies to `latest-results/` for the committed snapshot.
- **No `.python-lsp-compare/` in git.** Server binaries and version caches live there
  but are gitignored.

## File Layout

- `benchmarks/` — Benchmark suites (each has `config.json`, `requirements.txt`, `src/`)
- `configs/` — Example server config files for `--config` flag
- `results/` — Output directory (gitignored except `latest-results/`)
- `tools/` — Utility scripts (e.g. Pyright stdio launcher)
- `tests/` — Pytest tests; fixtures in `tests/fixtures/`
