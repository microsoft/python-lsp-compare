# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260726T065138Z.json`

- Generated at: 20260726T065138Z
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
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 6 | 3646.41 | 3.37 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 8 | 9755.81 | 20.49 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 6 | 37777.26 | 65.55 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 6 | 214176.20 | 353.46 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 541.91 | 3.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 836.82 | 12.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 4265.28 | 69.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 7859.37 | 116.21 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 1.84 | 2.02 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 7.45 | 14.85 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 34.78 | 126.92 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 207.97 | 362.75 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.33 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.72 | 1.96 | 100% | 3604.00 | -415.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 1.84 | 3.73 | 100% | 4019.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 187.30 | 193.85 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.45 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 1.11 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 4.70 | 5.01 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 10.09 | 12.06 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 20.95 | 45.52 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 303.17 | 426.78 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 3.31 | 3.39 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 4.90 | 5.61 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 33.20 | 38.13 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 179.96 | 184.69 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 227.56 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 328.90 | 5.61 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 1563.63 | 15.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 8176.35 | 163.72 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 5.07 | 8.03 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 5.11 | 8.57 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 22.94 | 82.48 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 136.58 | 376.73 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.56 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.39 | 4.63 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 166.91 | 169.81 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 1.11 | 1.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.26 | 3.68 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.08 | 1.12 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 2.94 | 3.29 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 27.97 | 29.19 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 319.09 | 367.76 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.36 | 3.38 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 1.66 | 1.70 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 41.74 | 48.90 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 194.91 | 198.27 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 834.15 | 7.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 906.36 | 16.37 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 9083.51 | 102.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 8032.71 | 148.02 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 19.64 | 26.21 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 39.51 | 151.54 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 93.91 | 319.82 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 117.38 | 366.93 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.29 | 0.33 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.71 | 0.80 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 4.88 | 6.85 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 191.69 | 195.71 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.42 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 1.09 | 1.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 3.49 | 5.30 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 12.70 | 20.93 | 100% | 256.00 | -185.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 14.37 | 14.77 | 100% | 448.00 | +7.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 236.71 | 244.80 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 404.96 | 931.26 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 2.40 | 2.62 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 12.28 | 15.75 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 21.25 | 58.61 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 193.23 | 207.28 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 314.13 | 1.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 906.55 | 18.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 3525.27 | 47.87 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 6757.19 | 86.77 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 3.66 | 8.47 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 7.35 | 12.99 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 36.62 | 76.85 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 71.30 | 275.95 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.38 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 1.34 | 1.75 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 4.22 | 7.09 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 337.16 | 339.03 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 1.22 | 1.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 3.12 | 5.33 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 2.21 | 2.53 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 5.09 | 5.76 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 30.00 | 30.55 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 140.41 | 171.63 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 1.81 | 1.82 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 7.26 | 10.78 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 28.87 | 29.22 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 89.82 | 95.10 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 1425.29 | 3.73 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 2997.73 | 62.16 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 17839.22 | 149.73 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 178970.83 | 1542.62 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 11.87 | 12.47 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 58.81 | 94.13 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 146.37 | 148.21 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 296.09 | 1182.67 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.22 | 0.24 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.30 | 0.51 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.50 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 2718.12 | 2818.87 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.48 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 2301.20 | 2414.54 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 2.58 | 2.68 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 3.21 | 3.35 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 6.96 | 8.08 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 13.79 | 25.31 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.48 | 0.51 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 2.99 | 3.04 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 681.90 | 711.74 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | no | 2544.82 | 2565.82 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 303.37 | 2.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 1500.36 | 8.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 818.31 | 10.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 4379.76 | 63.44 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 5.54 | 10.02 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 6.44 | 9.37 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 25.25 | 34.58 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 45.80 | 149.71 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.51 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 2.96 | 10.44 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 9.74 | 15.27 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.37 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 0.53 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 0.79 | 0.96 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 2.78 | 3.35 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.88 | 3.84 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 2.85 | 3.02 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 5.35 | 6.74 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 101.64 | 102.50 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260726T065138Z.json) | yes | 1.16 | 1.21 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 1.37 | 1.44 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260726T065138Z.json) | yes | 32.14 | 36.83 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260726T065138Z.json) | yes | 177.81 | 181.74 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 217.48 | 0.30 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.94 | 1.02 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.29 | 0.31 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 0.23 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 2743.68 | 70.29 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 18.56 | 31.72 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 132.75 | 139.69 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260726T065138Z.json) | yes | 59.56 | 76.74 | 100% | 75.00 | 0.00 | pass |
