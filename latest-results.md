# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260429T064548Z.json`

- Generated at: 20260429T064548Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.33 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.33/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 6 | 3967.10 | 3.43 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 8 | 10080.32 | 18.70 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 6 | 34049.52 | 57.72 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 6 | 207275.85 | 343.26 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 562.44 | 4.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 922.15 | 13.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 3475.91 | 50.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 7828.59 | 95.87 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 1.83 | 2.05 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 5.12 | 9.04 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 39.06 | 154.02 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 84.21 | 131.76 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.30 | 0.34 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 1.12 | 1.19 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 10.26 | 19.32 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 198.54 | 199.19 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.52 | 0.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 1.35 | 2.67 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 4.57 | 5.28 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 16.22 | 21.34 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 18.45 | 18.84 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 218.64 | 311.11 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.72 | 0.82 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 2.16 | 2.22 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 28.54 | 32.85 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 191.00 | 194.95 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 251.30 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 352.02 | 5.18 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 1412.19 | 15.40 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 8104.31 | 178.37 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 5.07 | 7.85 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 5.21 | 8.65 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 23.18 | 90.83 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 202.17 | 655.70 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.25 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.26 | 0.28 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.52 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 180.76 | 183.43 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.48 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 1.46 | 1.77 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 2.83 | 3.08 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 26.58 | 27.67 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 301.08 | 332.70 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.80 | 0.84 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 1.45 | 1.48 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 44.33 | 50.06 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 206.74 | 209.67 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 865.79 | 6.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 907.05 | 16.55 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 7820.37 | 91.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 7913.34 | 144.42 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 17.47 | 22.23 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 42.44 | 168.49 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 74.25 | 241.42 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 96.55 | 291.48 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.29 | 0.32 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.85 | 0.95 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 2.03 | 2.17 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 210.78 | 214.18 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.46 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 1.06 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 13.13 | 15.80 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 34.62 | 59.86 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 217.31 | 221.78 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 374.57 | 824.63 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 1.45 | 1.47 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 3.44 | 4.01 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 9.79 | 11.25 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 196.42 | 200.52 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 350.29 | 1.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 908.19 | 17.55 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 3373.58 | 46.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 6829.98 | 94.37 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 4.24 | 9.96 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 18.82 | 45.78 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 67.27 | 124.72 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 85.37 | 326.13 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.42 | 0.44 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.84 | 0.87 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 1.74 | 1.85 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 347.98 | 372.57 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.24 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.57 | 0.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 1.08 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.77 | 0.82 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 2.07 | 2.29 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 28.47 | 29.27 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 127.00 | 161.74 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.52 | 0.54 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 1.61 | 1.65 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 27.04 | 27.39 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 82.80 | 90.16 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 1561.52 | 3.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 3598.78 | 82.84 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 16695.39 | 133.97 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 172386.52 | 1479.78 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 11.62 | 14.05 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 51.56 | 81.25 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 144.35 | 146.86 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 381.12 | 1523.19 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.46 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 2500.81 | 2533.77 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.38 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.64 | 1.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 2206.14 | 2306.52 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 2.69 | 2.97 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 3.36 | 3.67 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 7.59 | 11.03 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 14.90 | 26.98 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 3.00 | 3.01 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 17.32 | 34.97 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 609.85 | 649.62 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | no | 2544.92 | 2575.51 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 375.76 | 2.09 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 1272.09 | 7.97 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 851.38 | 10.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 4213.11 | 66.76 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 4.40 | 8.11 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 6.17 | 10.33 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 24.18 | 30.36 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 42.97 | 148.09 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.51 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 4.37 | 12.06 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 19.53 | 40.54 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.61 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 0.72 | 0.79 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 22.41 | 37.40 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 2.34 | 4.85 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 2.54 | 2.69 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 5.14 | 9.91 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 86.44 | 88.31 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260429T064548Z.json) | yes | 0.92 | 0.97 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 2.31 | 4.69 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260429T064548Z.json) | yes | 29.07 | 33.18 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260429T064548Z.json) | yes | 181.23 | 184.35 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 443.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 215.75 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.94 | 0.98 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.33 | 0.68 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.21 | 0.23 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 0.21 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 2325.02 | 11.14 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 17.60 | 25.65 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 8.87 | 9.09 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260429T064548Z.json) | yes | 6.95 | 7.03 | 100% | 75.00 | 0.00 | pass |
