# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260804T064846Z.json`

- Generated at: 20260804T064846Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.66 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.66/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.2.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 6 | 3442.26 | 3.13 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | no | 8 | 8357.63 | 18.45 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 6 | 34380.66 | 59.34 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 6 | 217098.20 | 369.04 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 446.60 | 2.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 739.64 | 9.48 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 4147.17 | 71.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 7796.98 | 110.75 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 1.70 | 1.77 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 6.10 | 8.45 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 34.43 | 132.54 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 209.77 | 465.80 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.31 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 1.03 | 1.17 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2.46 | 2.73 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 174.00 | 174.70 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.24 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 4.21 | 4.37 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 8.44 | 10.85 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 9.79 | 12.61 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 314.54 | 456.94 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.47 | 0.49 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 3.04 | 3.15 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 33.02 | 36.28 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 164.68 | 168.60 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 241.87 | 1.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 270.63 | 4.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 1389.82 | 13.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 7618.49 | 172.57 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 3.97 | 6.82 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 4.57 | 7.21 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 21.91 | 73.64 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 220.91 | 590.90 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.24 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.27 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.52 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 151.60 | 151.90 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.86 | 2.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 1.10 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 1.05 | 1.08 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.85 | 2.97 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 23.40 | 25.77 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 247.97 | 283.38 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.63 | 0.67 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 1.81 | 1.93 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 37.55 | 45.00 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 241.27 | 243.53 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 259.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 793.42 | 6.89 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 686.02 | 12.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 7975.17 | 90.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 7718.77 | 139.02 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 17.01 | 20.61 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 38.37 | 143.46 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 70.10 | 233.12 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 103.15 | 252.74 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.62 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 5.06 | 7.41 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 188.78 | 189.74 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 1.04 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2.93 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 14.65 | 15.70 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 15.74 | 25.19 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 222.69 | 231.24 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 368.01 | 839.92 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.79 | 0.82 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.28 | 2.31 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 10.90 | 11.87 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 179.43 | 180.17 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 346.82 | 1.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 791.80 | 16.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 3297.63 | 43.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 7135.30 | 122.35 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 3.44 | 7.85 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 6.27 | 10.86 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 61.73 | 245.82 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 208.57 | 418.52 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.42 | 0.45 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.99 | 1.01 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 1.22 | 1.37 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 322.40 | 326.96 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.60 | 1.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 1.20 | 1.50 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2.73 | 2.99 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.57 | 2.66 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 9.09 | 15.57 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 39.01 | 40.28 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 130.06 | 160.45 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.31 | 2.34 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 7.41 | 10.88 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 40.59 | 42.23 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 78.71 | 88.83 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 1307.97 | 3.40 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2387.42 | 50.00 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 16147.42 | 130.16 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 182015.93 | 1565.57 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 10.58 | 11.94 | 100% | 773.00 | +650.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 46.44 | 76.60 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 141.74 | 143.24 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 236.35 | 944.53 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.20 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.35 | 0.72 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.47 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 2748.56 | 2796.70 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.42 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 2242.16 | 2272.63 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.40 | 0.42 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 2.50 | 2.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.97 | 3.04 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 6.23 | 7.72 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.82 | 2.84 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 12.85 | 17.75 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 597.23 | 623.31 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | no | 2692.89 | 2720.61 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 773.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 305.58 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 1423.46 | 8.29 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 771.38 | 10.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 4812.71 | 103.97 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 5.22 | 9.63 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 5.62 | 8.75 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 45.02 | 137.65 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 68.67 | 91.47 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.47 | 0.51 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2.78 | 9.38 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 94.69 | 196.57 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.36 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 0.52 | 0.55 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 0.78 | 0.93 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 40.56 | 76.92 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 1.76 | 3.63 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 2.49 | 2.80 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 4.76 | 6.24 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 89.46 | 90.45 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260804T064846Z.json) | yes | 1.14 | 1.16 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2.62 | 4.30 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260804T064846Z.json) | yes | 30.22 | 34.80 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260804T064846Z.json) | yes | 226.49 | 227.04 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | no | 187.93 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.96 | 1.00 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 2522.81 | 78.25 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 18.94 | 34.60 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 138.87 | 159.19 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260804T064846Z.json) | yes | 76.95 | 93.22 | 100% | 75.00 | 0.00 | pass |
