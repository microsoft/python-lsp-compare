# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260703T070117Z.json`

- Generated at: 20260703T070117Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.56 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.56/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 6 | 3465.72 | 3.09 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 8 | 9443.53 | 20.10 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 6 | 35145.56 | 61.95 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 6 | 207702.24 | 340.29 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 464.26 | 2.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 737.18 | 10.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 4170.16 | 72.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 7536.68 | 85.76 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.64 | 1.82 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 5.72 | 9.14 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 30.68 | 119.65 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 77.54 | 115.97 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.29 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 1.05 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.47 | 2.70 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 176.81 | 177.37 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.38 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 4.25 | 4.37 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 8.23 | 11.07 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 16.86 | 26.20 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 323.61 | 437.47 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.55 | 0.58 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 2.53 | 2.59 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 31.88 | 35.96 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 169.16 | 171.29 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 222.11 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 320.77 | 5.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 1419.04 | 13.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 7827.10 | 173.28 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 3.97 | 6.95 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 4.92 | 7.76 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 19.73 | 77.15 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 206.35 | 647.23 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.22 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.28 | 0.30 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.55 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 162.01 | 165.46 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 1.07 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 2.89 | 3.08 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 3.91 | 11.42 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 24.25 | 26.15 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 310.48 | 349.96 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.72 | 1.76 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 1.85 | 3.69 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 37.87 | 43.27 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 186.48 | 187.39 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 785.87 | 6.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 862.92 | 18.47 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 8087.36 | 92.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 7704.17 | 139.87 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 17.85 | 21.61 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 39.68 | 149.76 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 73.74 | 243.47 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 102.09 | 301.56 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.28 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.63 | 0.72 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 5.27 | 5.95 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 188.86 | 191.28 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.45 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 3.11 | 5.63 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 12.88 | 13.33 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 22.80 | 55.84 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 228.33 | 244.06 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 376.81 | 860.15 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.86 | 1.89 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 10.31 | 11.57 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 21.49 | 57.23 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 178.99 | 180.61 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 304.89 | 1.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 810.68 | 15.91 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 3343.75 | 45.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 7061.87 | 83.24 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 3.80 | 8.68 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 7.14 | 12.97 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 43.17 | 72.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 68.98 | 265.79 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.39 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 1.22 | 1.39 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.81 | 5.16 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 314.11 | 316.15 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.22 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.38 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 1.09 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.84 | 2.07 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 6.94 | 11.45 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 29.21 | 29.81 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 132.04 | 165.81 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.55 | 0.62 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.60 | 1.68 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 28.62 | 28.65 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 86.42 | 93.49 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1360.75 | 3.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2946.45 | 61.12 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 16680.61 | 139.38 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 173339.67 | 1495.73 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 11.36 | 12.62 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 51.80 | 82.74 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 147.35 | 151.02 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 295.34 | 1161.94 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.43 | 0.47 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.93 | 2.96 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 2573.22 | 2653.59 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.59 | 1.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.25 | 2.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 2234.24 | 2309.66 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 2.51 | 2.63 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 2.82 | 2.88 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 4.54 | 11.28 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 5.86 | 6.66 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.53 | 0.67 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 2.62 | 2.65 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 638.21 | 654.50 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | no | 2521.32 | 2554.13 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 327.83 | 2.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 1444.63 | 8.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 779.40 | 9.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 4232.74 | 63.89 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 5.06 | 9.47 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 6.36 | 9.36 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 23.32 | 29.77 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 43.12 | 148.93 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.57 | 0.63 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.81 | 9.80 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 8.47 | 14.50 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.32 | 0.34 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 0.59 | 0.77 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 0.85 | 0.89 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 11.55 | 35.76 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.61 | 0.62 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 2.98 | 3.24 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 4.62 | 5.67 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 109.46 | 144.25 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260703T070117Z.json) | yes | 1.45 | 1.50 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2.00 | 3.92 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260703T070117Z.json) | yes | 31.62 | 38.71 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260703T070117Z.json) | yes | 166.64 | 167.68 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 206.46 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 1.72 | 4.15 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.28 | 0.31 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 0.24 | 0.25 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 2779.68 | 72.55 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 47.24 | 80.41 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 124.97 | 136.69 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260703T070117Z.json) | yes | 45.43 | 58.18 | 100% | 75.00 | 0.00 | pass |
