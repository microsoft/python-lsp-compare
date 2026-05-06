# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260506T065027Z.json`

- Generated at: 20260506T065027Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.34 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.34/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.63.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 6 | 4374.80 | 3.75 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | no | 8 | 10030.46 | 19.65 | 195 | 97% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 6 | 36904.19 | 68.37 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 6 | 173713.28 | 281.39 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 567.75 | 4.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 835.18 | 13.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 3890.73 | 61.60 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 6811.37 | 88.47 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.94 | 2.24 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 6.91 | 11.64 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 41.87 | 165.09 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 53.76 | 63.10 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.26 | 0.29 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 1.42 | 1.61 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 9.53 | 19.50 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 197.66 | 200.92 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.50 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 0.97 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 4.34 | 4.49 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 15.60 | 17.37 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 18.45 | 18.95 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 264.94 | 387.29 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.63 | 0.73 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.80 | 1.94 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 34.25 | 36.78 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 185.64 | 187.71 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 263.07 | 2.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 377.05 | 5.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 1366.46 | 15.42 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 7598.91 | 168.56 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 5.18 | 8.15 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 6.18 | 9.71 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 23.65 | 92.83 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 186.35 | 589.77 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.19 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.20 | 0.25 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.58 | 0.66 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 173.51 | 174.98 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.57 | 0.64 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 1.01 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 2.60 | 5.52 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 3.07 | 3.94 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 27.11 | 29.38 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 283.43 | 344.57 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.27 | 1.30 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 2.79 | 5.96 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 43.66 | 46.22 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 198.51 | 200.68 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 969.95 | 7.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 877.52 | 15.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 8803.04 | 124.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 7729.84 | 139.20 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 19.51 | 23.99 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 44.58 | 176.95 | 100% | 39.00 | -235.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 75.99 | 217.61 | 100% | 6.00 | -268.20 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 82.06 | 269.23 | 100% | 274.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.25 | 0.32 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.99 | 1.20 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 2.31 | 2.60 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 198.05 | 201.27 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.55 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 0.96 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 16.02 | 17.40 | 100% | 256.00 | -185.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 16.15 | 18.72 | 100% | 448.00 | +7.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 228.33 | 231.91 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 526.77 | 1001.51 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.71 | 2.33 | 100% | 4378.00 | +86.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 11.12 | 12.99 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 12.91 | 37.08 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 192.69 | 197.15 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 373.82 | 1.75 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 929.89 | 18.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 3450.30 | 48.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 6418.52 | 90.90 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 4.85 | 11.50 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 20.08 | 28.78 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 68.75 | 103.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 86.72 | 334.82 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.36 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.79 | 0.86 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 2.11 | 2.98 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 332.69 | 373.29 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.16 | 0.17 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 0.99 | 1.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 1.19 | 4.18 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.72 | 0.84 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.95 | 2.32 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 26.79 | 27.91 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 132.49 | 170.74 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 1.37 | 2.69 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.43 | 1.52 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 25.31 | 26.87 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 88.83 | 94.64 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1780.84 | 4.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 3539.60 | 80.31 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 18090.94 | 151.41 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 141084.70 | 1139.82 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 13.48 | 15.68 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 69.77 | 104.41 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 124.39 | 127.29 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 388.86 | 1554.16 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.18 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.19 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.55 | 0.69 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 1994.14 | 2044.85 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.19 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.23 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 1660.95 | 1791.19 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 3.03 | 3.09 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 3.48 | 4.37 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 8.25 | 12.91 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 11.87 | 26.12 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.45 | 0.54 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 2.89 | 3.07 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 678.05 | 685.96 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | no | 1916.61 | 1964.38 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 419.37 | 2.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 1302.72 | 8.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 799.88 | 12.50 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 4069.94 | 61.36 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 5.68 | 10.49 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 7.38 | 11.27 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 23.57 | 33.16 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 50.14 | 169.65 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.17 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.52 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 5.24 | 15.00 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 13.11 | 17.81 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.40 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 0.65 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 0.78 | 1.02 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 7.37 | 12.89 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 2.46 | 5.38 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 3.03 | 3.48 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 6.23 | 8.58 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 82.65 | 83.37 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260506T065027Z.json) | yes | 1.02 | 1.39 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 4.27 | 6.04 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260506T065027Z.json) | yes | 30.29 | 33.26 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260506T065027Z.json) | yes | 180.11 | 181.78 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 443.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | no | 223.06 | 0.34 | 8 | 30 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 1.21 | 1.30 | 100% | 30.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.18 | 0.19 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.16 | 0.18 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.16 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 0.17 | 0.20 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 2448.28 | 12.10 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 18.50 | 30.87 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 11.50 | 12.66 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260506T065027Z.json) | yes | 6.29 | 6.83 | 100% | 75.00 | 0.00 | pass |
