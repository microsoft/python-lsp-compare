# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260927T060535Z.json`

- Generated at: 20260927T060535Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.84 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.84/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
| pylsp-mypy | 1.15.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pylsp-mypy/venv/bin/pylsp |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **Pyrefly**: Installed from PyPI into an isolated venv because GitHub release binaries are no longer published.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Wall clock ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 6 | 5079.98 | 4.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | no | 8 | 16961.98 | 38.50 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 6 | 38856.76 | 72.94 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 6 | 218633.21 | 369.89 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 487.97 | 3.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1088.58 | 22.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 4561.30 | 77.21 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 7863.89 | 112.38 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 1.60 | 1.74 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 5.37 | 9.00 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 84.80 | 335.27 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 215.05 | 509.12 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 1.13 | 1.51 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 2.57 | 3.15 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 176.10 | 177.63 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.46 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 1.03 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 4.12 | 4.24 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 12.01 | 13.11 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 24.39 | 35.16 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 347.48 | 487.62 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 2.60 | 3.39 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 5.56 | 5.62 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 31.62 | 33.88 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 165.58 | 166.49 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 266.08 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 298.87 | 5.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 1469.15 | 14.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 7810.15 | 175.06 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 4.69 | 7.42 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 4.77 | 7.22 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 16.11 | 63.12 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 219.55 | 675.07 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.27 | 0.33 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.50 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 155.05 | 156.69 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1.17 | 3.48 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1.91 | 1.94 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 4.80 | 5.17 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 26.37 | 28.95 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 253.29 | 284.96 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 3.15 | 3.19 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 5.86 | 12.71 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 40.43 | 45.66 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 246.34 | 252.35 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 866.86 | 8.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1423.14 | 37.93 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 7821.89 | 137.37 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 11588.10 | 178.39 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 20.07 | 27.80 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 85.57 | 290.79 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 87.72 | 350.04 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 87.86 | 199.83 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.89 | 1.21 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 5.40 | 7.63 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 194.70 | 206.22 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 5.11 | 5.92 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 16.83 | 18.22 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 57.26 | 87.14 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 224.47 | 228.99 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 793.86 | 1254.04 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 4.51 | 4.53 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 11.21 | 12.84 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 34.17 | 89.89 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 178.74 | 179.59 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 377.93 | 2.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 880.04 | 17.84 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 3795.74 | 51.28 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 7102.06 | 121.17 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 3.35 | 7.43 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 17.30 | 22.29 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 86.53 | 345.20 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 214.06 | 404.74 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.39 | 0.41 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.98 | 1.01 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 1.69 | 1.90 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 316.21 | 317.39 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.22 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.51 | 0.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 1.28 | 1.69 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.95 | 1.01 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 5.40 | 5.62 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 37.80 | 38.89 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 137.89 | 175.79 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.53 | 0.55 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 5.17 | 5.21 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 36.52 | 36.65 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 99.02 | 108.60 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 2725.60 | 4.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 15903.85 | 107.19 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 5414.77 | 170.64 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 183111.35 | 1565.53 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 11.07 | 12.28 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 48.30 | 79.50 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 148.82 | 151.73 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 847.92 | 3363.29 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.39 | 0.87 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.49 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1.37 | 2.78 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 2781.15 | 2824.53 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.46 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 2241.87 | 2288.17 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.65 | 0.80 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 2.48 | 2.55 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 6.15 | 6.29 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 6.87 | 7.38 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 3.01 | 3.43 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 5.88 | 5.96 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 479.84 | 507.62 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | no | 2653.34 | 2675.29 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 355.54 | 2.87 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 1538.61 | 9.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 856.33 | 12.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 4923.87 | 107.82 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 5.82 | 10.54 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 5.93 | 8.80 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 55.70 | 181.86 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 69.38 | 94.44 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.51 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 5.15 | 17.91 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 141.03 | 224.17 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.32 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 0.58 | 0.67 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 0.79 | 1.01 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 3.72 | 4.81 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.57 | 0.59 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 4.17 | 6.01 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 4.64 | 4.86 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 90.95 | 93.67 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 1.51 | 1.56 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260927T060535Z.json) | yes | 2.97 | 3.05 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20260927T060535Z.json) | yes | 34.15 | 38.51 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260927T060535Z.json) | yes | 234.00 | 237.11 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | no | 227.25 | 0.32 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.98 | 1.03 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.23 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 0.25 | 0.26 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 6772.98 | 80.28 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 17.41 | 26.78 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 168.47 | 193.24 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260927T060535Z.json) | yes | 54.97 | 70.13 | 100% | 75.00 | 0.00 | pass |
