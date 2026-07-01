# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260701T072414Z.json`

- Generated at: 20260701T072414Z
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
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 6 | 3589.71 | 3.23 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 8 | 9804.47 | 21.07 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 6 | 36593.97 | 67.25 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 6 | 204135.92 | 346.15 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 492.43 | 2.85 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 828.21 | 13.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 3864.61 | 60.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 7389.86 | 91.73 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.88 | 2.13 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 5.66 | 8.34 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 32.65 | 127.55 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 45.87 | 54.63 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.28 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 2.61 | 3.32 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 6.42 | 7.56 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 208.03 | 211.46 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.40 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 1.01 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 1.05 | 1.93 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 4.39 | 4.76 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 9.40 | 11.19 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 23.29 | 52.53 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 263.49 | 371.20 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 2.52 | 2.65 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 4.51 | 5.76 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 27.86 | 31.77 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 199.34 | 200.67 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 228.78 | 2.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 345.71 | 5.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 1395.32 | 13.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 8011.17 | 178.29 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 3.82 | 6.61 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 5.68 | 8.29 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 21.07 | 81.45 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 193.21 | 596.43 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.20 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.36 | 0.47 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.51 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 185.85 | 188.08 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 0.98 | 1.03 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2.30 | 2.91 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2.09 | 4.04 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 3.15 | 3.48 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 23.48 | 26.34 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 292.63 | 342.55 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.59 | 1.60 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 3.15 | 3.95 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 38.48 | 44.75 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 218.76 | 222.24 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 818.47 | 6.88 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 796.11 | 15.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 9488.42 | 137.55 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 8154.64 | 151.23 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 18.59 | 22.73 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 39.86 | 157.30 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 77.44 | 262.87 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 89.62 | 255.05 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.23 | 0.25 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 1.13 | 2.29 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2.54 | 2.87 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 212.85 | 214.05 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.17 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 1.37 | 1.45 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 13.56 | 13.95 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 30.96 | 54.87 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 236.59 | 242.78 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 598.38 | 1237.79 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.84 | 1.87 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 5.00 | 12.20 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 10.40 | 11.69 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 215.71 | 217.85 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 314.03 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 782.82 | 14.43 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 3333.52 | 45.28 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 6904.96 | 87.57 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 4.05 | 9.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 6.21 | 11.00 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 37.90 | 65.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 69.78 | 276.45 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.37 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.99 | 1.09 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 1.33 | 1.74 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 340.95 | 343.22 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.19 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 1.18 | 1.39 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.68 | 0.73 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.81 | 2.08 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 28.88 | 29.44 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 134.15 | 178.41 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.51 | 0.58 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.63 | 1.86 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 28.94 | 29.57 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 84.30 | 92.92 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1426.91 | 3.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 3053.70 | 64.32 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 17062.17 | 139.20 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 169507.03 | 1504.91 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 11.86 | 13.30 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 59.59 | 89.44 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 137.38 | 144.34 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 306.06 | 1222.89 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.17 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.21 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.47 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 2595.43 | 2760.83 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.25 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.53 | 0.72 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 2299.17 | 2398.02 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 2.58 | 2.85 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 2.91 | 3.02 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 6.20 | 6.91 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 9.99 | 17.89 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 2.69 | 2.72 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 5.18 | 9.61 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 629.22 | 673.72 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | no | 2489.96 | 2582.88 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 309.09 | 2.32 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 1449.95 | 8.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 813.73 | 10.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 4168.26 | 63.18 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 4.67 | 7.68 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 6.15 | 9.02 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 22.24 | 28.61 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 48.40 | 156.27 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.49 | 0.52 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2.97 | 10.54 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 10.90 | 15.36 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.35 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 0.51 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 0.80 | 0.92 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 2.11 | 2.22 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 1.19 | 3.06 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 3.32 | 3.78 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 5.30 | 6.50 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 94.63 | 96.62 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260701T072414Z.json) | yes | 1.46 | 1.48 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2.02 | 3.97 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260701T072414Z.json) | yes | 29.46 | 34.07 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260701T072414Z.json) | yes | 186.01 | 187.23 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 215.36 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 1.74 | 4.46 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.14 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.19 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.24 | 0.26 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.34 | 0.71 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 0.26 | 0.27 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 2968.82 | 78.83 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 46.74 | 78.09 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 120.41 | 125.51 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260701T072414Z.json) | yes | 69.35 | 97.47 | 100% | 75.00 | 0.00 | pass |
