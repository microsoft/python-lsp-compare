# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260623T070830Z.json`

- Generated at: 20260623T070830Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.52 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.52/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 6 | 3477.27 | 3.17 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 8 | 8774.47 | 17.03 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 6 | 35403.29 | 62.00 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 6 | 204526.08 | 338.13 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 473.41 | 2.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 811.13 | 12.44 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 4102.43 | 67.46 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 7417.85 | 89.15 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1.73 | 1.85 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 8.40 | 13.56 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 33.51 | 122.18 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 45.26 | 48.44 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.32 | 0.35 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 1.26 | 1.42 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 3.65 | 6.20 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 205.42 | 223.88 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.24 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.47 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 1.13 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 4.45 | 4.62 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 8.30 | 9.30 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 21.62 | 47.19 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 296.98 | 422.62 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 3.03 | 3.10 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 3.21 | 4.95 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 30.19 | 32.57 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 189.48 | 190.26 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 229.04 | 2.06 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 394.72 | 7.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 1331.61 | 14.38 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 8105.38 | 179.99 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 4.89 | 7.26 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 4.90 | 7.35 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 22.82 | 89.55 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 209.09 | 666.23 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.24 | 0.28 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.50 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.49 | 5.39 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 182.28 | 186.48 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.45 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 1.14 | 1.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.72 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 3.11 | 3.35 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 5.50 | 12.79 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 23.37 | 25.82 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 301.64 | 356.54 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1.78 | 1.80 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.30 | 4.89 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 42.71 | 47.77 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 205.82 | 211.12 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 793.06 | 6.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 815.84 | 16.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 8725.57 | 101.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 7858.02 | 151.38 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 17.44 | 21.03 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 40.92 | 153.62 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 87.76 | 285.79 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 120.51 | 375.17 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.24 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 1.95 | 3.19 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 5.25 | 5.87 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 209.86 | 224.39 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.76 | 1.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.91 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 13.22 | 15.64 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 31.32 | 56.50 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 227.81 | 241.84 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 406.32 | 989.09 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.82 | 0.95 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 2.30 | 2.36 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 11.77 | 14.91 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 197.65 | 198.91 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 314.58 | 1.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 769.64 | 14.13 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 3217.36 | 44.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 6942.27 | 87.31 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 3.76 | 8.35 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 7.85 | 13.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 31.79 | 53.46 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 66.66 | 263.30 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.38 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 1.01 | 1.08 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 1.37 | 1.70 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 342.88 | 346.56 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.21 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.35 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 1.01 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.78 | 0.80 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1.93 | 2.13 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 32.28 | 38.80 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 133.68 | 187.65 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1.66 | 1.69 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 1.98 | 6.75 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 28.62 | 28.90 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 78.46 | 85.40 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1350.40 | 3.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2862.06 | 58.70 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 16725.75 | 135.94 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 170013.15 | 1457.23 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 12.56 | 13.61 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 54.44 | 83.05 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 141.25 | 147.97 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 291.52 | 1149.98 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.23 | 0.28 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.26 | 0.27 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.46 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 2487.83 | 2520.79 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.29 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.37 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 2187.32 | 2241.06 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 1.02 | 2.37 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 2.50 | 2.54 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 3.14 | 3.43 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 6.59 | 7.74 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.46 | 0.48 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 2.69 | 2.76 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 617.83 | 633.77 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | no | 2467.24 | 2508.34 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 316.78 | 2.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 1300.56 | 8.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 838.37 | 11.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 4189.41 | 63.71 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 4.48 | 7.95 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 5.86 | 9.33 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 24.84 | 31.35 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 50.88 | 156.95 | 100% | 273.40 | +259.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.50 | 0.53 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.80 | 9.74 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 10.81 | 14.58 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 0.57 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 0.69 | 0.73 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 2.28 | 2.32 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.50 | 3.86 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 2.82 | 2.96 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 4.07 | 5.36 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 101.27 | 124.86 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260623T070830Z.json) | yes | 1.50 | 1.52 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2.73 | 4.78 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260623T070830Z.json) | yes | 31.04 | 34.05 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260623T070830Z.json) | yes | 179.35 | 181.51 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 273.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 203.16 | 0.28 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.91 | 0.94 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.27 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 0.20 | 0.21 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 2079.55 | 31.10 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 19.26 | 33.77 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 61.05 | 80.88 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260623T070830Z.json) | yes | 13.00 | 21.97 | 100% | 75.00 | 0.00 | pass |
