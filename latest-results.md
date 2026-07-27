# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260727T070156Z.json`

- Generated at: 20260727T070156Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.63 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.63/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 6 | 3334.42 | 2.96 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 8 | 9059.62 | 18.13 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 6 | 34098.57 | 57.10 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 6 | 189146.88 | 331.31 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 455.73 | 2.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 718.40 | 10.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 3744.20 | 58.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 6998.09 | 86.61 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1.69 | 1.90 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 5.45 | 8.39 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 31.68 | 121.09 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 77.37 | 117.31 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.26 | 0.29 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.99 | 1.05 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 4.05 | 5.95 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 179.30 | 182.83 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 4.12 | 4.47 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 7.82 | 8.83 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 12.68 | 13.06 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 258.37 | 359.96 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 1.43 | 2.90 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 2.99 | 3.04 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 26.58 | 29.90 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 171.25 | 175.20 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 215.25 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 330.56 | 5.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 1410.96 | 13.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 7258.59 | 159.47 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 3.92 | 6.63 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 4.65 | 7.48 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 21.87 | 80.47 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 166.40 | 518.13 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.20 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.28 | 0.33 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.51 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 159.40 | 160.87 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 0.99 | 1.03 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 1.39 | 2.46 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 2.77 | 2.95 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 23.87 | 26.58 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 281.15 | 313.64 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1.51 | 1.55 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 2.26 | 4.72 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 39.85 | 45.90 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 189.39 | 196.61 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 769.08 | 6.37 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 795.10 | 16.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 7796.87 | 88.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 7306.53 | 131.58 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 17.00 | 20.95 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 38.12 | 150.71 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 72.68 | 237.96 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 77.41 | 211.86 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.22 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.74 | 0.82 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 2.45 | 2.69 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 186.78 | 188.57 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.40 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 1.02 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 12.25 | 12.92 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 28.89 | 34.93 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 212.46 | 214.47 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 356.89 | 804.99 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 2.21 | 2.26 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 10.39 | 11.77 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 11.07 | 12.56 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 180.21 | 185.44 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 298.88 | 1.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 952.81 | 20.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 3192.46 | 42.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 6163.60 | 79.93 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 3.51 | 8.04 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 6.25 | 10.58 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 42.04 | 75.93 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 69.22 | 268.34 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.37 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 1.18 | 1.25 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 3.01 | 4.05 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 304.60 | 308.34 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.19 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.90 | 2.24 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 1.18 | 1.40 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 2.93 | 3.28 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1.87 | 2.03 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 13.86 | 30.11 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 25.87 | 26.32 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 127.44 | 151.86 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1.63 | 1.65 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 11.20 | 22.62 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 25.98 | 27.44 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 74.22 | 82.27 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1301.99 | 3.43 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 3017.64 | 62.71 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 16554.08 | 132.41 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 157389.63 | 1472.05 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 10.62 | 12.19 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 62.18 | 88.30 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 140.18 | 148.67 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 299.95 | 1198.61 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.17 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.30 | 0.64 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.49 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 2582.34 | 2611.89 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.26 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 2216.72 | 2274.61 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.40 | 0.41 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 2.49 | 2.59 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 3.08 | 3.15 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 5.54 | 5.97 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 2.90 | 2.92 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 12.82 | 28.91 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 593.39 | 616.70 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | no | 2418.54 | 2461.52 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 293.49 | 2.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 1400.01 | 7.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 787.47 | 10.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 4030.45 | 58.24 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 4.71 | 7.95 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 5.51 | 8.66 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 22.15 | 31.03 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 43.51 | 149.28 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 2.95 | 10.42 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 8.95 | 17.25 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.35 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 0.53 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 0.79 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 2.92 | 4.28 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 1.22 | 3.24 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 2.66 | 2.79 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 4.79 | 6.02 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 89.64 | 93.21 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260727T070156Z.json) | yes | 1.16 | 1.19 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 3.18 | 4.54 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260727T070156Z.json) | yes | 28.15 | 32.78 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260727T070156Z.json) | yes | 167.56 | 170.19 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 210.98 | 0.38 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 1.81 | 4.49 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.23 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.15 | 0.15 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 0.21 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 2246.68 | 39.77 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 35.51 | 59.72 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 77.16 | 118.23 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260727T070156Z.json) | yes | 6.64 | 6.82 | 100% | 75.00 | 0.00 | pass |
