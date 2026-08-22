# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260822T060451Z.json`

- Generated at: 20260822T060451Z
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
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 6 | 3233.52 | 3.05 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | no | 8 | 8639.14 | 19.05 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 6 | 37098.43 | 71.22 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 6 | 216454.70 | 370.51 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 429.66 | 2.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 798.46 | 11.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 4560.91 | 84.68 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 7869.10 | 114.13 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1.67 | 1.82 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 6.38 | 10.43 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 33.19 | 120.22 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 224.45 | 422.38 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.31 | 0.35 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 1.26 | 1.88 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 1.96 | 2.23 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 177.01 | 178.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.41 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 1.05 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 4.29 | 4.44 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 8.31 | 10.45 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 17.09 | 38.83 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 383.02 | 490.18 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.55 | 2.58 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.88 | 2.96 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 32.33 | 40.79 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 163.86 | 165.00 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 224.65 | 1.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 277.71 | 4.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 1438.49 | 13.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 7653.81 | 173.03 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 4.02 | 6.82 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 4.60 | 6.77 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 18.78 | 71.93 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 216.08 | 668.23 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.55 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.92 | 2.52 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 152.65 | 153.10 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.61 | 2.76 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.94 | 7.77 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 25.13 | 26.21 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 251.25 | 282.89 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.64 | 0.67 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1.95 | 3.32 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 39.05 | 43.65 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 244.10 | 245.87 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 755.67 | 6.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 690.40 | 10.50 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 7741.35 | 136.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 9873.19 | 139.42 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 18.67 | 22.21 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 36.62 | 144.65 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 70.66 | 235.58 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 87.64 | 196.42 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.73 | 0.83 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.66 | 2.88 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 189.27 | 190.74 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.22 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.47 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 10.82 | 15.77 | 100% | 256.00 | -184.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 12.06 | 12.73 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 220.20 | 225.51 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 614.35 | 1224.65 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.19 | 6.83 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.22 | 2.26 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 10.90 | 12.64 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 182.61 | 189.14 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 301.57 | 1.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 731.36 | 14.63 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 3384.71 | 46.46 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 6948.79 | 121.83 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 3.44 | 8.01 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 7.36 | 13.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 63.91 | 246.43 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 209.86 | 447.49 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.40 | 0.43 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 1.31 | 1.66 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 3.48 | 4.77 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 322.46 | 325.14 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.22 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 1.11 | 1.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.81 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1.84 | 1.95 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.44 | 7.39 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 38.47 | 38.89 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 134.57 | 164.07 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.53 | 0.59 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1.61 | 1.64 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 37.26 | 38.62 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 88.66 | 101.97 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1243.40 | 3.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2463.09 | 52.82 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 16392.86 | 133.84 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 181304.30 | 1571.58 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 11.17 | 13.13 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 47.28 | 78.48 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 144.03 | 147.24 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 241.49 | 964.96 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.24 | 0.31 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.44 | 0.49 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 2774.19 | 2845.08 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.28 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 2253.20 | 2298.71 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 2.60 | 2.80 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.97 | 3.04 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 6.88 | 8.12 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 19.96 | 34.81 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.22 | 4.91 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.74 | 2.80 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 614.19 | 628.88 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | no | 2683.87 | 2724.98 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 278.58 | 2.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 1448.26 | 9.07 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 760.89 | 10.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 4937.34 | 106.33 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 4.78 | 7.88 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 5.65 | 8.38 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 46.78 | 143.25 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 67.88 | 90.14 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.65 | 8.88 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 97.20 | 169.17 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.38 | 0.40 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 0.58 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 1.08 | 2.03 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 42.42 | 79.87 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 1.21 | 3.09 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 2.64 | 3.22 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 4.61 | 5.51 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 92.80 | 100.78 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260822T060451Z.json) | yes | 1.05 | 1.06 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2.53 | 4.23 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260822T060451Z.json) | yes | 34.37 | 37.53 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260822T060451Z.json) | yes | 231.35 | 238.00 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | no | 182.81 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.97 | 1.01 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 2734.42 | 85.53 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 61.34 | 88.43 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 140.24 | 148.00 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260822T060451Z.json) | yes | 55.01 | 64.54 | 100% | 75.00 | 0.00 | pass |
