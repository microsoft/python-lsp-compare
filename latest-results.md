# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260625T070552Z.json`

- Generated at: 20260625T070552Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.53 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.53/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 6 | 3379.02 | 2.98 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 8 | 9817.70 | 21.11 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 6 | 34041.43 | 58.29 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 6 | 199147.41 | 334.03 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 433.44 | 2.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 850.23 | 12.53 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 3859.00 | 61.61 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 6916.06 | 84.06 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1.63 | 1.73 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 6.08 | 9.08 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 29.55 | 115.24 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 43.23 | 50.64 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.30 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.93 | 0.99 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2.16 | 2.35 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 191.85 | 202.47 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.40 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 1.04 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 4.61 | 4.87 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 8.39 | 10.06 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 17.95 | 18.45 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 272.27 | 376.05 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 3.04 | 3.07 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 12.80 | 41.52 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 28.38 | 31.83 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 179.56 | 180.77 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 225.27 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 325.32 | 5.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 1363.81 | 12.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 7613.78 | 171.77 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 4.45 | 7.65 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 4.60 | 6.89 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 21.69 | 84.24 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 209.70 | 470.73 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.37 | 0.40 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.48 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 169.89 | 171.50 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.35 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.36 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 1.08 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2.01 | 3.08 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 2.92 | 2.98 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 21.85 | 22.99 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 282.46 | 312.19 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.62 | 0.67 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1.81 | 1.84 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 34.80 | 39.72 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 195.70 | 195.94 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 778.48 | 6.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 859.63 | 16.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 8226.20 | 95.14 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 7473.43 | 141.93 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 17.09 | 20.74 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 39.28 | 149.71 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 71.54 | 244.23 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 112.70 | 350.86 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.65 | 0.72 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 5.24 | 5.90 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 197.97 | 199.20 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.24 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.42 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 11.67 | 12.87 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 19.53 | 33.62 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 205.97 | 209.13 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 392.44 | 920.85 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 2.30 | 2.31 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 10.66 | 13.42 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 16.70 | 50.43 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 191.98 | 195.96 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 305.78 | 1.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 831.17 | 16.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 3254.72 | 44.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 6605.66 | 82.46 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 3.68 | 8.39 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 6.86 | 12.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 31.05 | 53.57 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 67.96 | 261.60 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 1.16 | 1.28 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 3.65 | 5.15 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 325.91 | 330.16 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.22 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 1.24 | 1.51 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2.92 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1.86 | 1.94 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 5.54 | 16.36 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 27.28 | 27.42 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 132.81 | 169.57 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 1.16 | 3.04 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1.68 | 1.70 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 26.83 | 26.96 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 81.39 | 89.81 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1328.21 | 3.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2914.63 | 60.12 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 15922.10 | 127.62 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 166533.93 | 1463.56 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 10.29 | 11.96 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 47.28 | 84.40 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 141.12 | 146.26 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 290.81 | 1148.77 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.23 | 0.26 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.48 | 0.59 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 2498.26 | 2566.91 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.28 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.43 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 2208.33 | 2239.48 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 2.39 | 2.47 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 2.80 | 2.84 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 6.80 | 8.33 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 7.44 | 21.61 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 1.81 | 5.00 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 2.60 | 2.63 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 583.10 | 606.79 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | no | 2467.71 | 2511.43 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 307.84 | 2.11 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 1415.59 | 8.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 779.15 | 9.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 4004.56 | 60.43 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 5.46 | 8.39 | 100% | 454.00 | +440.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 5.56 | 11.48 | 100% | 14.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 21.40 | 24.78 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 39.08 | 138.67 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.56 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2.75 | 9.53 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 12.02 | 19.66 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.39 | 0.43 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 0.53 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 0.90 | 1.18 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 2.28 | 2.33 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 1.77 | 3.57 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 2.86 | 2.99 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 4.55 | 6.68 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 91.35 | 93.19 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260625T070552Z.json) | yes | 1.49 | 1.54 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 2.51 | 4.31 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260625T070552Z.json) | yes | 30.62 | 36.23 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260625T070552Z.json) | yes | 175.08 | 175.76 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 203.93 | 0.39 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 1.69 | 4.11 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.27 | 0.28 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 0.24 | 0.28 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 3053.63 | 88.52 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 83.63 | 107.57 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 128.74 | 142.34 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260625T070552Z.json) | yes | 53.18 | 61.82 | 100% | 75.00 | 0.00 | pass |
