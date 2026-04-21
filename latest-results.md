# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260421T233624Z.json`

- Generated at: 20260421T233624Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /Users/kylei/projects/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.32 | /Users/kylei/projects/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.32/ty-aarch64-apple-darwin/ty |
| Pyrefly | 0.62.0 | /Users/kylei/projects/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
| pylsp-mypy | 1.14.0 | /Users/kylei/projects/python-lsp-compare/.python-lsp-compare/servers/pylsp-mypy/venv/bin/pylsp |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **Pyrefly**: Installed from PyPI into an isolated venv because GitHub release binaries are no longer published.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Wall clock ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 6 | 16126.04 | 2.84 | 150 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 6 | 22090.14 | 29.72 | 150 | 97% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 8 | 18462.99 | 33.24 | 205 | 98% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 6 | 677191.27 | 3751.65 | 150 | 77% | 6 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1039.54 | 3.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1037.96 | 16.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 2059.58 | 22.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 4061.65 | 79.04 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1.29 | 1.42 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 3.43 | 6.23 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 29.27 | 43.15 | 100% | 181.00 | -20.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 65.84 | 261.55 | 100% | 250.00 | +49.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.19 | 0.26 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.69 | 0.73 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1.55 | 1.67 | 100% | 4747.00 | +728.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 183.35 | 185.83 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.08 | 0.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.25 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 0.73 | 0.89 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 2.54 | 2.92 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 12.84 | 14.31 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 14.89 | 15.46 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 93.25 | 119.71 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.63 | 0.73 | 100% | 2131.00 | +1853.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1.24 | 1.33 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 13.76 | 14.97 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 179.32 | 182.74 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4244.00, 4747.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2131.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 724.43 | 1.64 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 1074.77 | 7.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2530.03 | 92.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 4574.04 | 115.60 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 2.76 | 5.01 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 4.90 | 7.10 | 100% | 256.00 | +246.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 29.95 | 31.92 | 100% | 2.00 | -8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 456.89 | 1826.49 | 100% | 38.00 | +28.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.13 | 0.16 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.34 | 0.41 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1.46 | 3.55 | 100% | 327.00 | +270.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 169.29 | 173.69 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.12 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.21 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.30 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 0.69 | 0.75 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 2.23 | 2.50 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2.32 | 5.24 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 12.60 | 14.26 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 182.48 | 236.66 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.81 | 1.06 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1.28 | 2.93 | 100% | 1144.00 | +1061.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 19.18 | 20.97 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 195.61 | 203.15 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (327.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1144.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1453.59 | 5.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 894.91 | 14.97 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 3898.58 | 35.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 5175.41 | 118.64 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 16.64 | 20.12 | 100% | 1000.00 | +725.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 42.75 | 107.25 | 100% | 6.00 | -268.20 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 50.08 | 199.11 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 50.44 | 166.49 | 100% | 274.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.11 | 0.13 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.40 | 0.49 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1.59 | 1.72 | 100% | 3807.00 | +3457.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 191.68 | 212.83 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.07 | 0.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.25 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 0.67 | 0.73 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 9.49 | 17.95 | 100% | 256.00 | -185.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 10.35 | 10.66 | 100% | 448.00 | +7.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 120.29 | 130.14 | 100% | 441.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 172.17 | 245.29 | 100% | 442.00 | +1.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.98 | 1.27 | 100% | 4378.00 | +86.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 5.47 | 6.65 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 13.46 | 23.18 | 100% | 3434.00 | -858.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 185.95 | 189.52 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 350.00, 3807.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 3434.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 822.13 | 1.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 923.97 | 15.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 2055.72 | 22.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 3343.49 | 68.30 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 3.55 | 7.76 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 10.41 | 14.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 12.45 | 20.80 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 70.45 | 280.02 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.23 | 0.25 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 1.12 | 2.45 | 100% | 13782.00 | +3210.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 1.16 | 1.45 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 274.28 | 284.21 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.08 | 0.09 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.31 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 0.66 | 0.74 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.79 | 1.23 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1.23 | 1.43 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 5.02 | 13.20 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 39.41 | 112.80 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 58.66 | 69.07 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.60 | 0.71 | 100% | 1940.00 | +1040.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 1.09 | 1.34 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 14.69 | 15.64 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 41.29 | 43.35 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13782.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1940.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 11334.83 | 3.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 12103.76 | 87.16 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 6222.15 | 120.46 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 657405.80 | 22073.66 | 5 | 25 | 20% | 3 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 10.99 | 11.92 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 37.19 | 56.16 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 86.33 | 96.69 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 596.60 | 2385.23 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.08 | 0.08 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.18 | 0.20 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.29 | 0.36 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 36366.29 | 38039.35 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.23 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 35713.18 | 37307.49 | 0% | 0.00 | -1.00 | fail (10) |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 1.70 | 1.84 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2.09 | 5.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 2.34 | 2.54 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 7.43 | 13.60 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 2.25 | 2.40 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 3.22 | 7.01 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 390.68 | 402.22 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | no | 38200.81 | 40116.50 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- auto tokenizer definition: result differences detected (0.00, 1.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 751.52 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 897.72 | 4.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 731.76 | 10.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 2630.87 | 54.65 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 3.38 | 5.61 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 5.53 | 8.33 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 15.70 | 21.27 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 40.75 | 151.38 | 100% | 350.40 | +334.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.09 | 0.11 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.30 | 0.41 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 4.86 | 12.96 | 100% | 343.00 | +317.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 9.46 | 24.42 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.26 | 0.31 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 0.39 | 0.42 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.69 | 0.78 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 1.34 | 1.43 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 2.62 | 3.39 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 2.82 | 3.50 | 100% | 205.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2.98 | 4.49 | 100% | 32.00 | -173.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 54.25 | 54.66 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260421T233624Z.json) | yes | 0.38 | 0.46 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2.95 | 4.85 | 100% | 4190.00 | +3428.00 | pass |
| [Pyright](latest-results/pyright-20260421T233624Z.json) | yes | 13.61 | 15.07 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260421T233624Z.json) | yes | 192.49 | 224.85 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 350.40, 443.00).
- client session hover: result differences detected (26.00, 343.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 4190.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 316.80 | 0.17 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.63 | 0.72 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.13 | 0.14 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.10 | 0.11 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 0.11 | 0.12 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 5805.40 | 3.76 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 4.18 | 4.57 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 4.45 | 4.92 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260421T233624Z.json) | yes | 2.64 | 2.98 | 100% | 75.00 | 0.00 | pass |
