# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260514T065601Z.json`

- Generated at: 20260514T065601Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.35 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.35/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 6 | 3923.13 | 3.20 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 8 | 9816.95 | 18.61 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 6 | 34873.97 | 62.58 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 6 | 210518.96 | 350.40 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 518.04 | 3.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 824.65 | 10.81 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 3479.24 | 50.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 7407.32 | 88.79 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.63 | 1.76 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 5.08 | 9.00 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 30.51 | 118.96 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 48.15 | 50.00 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.30 | 0.32 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 1.09 | 1.19 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 1.87 | 2.02 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 200.73 | 211.28 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.24 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.54 | 0.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 1.06 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 4.49 | 4.82 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 12.68 | 13.23 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 18.16 | 43.84 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 215.89 | 284.10 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.82 | 1.86 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3.27 | 3.30 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 30.57 | 33.40 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 189.50 | 191.95 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 250.46 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 408.49 | 7.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 1338.55 | 14.21 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 8125.72 | 181.78 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 4.79 | 8.07 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 5.15 | 8.52 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 26.13 | 99.41 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 215.15 | 595.67 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.27 | 0.29 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.53 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3.52 | 5.32 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 178.93 | 182.39 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.42 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 1.09 | 1.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 1.12 | 2.73 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 2.16 | 5.24 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 2.70 | 3.00 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 23.26 | 25.68 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 306.32 | 337.04 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.39 | 1.47 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3.29 | 5.15 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 42.07 | 46.75 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 207.44 | 213.26 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 852.43 | 6.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 771.09 | 14.89 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 8674.03 | 121.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 8157.36 | 154.75 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 17.59 | 22.04 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 36.14 | 142.85 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 75.04 | 244.59 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 128.47 | 397.72 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.27 | 0.30 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.81 | 0.88 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 7.34 | 18.15 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 210.68 | 217.87 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.56 | 0.72 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.86 | 2.25 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 1.07 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 12.93 | 14.72 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 22.42 | 30.05 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 229.45 | 236.42 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 519.60 | 1032.05 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.48 | 1.69 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 7.66 | 13.64 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 9.97 | 10.87 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 204.06 | 210.04 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 353.96 | 1.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 824.31 | 15.89 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 3287.70 | 44.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 6976.35 | 85.87 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 4.39 | 10.56 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 18.33 | 24.97 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 35.42 | 64.54 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 72.82 | 285.15 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.39 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.80 | 0.83 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 2.03 | 2.72 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 336.06 | 341.03 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.49 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 1.08 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.91 | 2.11 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3.97 | 9.27 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 28.15 | 28.47 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 122.84 | 152.65 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.50 | 1.53 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 1.57 | 4.05 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 28.63 | 29.20 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 78.73 | 84.97 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1594.90 | 3.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3703.65 | 86.63 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 16772.62 | 136.60 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 175437.15 | 1525.34 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 11.53 | 13.94 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 50.70 | 78.09 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 141.62 | 149.38 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 414.06 | 1654.87 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.23 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.52 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 2590.82 | 2660.91 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.23 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.62 | 1.79 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 2282.39 | 2424.83 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 2.77 | 3.05 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 3.37 | 3.63 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 7.17 | 9.61 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 10.68 | 33.02 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 2.94 | 2.96 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 7.57 | 25.41 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 624.19 | 649.42 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | no | 2609.07 | 2696.68 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 353.33 | 2.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 1321.83 | 8.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 841.10 | 10.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 4415.07 | 65.85 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 4.76 | 8.06 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 6.06 | 10.49 | 100% | 445.00 | +431.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 25.50 | 32.46 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 42.96 | 143.42 | 100% | 267.40 | +253.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.54 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 4.08 | 10.82 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 13.76 | 16.59 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.39 | 0.42 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 0.57 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 0.71 | 0.81 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 3.40 | 3.52 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.72 | 0.88 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 2.40 | 2.55 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 4.80 | 6.83 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 99.62 | 100.28 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260514T065601Z.json) | yes | 1.12 | 1.15 | 100% | 1657.00 | +1237.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 3.36 | 5.91 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260514T065601Z.json) | yes | 30.81 | 35.63 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260514T065601Z.json) | yes | 186.96 | 189.93 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 267.40, 445.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1657.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 205.82 | 0.33 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 1.07 | 1.19 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.30 | 0.54 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.21 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 0.22 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 2237.86 | 10.50 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 12.83 | 15.62 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 10.14 | 11.19 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260514T065601Z.json) | yes | 8.51 | 8.91 | 100% | 75.00 | 0.00 | pass |
