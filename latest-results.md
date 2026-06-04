# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260604T073256Z.json`

- Generated at: 20260604T073256Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.43 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.43/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.0.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 6 | 3784.27 | 3.22 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 8 | 9844.16 | 18.74 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 6 | 33890.58 | 61.42 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 6 | 208680.88 | 345.62 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 500.55 | 3.19 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 857.15 | 12.97 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 3288.94 | 47.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 6913.32 | 86.63 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1.78 | 1.84 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 5.62 | 9.06 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 39.86 | 147.53 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 53.53 | 59.64 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.28 | 0.29 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 1.00 | 1.05 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3.07 | 3.25 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 190.24 | 190.89 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.50 | 0.65 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 4.50 | 4.68 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 11.60 | 12.06 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 17.83 | 41.49 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 198.45 | 242.15 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 2.09 | 2.13 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3.89 | 5.86 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 30.76 | 35.12 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 183.80 | 185.45 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 240.16 | 2.08 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 391.74 | 7.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 1300.87 | 14.67 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 7982.98 | 181.64 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 4.79 | 7.82 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 4.90 | 7.51 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 30.45 | 117.37 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 234.72 | 512.56 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.26 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.30 | 0.34 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.54 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 172.82 | 176.07 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.44 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 1.08 | 1.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 1.46 | 5.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 3.08 | 3.20 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3.59 | 7.72 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 24.49 | 26.66 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 297.28 | 328.48 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 1.49 | 3.67 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1.94 | 1.96 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 43.08 | 46.49 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 202.30 | 203.86 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 852.25 | 6.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 745.55 | 13.11 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 8273.43 | 115.88 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 7964.02 | 150.73 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 17.45 | 21.56 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 38.38 | 152.20 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 72.99 | 246.40 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 129.46 | 405.51 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.27 | 0.31 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.81 | 0.93 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 11.00 | 17.84 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 207.50 | 211.53 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.53 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 1.93 | 2.98 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 11.44 | 13.52 | 100% | 256.00 | -185.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 11.51 | 13.79 | 100% | 448.00 | +7.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 216.06 | 220.01 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 493.89 | 909.22 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1.61 | 1.68 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2.82 | 8.89 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 11.20 | 12.52 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 199.54 | 211.80 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 341.15 | 1.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 925.47 | 18.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 3254.42 | 46.06 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 6851.10 | 85.55 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 3.82 | 8.82 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 7.92 | 13.83 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 36.68 | 69.60 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 80.98 | 313.41 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.40 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 1.42 | 1.92 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2.68 | 2.77 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 335.05 | 337.63 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.45 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 1.10 | 1.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2.93 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 2.28 | 2.38 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 6.62 | 19.06 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 27.80 | 28.22 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 136.23 | 178.12 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 1.08 | 2.78 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1.97 | 2.14 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 27.11 | 27.36 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 84.27 | 91.21 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1463.50 | 3.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3611.53 | 83.86 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 16498.20 | 136.59 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 174765.86 | 1505.54 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 11.33 | 13.43 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 51.64 | 85.06 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 146.02 | 147.57 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 406.65 | 1490.90 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.48 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2.12 | 2.93 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 2592.99 | 2691.48 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.38 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2.73 | 2.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 2263.77 | 2352.80 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 2.57 | 2.75 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 3.59 | 3.81 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 7.11 | 22.03 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 7.21 | 8.37 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.67 | 0.70 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 3.76 | 4.48 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 623.23 | 662.11 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | no | 2522.32 | 2540.43 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 386.67 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 1274.73 | 8.08 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 845.54 | 11.59 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 4203.60 | 63.63 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 4.55 | 7.77 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 6.05 | 9.58 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 23.11 | 28.71 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 48.81 | 167.87 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.52 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3.98 | 10.52 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 11.06 | 15.97 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.34 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 0.55 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 0.71 | 0.76 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 2.34 | 2.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 2.91 | 3.02 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 3.18 | 4.91 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 4.11 | 5.10 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 98.12 | 99.51 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260604T073256Z.json) | yes | 1.59 | 1.62 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 1.66 | 1.81 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260604T073256Z.json) | yes | 30.53 | 35.24 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260604T073256Z.json) | yes | 183.51 | 186.33 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 228.56 | 0.32 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.94 | 0.98 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.27 | 0.50 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.30 | 0.57 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 0.21 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 2238.63 | 8.91 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 10.73 | 10.95 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 9.01 | 9.22 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260604T073256Z.json) | yes | 6.99 | 7.08 | 100% | 75.00 | 0.00 | pass |
