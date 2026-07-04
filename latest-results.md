# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260704T065705Z.json`

- Generated at: 20260704T065705Z
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
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 6 | 3568.30 | 3.28 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 8 | 9176.82 | 18.26 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 6 | 34869.03 | 59.88 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 6 | 202436.12 | 337.68 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 470.11 | 2.80 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 792.96 | 10.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 4023.41 | 67.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 7391.35 | 90.02 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.82 | 2.13 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 6.59 | 11.09 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 32.85 | 128.47 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 83.90 | 122.73 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.26 | 0.28 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.98 | 1.10 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2.77 | 4.06 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 186.06 | 187.16 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.37 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 1.02 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 1.12 | 2.73 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 4.08 | 4.43 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 9.28 | 11.10 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 14.36 | 16.76 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 294.39 | 420.04 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.97 | 2.51 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 2.48 | 2.51 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 33.69 | 37.97 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 175.04 | 176.10 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 226.42 | 2.11 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 351.31 | 6.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 1409.22 | 13.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 7608.65 | 165.54 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 4.33 | 7.59 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 5.61 | 8.54 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 23.70 | 84.21 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 185.65 | 578.27 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.20 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.47 | 0.52 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 1.28 | 4.40 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 165.68 | 171.01 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.34 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 1.04 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2.21 | 4.31 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 3.01 | 3.38 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 23.33 | 27.80 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 285.30 | 334.26 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.54 | 1.57 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2.61 | 3.93 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 37.06 | 42.08 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 190.03 | 191.85 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 831.29 | 6.95 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 896.75 | 19.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 7871.02 | 90.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 7668.42 | 131.15 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 19.04 | 23.24 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 40.15 | 158.23 | 100% | 39.00 | -232.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 49.56 | 102.72 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 71.86 | 235.81 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.26 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.60 | 0.67 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2.70 | 3.57 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 192.53 | 196.60 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.38 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 1.01 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 13.47 | 14.14 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 29.17 | 59.75 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 222.32 | 228.36 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 367.42 | 842.02 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.81 | 1.84 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 10.51 | 12.70 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 23.54 | 57.60 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 190.32 | 197.95 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 310.12 | 1.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 883.59 | 17.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 3333.49 | 44.29 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 6783.57 | 85.43 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 3.93 | 8.60 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 6.60 | 12.24 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 60.17 | 121.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 73.57 | 280.46 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.37 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 1.31 | 1.65 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 3.26 | 3.67 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 310.63 | 314.96 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.19 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.38 | 0.80 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.41 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 1.07 | 1.24 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.80 | 2.10 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 6.14 | 8.47 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 28.27 | 28.55 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 131.72 | 168.72 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.51 | 1.54 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 3.59 | 5.08 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 26.99 | 27.81 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 81.40 | 86.57 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1412.36 | 3.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2993.37 | 61.93 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 16746.54 | 135.95 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 168781.17 | 1491.31 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 12.06 | 13.43 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 56.99 | 80.60 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 134.05 | 140.43 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 304.24 | 1200.28 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.22 | 0.24 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.48 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.65 | 2.01 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 2583.57 | 2652.58 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.25 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.53 | 0.84 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 2242.78 | 2423.15 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 2.46 | 2.51 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 2.98 | 3.17 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 4.46 | 11.55 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 6.26 | 7.38 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.52 | 0.54 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 2.68 | 2.73 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 615.51 | 640.02 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | no | 2493.70 | 2535.45 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 318.01 | 2.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 1485.35 | 8.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 829.85 | 11.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 4202.95 | 62.64 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 5.41 | 8.47 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 6.84 | 10.01 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 23.34 | 31.04 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 50.02 | 154.17 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 0.48 | 0.52 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 3.09 | 10.93 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 8.97 | 17.07 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.33 | 0.34 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 0.50 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 1.07 | 1.98 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 11.75 | 39.34 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 1.19 | 3.05 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 3.52 | 3.99 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 5.86 | 7.89 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 91.04 | 94.77 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260704T065705Z.json) | yes | 1.48 | 1.51 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2.72 | 4.79 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260704T065705Z.json) | yes | 29.95 | 36.13 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260704T065705Z.json) | yes | 178.11 | 188.94 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 214.74 | 0.27 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.85 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.24 | 0.25 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 0.21 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 2214.24 | 38.20 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 17.69 | 30.98 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 90.67 | 132.48 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260704T065705Z.json) | yes | 6.24 | 6.72 | 100% | 75.00 | 0.00 | pass |
