# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260712T065029Z.json`

- Generated at: 20260712T065029Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.58 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.58/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 6 | 3628.75 | 3.31 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 8 | 9840.11 | 20.92 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 6 | 39608.87 | 71.50 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 6 | 214798.43 | 350.08 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 472.96 | 3.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 775.46 | 11.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 4162.31 | 66.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 7964.67 | 93.28 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1.98 | 2.12 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 7.32 | 12.85 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 33.02 | 127.95 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 93.58 | 139.49 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.33 | 0.37 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 1.08 | 1.28 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2.53 | 2.79 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 186.85 | 189.62 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.42 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 1.06 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 4.86 | 5.02 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 9.91 | 10.40 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 18.39 | 23.80 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 293.37 | 407.02 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2.11 | 3.31 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 3.01 | 3.19 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 32.42 | 37.60 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 180.02 | 180.73 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 234.36 | 2.14 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 338.64 | 5.49 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 1555.56 | 15.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 8228.72 | 178.30 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 5.43 | 7.89 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 5.53 | 9.44 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 22.83 | 83.35 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 205.91 | 651.34 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.24 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.57 | 0.67 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 1.39 | 3.03 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 168.45 | 169.15 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 1.10 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 1.53 | 2.65 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 3.22 | 3.75 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 26.36 | 30.71 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 318.66 | 361.49 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 1.43 | 3.60 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1.58 | 1.63 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 43.34 | 50.50 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 197.37 | 200.23 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 858.82 | 7.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 904.15 | 19.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 10007.60 | 135.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 8130.06 | 145.94 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 18.64 | 22.35 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 40.96 | 155.58 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 83.91 | 279.46 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 96.77 | 278.56 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.28 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.72 | 0.88 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 5.76 | 5.85 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 199.39 | 201.38 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.39 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2.90 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 14.35 | 14.83 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 26.59 | 51.47 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 241.01 | 242.04 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 578.86 | 1155.31 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 2.26 | 2.49 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 11.84 | 13.79 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 19.90 | 58.11 | 100% | 2481.00 | -1811.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 191.46 | 196.87 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 330.39 | 1.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 874.27 | 17.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 3687.18 | 50.87 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 7631.12 | 91.59 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 4.07 | 9.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 7.54 | 12.99 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 50.34 | 88.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 69.56 | 275.06 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.39 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 1.36 | 1.56 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 3.22 | 5.09 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 343.16 | 345.64 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.44 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 1.48 | 2.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2.74 | 2.99 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1.89 | 2.28 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 3.58 | 5.63 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 31.55 | 32.34 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 147.98 | 178.96 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1.58 | 1.60 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 6.13 | 19.64 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 31.41 | 31.98 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 97.00 | 121.45 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1411.38 | 3.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 3013.88 | 62.46 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 18656.28 | 152.01 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 178637.24 | 1528.23 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 11.60 | 12.07 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 62.33 | 96.43 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 149.15 | 152.98 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 301.59 | 1204.94 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.41 | 0.94 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.51 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 2664.75 | 2768.45 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.24 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.30 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.48 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 2299.55 | 2403.90 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.71 | 1.41 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 2.76 | 2.97 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 3.04 | 3.19 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 7.65 | 8.31 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 2.69 | 2.73 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 9.54 | 27.79 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 689.09 | 717.54 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | no | 2524.93 | 2546.13 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 320.84 | 2.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 1539.94 | 8.82 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 873.40 | 11.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 4206.63 | 63.13 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 5.34 | 8.89 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 6.44 | 9.23 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 23.21 | 29.46 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 47.21 | 157.07 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.49 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 3.73 | 13.26 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 11.03 | 15.31 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.34 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 0.56 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 0.85 | 0.94 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 2.27 | 2.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 2.95 | 3.26 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 3.17 | 4.99 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 5.42 | 6.33 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 112.48 | 148.67 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260712T065029Z.json) | yes | 1.10 | 1.11 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2.24 | 4.74 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260712T065029Z.json) | yes | 31.98 | 36.26 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260712T065029Z.json) | yes | 166.65 | 170.29 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 213.48 | 0.42 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 1.79 | 4.31 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.31 | 0.33 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 0.25 | 0.27 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 2846.84 | 73.39 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 26.63 | 48.95 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 138.55 | 157.97 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260712T065029Z.json) | yes | 55.00 | 84.75 | 100% | 75.00 | 0.00 | pass |
