# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260713T070045Z.json`

- Generated at: 20260713T070045Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.59 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.59/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 6 | 3355.28 | 2.87 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 8 | 9241.23 | 18.83 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 6 | 34590.17 | 59.91 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 6 | 200310.96 | 325.71 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 463.11 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 721.89 | 9.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 3905.15 | 63.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 7109.21 | 83.37 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1.61 | 1.72 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 6.05 | 11.11 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 30.27 | 118.08 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 77.73 | 113.57 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 1.02 | 1.17 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.57 | 2.87 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 171.38 | 172.27 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.92 | 2.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 1.02 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 4.14 | 4.32 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 7.85 | 9.70 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 13.79 | 18.77 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 280.52 | 387.07 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.93 | 2.28 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.76 | 2.79 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 29.05 | 31.59 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 162.57 | 163.23 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 218.14 | 1.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 310.52 | 4.96 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 1391.27 | 13.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 7339.44 | 161.01 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 4.42 | 7.61 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 4.65 | 7.45 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 21.21 | 76.46 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 187.90 | 599.11 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.22 | 0.23 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.50 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.75 | 2.26 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 154.72 | 156.07 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.36 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.00 | 4.81 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.71 | 2.78 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 24.78 | 29.72 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 281.19 | 308.27 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.63 | 0.65 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1.56 | 1.61 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 36.77 | 44.10 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 180.18 | 180.73 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 751.09 | 6.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 867.29 | 16.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 8464.15 | 96.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 7275.94 | 131.24 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 16.84 | 19.96 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 37.78 | 143.88 | 100% | 39.00 | -232.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 87.99 | 251.74 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 90.36 | 292.90 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.25 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.64 | 0.70 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 4.14 | 5.70 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 179.79 | 180.26 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 3.34 | 4.62 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 11.14 | 11.86 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 23.69 | 48.96 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 207.92 | 210.75 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 382.85 | 895.58 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.04 | 2.08 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 10.29 | 12.70 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 16.03 | 47.82 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 179.49 | 187.02 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 301.63 | 1.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 805.53 | 15.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 3302.80 | 44.49 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 6602.66 | 81.29 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 3.52 | 8.02 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 7.05 | 12.81 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 39.85 | 96.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 65.13 | 258.99 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.37 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 1.23 | 1.51 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.63 | 2.67 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 308.75 | 313.45 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 1.23 | 1.52 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.25 | 4.48 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1.73 | 1.89 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 5.37 | 6.80 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 28.53 | 29.07 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 132.90 | 155.21 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1.45 | 1.48 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 3.08 | 4.30 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 28.07 | 28.43 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 80.88 | 91.01 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1324.85 | 3.30 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2904.28 | 60.08 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 16123.56 | 132.98 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 167967.54 | 1440.09 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 10.66 | 11.98 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 47.80 | 77.06 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 141.01 | 146.86 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 289.35 | 1139.17 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.45 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 4.12 | 5.84 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 2471.36 | 2511.55 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.26 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.57 | 1.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.91 | 2.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 2150.67 | 2195.69 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.44 | 0.49 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 2.40 | 2.45 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.76 | 2.81 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 6.66 | 8.11 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.61 | 2.66 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 5.56 | 14.07 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 609.45 | 649.58 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | no | 2435.00 | 2447.38 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 296.47 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 1403.23 | 8.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 805.53 | 11.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 4016.17 | 57.29 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 4.74 | 8.02 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 5.52 | 8.44 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 22.03 | 26.45 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 48.56 | 152.35 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 0.49 | 0.52 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.78 | 9.70 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 9.47 | 14.19 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.35 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 0.53 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 1.30 | 2.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 2.56 | 3.12 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 1.19 | 3.02 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 2.41 | 2.54 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 4.50 | 6.07 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 93.40 | 95.22 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260713T070045Z.json) | yes | 1.07 | 1.07 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2.51 | 4.28 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260713T070045Z.json) | yes | 30.00 | 35.21 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260713T070045Z.json) | yes | 158.99 | 161.48 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 203.79 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 1.75 | 4.13 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.22 | 0.31 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.28 | 0.29 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 2622.40 | 59.06 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 60.79 | 81.44 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 109.11 | 132.30 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260713T070045Z.json) | yes | 7.29 | 7.40 | 100% | 75.00 | 0.00 | pass |
