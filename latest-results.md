# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260719T064755Z.json`

- Generated at: 20260719T064755Z
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
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 6 | 3446.09 | 3.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 8 | 8595.99 | 18.33 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 6 | 30779.93 | 48.47 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 6 | 169935.62 | 253.66 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 462.44 | 2.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 730.76 | 10.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 3553.03 | 54.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 6596.00 | 77.69 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 1.88 | 2.08 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 5.72 | 9.91 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 31.75 | 116.82 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 66.88 | 104.67 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.26 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 1.04 | 1.12 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 5.29 | 8.21 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 162.56 | 163.50 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.34 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 0.78 | 0.84 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.92 | 4.67 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 4.11 | 4.41 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 8.23 | 9.74 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 12.49 | 13.95 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 241.94 | 346.47 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.04 | 3.47 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 3.03 | 3.11 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 25.43 | 29.99 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 154.12 | 155.51 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 211.03 | 1.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 313.24 | 5.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 1276.49 | 12.82 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 6532.87 | 132.24 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 4.27 | 7.22 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 4.69 | 7.26 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 20.65 | 75.22 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 99.82 | 266.84 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.18 | 0.23 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.52 | 1.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.55 | 0.66 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 143.51 | 145.71 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.26 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.37 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 0.89 | 0.94 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 2.91 | 3.26 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 3.67 | 6.91 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 21.56 | 24.01 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 249.39 | 284.85 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 1.55 | 1.59 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 3.35 | 4.08 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 37.34 | 43.68 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 167.58 | 169.31 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 757.49 | 6.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 879.99 | 16.43 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 6680.35 | 57.55 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 6500.52 | 114.84 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 16.31 | 19.49 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 38.24 | 143.96 | 100% | 39.00 | -232.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 60.57 | 165.30 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 64.55 | 216.50 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.23 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.77 | 0.88 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.47 | 2.78 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 165.85 | 166.70 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.17 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.51 | 0.67 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 0.91 | 0.96 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 12.89 | 14.24 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 30.93 | 57.40 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 185.82 | 188.68 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 211.05 | 243.70 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 2.34 | 2.38 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 10.38 | 17.22 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 10.88 | 12.27 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 161.06 | 161.50 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 301.47 | 1.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 745.83 | 14.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 3016.62 | 41.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 5416.65 | 73.77 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 3.75 | 8.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 6.50 | 10.78 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 39.71 | 87.75 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 65.63 | 246.30 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.34 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 1.26 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 1.34 | 2.30 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 282.70 | 287.87 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.92 | 2.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 0.95 | 1.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 1.13 | 2.86 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 2.06 | 2.32 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.30 | 5.20 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 23.31 | 23.93 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 122.12 | 152.13 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.85 | 2.15 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 1.69 | 1.72 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 22.16 | 22.50 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 75.99 | 85.74 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 1367.70 | 4.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2714.20 | 56.35 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 14972.46 | 116.49 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 141072.40 | 1069.05 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 13.12 | 14.05 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 48.72 | 76.39 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 114.99 | 115.95 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 266.87 | 1052.69 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.16 | 0.18 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.48 | 0.64 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.79 | 2.56 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 1845.13 | 1952.87 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.24 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.24 | 5.32 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 1586.15 | 1649.93 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 2.49 | 2.64 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 3.91 | 4.85 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 5.89 | 6.72 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 11.94 | 18.51 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.52 | 0.61 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 4.23 | 4.34 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 526.91 | 534.48 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | no | 1796.49 | 1879.28 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 345.95 | 2.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 1280.98 | 7.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 666.81 | 11.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 3817.19 | 54.39 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 4.37 | 7.30 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 6.79 | 9.07 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 23.19 | 31.46 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 46.55 | 140.80 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.51 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.92 | 10.55 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 9.85 | 14.66 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.31 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 0.52 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 0.91 | 1.17 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 2.56 | 3.13 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 3.23 | 4.04 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 4.27 | 4.51 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 4.95 | 6.93 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 83.62 | 84.78 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260719T064755Z.json) | yes | 1.54 | 2.49 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2.23 | 4.55 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260719T064755Z.json) | yes | 27.71 | 33.17 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260719T064755Z.json) | yes | 152.75 | 153.57 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 196.77 | 0.25 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.76 | 0.88 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.12 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.25 | 0.26 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.13 | 0.13 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.18 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 0.21 | 0.27 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 2348.39 | 58.45 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 37.32 | 70.23 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 86.13 | 112.83 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260719T064755Z.json) | yes | 51.89 | 56.49 | 100% | 75.00 | 0.00 | pass |
