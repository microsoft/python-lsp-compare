# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260909T060548Z.json`

- Generated at: 20260909T060548Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.79 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.79/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 6 | 3731.11 | 2.90 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | no | 8 | 5725.06 | 12.04 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 6 | 23849.91 | 38.62 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 6 | 130337.95 | 198.71 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 286.53 | 2.30 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 494.50 | 9.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 2893.90 | 49.09 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 5317.26 | 69.94 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 1.46 | 1.57 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 4.65 | 8.06 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 22.90 | 88.98 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 114.94 | 247.49 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.24 | 0.26 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.91 | 0.98 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1.48 | 1.73 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 120.80 | 122.99 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.35 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 0.65 | 0.70 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 2.97 | 3.19 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 6.94 | 7.97 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 19.71 | 27.89 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 216.23 | 303.51 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1.08 | 2.30 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 2.69 | 2.72 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 23.33 | 28.71 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 110.35 | 112.71 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 187.46 | 1.93 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 200.26 | 3.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 981.52 | 9.93 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 5075.84 | 113.36 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 2.94 | 5.13 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 3.81 | 5.49 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 13.57 | 53.06 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 138.32 | 420.83 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.15 | 0.21 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.19 | 0.23 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.46 | 0.53 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 107.04 | 108.78 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.10 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.15 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.34 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 0.59 | 0.63 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.18 | 6.56 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 3.31 | 3.55 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 17.58 | 20.59 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 158.88 | 187.02 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.52 | 0.59 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 2.17 | 2.23 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 28.35 | 32.01 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 161.96 | 163.05 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 610.56 | 5.49 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 624.79 | 12.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 5466.63 | 49.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 5081.92 | 86.66 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 13.73 | 16.16 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 29.33 | 108.81 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 37.29 | 52.33 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 49.91 | 164.04 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.21 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.57 | 0.66 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 4.05 | 5.84 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 131.00 | 132.73 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.33 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 0.57 | 0.64 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.94 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 11.22 | 12.38 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 19.41 | 45.42 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 139.81 | 148.12 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 191.28 | 227.75 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 2.11 | 2.16 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 5.35 | 9.49 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 6.56 | 7.52 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 124.62 | 127.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 295.05 | 1.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 585.52 | 11.98 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 2307.07 | 32.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 4872.94 | 76.24 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 2.72 | 5.62 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 5.19 | 8.60 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 51.69 | 198.24 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 121.16 | 309.44 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.29 | 0.35 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.91 | 1.00 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.83 | 4.05 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 212.01 | 212.72 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.15 | 0.18 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.18 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.31 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 0.65 | 0.69 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 3.20 | 3.46 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 3.65 | 6.48 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 24.26 | 24.79 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 99.21 | 128.40 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1.53 | 5.09 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 3.12 | 3.24 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 23.13 | 23.43 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 58.90 | 63.23 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 2115.58 | 3.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1882.97 | 40.34 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 11227.78 | 83.68 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 107007.49 | 793.53 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 8.49 | 9.41 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 38.09 | 57.21 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 92.72 | 96.62 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 189.75 | 744.37 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.15 | 0.18 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.45 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.71 | 3.03 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 1436.76 | 1480.35 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.18 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.43 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 1111.40 | 1165.12 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.32 | 0.34 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 1.99 | 2.18 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 4.43 | 5.30 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 5.29 | 6.60 | 100% | 23.00 | +23.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 4.49 | 4.58 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 8.76 | 27.74 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 375.02 | 394.52 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | no | 1324.80 | 1353.90 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 235.93 | 2.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 973.00 | 6.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 449.69 | 7.09 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 2982.49 | 52.51 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 3.72 | 6.55 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 4.54 | 6.61 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 28.42 | 100.41 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 32.59 | 54.93 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.43 | 0.46 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.31 | 7.88 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 10.94 | 16.97 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.23 | 0.26 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 0.42 | 0.48 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 0.69 | 0.76 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 1.56 | 1.63 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 2.93 | 3.02 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 3.30 | 3.58 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 3.52 | 4.58 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 54.52 | 56.32 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1.57 | 2.99 | 100% | 3585.00 | +3165.00 | pass |
| [Ty](latest-results/ty-20260909T060548Z.json) | yes | 1.91 | 1.94 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260909T060548Z.json) | yes | 23.56 | 25.36 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260909T060548Z.json) | yes | 162.94 | 195.72 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | no | 158.94 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.73 | 0.88 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.18 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 0.15 | 0.18 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 1328.39 | 24.01 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 13.11 | 23.56 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 55.14 | 83.61 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260909T060548Z.json) | yes | 3.79 | 4.09 | 100% | 75.00 | 0.00 | pass |
