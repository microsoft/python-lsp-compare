# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260531T071356Z.json`

- Generated at: 20260531T071356Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.40 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.40/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 6 | 3859.99 | 3.40 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 8 | 10179.17 | 19.79 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 6 | 35515.50 | 61.75 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 6 | 206257.07 | 345.24 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 520.18 | 3.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 854.25 | 12.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 3787.05 | 60.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 7328.85 | 89.83 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 1.73 | 2.07 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 6.35 | 10.11 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 38.38 | 142.21 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 44.59 | 48.20 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.31 | 0.32 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 1.06 | 1.19 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 3.27 | 3.62 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 205.21 | 217.04 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.49 | 0.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 4.80 | 5.61 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 14.13 | 14.67 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 17.68 | 44.30 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 255.86 | 373.58 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 2.07 | 2.10 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 4.04 | 6.26 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 38.64 | 52.16 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 193.51 | 197.60 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 245.65 | 2.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 398.00 | 7.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 1369.49 | 15.42 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 8062.45 | 183.42 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 5.21 | 8.23 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 5.24 | 8.19 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 33.62 | 124.47 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 225.73 | 497.24 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.30 | 0.48 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.55 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 1.55 | 3.81 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 181.04 | 183.32 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 1.14 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 1.17 | 1.21 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 3.43 | 3.77 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 24.50 | 27.40 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 301.05 | 339.85 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.73 | 0.78 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 2.07 | 2.27 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 46.39 | 49.62 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 208.14 | 211.08 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 878.16 | 6.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 831.46 | 15.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 7999.73 | 93.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 8138.22 | 155.09 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 17.86 | 22.29 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 43.89 | 174.26 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 79.01 | 267.02 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 126.22 | 394.18 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.28 | 0.31 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.89 | 1.07 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 6.92 | 16.56 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 211.35 | 212.93 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.28 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.47 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 1.09 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 12.58 | 12.79 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 22.47 | 32.98 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 233.76 | 240.12 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 377.59 | 848.22 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 1.62 | 1.64 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 3.33 | 10.26 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 10.72 | 12.38 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 203.03 | 204.48 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 339.52 | 1.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 939.63 | 18.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 3376.99 | 47.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 7070.35 | 88.22 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 3.80 | 8.57 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 7.43 | 12.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 34.93 | 58.38 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 81.41 | 318.00 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.39 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 1.48 | 1.77 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 1.50 | 2.93 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 346.33 | 349.76 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.20 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.42 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 2.26 | 2.53 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 7.54 | 22.90 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 29.96 | 30.47 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 140.27 | 191.54 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 1.82 | 1.84 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 2.69 | 3.53 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 28.81 | 29.36 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 87.96 | 97.76 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 1507.44 | 3.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 3736.61 | 87.29 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 17631.06 | 144.44 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 171292.32 | 1487.38 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 12.18 | 13.94 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 54.15 | 85.22 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 146.89 | 148.06 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 409.32 | 1635.58 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.48 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 2541.09 | 2579.87 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.65 | 1.92 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 2240.99 | 2322.77 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 2.45 | 2.51 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 3.45 | 3.59 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 6.56 | 7.17 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 13.95 | 32.54 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 3.23 | 3.33 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 12.34 | 29.09 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 660.59 | 693.31 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | no | 2505.45 | 2520.06 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 369.04 | 2.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 1351.18 | 8.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 861.69 | 12.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 4364.88 | 67.49 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 5.01 | 8.51 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 6.46 | 10.04 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 23.78 | 29.90 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 51.33 | 176.78 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.54 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 4.10 | 10.96 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 11.00 | 14.59 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.33 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 0.52 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 0.76 | 0.95 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 2.42 | 2.53 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 3.10 | 3.24 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 3.33 | 5.53 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 4.71 | 5.98 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 109.80 | 139.81 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260531T071356Z.json) | yes | 1.61 | 1.63 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 2.47 | 5.04 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260531T071356Z.json) | yes | 33.46 | 36.58 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260531T071356Z.json) | yes | 190.45 | 191.07 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 238.65 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.95 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.28 | 0.53 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.20 | 0.23 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 2318.88 | 13.23 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 16.88 | 31.80 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 13.66 | 27.90 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260531T071356Z.json) | yes | 9.16 | 11.22 | 100% | 75.00 | 0.00 | pass |
