# python-lsp-compare

`python-lsp-compare` is a small benchmark and regression harness for Python Language Server Protocol implementations.

It focuses on four things:

1. Running LSP servers over stdio with raw JSON-RPC messages.
2. Executing repeatable scenarios against those servers.
3. Capturing request/notification timings, payload sizes, and results.
4. Producing machine-readable reports that are easy to diff across servers.

## Features

- Pure Python implementation of LSP framing over stdio.
- Built-in Python scenarios for hover, completion, and document symbols.
- Per-call metrics including latency, bytes sent, bytes received, success, and errors.
- JSON report output for later aggregation.
- MIT licensed from the start.

## Quick Start

Create a virtual environment, install the package in editable mode, and point it at an LSP server command.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
python -m python_lsp_compare list-scenarios
python -m python_lsp_compare run --server-command pylsp --scenario hover --scenario completion
python -m python_lsp_compare run --server-command pyright-langserver --server-arg=--stdio
```

The default report path is created under `results/`.

## CLI

List the bundled scenarios:

```powershell
python -m python_lsp_compare list-scenarios
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

Arguments:

- `--server-command`: executable to launch.
- `--server-arg`: additional argument, repeatable.
- `--scenario`: scenario name, repeatable. If omitted, all scenarios run.
- `--timeout-seconds`: per-request timeout.
- `--output`: JSON report path.

## Report Shape

Reports include:

- Server command and run timestamp.
- One entry per scenario.
- One metric per LSP call, including initialize/shutdown.
- Scenario success/failure and any captured error message.

## Tests

The repository includes unit tests with a fake stdio LSP server.

```powershell
python -m unittest discover -s tests -v
```
