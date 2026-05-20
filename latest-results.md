# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260520T070736Z.json`

- Generated at: 20260520T070736Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.38 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.38/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.0.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
| pylsp-mypy | 1.14.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pylsp-mypy/venv/bin/pylsp |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **Pyrefly**: Installed from PyPI into an isolated venv because GitHub release binaries are no longer published.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Wall clock ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 6 | 4040.16 | 3.41 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 8 | 10196.02 | 19.97 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 6 | 37170.50 | 69.73 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 6 | 210060.15 | 352.75 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 532.68 | 3.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 839.94 | 12.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 3497.94 | 51.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 7395.40 | 91.02 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.83 | 2.00 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 6.21 | 10.95 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 36.52 | 142.98 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 47.49 | 50.38 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.32 | 0.34 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 1.10 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 1.93 | 2.10 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 207.08 | 217.07 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.49 | 0.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 4.81 | 5.50 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 11.84 | 14.09 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 14.81 | 14.97 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 215.96 | 327.57 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.92 | 2.00 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 13.44 | 45.06 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 31.26 | 35.15 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 194.67 | 197.10 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 260.53 | 2.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 392.58 | 7.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 1380.22 | 14.58 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 8368.21 | 187.15 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 5.05 | 7.77 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 5.69 | 8.99 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 29.27 | 114.89 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 221.41 | 682.60 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.25 | 0.31 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.30 | 0.34 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.56 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 182.39 | 184.10 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 1.17 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 2.79 | 3.18 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 3.75 | 11.17 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 24.74 | 26.44 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 319.97 | 370.95 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 1.56 | 3.95 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.72 | 2.53 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 42.13 | 43.00 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 210.80 | 211.62 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 878.32 | 6.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 780.92 | 15.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 9565.89 | 152.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 8229.84 | 157.21 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 18.34 | 22.96 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 42.03 | 166.74 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 80.63 | 266.75 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 122.65 | 380.56 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.28 | 0.31 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.87 | 0.89 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 11.07 | 19.10 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 218.34 | 223.91 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.45 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 1.06 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 12.62 | 13.00 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 24.78 | 43.74 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 238.86 | 243.94 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 667.28 | 1463.48 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 1.05 | 1.11 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.52 | 1.70 | 100% | 4378.00 | +86.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 12.27 | 14.21 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 205.16 | 206.64 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 358.05 | 1.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 911.40 | 18.32 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 3485.88 | 47.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 7106.51 | 91.71 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 4.25 | 10.10 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 18.67 | 26.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 46.65 | 107.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 80.01 | 308.28 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.41 | 0.44 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.76 | 0.84 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 1.40 | 1.77 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 352.02 | 359.50 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.46 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 1.08 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 2.02 | 2.33 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 7.15 | 22.47 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 29.87 | 30.12 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 129.71 | 164.83 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.56 | 1.58 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 3.40 | 3.68 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 28.94 | 29.32 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 87.30 | 98.00 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1647.54 | 4.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 3894.79 | 91.97 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 17855.02 | 144.42 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 174590.26 | 1522.08 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 12.69 | 14.69 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 60.39 | 93.89 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 145.69 | 150.16 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 439.47 | 1620.00 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.24 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.57 | 0.71 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 2.93 | 2.95 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 2635.41 | 2694.43 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.29 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.44 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 1.95 | 3.74 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 2275.58 | 2311.34 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 2.68 | 2.95 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 2.70 | 3.02 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 3.75 | 4.17 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 7.94 | 12.16 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 3.11 | 3.22 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 12.79 | 35.24 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 652.76 | 668.40 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | no | 2551.05 | 2589.12 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 363.04 | 2.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 1385.54 | 8.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 849.00 | 11.59 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 4369.93 | 67.29 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 5.10 | 8.35 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 6.43 | 10.20 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 25.81 | 33.90 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 49.14 | 171.58 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.53 | 0.58 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 4.31 | 11.75 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 11.69 | 18.01 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.38 | 0.40 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 0.55 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 0.72 | 0.81 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 3.36 | 3.75 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.72 | 0.85 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 2.70 | 2.85 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 5.39 | 8.06 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 109.51 | 139.95 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260520T070736Z.json) | yes | 1.10 | 1.14 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 3.39 | 5.98 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260520T070736Z.json) | yes | 31.20 | 35.44 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260520T070736Z.json) | yes | 186.09 | 188.21 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 235.89 | 0.33 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 1.02 | 1.16 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.30 | 0.58 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.22 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 0.23 | 0.26 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 2291.50 | 9.47 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 10.91 | 11.07 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 9.58 | 9.87 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260520T070736Z.json) | yes | 7.91 | 10.23 | 100% | 75.00 | 0.00 | pass |
