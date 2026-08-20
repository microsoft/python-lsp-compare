# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260820T060621Z.json`

- Generated at: 20260820T060621Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.73 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.73/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 6 | 3265.44 | 3.02 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | no | 8 | 7563.04 | 14.71 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 6 | 35496.44 | 62.01 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 6 | 205298.91 | 361.93 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 423.98 | 2.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 772.67 | 11.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 4467.89 | 75.43 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 7485.26 | 109.13 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1.59 | 1.71 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 7.73 | 11.94 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 31.56 | 123.36 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 184.39 | 486.73 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.25 | 0.29 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 1.22 | 1.37 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1.48 | 1.65 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 184.39 | 194.01 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 1.00 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 4.03 | 4.27 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 8.30 | 10.31 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 18.39 | 46.95 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 336.94 | 466.40 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.78 | 2.87 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 4.72 | 5.27 | 100% | 1909.00 | +1631.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 30.82 | 33.78 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 171.86 | 174.26 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 223.69 | 1.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 284.72 | 4.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 1386.27 | 13.32 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 7417.65 | 164.68 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 3.92 | 7.00 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 4.61 | 7.20 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 20.47 | 74.43 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 184.99 | 551.42 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.18 | 0.19 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.27 | 0.31 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.49 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 161.45 | 162.62 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.37 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1.38 | 2.46 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.64 | 2.78 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 23.67 | 25.35 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 234.07 | 273.98 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1.40 | 1.45 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 2.25 | 3.39 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 38.14 | 42.09 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 241.86 | 243.31 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 773.53 | 6.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 685.68 | 12.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 8494.58 | 99.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 7623.69 | 130.74 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 18.36 | 22.39 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 37.29 | 147.02 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 51.92 | 71.89 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 75.36 | 250.94 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.23 | 0.25 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.61 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 2.48 | 3.24 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 193.66 | 196.76 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 1.01 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 13.02 | 13.56 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 21.06 | 35.78 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 221.38 | 241.12 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 410.98 | 969.51 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.18 | 2.20 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 2.24 | 6.79 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 9.54 | 12.55 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 185.74 | 188.74 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 311.24 | 1.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 780.29 | 15.76 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 3246.68 | 44.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 6972.62 | 115.83 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 3.46 | 8.05 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 6.61 | 11.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 67.55 | 261.50 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 187.74 | 492.70 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.36 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1.04 | 1.09 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 1.13 | 1.27 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 315.77 | 318.60 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 1.12 | 1.33 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1.82 | 2.01 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 9.34 | 19.37 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 37.29 | 37.35 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 127.77 | 158.16 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.63 | 0.91 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1.53 | 1.55 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 37.24 | 37.37 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 85.03 | 97.80 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1247.83 | 3.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 2413.92 | 50.10 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 16475.11 | 130.95 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 171063.74 | 1544.00 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 10.99 | 11.78 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 53.82 | 81.94 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 128.78 | 130.16 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 249.16 | 995.87 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.18 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.48 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 2740.39 | 2819.40 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 2242.03 | 2305.44 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.37 | 0.39 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 2.56 | 2.68 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.98 | 3.10 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 5.45 | 5.76 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.61 | 1.37 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.78 | 2.81 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 594.60 | 672.93 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | no | 2606.26 | 2654.49 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 285.18 | 2.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 1425.91 | 8.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 761.96 | 10.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 4735.95 | 107.16 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 5.19 | 9.27 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 5.92 | 9.01 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 44.09 | 139.00 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 65.97 | 92.56 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.55 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 2.88 | 9.75 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 144.85 | 310.28 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 0.47 | 0.54 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 0.95 | 1.34 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 3.68 | 4.45 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1.77 | 3.54 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 2.62 | 3.02 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 4.76 | 6.10 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 85.94 | 86.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260820T060621Z.json) | yes | 1.04 | 1.06 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 3.13 | 4.33 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260820T060621Z.json) | yes | 32.70 | 36.40 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260820T060621Z.json) | yes | 235.34 | 236.87 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | no | 196.72 | 0.37 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1.80 | 4.50 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 1667.07 | 24.83 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 12.31 | 18.26 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 55.58 | 58.80 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260820T060621Z.json) | yes | 6.60 | 6.76 | 100% | 75.00 | 0.00 | pass |
