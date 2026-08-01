# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260801T064654Z.json`

- Generated at: 20260801T064654Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.65 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.65/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.2.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 6 | 3425.67 | 3.10 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | no | 8 | 8651.79 | 19.24 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 6 | 34949.04 | 59.99 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 6 | 220584.52 | 368.39 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 490.28 | 2.73 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 793.64 | 11.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 4088.71 | 67.57 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 7907.34 | 105.65 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 1.75 | 2.03 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 5.99 | 11.50 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 33.41 | 121.86 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 176.04 | 455.67 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 1.03 | 1.18 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.66 | 1.96 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 179.30 | 181.28 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.39 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 4.74 | 4.90 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 8.57 | 11.44 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 17.46 | 44.68 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 297.71 | 408.61 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2.56 | 2.60 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.83 | 2.85 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 32.75 | 37.18 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 167.13 | 168.01 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 222.72 | 1.93 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 286.72 | 5.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 1465.03 | 13.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 7793.02 | 172.12 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 4.07 | 7.46 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 4.64 | 6.96 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 21.41 | 74.81 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 202.96 | 618.68 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.25 | 0.28 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.26 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.47 | 0.52 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 156.93 | 163.15 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.37 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.94 | 2.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 1.06 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.63 | 3.43 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.89 | 3.05 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 23.49 | 25.93 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 249.88 | 282.35 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 1.67 | 1.73 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.81 | 3.62 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 37.95 | 43.33 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 249.75 | 253.63 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 259.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 783.22 | 6.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 788.49 | 17.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 8075.16 | 92.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 7797.07 | 134.30 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 17.97 | 22.47 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 36.15 | 143.59 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 73.54 | 245.21 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 79.84 | 170.85 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.28 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.60 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 5.44 | 6.93 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 190.01 | 191.84 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.38 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 1.05 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2.93 | 3.04 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 12.33 | 12.81 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 24.90 | 59.74 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 218.10 | 220.85 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 375.92 | 866.58 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.31 | 2.54 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 11.06 | 13.22 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 17.00 | 48.35 | 100% | 794.00 | -3498.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 182.50 | 183.67 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 312.65 | 1.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 702.32 | 13.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 3314.34 | 44.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 7366.98 | 125.04 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 3.51 | 8.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 6.47 | 11.60 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 63.45 | 252.74 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 209.08 | 502.21 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.06 | 1.15 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 1.21 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 337.66 | 341.41 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 1.12 | 1.28 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.70 | 0.71 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.17 | 2.49 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 38.72 | 39.92 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 132.57 | 162.06 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.51 | 0.55 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 1.79 | 1.84 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 38.59 | 39.88 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 80.17 | 85.28 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 1312.73 | 3.53 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2422.15 | 51.43 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 16573.18 | 134.25 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 184783.55 | 1561.71 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 11.46 | 12.61 | 100% | 772.00 | +649.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 49.34 | 77.44 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 145.62 | 147.06 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 240.94 | 950.06 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.28 | 0.43 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.46 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.90 | 2.47 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 2764.89 | 2788.82 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.31 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.46 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.50 | 1.21 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 2225.42 | 2265.19 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 2.65 | 2.70 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2.73 | 8.98 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.91 | 3.00 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 6.43 | 7.64 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.70 | 2.76 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 12.05 | 32.18 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 614.54 | 636.75 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | no | 2669.98 | 2707.87 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 772.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 304.07 | 2.18 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 1432.63 | 8.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 735.85 | 9.55 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 4936.55 | 111.52 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 4.62 | 8.14 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 6.31 | 9.31 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 40.62 | 135.77 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 82.09 | 138.80 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 0.50 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2.78 | 9.24 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 151.01 | 219.04 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.38 | 0.41 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 0.53 | 0.60 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 1.15 | 2.19 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 3.76 | 4.03 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.21 | 3.10 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 2.71 | 2.86 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 4.81 | 6.08 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 89.02 | 90.88 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260801T064654Z.json) | yes | 1.11 | 1.13 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2.78 | 4.95 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260801T064654Z.json) | yes | 31.00 | 37.71 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260801T064654Z.json) | yes | 231.74 | 233.46 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | no | 196.00 | 0.39 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 1.80 | 4.21 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.21 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 2726.63 | 82.39 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 41.84 | 71.05 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 148.95 | 169.22 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260801T064654Z.json) | yes | 56.39 | 68.21 | 100% | 75.00 | 0.00 | pass |
