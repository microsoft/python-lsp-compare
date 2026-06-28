# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260628T071620Z.json`

- Generated at: 20260628T071620Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.55 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.55/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 6 | 3440.36 | 3.15 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 8 | 8727.89 | 16.91 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 6 | 36327.07 | 62.66 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 6 | 209712.05 | 344.38 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 429.10 | 2.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 743.39 | 9.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 4042.21 | 64.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 7045.86 | 90.37 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.81 | 2.00 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 5.63 | 8.83 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 31.06 | 121.05 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 54.39 | 65.30 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 1.64 | 3.37 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.46 | 2.66 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 202.40 | 214.13 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.41 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 1.08 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 4.64 | 4.96 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 8.16 | 10.56 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 15.23 | 21.34 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 285.55 | 397.84 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.52 | 0.56 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 2.58 | 2.65 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 30.27 | 34.47 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 189.33 | 191.23 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 223.13 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 315.88 | 5.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 1465.26 | 14.14 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 8045.40 | 179.70 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 4.13 | 7.02 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 5.05 | 7.72 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 22.78 | 80.21 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 211.01 | 536.24 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.25 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.26 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.50 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 177.52 | 178.93 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.38 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.61 | 7.18 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 2.88 | 3.07 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 25.23 | 26.61 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 302.42 | 345.79 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.64 | 0.67 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.71 | 1.73 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 40.45 | 47.15 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 206.48 | 207.88 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 782.15 | 6.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 884.65 | 18.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 8744.05 | 101.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 7943.21 | 151.18 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 17.99 | 20.91 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 39.46 | 150.97 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 79.57 | 265.49 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 120.00 | 374.50 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.61 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 5.63 | 8.27 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 205.51 | 206.26 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 1.08 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.92 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 12.44 | 12.93 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 36.85 | 62.94 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 230.22 | 242.74 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 414.84 | 986.21 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.88 | 1.89 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 5.51 | 5.62 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 12.68 | 14.88 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 199.09 | 200.05 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 304.76 | 1.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 810.04 | 15.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 3442.20 | 45.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 7040.47 | 87.34 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 3.77 | 8.54 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 7.02 | 11.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 33.77 | 58.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 68.32 | 268.72 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.39 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 1.25 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 3.26 | 5.05 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 341.74 | 349.12 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.70 | 1.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 1.30 | 1.69 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 1.84 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.84 | 2.04 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.04 | 3.76 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 30.12 | 30.78 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 133.38 | 166.79 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.57 | 0.61 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.59 | 1.63 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 29.80 | 30.55 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 85.07 | 94.76 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1389.46 | 3.89 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2948.43 | 61.42 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 17150.35 | 141.30 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 175565.80 | 1495.74 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 11.72 | 12.99 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 52.49 | 82.63 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 145.44 | 148.56 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 294.26 | 1162.56 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.49 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.52 | 1.13 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.80 | 2.40 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 2566.10 | 2624.21 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.45 | 0.83 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.86 | 2.09 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.91 | 2.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 2249.12 | 2294.34 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 2.62 | 2.70 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 3.33 | 3.67 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 6.51 | 6.97 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 8.84 | 22.60 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.75 | 9.60 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 2.96 | 3.55 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 646.16 | 669.33 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | no | 2515.40 | 2557.55 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 311.75 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 1482.99 | 8.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 817.07 | 10.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 4071.30 | 61.94 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 5.46 | 9.96 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 6.03 | 9.04 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 22.04 | 26.01 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 42.23 | 146.98 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.90 | 10.20 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 12.83 | 15.72 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.38 | 0.41 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 0.57 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 0.85 | 1.09 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 3.19 | 3.29 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 3.02 | 3.16 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 3.70 | 3.82 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 5.05 | 6.73 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 93.91 | 96.03 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260628T071620Z.json) | yes | 1.51 | 1.57 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 2.00 | 3.93 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260628T071620Z.json) | yes | 31.63 | 37.58 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260628T071620Z.json) | yes | 177.72 | 178.81 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 214.08 | 0.41 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 1.72 | 4.20 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.30 | 0.31 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 0.24 | 0.26 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 1994.35 | 29.84 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 25.74 | 45.05 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 56.76 | 68.57 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260628T071620Z.json) | yes | 7.04 | 7.16 | 100% | 75.00 | 0.00 | pass |
