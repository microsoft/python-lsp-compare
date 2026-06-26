# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260626T071222Z.json`

- Generated at: 20260626T071222Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.54 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.54/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 6 | 3391.49 | 3.03 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 8 | 9283.77 | 18.65 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 6 | 36185.35 | 66.50 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 6 | 231916.24 | 343.11 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 435.63 | 2.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 818.31 | 11.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 3988.70 | 64.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 7414.73 | 87.36 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.64 | 1.79 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 5.84 | 8.71 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 33.22 | 119.85 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 45.86 | 51.74 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 1.10 | 1.25 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.81 | 2.22 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 198.98 | 211.87 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.27 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.42 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 4.45 | 4.50 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 8.22 | 11.39 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 19.43 | 42.91 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 287.63 | 401.02 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 2.52 | 2.58 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 3.27 | 4.89 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 29.56 | 33.96 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 186.44 | 188.71 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 227.63 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 317.27 | 5.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 1431.64 | 13.82 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 7973.05 | 177.23 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 4.07 | 7.48 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 4.93 | 7.70 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 22.58 | 78.09 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 205.19 | 623.67 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.24 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.53 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.48 | 3.93 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 176.34 | 178.14 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.10 | 1.14 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 2.83 | 3.03 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 24.32 | 27.23 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 298.48 | 336.43 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.64 | 0.66 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.72 | 1.89 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 39.75 | 46.18 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 205.09 | 208.59 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 778.04 | 6.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 766.29 | 13.35 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 9134.64 | 127.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 7920.56 | 153.17 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 17.78 | 21.33 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 40.34 | 153.31 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 72.31 | 240.65 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 132.48 | 423.83 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.26 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.63 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 5.04 | 7.23 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 207.26 | 208.40 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 1.06 | 1.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2.52 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 12.11 | 12.92 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 17.99 | 27.04 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 225.53 | 237.16 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 552.90 | 1084.56 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.87 | 0.92 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.88 | 1.97 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 11.92 | 15.64 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 199.52 | 201.38 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 305.70 | 1.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 751.57 | 13.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 3353.61 | 44.82 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 6870.60 | 85.99 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 3.64 | 8.10 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 6.81 | 12.32 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 25.81 | 32.00 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 66.58 | 263.14 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.39 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.01 | 1.08 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 1.24 | 1.63 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 346.51 | 383.13 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 1.17 | 1.45 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.77 | 0.81 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.85 | 2.03 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 28.46 | 28.70 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 132.53 | 166.53 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.48 | 0.50 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.59 | 1.64 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 28.01 | 28.39 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 83.08 | 93.86 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1332.72 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2950.51 | 60.84 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 16835.50 | 139.64 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 197535.09 | 1491.36 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 11.01 | 12.30 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 51.30 | 81.87 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 156.74 | 160.89 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 293.26 | 1153.70 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.46 | 0.51 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.23 | 2.83 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 2560.04 | 2607.29 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.28 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.43 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 2239.55 | 2315.54 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 2.61 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 2.75 | 2.80 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 6.26 | 6.76 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 6.72 | 16.55 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 2.55 | 2.57 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2.71 | 9.35 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 639.72 | 667.44 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | no | 2497.84 | 2539.31 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 311.76 | 2.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 1441.27 | 8.22 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 866.16 | 11.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 4202.22 | 63.55 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 4.71 | 7.88 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 5.95 | 8.90 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 24.38 | 31.12 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 49.96 | 158.77 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.23 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.50 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2.87 | 10.12 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 10.70 | 14.02 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.38 | 0.41 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 0.54 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 0.79 | 0.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 2.33 | 2.40 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2.42 | 3.73 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 3.04 | 3.40 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 5.01 | 5.99 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 96.82 | 99.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260626T071222Z.json) | yes | 1.47 | 1.50 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.95 | 3.81 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260626T071222Z.json) | yes | 30.08 | 35.14 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260626T071222Z.json) | yes | 183.50 | 184.32 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 214.98 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 1.73 | 4.11 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.27 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 0.24 | 0.25 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 2598.67 | 59.89 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 41.16 | 67.23 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 117.96 | 128.12 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260626T071222Z.json) | yes | 20.55 | 27.28 | 100% | 75.00 | 0.00 | pass |
