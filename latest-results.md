# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260720T065915Z.json`

- Generated at: 20260720T065915Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.61 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.61/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 6 | 3796.94 | 3.62 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 8 | 9007.00 | 17.50 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 6 | 38973.12 | 71.95 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 6 | 217840.26 | 358.42 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 519.83 | 3.37 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 794.66 | 11.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 4455.20 | 77.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 8078.27 | 93.79 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1.77 | 1.94 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 6.73 | 12.58 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 35.02 | 128.06 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 88.12 | 147.65 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1.75 | 3.60 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 4.77 | 6.42 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 190.57 | 195.70 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.44 | 0.58 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.81 | 1.72 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 1.08 | 1.18 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 5.00 | 5.25 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 10.89 | 12.69 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 14.12 | 18.86 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 345.12 | 442.28 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 1.67 | 3.48 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 3.66 | 3.75 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 34.50 | 39.05 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 184.15 | 186.38 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 226.27 | 1.97 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 340.48 | 6.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1473.80 | 13.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 8563.77 | 186.53 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 4.17 | 7.04 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 4.83 | 7.02 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 25.09 | 85.15 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 215.69 | 684.50 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.25 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.45 | 0.89 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.51 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 174.02 | 176.82 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.38 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 1.12 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 2.97 | 3.45 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 3.56 | 9.59 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 25.31 | 27.99 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 337.93 | 393.48 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.68 | 0.70 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1.62 | 1.67 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 38.82 | 47.31 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 203.88 | 205.46 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 836.70 | 7.22 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 800.63 | 16.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 9575.47 | 131.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 8320.52 | 146.80 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 18.54 | 22.34 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 41.88 | 157.24 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 85.02 | 285.04 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 97.49 | 283.77 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.28 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.78 | 0.90 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 2.86 | 3.55 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 199.83 | 202.26 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 1.09 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 14.67 | 15.33 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 31.04 | 47.80 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 244.06 | 249.99 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 562.13 | 1100.88 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 2.39 | 2.44 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 5.59 | 13.55 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 11.26 | 12.45 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 191.52 | 193.54 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 325.04 | 1.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 830.48 | 16.18 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 3614.39 | 48.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 7228.18 | 98.11 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 3.88 | 8.71 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 7.70 | 13.84 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 67.61 | 126.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 69.36 | 275.27 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.41 | 0.44 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 1.07 | 1.33 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1.36 | 1.53 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 355.95 | 395.14 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.44 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 1.36 | 1.62 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 2.15 | 2.53 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 5.08 | 8.70 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 32.69 | 34.81 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 142.26 | 171.94 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1.84 | 1.90 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 5.14 | 8.83 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 32.97 | 37.35 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 92.46 | 101.96 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1516.92 | 4.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 3068.38 | 63.41 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 18286.13 | 149.82 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 181342.71 | 1560.04 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 14.77 | 16.53 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 59.11 | 95.11 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 153.22 | 155.38 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 305.71 | 1205.35 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.26 | 0.28 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.55 | 0.65 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 2712.50 | 2791.82 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.32 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1.04 | 2.40 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 1.10 | 2.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 2334.47 | 2430.92 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 2.75 | 3.01 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 4.01 | 5.11 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 4.39 | 12.79 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 7.14 | 9.59 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 3.20 | 3.34 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 5.57 | 13.83 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 681.26 | 701.38 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | no | 2597.26 | 2626.19 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 372.16 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1568.13 | 9.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 860.48 | 11.60 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 4306.81 | 65.25 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 7.17 | 12.55 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 7.33 | 11.24 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 25.95 | 34.50 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 50.87 | 163.04 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 0.26 | 0.28 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 0.66 | 0.70 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 3.23 | 11.25 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 10.57 | 15.45 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.41 | 0.43 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 1.00 | 1.10 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1.28 | 2.82 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 3.35 | 3.98 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.68 | 0.74 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 4.38 | 5.95 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 6.30 | 8.06 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 104.84 | 106.32 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260720T065915Z.json) | yes | 1.37 | 1.52 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 2.79 | 5.27 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260720T065915Z.json) | yes | 32.83 | 37.50 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260720T065915Z.json) | yes | 181.55 | 218.67 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 220.58 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.98 | 1.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.27 | 0.28 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 0.24 | 0.26 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 2091.32 | 30.38 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 27.33 | 52.35 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 56.41 | 58.18 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260720T065915Z.json) | yes | 7.42 | 7.78 | 100% | 75.00 | 0.00 | pass |
