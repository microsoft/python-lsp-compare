# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260521T071200Z.json`

- Generated at: 20260521T071200Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.38 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.38/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 6 | 3908.55 | 3.15 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 8 | 10032.02 | 19.74 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 6 | 33452.13 | 57.94 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 6 | 202665.46 | 335.84 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 537.76 | 3.34 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 831.08 | 12.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 3661.94 | 56.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 7101.34 | 86.44 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.63 | 1.79 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 6.96 | 14.71 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 35.10 | 137.33 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 45.52 | 50.16 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.29 | 0.31 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 1.06 | 1.14 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 3.24 | 3.60 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 197.36 | 204.23 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.20 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.50 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 1.04 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 4.31 | 4.53 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 12.64 | 13.25 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 18.59 | 44.31 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 243.84 | 351.47 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.90 | 1.92 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 3.92 | 5.92 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 31.49 | 34.62 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 183.97 | 185.53 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 237.82 | 1.89 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 382.00 | 7.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 1334.99 | 14.61 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 7763.50 | 175.59 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 4.66 | 7.18 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 5.07 | 8.31 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 29.42 | 113.54 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 214.77 | 552.39 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.24 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.54 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.58 | 4.41 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 172.65 | 174.27 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.20 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 1.34 | 2.99 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 1.12 | 1.16 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 2.56 | 2.77 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 24.28 | 26.18 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 288.43 | 321.35 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.74 | 0.76 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.36 | 1.38 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 43.16 | 47.19 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 201.03 | 203.30 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 839.58 | 6.14 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 765.46 | 15.37 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 7628.82 | 91.46 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 7727.20 | 147.17 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 17.34 | 22.39 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 40.69 | 161.50 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 73.09 | 240.15 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 120.86 | 381.11 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.24 | 0.26 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.76 | 0.87 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 6.74 | 15.82 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 203.81 | 205.48 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.43 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 11.50 | 13.40 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 22.53 | 30.82 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 211.55 | 214.87 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 373.93 | 834.89 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.40 | 1.44 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 6.65 | 15.76 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 9.11 | 10.60 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 198.58 | 207.53 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 344.89 | 1.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 876.42 | 17.48 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 3253.69 | 44.04 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 6765.74 | 84.09 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 4.54 | 11.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 18.11 | 21.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 31.74 | 55.69 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 77.29 | 305.68 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.38 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 1.41 | 1.89 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.21 | 5.15 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 331.53 | 339.97 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.21 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.60 | 1.14 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.90 | 2.03 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.52 | 6.58 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 28.87 | 30.68 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 122.24 | 152.87 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.49 | 1.52 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 4.79 | 9.62 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 27.28 | 28.46 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 78.06 | 83.96 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1604.89 | 3.77 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 3602.33 | 83.98 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 16280.04 | 132.55 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 169222.60 | 1459.89 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 11.89 | 14.33 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 53.64 | 84.99 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 140.55 | 146.32 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 412.90 | 1650.40 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.53 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 2491.00 | 2550.93 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 2196.57 | 2251.13 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 2.49 | 2.53 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 3.41 | 3.73 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 4.57 | 12.39 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 6.77 | 9.32 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.00 | 5.97 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 3.05 | 3.11 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 601.39 | 624.96 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | no | 2468.84 | 2504.23 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 343.61 | 2.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 1292.65 | 8.18 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 838.75 | 10.72 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 4085.07 | 61.89 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 5.12 | 9.61 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 6.10 | 10.33 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 23.95 | 29.51 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 43.74 | 161.40 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.56 | 0.58 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 4.56 | 12.84 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 10.69 | 18.09 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.32 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 0.59 | 0.71 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 0.74 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 2.29 | 2.43 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 2.36 | 2.47 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.50 | 5.48 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 4.36 | 5.10 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 94.60 | 97.51 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260521T071200Z.json) | yes | 1.08 | 1.09 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2.48 | 5.04 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260521T071200Z.json) | yes | 30.14 | 34.63 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260521T071200Z.json) | yes | 177.93 | 180.39 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 221.42 | 0.30 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.92 | 1.00 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.28 | 0.55 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.20 | 0.22 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 0.21 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 2514.56 | 24.33 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 17.87 | 33.28 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 13.47 | 16.72 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260521T071200Z.json) | yes | 41.66 | 54.50 | 100% | 75.00 | 0.00 | pass |
