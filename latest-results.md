# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260808T061232Z.json`

- Generated at: 20260808T061232Z
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
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 6 | 3537.74 | 3.28 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | no | 8 | 7565.98 | 14.64 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 6 | 36975.93 | 67.63 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 6 | 219129.08 | 371.90 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 460.50 | 2.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 744.68 | 9.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 4116.16 | 66.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 7925.09 | 114.63 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 1.60 | 1.73 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 7.23 | 11.62 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 33.66 | 122.67 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 226.16 | 433.74 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.30 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 1.56 | 3.24 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.40 | 2.65 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 176.94 | 178.04 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.41 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 1.06 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 4.28 | 4.45 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 8.68 | 10.33 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 10.07 | 11.19 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 292.52 | 400.19 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 1.91 | 3.04 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 3.11 | 3.14 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 30.68 | 34.84 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 164.69 | 166.42 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 246.89 | 2.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 269.97 | 4.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 1467.79 | 13.88 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 7870.74 | 173.64 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 4.22 | 7.40 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 5.04 | 7.93 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 18.46 | 72.41 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 207.83 | 634.15 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.26 | 0.30 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.44 | 0.45 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.56 | 0.66 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 157.33 | 158.10 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.60 | 5.42 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 3.00 | 3.21 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 24.34 | 28.13 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 255.79 | 290.94 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.66 | 0.73 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 1.72 | 1.75 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 39.85 | 47.53 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 246.13 | 250.74 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 259.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 816.10 | 6.85 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 724.67 | 14.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 9439.45 | 129.04 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 7781.39 | 135.93 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 17.91 | 22.11 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 36.81 | 145.70 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 72.71 | 240.88 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 86.03 | 189.41 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.28 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.79 | 0.92 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.76 | 3.01 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 188.34 | 190.54 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.45 | 0.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 13.44 | 14.23 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 25.57 | 48.57 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 222.95 | 224.55 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 560.83 | 1140.94 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 2.42 | 2.43 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 5.74 | 10.23 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 10.41 | 13.29 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 181.22 | 181.94 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 341.05 | 1.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 766.67 | 15.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 3405.27 | 44.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 7288.58 | 122.40 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 3.67 | 8.66 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 7.24 | 12.90 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 64.23 | 248.38 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 207.38 | 425.78 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.42 | 0.45 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 1.26 | 1.44 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.70 | 3.49 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 327.77 | 331.59 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.92 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 2.23 | 2.39 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.54 | 3.52 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 37.48 | 37.78 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 132.74 | 167.32 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 1.99 | 2.07 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 3.47 | 12.22 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 38.29 | 39.58 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 83.08 | 93.90 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 1358.53 | 4.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2394.21 | 49.77 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 17105.16 | 143.20 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 183372.31 | 1577.46 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 11.34 | 12.71 | 100% | 773.00 | +650.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 53.17 | 82.80 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 152.89 | 159.37 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 239.71 | 957.98 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.23 | 0.26 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.46 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.76 | 2.33 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 2804.47 | 2864.52 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.36 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.61 | 1.25 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 2245.46 | 2276.41 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.45 | 0.47 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 2.64 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 4.00 | 4.65 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 6.48 | 7.03 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 4.05 | 4.85 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 8.21 | 24.51 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 655.27 | 676.76 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | no | 2681.81 | 2719.39 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 773.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 314.67 | 2.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 1442.10 | 8.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 728.21 | 8.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 4890.97 | 107.33 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 5.40 | 9.68 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 6.09 | 9.70 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 36.91 | 131.03 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 69.80 | 92.63 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.48 | 0.52 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.72 | 9.08 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 85.47 | 180.54 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.36 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 0.52 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 0.76 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 60.04 | 108.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.57 | 0.60 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 2.98 | 3.97 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 4.65 | 5.70 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 89.11 | 91.42 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260808T061232Z.json) | yes | 1.19 | 1.24 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 2.00 | 3.84 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260808T061232Z.json) | yes | 29.92 | 34.45 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260808T061232Z.json) | yes | 232.21 | 233.70 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | no | 192.68 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.99 | 1.03 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 1744.90 | 29.52 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 22.40 | 33.42 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 59.38 | 61.48 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260808T061232Z.json) | yes | 6.79 | 6.90 | 100% | 75.00 | 0.00 | pass |
