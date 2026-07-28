# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260728T064858Z.json`

- Generated at: 20260728T064858Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.64 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.64/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.1.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 6 | 3527.48 | 3.22 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 8 | 8625.39 | 16.36 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 6 | 36321.09 | 63.59 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 6 | 229895.83 | 384.67 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 500.06 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 706.86 | 9.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 4298.86 | 74.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 8224.46 | 118.25 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 1.68 | 1.84 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 7.31 | 12.76 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 31.03 | 121.05 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 221.03 | 461.57 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 1.70 | 3.84 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2.41 | 2.83 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 187.40 | 189.31 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.40 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 1.13 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 4.46 | 4.69 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 9.28 | 9.88 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 11.61 | 13.55 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 327.42 | 400.99 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.53 | 0.61 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 3.11 | 3.16 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 36.87 | 44.97 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 177.21 | 179.81 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 226.31 | 2.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 336.50 | 5.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 1492.29 | 14.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 8237.59 | 181.40 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 4.13 | 7.13 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 5.09 | 7.84 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 22.73 | 81.53 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 217.23 | 665.14 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.26 | 0.29 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.58 | 0.64 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 1.07 | 2.73 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 162.99 | 165.87 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.45 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2.70 | 4.30 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 3.04 | 3.38 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 25.54 | 27.08 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 270.75 | 306.77 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 1.66 | 1.71 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 1.85 | 3.78 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 39.43 | 46.23 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 254.96 | 256.87 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 796.56 | 6.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 791.85 | 14.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 8401.66 | 95.29 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 8257.01 | 149.08 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 17.96 | 22.03 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 38.43 | 151.28 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 74.53 | 247.21 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 111.96 | 288.08 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.70 | 0.79 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2.82 | 3.10 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 197.87 | 200.24 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.47 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 1.09 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 13.53 | 13.73 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 24.61 | 61.81 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 245.27 | 252.52 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 389.83 | 906.95 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 2.20 | 2.22 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 8.33 | 13.53 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 10.93 | 12.51 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 189.21 | 190.97 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 315.48 | 1.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 782.70 | 14.63 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 3386.04 | 45.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 7392.40 | 128.71 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 3.65 | 8.49 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 7.07 | 12.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 67.26 | 267.06 | 100% | 38.00 | +37.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 220.09 | 458.70 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.38 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.98 | 1.02 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 1.26 | 1.55 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 339.59 | 345.63 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.43 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 1.18 | 1.27 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.76 | 0.83 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 2.11 | 2.42 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 40.58 | 41.72 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 133.68 | 155.84 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 1.78 | 1.81 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 3.90 | 8.38 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 42.10 | 43.89 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 83.11 | 89.16 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 1390.75 | 3.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2918.30 | 60.09 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 17242.66 | 143.66 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 192371.77 | 1620.63 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 11.82 | 12.75 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 54.87 | 83.77 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 156.28 | 156.79 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 295.65 | 1166.22 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.42 | 0.97 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.45 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 1.68 | 2.93 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 2897.00 | 2960.01 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.48 | 0.62 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 1.88 | 2.96 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 2278.40 | 2343.91 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.63 | 0.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 2.97 | 3.05 | 100% | 23.00 | +23.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 2.99 | 3.15 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 6.28 | 7.48 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.58 | 0.64 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 2.75 | 2.81 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 656.24 | 675.74 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | no | 2768.47 | 2816.27 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 298.31 | 2.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 1499.59 | 8.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 839.28 | 11.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 5412.60 | 109.95 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 5.75 | 9.89 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 6.12 | 8.94 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 49.99 | 154.74 | 100% | 274.40 | +260.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 118.90 | 169.13 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.59 | 0.64 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2.75 | 9.52 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 82.12 | 227.35 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.40 | 0.44 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 0.56 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 0.81 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 5.78 | 8.27 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 3.04 | 3.70 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 3.06 | 4.67 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 5.02 | 7.21 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 93.14 | 94.25 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260728T064858Z.json) | yes | 1.13 | 1.14 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2.00 | 3.86 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260728T064858Z.json) | yes | 31.41 | 35.78 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260728T064858Z.json) | yes | 249.83 | 258.69 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 219.73 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.96 | 1.01 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.31 | 0.34 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.22 | 0.26 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 2030.19 | 29.25 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 12.19 | 12.29 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 67.95 | 107.01 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260728T064858Z.json) | yes | 7.59 | 7.70 | 100% | 75.00 | 0.00 | pass |
