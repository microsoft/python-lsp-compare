# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260630T071214Z.json`

- Generated at: 20260630T071214Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.55 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.55/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 6 | 3472.83 | 3.17 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 8 | 9225.38 | 18.64 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 6 | 37164.71 | 67.20 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 6 | 210889.33 | 350.03 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 433.06 | 2.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 804.92 | 10.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 4030.11 | 64.76 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 7792.69 | 91.61 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.82 | 1.96 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 5.83 | 9.60 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 33.26 | 122.60 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 60.84 | 82.30 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 1.01 | 1.15 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.43 | 2.67 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 200.73 | 207.88 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.40 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 1.07 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 4.48 | 5.00 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 8.15 | 9.05 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 14.50 | 20.09 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 287.26 | 394.93 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 2.52 | 2.59 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 3.15 | 4.69 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 29.30 | 32.34 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 190.96 | 195.88 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 232.85 | 2.07 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 317.70 | 5.36 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 1455.79 | 14.49 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 8115.69 | 181.83 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 4.25 | 7.68 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 5.21 | 8.01 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 22.46 | 79.81 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 207.36 | 627.29 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.50 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.40 | 4.90 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 179.34 | 182.74 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 1.08 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 1.09 | 1.13 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 2.98 | 3.22 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 26.59 | 28.13 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 304.37 | 343.19 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.64 | 0.66 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.74 | 1.78 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 40.74 | 46.05 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 216.99 | 233.92 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 785.27 | 6.67 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 871.12 | 19.47 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 9584.39 | 127.66 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 8166.80 | 155.89 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 18.11 | 22.42 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 37.86 | 149.53 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 89.38 | 303.23 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 122.19 | 380.93 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.28 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.76 | 0.87 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 5.30 | 5.87 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 220.17 | 237.96 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.37 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 1.08 | 1.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.91 | 2.96 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 12.89 | 13.15 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 34.69 | 55.30 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 230.76 | 233.79 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 537.58 | 1042.67 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.88 | 1.90 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 10.19 | 13.23 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 16.60 | 49.73 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 205.24 | 208.44 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 322.31 | 1.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 816.44 | 15.48 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 3460.21 | 46.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 7055.64 | 88.71 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 3.84 | 8.46 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 7.24 | 11.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 34.42 | 57.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 68.59 | 267.40 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 1.29 | 1.65 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 1.37 | 2.50 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 348.76 | 356.88 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 1.23 | 1.45 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.86 | 2.06 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 5.69 | 10.60 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 30.33 | 31.54 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 136.35 | 170.85 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 1.54 | 3.11 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.60 | 1.64 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 28.79 | 29.62 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 85.54 | 93.49 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1382.41 | 3.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 3122.18 | 66.10 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 17151.27 | 141.39 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 175415.01 | 1516.33 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 12.14 | 13.47 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 53.81 | 86.75 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 150.89 | 154.11 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 294.50 | 1176.33 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.38 | 0.81 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.46 | 0.50 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 2597.83 | 2652.23 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.28 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.50 | 0.74 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 2282.43 | 2369.09 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 2.62 | 2.83 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 3.21 | 3.26 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 6.89 | 8.04 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 25.05 | 48.19 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 2.77 | 2.82 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 10.52 | 33.02 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 645.31 | 671.78 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | no | 2547.88 | 2556.58 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 316.92 | 2.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 1482.94 | 8.73 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 847.01 | 11.83 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 4343.51 | 65.79 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 5.73 | 11.95 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 6.18 | 8.77 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 25.80 | 31.34 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 50.53 | 155.01 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.49 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.89 | 10.13 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 12.72 | 15.03 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.39 | 0.42 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 0.56 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 0.92 | 1.42 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 3.27 | 3.37 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.53 | 3.82 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 3.12 | 3.28 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 5.17 | 6.15 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 101.05 | 103.27 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260630T071214Z.json) | yes | 1.46 | 1.48 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2.79 | 4.88 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260630T071214Z.json) | yes | 31.35 | 39.00 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260630T071214Z.json) | yes | 186.10 | 187.83 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 210.27 | 0.42 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 1.72 | 4.18 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.34 | 0.35 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 0.25 | 0.28 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 2235.72 | 38.64 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 18.16 | 32.30 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 90.30 | 131.50 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260630T071214Z.json) | yes | 7.47 | 7.64 | 100% | 75.00 | 0.00 | pass |
