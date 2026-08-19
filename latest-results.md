# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260819T060556Z.json`

- Generated at: 20260819T060556Z
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
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 6 | 3441.50 | 3.35 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | no | 8 | 8503.34 | 18.40 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 6 | 41576.66 | 81.05 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 6 | 227715.00 | 386.09 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 469.95 | 3.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 762.58 | 9.36 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 4565.47 | 80.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 8397.51 | 118.03 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 1.70 | 1.87 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 6.51 | 10.18 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 33.35 | 122.72 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 221.14 | 542.76 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.30 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 1.29 | 1.52 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2.03 | 2.36 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 191.76 | 195.04 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 1.12 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 5.00 | 5.09 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 10.23 | 10.65 | 100% | 149.00 | -19.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 10.78 | 13.81 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 360.70 | 454.92 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.98 | 2.36 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 3.04 | 3.19 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 33.66 | 37.17 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 171.14 | 172.33 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 237.72 | 2.12 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 280.42 | 4.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 1557.19 | 15.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 8211.23 | 180.29 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 4.74 | 8.45 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 5.20 | 7.70 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 21.38 | 73.24 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 215.38 | 658.98 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.25 | 0.29 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.27 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.57 | 0.65 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 162.92 | 167.76 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.97 | 2.76 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 1.14 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 1.07 | 1.15 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 3.35 | 3.81 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 28.40 | 33.48 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 265.38 | 300.02 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.63 | 0.66 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 1.60 | 1.69 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 44.13 | 47.66 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 256.63 | 262.62 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 793.13 | 7.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 731.09 | 15.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 8326.57 | 141.64 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 12596.22 | 185.33 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 19.87 | 23.33 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 37.89 | 149.95 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 72.29 | 127.56 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 84.44 | 275.90 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.68 | 0.74 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2.75 | 2.98 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 199.20 | 202.22 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 1.12 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 13.19 | 13.80 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 29.30 | 41.60 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 246.85 | 253.89 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 829.31 | 1296.01 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 2.26 | 2.30 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 8.03 | 14.22 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 11.80 | 13.52 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 188.76 | 189.35 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 316.64 | 1.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 774.18 | 15.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 3555.81 | 47.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 7461.57 | 129.42 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 3.68 | 8.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 7.54 | 12.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 68.02 | 269.33 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 223.46 | 474.54 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 1.10 | 1.19 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 1.21 | 1.54 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 340.57 | 350.35 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 1.19 | 1.44 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 2.02 | 2.18 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 3.27 | 7.75 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 41.05 | 43.51 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 137.97 | 165.27 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 1.65 | 1.66 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 4.01 | 12.82 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 40.82 | 43.23 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 89.90 | 100.33 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 1324.36 | 3.81 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2440.67 | 51.55 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 17799.87 | 148.00 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 190081.96 | 1630.37 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 12.52 | 13.21 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 56.28 | 80.32 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 158.19 | 160.69 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 250.70 | 985.26 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.44 | 1.05 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.51 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 2891.44 | 2941.58 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.31 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.32 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.46 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 2316.52 | 2394.26 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.64 | 0.70 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 2.79 | 2.93 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 3.13 | 3.26 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 6.92 | 8.00 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 2.86 | 2.89 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 5.63 | 11.34 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 675.85 | 696.18 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | no | 2782.90 | 2817.34 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 299.70 | 2.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 1502.11 | 9.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 776.58 | 10.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 5236.16 | 116.79 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 4.59 | 8.03 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 6.12 | 8.76 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 46.02 | 145.57 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 87.72 | 147.60 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.50 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2.70 | 8.96 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 154.02 | 236.97 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.37 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 0.54 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 0.77 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 3.21 | 3.87 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 1.40 | 3.64 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 3.20 | 4.56 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 4.96 | 5.87 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 101.67 | 113.91 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260819T060556Z.json) | yes | 1.12 | 1.17 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2.07 | 4.04 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260819T060556Z.json) | yes | 36.11 | 42.70 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260819T060556Z.json) | yes | 237.34 | 240.64 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | no | 188.81 | 0.40 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 1.81 | 4.29 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 2549.03 | 71.61 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 26.04 | 44.35 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 134.35 | 154.11 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260819T060556Z.json) | yes | 54.43 | 61.45 | 100% | 75.00 | 0.00 | pass |
