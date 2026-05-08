# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260508T063204Z.json`

- Generated at: 20260508T063204Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.34 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.34/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.64.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 6 | 3921.27 | 3.30 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 8 | 9731.55 | 18.42 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 6 | 34198.32 | 61.92 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 6 | 204265.39 | 339.66 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 530.79 | 4.25 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 837.93 | 11.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 3447.25 | 49.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 7104.86 | 86.02 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.60 | 1.75 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 5.31 | 9.55 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 31.83 | 122.58 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 43.63 | 47.05 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.29 | 0.33 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 1.07 | 1.15 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 2.37 | 3.10 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 197.32 | 211.30 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.47 | 0.58 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 4.60 | 5.31 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 17.20 | 17.70 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 18.96 | 42.23 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 210.86 | 289.91 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.97 | 2.00 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 5.36 | 6.86 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 30.10 | 33.81 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 183.50 | 184.08 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 242.14 | 1.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 375.32 | 6.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 1356.00 | 14.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 7898.94 | 176.03 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 4.68 | 7.78 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 4.94 | 8.52 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 26.03 | 99.09 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 203.34 | 648.94 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.28 | 0.40 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.54 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 1.33 | 2.97 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 173.58 | 174.73 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 1.10 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 1.75 | 3.58 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 2.65 | 2.82 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 23.75 | 26.22 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 294.09 | 329.23 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.42 | 1.43 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 2.19 | 4.33 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 43.27 | 46.94 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 208.05 | 218.48 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 848.23 | 6.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 740.92 | 13.80 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 8596.38 | 121.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 7750.35 | 150.21 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 17.66 | 22.72 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 34.01 | 134.67 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 69.44 | 231.74 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 138.04 | 448.32 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.27 | 0.29 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.71 | 0.82 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 6.85 | 16.21 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 203.20 | 204.24 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.43 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 2.90 | 3.00 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 11.97 | 12.71 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 19.84 | 28.15 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 214.61 | 218.21 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 525.79 | 1051.89 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.49 | 1.59 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 5.38 | 13.15 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 8.73 | 10.31 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 194.16 | 195.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 349.12 | 1.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 832.80 | 16.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 3282.68 | 45.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 6856.68 | 85.36 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 4.34 | 10.61 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 19.19 | 26.82 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 31.92 | 55.00 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 75.99 | 290.58 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.40 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.75 | 0.79 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 1.76 | 2.15 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 335.91 | 336.87 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.23 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.25 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.53 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 1.10 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.94 | 2.03 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 2.88 | 5.89 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 29.28 | 29.36 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 124.38 | 155.55 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.53 | 0.55 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1.58 | 1.60 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 28.58 | 28.96 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 79.98 | 85.94 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 1579.61 | 3.64 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 3590.90 | 83.13 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 16212.45 | 132.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 170719.34 | 1479.67 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 11.47 | 14.06 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 50.74 | 80.53 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 140.43 | 147.03 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 393.22 | 1571.44 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.23 | 0.25 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.47 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 2529.48 | 2556.44 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.25 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.38 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 2221.30 | 2301.14 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 2.47 | 2.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 3.19 | 3.24 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 5.86 | 6.15 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 8.12 | 17.44 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 3.06 | 3.17 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 13.84 | 17.12 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 606.37 | 627.77 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | no | 2504.67 | 2548.69 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 371.38 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 1303.56 | 8.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 855.79 | 11.58 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 3935.23 | 60.67 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 5.02 | 9.97 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 6.07 | 10.25 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 22.74 | 27.58 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 45.51 | 154.55 | 100% | 267.40 | +251.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.24 | 0.27 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.52 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 4.68 | 13.09 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 12.23 | 18.86 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.40 | 0.43 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.58 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 0.85 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 2.41 | 2.46 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 2.31 | 2.37 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 4.13 | 5.44 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 4.60 | 7.21 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 85.66 | 86.57 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260508T063204Z.json) | yes | 0.77 | 0.81 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 3.20 | 5.71 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260508T063204Z.json) | yes | 31.50 | 33.85 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260508T063204Z.json) | yes | 180.32 | 181.36 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 267.40, 443.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 211.15 | 0.34 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 1.11 | 1.23 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.31 | 0.65 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.22 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 0.24 | 0.25 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 2286.73 | 13.13 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 23.21 | 43.23 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 9.41 | 11.16 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260508T063204Z.json) | yes | 6.78 | 8.82 | 100% | 75.00 | 0.00 | pass |
