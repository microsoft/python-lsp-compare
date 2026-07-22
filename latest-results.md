# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260722T064821Z.json`

- Generated at: 20260722T064821Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.62 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.62/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 6 | 3452.64 | 3.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 8 | 9385.85 | 19.83 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 6 | 36124.86 | 66.95 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 6 | 205843.99 | 341.29 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 470.63 | 3.29 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 816.96 | 11.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 4135.22 | 64.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 7362.69 | 108.71 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 1.56 | 1.70 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 6.03 | 9.66 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 33.66 | 120.03 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 194.56 | 338.93 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.29 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 1.62 | 3.24 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.02 | 2.41 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 176.27 | 177.16 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.41 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.79 | 2.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 4.45 | 4.69 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 10.29 | 12.71 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 20.27 | 44.61 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 287.54 | 392.57 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 3.21 | 4.98 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 4.12 | 4.55 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 28.67 | 32.02 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 167.23 | 169.61 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 221.72 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 315.27 | 5.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 1422.08 | 13.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 7564.98 | 165.85 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 4.23 | 7.38 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 4.46 | 6.76 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 19.68 | 76.98 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 192.68 | 610.44 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.22 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.29 | 0.33 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.56 | 0.65 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 157.62 | 159.93 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.40 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 2.78 | 2.90 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 4.21 | 7.75 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 24.40 | 27.27 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 292.93 | 328.93 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.61 | 0.65 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 1.66 | 1.73 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 39.35 | 44.64 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 184.97 | 186.59 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 820.44 | 7.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 732.57 | 14.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 9179.47 | 130.43 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 7429.22 | 135.77 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 19.50 | 23.64 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 38.46 | 148.40 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 75.43 | 251.23 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 95.57 | 285.00 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.27 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.76 | 0.87 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.73 | 3.08 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 187.13 | 196.31 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.40 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 1.03 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 13.91 | 14.38 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 25.87 | 58.78 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 217.58 | 224.60 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 565.18 | 1118.70 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 2.48 | 2.76 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.76 | 8.53 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 10.37 | 13.16 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 177.55 | 181.56 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 301.76 | 1.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 811.28 | 16.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 3280.62 | 44.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 6719.37 | 83.63 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 3.44 | 7.82 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 6.78 | 11.20 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 41.12 | 74.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 68.85 | 266.79 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.37 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 1.25 | 1.53 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 3.67 | 5.47 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 319.78 | 325.15 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.38 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.52 | 1.22 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 1.27 | 1.53 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 2.02 | 2.20 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 3.17 | 5.08 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 28.63 | 29.18 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 131.30 | 160.02 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 1.72 | 1.75 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 3.95 | 6.83 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 27.37 | 27.57 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 82.64 | 95.79 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 1335.59 | 3.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2990.09 | 62.65 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 16676.76 | 140.14 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 172413.24 | 1488.36 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 10.16 | 11.48 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 53.74 | 84.00 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 139.71 | 140.55 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 294.94 | 1160.12 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.48 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.93 | 2.98 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 2608.42 | 2695.14 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.92 | 2.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 2199.32 | 2261.79 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 2.52 | 2.69 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 3.06 | 3.09 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 6.43 | 13.91 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 6.45 | 7.44 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 2.88 | 2.89 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 6.05 | 22.62 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 639.62 | 673.16 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | no | 2491.83 | 2518.05 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 302.50 | 2.18 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 1430.71 | 7.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 834.95 | 11.40 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 4354.49 | 65.41 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 4.82 | 7.77 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 6.27 | 8.93 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 24.15 | 30.08 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 50.05 | 148.00 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.48 | 0.53 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2.86 | 10.03 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 8.95 | 13.37 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 0.55 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 0.74 | 0.88 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 2.44 | 3.18 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 1.81 | 3.63 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 2.72 | 3.08 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 4.83 | 5.84 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 106.01 | 109.28 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260722T064821Z.json) | yes | 1.15 | 1.18 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 1.93 | 3.69 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260722T064821Z.json) | yes | 29.11 | 33.43 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260722T064821Z.json) | yes | 185.52 | 223.97 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 205.80 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 1.72 | 4.15 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.29 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 0.23 | 0.26 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 2678.92 | 68.18 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 19.05 | 35.30 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 122.54 | 148.79 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260722T064821Z.json) | yes | 62.95 | 79.31 | 100% | 75.00 | 0.00 | pass |
