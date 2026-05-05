# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260505T064131Z.json`

- Generated at: 20260505T064131Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.34 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.34/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.63.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 6 | 3974.92 | 3.43 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | no | 8 | 10054.29 | 19.70 | 201 | 98% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 6 | 33014.59 | 56.21 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 6 | 205571.25 | 336.88 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 552.86 | 4.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 884.63 | 12.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 3313.21 | 47.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 6936.46 | 85.12 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.61 | 1.78 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 5.64 | 9.12 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 37.19 | 146.36 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 51.18 | 55.97 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.31 | 0.32 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 1.02 | 1.07 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 8.48 | 18.83 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 188.82 | 190.31 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.49 | 0.63 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 4.21 | 4.31 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 14.21 | 15.95 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 17.75 | 18.64 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 201.55 | 297.51 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.61 | 0.65 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.98 | 2.00 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 28.87 | 32.27 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 180.34 | 182.39 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 240.30 | 1.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 339.56 | 5.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 1324.54 | 14.28 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 7634.67 | 169.65 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 4.53 | 7.60 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 5.02 | 8.32 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 21.76 | 85.72 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 194.01 | 623.48 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.23 | 0.25 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.27 | 0.36 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.52 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 169.96 | 170.76 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 1.06 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 2.06 | 4.33 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 2.64 | 2.78 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 22.64 | 25.61 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 286.60 | 314.42 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.39 | 1.42 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 1.60 | 3.56 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 43.29 | 47.08 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 196.64 | 197.79 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 857.81 | 6.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 815.13 | 15.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 7714.53 | 91.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 7481.88 | 138.89 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 17.11 | 21.88 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 41.14 | 163.28 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 71.43 | 236.25 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 91.11 | 276.52 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.26 | 0.28 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.86 | 1.41 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 2.01 | 2.09 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 199.66 | 200.91 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.49 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 1.06 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 13.56 | 15.87 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 27.39 | 53.81 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 211.06 | 215.48 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 373.96 | 815.39 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.73 | 2.02 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 6.29 | 15.22 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 9.55 | 11.23 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 191.56 | 192.42 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 345.76 | 1.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 872.76 | 16.78 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 3242.18 | 44.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 6713.16 | 90.66 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 4.37 | 10.73 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 17.72 | 26.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 63.48 | 109.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 79.89 | 304.77 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.41 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.79 | 0.82 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 1.63 | 1.88 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 334.25 | 359.80 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.24 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.27 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.94 | 2.16 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 2.44 | 5.03 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 27.65 | 28.27 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 122.89 | 157.56 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.52 | 0.55 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.55 | 1.59 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 26.91 | 27.36 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 78.39 | 84.48 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1595.62 | 3.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 3435.69 | 78.38 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 16131.37 | 131.56 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 172674.91 | 1473.29 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 12.45 | 14.52 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 47.57 | 74.77 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 145.52 | 147.07 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 372.91 | 1490.34 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.48 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 2501.49 | 2563.67 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.67 | 2.05 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 2197.61 | 2260.23 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 2.60 | 2.78 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 3.46 | 3.94 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 5.87 | 6.65 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 17.63 | 32.84 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.47 | 0.49 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 3.21 | 3.71 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 603.47 | 631.51 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | no | 2519.21 | 2559.27 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 382.57 | 2.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 1288.76 | 8.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 892.45 | 11.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 4130.17 | 63.65 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 4.63 | 9.39 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 6.26 | 10.19 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 23.75 | 28.76 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 50.65 | 158.21 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.52 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 4.27 | 11.53 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 14.24 | 18.28 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.37 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 0.60 | 0.76 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 0.73 | 0.82 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 18.64 | 38.37 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 1.40 | 3.74 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 2.41 | 2.61 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 4.84 | 7.36 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 85.47 | 86.03 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T064131Z.json) | yes | 1.11 | 1.98 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 2.19 | 2.22 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260505T064131Z.json) | yes | 31.32 | 35.96 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T064131Z.json) | yes | 176.15 | 176.96 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 443.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | no | 213.12 | 0.35 | 8 | 36 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 1.19 | 1.23 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | no | 0.22 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.19 | 0.20 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.20 | 0.22 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.31 | 0.35 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 0.21 | 0.21 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 2600.97 | 30.37 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 44.68 | 61.41 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 22.27 | 26.26 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T064131Z.json) | yes | 24.15 | 44.13 | 100% | 75.00 | 0.00 | pass |
