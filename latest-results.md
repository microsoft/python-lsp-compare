# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260709T070721Z.json`

- Generated at: 20260709T070721Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.57 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.57/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.1.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 6 | 3385.63 | 2.94 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 8 | 9344.36 | 19.50 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 6 | 34140.12 | 57.77 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 6 | 197568.12 | 329.01 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 439.21 | 2.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 807.07 | 13.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 3683.81 | 57.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 7280.27 | 84.35 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.72 | 1.89 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 5.93 | 9.21 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 31.32 | 121.96 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 70.16 | 102.85 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.27 | 0.28 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.99 | 1.06 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 5.24 | 8.31 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 176.59 | 177.89 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.43 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 1.00 | 1.05 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.34 | 2.91 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 3.89 | 3.94 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 7.76 | 10.08 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 25.57 | 51.06 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 251.05 | 353.32 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 2.57 | 2.59 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 3.84 | 5.59 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 27.79 | 31.50 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 170.13 | 171.81 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 213.38 | 1.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 326.44 | 5.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 1381.17 | 13.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 7300.78 | 158.80 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 3.88 | 7.04 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 4.40 | 6.83 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 22.09 | 80.81 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 170.68 | 531.46 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.19 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.27 | 0.31 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.46 | 0.51 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 160.45 | 162.06 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.21 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.33 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 1.03 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 2.63 | 2.84 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.65 | 6.82 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 24.36 | 26.33 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 277.17 | 323.71 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.44 | 1.49 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 1.83 | 3.69 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 36.84 | 44.28 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 184.67 | 185.26 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 773.81 | 6.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 742.56 | 14.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 7726.99 | 88.23 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 7338.43 | 125.63 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 17.64 | 21.88 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 38.86 | 153.64 | 100% | 39.00 | -232.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 48.01 | 100.63 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 68.73 | 231.03 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.23 | 0.25 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.59 | 0.67 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.52 | 2.83 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 186.43 | 187.82 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.40 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 1.05 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 12.41 | 12.94 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 16.30 | 24.31 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 212.21 | 214.04 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 359.02 | 784.76 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.95 | 2.01 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 12.40 | 14.83 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 12.88 | 17.23 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 180.44 | 181.22 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 307.11 | 1.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 784.88 | 14.77 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 3242.68 | 42.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 6563.32 | 80.87 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 3.74 | 8.77 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 7.44 | 12.96 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 50.05 | 110.58 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 70.16 | 271.13 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.37 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.96 | 1.02 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 1.28 | 1.55 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 302.01 | 304.41 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.18 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.42 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 1.16 | 1.42 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.68 | 1.86 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.01 | 5.69 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 25.95 | 26.43 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 124.34 | 161.97 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.48 | 0.51 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.43 | 1.45 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 25.15 | 25.69 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 81.45 | 86.80 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1358.13 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 3079.26 | 64.52 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 16699.10 | 136.92 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 165090.24 | 1467.36 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 10.91 | 11.34 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 57.71 | 85.22 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 132.61 | 145.46 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 302.99 | 1196.83 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.44 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.58 | 1.63 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 2543.12 | 2589.10 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 2217.20 | 2309.03 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 2.47 | 2.63 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 2.83 | 2.90 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 6.48 | 6.87 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 11.54 | 19.36 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 2.62 | 2.64 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 7.26 | 25.27 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 619.56 | 638.73 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | no | 2441.39 | 2467.18 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 293.98 | 2.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 1406.35 | 8.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 795.20 | 10.40 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 3995.07 | 57.06 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 4.92 | 8.87 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 5.92 | 9.56 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 21.21 | 27.25 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 42.58 | 151.87 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.50 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.91 | 10.21 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 9.16 | 13.91 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.34 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 0.47 | 0.56 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 0.79 | 0.89 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 2.12 | 2.27 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2.38 | 3.68 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 2.69 | 3.08 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 4.92 | 7.19 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 86.79 | 89.89 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260709T070721Z.json) | yes | 1.06 | 1.09 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 3.79 | 4.47 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260709T070721Z.json) | yes | 29.37 | 32.88 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260709T070721Z.json) | yes | 166.03 | 168.93 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 214.69 | 0.37 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 1.75 | 4.47 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.13 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.24 | 0.25 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 0.20 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 2594.26 | 60.61 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 16.31 | 27.39 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 126.06 | 136.15 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260709T070721Z.json) | yes | 39.47 | 60.27 | 100% | 75.00 | 0.00 | pass |
