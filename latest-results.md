# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260619T074558Z.json`

- Generated at: 20260619T074558Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.51 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.51/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 6 | 3608.52 | 3.34 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 8 | 9679.98 | 20.71 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 6 | 35791.75 | 65.12 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 6 | 210502.34 | 352.52 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 501.98 | 3.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 772.07 | 10.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 3498.98 | 52.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 7469.07 | 89.64 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.82 | 1.97 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 6.83 | 12.19 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 32.48 | 116.75 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 46.07 | 49.69 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.33 | 0.34 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 1.08 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.47 | 2.72 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 200.71 | 203.06 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.50 | 0.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 1.04 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 5.05 | 6.01 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 13.14 | 13.45 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 16.82 | 40.49 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 220.10 | 310.41 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 2.46 | 2.55 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.77 | 2.87 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 32.48 | 37.95 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 195.30 | 197.12 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 237.36 | 2.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 319.54 | 4.97 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 1347.10 | 14.94 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 8222.98 | 186.64 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 4.98 | 7.26 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 5.08 | 7.51 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 20.48 | 80.06 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 238.43 | 577.77 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.25 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.29 | 0.34 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.51 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 179.81 | 181.86 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.47 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.49 | 1.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 1.11 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.48 | 4.06 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 3.19 | 3.65 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 24.20 | 27.28 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 307.53 | 348.51 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 1.38 | 3.55 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.90 | 2.01 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 44.45 | 47.67 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 206.33 | 207.03 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 812.23 | 6.84 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 730.76 | 14.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 8928.06 | 123.40 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 8159.27 | 155.80 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 18.55 | 22.60 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 39.79 | 149.82 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 87.14 | 286.51 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 123.79 | 379.99 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.29 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.96 | 1.12 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.81 | 3.11 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 211.10 | 217.13 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.50 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 1.04 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 13.20 | 13.66 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 22.05 | 31.37 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 236.75 | 244.52 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 518.35 | 1014.73 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.95 | 1.97 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 5.87 | 14.94 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 10.03 | 11.57 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 206.32 | 216.10 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3120.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 330.57 | 1.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 944.41 | 19.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 3321.38 | 46.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 6966.50 | 89.28 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 3.86 | 8.69 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 8.05 | 13.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 47.89 | 74.86 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 71.30 | 277.94 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.39 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 1.32 | 1.64 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.08 | 4.61 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 339.43 | 345.69 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 1.12 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.99 | 2.24 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 11.11 | 26.25 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 29.46 | 30.03 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 136.90 | 166.24 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.70 | 1.74 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 14.37 | 31.11 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 28.50 | 29.47 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 84.53 | 92.51 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1401.19 | 3.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2979.52 | 62.29 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 17358.66 | 145.11 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 175390.83 | 1528.27 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 11.60 | 12.82 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 55.56 | 87.58 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 149.05 | 150.43 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 296.91 | 1171.91 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.25 | 0.29 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.49 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.52 | 1.29 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 2638.14 | 2726.95 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 2280.87 | 2349.96 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 2.88 | 3.05 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 2.97 | 3.17 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 7.44 | 8.61 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 13.17 | 33.06 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.59 | 0.63 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 2.70 | 2.73 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 661.65 | 681.57 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | no | 2570.41 | 2600.99 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 325.19 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 1337.56 | 8.85 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 837.54 | 11.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 4293.68 | 65.47 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 5.43 | 8.61 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 6.13 | 9.81 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 25.90 | 32.71 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 48.47 | 150.93 | 100% | 273.40 | +259.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 0.60 | 0.70 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.88 | 10.11 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 11.46 | 14.95 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.37 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 0.55 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 1.65 | 4.00 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 2.36 | 2.49 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 2.89 | 3.03 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 3.09 | 4.38 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 4.49 | 5.95 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 101.09 | 102.19 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260619T074558Z.json) | yes | 1.58 | 1.59 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2.75 | 4.70 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260619T074558Z.json) | yes | 32.07 | 36.35 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260619T074558Z.json) | yes | 186.55 | 188.30 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 273.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 211.60 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.98 | 1.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.28 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 0.23 | 0.25 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 2884.54 | 76.10 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 50.54 | 90.62 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 129.25 | 135.93 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260619T074558Z.json) | yes | 48.51 | 50.49 | 100% | 75.00 | 0.00 | pass |
