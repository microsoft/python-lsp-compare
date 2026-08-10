# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260810T062427Z.json`

- Generated at: 20260810T062427Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.69 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.69/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 6 | 3524.68 | 3.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | no | 8 | 8436.53 | 18.46 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 6 | 34959.16 | 59.83 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 6 | 219628.10 | 372.13 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 457.49 | 3.06 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 685.98 | 8.93 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 3877.95 | 62.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 7935.93 | 114.50 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 1.72 | 1.90 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 5.87 | 8.88 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 30.93 | 120.65 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 223.63 | 533.92 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.33 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.96 | 1.02 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.43 | 2.63 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 178.38 | 181.25 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.42 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 1.05 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 4.53 | 4.99 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 9.95 | 12.30 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 10.62 | 13.64 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 274.77 | 377.54 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.44 | 0.49 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 3.09 | 3.14 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 28.92 | 31.58 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 164.93 | 165.74 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 243.12 | 1.98 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 270.96 | 4.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 1408.46 | 13.60 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 7762.56 | 174.55 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 3.91 | 6.63 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 4.80 | 7.20 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 20.06 | 71.59 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 219.36 | 678.22 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.25 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.30 | 0.31 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.58 | 0.64 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 154.95 | 156.43 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.24 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.46 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 1.07 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.17 | 5.44 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 2.95 | 3.25 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 26.56 | 33.43 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 252.38 | 283.59 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.62 | 0.64 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 1.71 | 1.75 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 36.51 | 42.40 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 245.01 | 248.50 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 259.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 813.97 | 6.97 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 753.65 | 14.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 8098.24 | 92.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 7879.99 | 138.80 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 18.10 | 21.51 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 36.66 | 143.91 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 74.47 | 244.63 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 90.93 | 209.34 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.29 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.72 | 0.79 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 5.03 | 8.23 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 191.35 | 192.43 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.35 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.82 | 2.92 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 13.76 | 13.97 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 23.35 | 36.98 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 228.93 | 242.10 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 377.96 | 863.74 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.33 | 6.95 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 2.48 | 2.72 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 11.03 | 13.12 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 181.69 | 183.31 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 332.73 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 700.80 | 13.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 3368.92 | 45.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 7219.81 | 122.59 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 3.46 | 8.08 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 7.26 | 12.99 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 63.65 | 252.51 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 208.69 | 459.57 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.40 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 1.01 | 1.05 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 1.24 | 1.42 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 326.59 | 328.59 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 1.19 | 1.50 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 2.14 | 2.42 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.41 | 7.49 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 37.85 | 38.33 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 132.72 | 167.31 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.49 | 0.50 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 1.85 | 1.86 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 38.61 | 39.72 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 87.36 | 97.66 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 1363.47 | 3.64 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2413.31 | 50.96 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 16785.87 | 136.23 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 183887.31 | 1569.32 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 11.10 | 12.01 | 100% | 773.00 | +650.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 50.40 | 83.99 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 152.67 | 155.40 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 243.08 | 971.38 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.30 | 0.55 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.47 | 0.51 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 2782.06 | 2833.50 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.32 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.95 | 2.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 2232.25 | 2297.08 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.44 | 0.47 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 2.73 | 2.83 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 3.39 | 3.44 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 6.52 | 8.74 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 3.17 | 3.24 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 10.73 | 20.55 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 622.80 | 645.76 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | no | 2676.90 | 2722.92 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 773.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 313.90 | 2.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 1419.71 | 8.28 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 739.01 | 9.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 4942.51 | 113.02 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 4.70 | 8.20 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 6.32 | 9.68 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 41.31 | 132.36 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 85.96 | 144.22 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.53 | 0.63 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2.72 | 9.15 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 152.83 | 258.85 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 0.55 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 0.94 | 1.62 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 3.51 | 4.38 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.57 | 0.61 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 2.93 | 3.44 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 4.81 | 6.91 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 90.20 | 93.04 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260810T062427Z.json) | yes | 1.16 | 1.19 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 3.17 | 4.40 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260810T062427Z.json) | yes | 30.39 | 35.39 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260810T062427Z.json) | yes | 232.60 | 234.34 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | no | 189.56 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.97 | 1.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.22 | 0.29 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 2683.26 | 81.81 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 23.27 | 55.60 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 153.47 | 166.27 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260810T062427Z.json) | yes | 68.68 | 105.75 | 100% | 75.00 | 0.00 | pass |
