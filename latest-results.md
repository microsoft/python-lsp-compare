# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260803T070230Z.json`

- Generated at: 20260803T070230Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.65 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.65/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 6 | 3361.95 | 2.98 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | no | 8 | 8353.37 | 17.69 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 6 | 34881.23 | 59.52 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 6 | 223305.64 | 380.46 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 464.31 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 801.59 | 10.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 4125.99 | 66.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 7971.67 | 113.36 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 1.73 | 1.84 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 6.47 | 11.85 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 31.33 | 121.19 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 212.65 | 478.94 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.31 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 1.04 | 1.16 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 4.44 | 7.17 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 180.69 | 181.86 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.97 | 2.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 4.81 | 4.94 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 7.55 | 8.03 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 13.94 | 14.85 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 291.21 | 399.67 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.62 | 2.77 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.96 | 2.99 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 34.50 | 41.57 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 167.59 | 170.01 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 220.61 | 1.93 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 273.17 | 4.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 1446.76 | 13.59 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 7816.76 | 175.48 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 4.68 | 7.95 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 4.71 | 7.58 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 20.48 | 72.70 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 219.58 | 676.52 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.30 | 0.36 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.49 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 157.52 | 160.20 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.24 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.37 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 1.07 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.08 | 4.87 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.87 | 3.12 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 24.61 | 26.94 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 253.61 | 290.81 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 1.21 | 2.97 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 1.67 | 1.70 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 37.78 | 41.34 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 245.60 | 246.71 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 259.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 762.91 | 6.30 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 824.56 | 16.14 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 8126.45 | 91.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 7811.30 | 136.34 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 17.29 | 21.26 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 37.13 | 145.35 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 71.33 | 238.09 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 77.68 | 159.40 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.28 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.69 | 0.77 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 6.05 | 8.14 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 193.71 | 195.23 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.12 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 11.47 | 12.38 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 16.64 | 22.34 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 225.52 | 228.19 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 372.98 | 860.14 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.23 | 2.25 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 10.51 | 13.02 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 18.77 | 49.05 | 100% | 794.00 | -3498.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 183.72 | 185.27 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 304.67 | 1.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 715.72 | 13.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 3317.25 | 44.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 7275.64 | 123.70 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 3.51 | 8.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 6.77 | 12.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 62.10 | 246.16 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 210.38 | 456.91 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.38 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 1.20 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.85 | 3.65 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 330.70 | 334.47 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 1.17 | 1.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 1.25 | 2.78 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.08 | 2.21 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.43 | 7.31 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 38.09 | 38.45 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 130.14 | 159.33 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.51 | 0.54 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 1.82 | 1.83 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 38.14 | 38.49 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 81.54 | 89.23 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 1302.59 | 3.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2404.87 | 51.15 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 16415.10 | 133.21 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 187233.01 | 1612.02 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 10.70 | 11.10 | 100% | 772.00 | +649.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 46.32 | 75.13 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 144.41 | 145.94 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 241.84 | 949.72 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.23 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.44 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.94 | 2.53 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 2849.81 | 2880.85 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.28 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 1.39 | 2.86 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 2299.19 | 2370.54 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.97 | 3.15 | 100% | 23.00 | +23.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 2.98 | 3.13 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 5.97 | 6.47 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 11.01 | 18.38 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.56 | 0.58 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.71 | 2.74 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 612.89 | 648.40 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | no | 2763.73 | 2800.04 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 772.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 306.85 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 1449.68 | 8.28 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 761.62 | 9.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 5197.26 | 121.87 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 5.21 | 9.30 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 5.84 | 9.41 | 100% | 454.00 | +440.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 43.28 | 134.34 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 111.83 | 188.03 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 0.50 | 0.53 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2.67 | 8.92 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 154.88 | 244.06 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.37 | 0.40 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 0.53 | 0.57 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 1.00 | 1.62 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 3.80 | 4.71 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 1.17 | 2.92 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 2.84 | 3.21 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 4.62 | 6.03 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 92.63 | 95.61 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260803T070230Z.json) | yes | 1.09 | 1.11 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 1.98 | 3.74 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260803T070230Z.json) | yes | 30.09 | 35.47 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260803T070230Z.json) | yes | 246.23 | 252.66 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | no | 189.12 | 0.28 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.96 | 1.01 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 2382.72 | 63.77 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 35.90 | 49.05 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 91.26 | 141.72 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260803T070230Z.json) | yes | 64.15 | 81.58 | 100% | 75.00 | 0.00 | pass |
