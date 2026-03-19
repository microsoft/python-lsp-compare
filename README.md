# python-lsp-compare

`python-lsp-compare` is a small benchmark and regression harness for Python Language Server Protocol implementations.

It focuses on four things:

1. Running LSP servers over stdio with raw JSON-RPC messages.
2. Executing repeatable scenarios against those servers.
3. Capturing request/notification timings, payload sizes, and results.
4. Producing machine-readable reports that are easy to diff across servers.

Benchmark suites are package-oriented, not just API-oriented. That means testing LSP behavior against realistic dependency surfaces like SQLAlchemy-heavy code, web frameworks, and data-science imports.

## Features

- Pure Python implementation of LSP framing over stdio.
- Built-in Python scenarios for hover, completion, and document symbols.
- Config-driven benchmark suites under `benchmarks/` with package-specific fixtures and `requirements.txt` files.
- Per-call metrics including latency, bytes sent, bytes received, success, and errors.
- Aggregate stats for benchmark points including mean, median, min, max, and p95.
- JSON report output for later aggregation.
- MIT licensed from the start.

## Quick Start

Create a virtual environment, install the package in editable mode, and point it at an LSP server command.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
python -m python_lsp_compare list-scenarios
python -m python_lsp_compare list-benchmarks
python -m python_lsp_compare run --server-command pylsp --scenario hover --scenario completion
python -m python_lsp_compare run --server-command pyright-langserver --server-arg=--stdio
python -m python_lsp_compare run-benchmark --server-command pyright-langserver --server-arg=--stdio --benchmark sqlalchemy
```

The default report path is created under `results/`.

## CLI

List the bundled scenarios:

```powershell
python -m python_lsp_compare list-scenarios
```

List the benchmark suites:

```powershell
python -m python_lsp_compare list-benchmarks
```

Run one or more scenarios:

```powershell
python -m python_lsp_compare run \
  --server-command pyright-langserver \
  --server-arg=--stdio \
  --scenario hover \
  --scenario completion \
  --output results/pyright.json
```

Run one or more package-oriented benchmark suites:

```powershell
python -m python_lsp_compare run-benchmark \
  --server-command pyright-langserver \
  --server-arg=--stdio \
  --benchmark sqlalchemy \
  --benchmark web \
  --environment-mode isolated \
  --install-requirements \
  --output results/pyright-benchmarks.json
```

Arguments:

- `--server-command`: executable to launch.
- `--server-arg`: additional argument, repeatable.
- `--scenario`: scenario name, repeatable. If omitted, all scenarios run.
- `--timeout-seconds`: per-request timeout.
- `--output`: JSON report path.

Benchmark arguments:

- `--benchmark`: benchmark suite name, repeatable. If omitted, all suites under `benchmarks/` run.
- `--benchmark-root`: alternate benchmark suite directory.
- `--install-requirements`: install each suite's `requirements.txt` and extra packages with pip before running.
- `--environment-mode`: use the current process environment or create a per-suite virtual environment.
- `--environment-root`: override where isolated environments are created. By default each suite uses its own `.venv`.
- `--python-executable`: base interpreter to use for virtual environment creation and pip installation.

If `--install-requirements` is set and no environment mode is provided, the CLI defaults to isolated environments so dependency installation does not mutate the active Python environment.

## Report Shape

Reports include:

- Server command and run timestamp.
- One entry per scenario.
- One entry per benchmark suite when using `run-benchmark`.
- One metric per LSP call, including initialize/shutdown.
- Scenario success/failure and any captured error message.
- Aggregate duration summaries for each benchmark point and method.

## Benchmark Suites

Each suite folder follows the same internal structure:

- `config.json` describes request points and iteration counts.
- `requirements.txt` describes the dependency surface to benchmark.
- `src/` contains the Python files to open and query.
- `.venv/` can be created per suite when running in isolated mode.

Bundled examples:

- `benchmarks/sqlalchemy`
- `benchmarks/web`
- `benchmarks/data_science`

## Isolated Environments

Benchmark suites can now run inside per-suite virtual environments. This is useful when you want to install suite dependencies without contaminating the interpreter used for development or testing.

Example:

```powershell
python -m python_lsp_compare run-benchmark \
  --server-command python \
  --server-arg=-m \
  --server-arg=pylsp \
  --benchmark sqlalchemy \
  --install-requirements \
  --environment-mode isolated
```

When the server is launched with a Python executable, the runner swaps that executable for the suite's virtual environment interpreter. For non-Python launchers such as Node-based servers, the runner still isolates `PATH`, `VIRTUAL_ENV`, and related Python environment variables for the server process.

## Tests

The repository includes unit tests with a fake stdio LSP server.

```powershell
python -m unittest discover -s tests -v
```
