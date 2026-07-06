# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260706T072547Z.json`

- Generated at: 20260706T072547Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.56 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.56/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 6 | 3374.55 | 2.96 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 8 | 8571.30 | 16.12 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 6 | 34453.07 | 58.49 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 6 | 189464.95 | 334.38 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 429.13 | 2.43 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 712.88 | 9.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 4107.82 | 68.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 6957.16 | 82.66 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.67 | 1.84 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 6.99 | 12.43 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 31.43 | 122.19 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 59.12 | 88.58 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.28 | 0.29 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 1.00 | 1.06 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 2.24 | 2.45 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 178.58 | 179.58 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 4.19 | 4.65 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 7.60 | 9.98 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 14.76 | 17.04 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 301.06 | 445.53 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.61 | 1.02 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 2.41 | 2.45 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 30.60 | 37.30 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 170.36 | 171.34 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 220.63 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 329.40 | 5.57 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 1424.59 | 14.32 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 7378.18 | 164.75 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 4.36 | 7.60 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 4.99 | 7.98 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 22.57 | 81.67 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 197.82 | 595.42 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.20 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.28 | 0.38 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.49 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 159.31 | 159.82 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.41 | 0.96 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 1.10 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 2.79 | 2.95 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 3.33 | 7.26 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 23.92 | 25.38 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 279.48 | 324.26 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 1.29 | 3.21 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.58 | 1.62 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 42.49 | 48.62 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 186.01 | 187.18 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 774.47 | 6.25 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 782.57 | 14.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 7691.39 | 86.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 7298.53 | 131.99 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 17.61 | 21.80 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 43.11 | 166.35 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 71.32 | 233.94 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 77.73 | 214.56 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.24 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.64 | 0.74 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 2.53 | 2.80 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 189.84 | 200.48 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 1.03 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 11.44 | 12.54 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 24.03 | 40.84 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 209.78 | 211.20 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 351.57 | 799.44 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.73 | 0.85 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.78 | 1.79 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 10.61 | 13.20 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 181.59 | 184.44 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 305.28 | 1.53 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 787.56 | 15.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 3190.00 | 41.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 6623.98 | 80.32 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 3.77 | 8.42 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 6.48 | 12.21 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 42.25 | 81.70 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 70.48 | 279.99 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.38 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 1.19 | 1.27 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 1.19 | 1.96 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 306.08 | 309.35 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.20 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.46 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 1.08 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.78 | 1.92 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 3.95 | 13.41 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 26.87 | 29.60 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 124.89 | 160.12 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.43 | 0.45 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.52 | 1.55 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 25.34 | 25.45 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 75.64 | 87.50 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1345.43 | 3.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 3001.02 | 62.22 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 16651.49 | 131.82 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 157345.57 | 1488.68 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 11.01 | 12.68 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 56.31 | 83.24 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 134.44 | 141.84 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 304.62 | 1216.81 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.18 | 0.20 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.25 | 0.40 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.44 | 0.50 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 2565.89 | 2645.07 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.40 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 2261.28 | 2307.76 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.42 | 0.44 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 2.53 | 2.62 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 2.86 | 2.95 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 6.16 | 6.89 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 2.68 | 2.72 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 5.71 | 11.71 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 595.80 | 612.49 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | no | 2479.27 | 2521.60 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 299.60 | 2.18 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 1387.78 | 8.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 802.66 | 10.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 3861.54 | 57.86 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 5.71 | 12.06 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 5.76 | 8.94 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 20.97 | 26.63 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 46.61 | 153.09 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.55 | 0.68 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 3.03 | 10.79 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 9.97 | 14.66 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.37 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 0.52 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 0.80 | 1.02 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 2.66 | 2.82 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 1.84 | 3.76 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 3.03 | 3.64 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 4.40 | 5.38 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 87.18 | 88.53 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260706T072547Z.json) | yes | 1.44 | 1.47 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 2.00 | 3.85 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260706T072547Z.json) | yes | 29.30 | 35.04 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260706T072547Z.json) | yes | 168.53 | 177.48 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 211.45 | 0.38 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 1.79 | 4.49 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.14 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.27 | 0.29 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 0.19 | 0.21 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 1943.76 | 23.02 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 17.69 | 33.80 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 44.81 | 45.82 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260706T072547Z.json) | yes | 6.56 | 6.74 | 100% | 75.00 | 0.00 | pass |
