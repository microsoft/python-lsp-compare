# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260702T070257Z.json`

- Generated at: 20260702T070257Z
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
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 6 | 3357.82 | 2.96 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 8 | 8689.52 | 16.62 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 6 | 34663.00 | 59.39 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 6 | 203825.04 | 339.53 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 433.87 | 2.37 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 849.39 | 10.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 3875.93 | 62.33 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 6947.06 | 86.27 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1.72 | 1.81 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 5.69 | 8.87 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 32.08 | 118.78 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 52.08 | 62.36 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.32 | 0.39 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 1.08 | 1.21 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 1.61 | 1.81 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 191.85 | 195.41 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.45 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 1.05 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 4.76 | 4.88 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 7.03 | 7.56 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 17.96 | 42.53 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 276.05 | 389.03 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 2.54 | 2.58 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.61 | 2.65 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 28.37 | 29.38 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 181.61 | 182.17 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 230.82 | 2.12 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 319.42 | 5.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 1397.81 | 13.28 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 7710.64 | 171.21 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 4.51 | 7.71 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 4.93 | 7.59 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 20.49 | 76.89 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 197.11 | 605.90 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.24 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.50 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.84 | 3.70 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 173.49 | 179.43 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.37 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 1.07 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.45 | 5.48 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 3.20 | 3.85 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 22.79 | 25.49 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 284.70 | 318.93 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.66 | 0.69 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 2.02 | 2.26 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 38.25 | 43.02 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 199.68 | 201.91 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 764.38 | 6.19 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 773.60 | 14.80 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 8454.81 | 98.40 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 7818.90 | 150.97 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 17.53 | 21.60 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 39.66 | 149.17 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 81.85 | 268.81 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 128.79 | 406.11 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.26 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.61 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 4.90 | 6.82 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 205.04 | 207.05 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.40 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 1.17 | 1.57 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.32 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 11.15 | 12.12 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 26.41 | 32.15 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 219.30 | 230.35 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 397.22 | 942.14 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.71 | 0.83 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1.82 | 1.86 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 11.93 | 13.81 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 200.53 | 202.30 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 295.40 | 1.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 836.32 | 16.35 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 3324.40 | 43.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 6921.01 | 86.99 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 3.75 | 8.55 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 6.64 | 11.75 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 25.96 | 35.04 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 67.45 | 262.40 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.38 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 1.17 | 1.30 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.66 | 2.70 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 349.69 | 393.07 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 1.23 | 1.49 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 3.53 | 5.31 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1.77 | 1.86 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 7.55 | 20.33 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 29.52 | 29.89 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 128.74 | 163.53 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.55 | 0.59 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1.60 | 1.64 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 28.56 | 29.45 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 82.88 | 93.33 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1332.22 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2925.62 | 60.68 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 16214.29 | 130.27 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 170329.53 | 1479.40 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 10.66 | 12.53 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 48.84 | 80.26 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 145.05 | 153.45 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 290.10 | 1143.56 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.35 | 0.72 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.48 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.96 | 2.56 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 2524.06 | 2557.93 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.28 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.41 | 0.78 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.48 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 2221.53 | 2250.24 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 2.56 | 2.75 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 2.83 | 2.85 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 4.89 | 11.71 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 6.71 | 7.79 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 2.68 | 2.83 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 7.05 | 15.64 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 594.86 | 621.47 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | no | 2503.82 | 2528.30 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 301.13 | 2.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 1395.75 | 8.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 829.54 | 11.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 4097.90 | 62.36 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 4.69 | 8.05 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 5.79 | 8.87 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 22.91 | 28.47 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 50.46 | 156.46 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.84 | 9.83 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 12.27 | 16.64 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.38 | 0.42 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 0.55 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 1.08 | 2.24 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 2.26 | 2.33 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 2.92 | 3.39 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 2.99 | 3.66 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 4.72 | 5.98 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 95.22 | 97.53 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260702T070257Z.json) | yes | 1.46 | 1.49 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 1.98 | 3.88 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260702T070257Z.json) | yes | 29.53 | 33.97 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260702T070257Z.json) | yes | 179.13 | 181.24 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 206.24 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 1.67 | 4.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.28 | 0.29 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 0.23 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 1949.39 | 26.36 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 22.06 | 35.18 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 49.72 | 52.35 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260702T070257Z.json) | yes | 7.29 | 7.53 | 100% | 75.00 | 0.00 | pass |
