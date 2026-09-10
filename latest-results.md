# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260910T060546Z.json`

- Generated at: 20260910T060546Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.80 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.80/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 6 | 5085.86 | 4.06 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | no | 8 | 7530.39 | 14.71 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 6 | 40634.95 | 73.48 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 6 | 208112.41 | 365.93 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 430.16 | 3.34 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 664.65 | 9.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 4707.08 | 76.72 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 7726.63 | 110.62 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 1.69 | 1.91 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 7.59 | 14.39 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 32.97 | 124.74 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 188.56 | 482.83 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.27 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 1.13 | 1.41 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2.31 | 2.54 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 187.76 | 189.94 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.40 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 0.95 | 1.00 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 4.27 | 4.42 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 10.08 | 14.60 | 100% | 149.00 | -19.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 10.99 | 13.98 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 343.83 | 514.61 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.43 | 0.48 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 3.60 | 3.64 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 30.65 | 33.57 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 171.57 | 175.56 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 263.26 | 2.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 292.30 | 5.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 1432.16 | 13.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 7552.13 | 169.73 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 4.81 | 8.00 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 4.99 | 7.54 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 20.44 | 75.59 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 196.25 | 601.66 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.19 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.54 | 0.64 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.90 | 2.46 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 164.19 | 166.79 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.40 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 1.01 | 1.04 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.01 | 2.97 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.65 | 3.46 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 4.72 | 5.23 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 25.67 | 28.69 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 240.22 | 281.81 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2.34 | 3.50 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 2.76 | 2.80 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 38.16 | 44.34 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 247.00 | 254.00 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 887.21 | 8.35 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 727.29 | 13.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 7839.39 | 136.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 11669.10 | 172.22 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 19.15 | 22.45 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 38.43 | 150.71 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 70.69 | 125.55 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 81.26 | 270.02 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.23 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.71 | 0.78 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2.50 | 2.74 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 200.23 | 202.18 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.19 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.37 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 0.97 | 1.00 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 19.36 | 19.81 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 20.53 | 37.58 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 215.00 | 218.78 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 766.58 | 1156.82 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 2.85 | 2.91 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 5.93 | 13.85 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 12.20 | 16.52 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 193.53 | 197.77 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 376.41 | 2.49 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 728.77 | 14.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 3669.49 | 47.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 6649.44 | 114.87 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 3.59 | 8.51 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 6.24 | 10.89 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 64.96 | 252.23 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 186.38 | 466.01 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.38 | 0.39 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 1.29 | 1.60 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 4.08 | 5.17 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 317.41 | 324.23 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.17 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.85 | 2.13 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 1.01 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.73 | 0.78 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 4.37 | 5.07 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 34.74 | 36.64 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 139.81 | 179.25 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.49 | 0.50 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 3.93 | 4.02 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 34.83 | 36.68 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 90.38 | 99.73 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 2805.46 | 4.85 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2453.40 | 51.98 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 17569.25 | 121.05 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 173516.30 | 1562.61 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 11.62 | 12.36 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 63.19 | 93.02 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 131.46 | 138.67 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 248.82 | 973.56 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.54 | 0.68 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2.96 | 3.11 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 2748.37 | 2822.43 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.54 | 0.86 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.18 | 2.76 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 2291.86 | 2419.91 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 2.95 | 3.27 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 5.56 | 10.87 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 6.23 | 6.49 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 7.93 | 9.32 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.35 | 2.74 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 5.95 | 6.11 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 533.04 | 558.65 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | no | 2638.42 | 2739.15 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 323.36 | 2.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 1587.86 | 9.23 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 752.17 | 9.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 4828.51 | 101.67 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 5.98 | 9.58 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 6.17 | 9.04 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 44.41 | 141.49 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 72.28 | 108.49 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.16 | 0.19 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.58 | 0.67 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 2.79 | 9.33 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 116.04 | 243.27 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.29 | 0.31 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 0.53 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 0.89 | 1.11 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 3.66 | 4.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.52 | 0.53 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 4.34 | 4.64 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 5.02 | 5.98 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 81.39 | 86.53 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.44 | 1.50 | 100% | 3585.00 | +3165.00 | pass |
| [Ty](latest-results/ty-20260910T060546Z.json) | yes | 2.53 | 2.58 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260910T060546Z.json) | yes | 33.69 | 38.02 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260910T060546Z.json) | yes | 235.00 | 243.90 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | no | 193.25 | 0.36 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1.77 | 4.56 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 1718.55 | 26.89 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 17.99 | 29.79 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 56.51 | 61.42 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260910T060546Z.json) | yes | 6.17 | 6.22 | 100% | 75.00 | 0.00 | pass |
