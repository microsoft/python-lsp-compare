# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260617T074225Z.json`

- Generated at: 20260617T074225Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.49 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.49/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.0.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 6 | 3688.44 | 3.36 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 8 | 9180.94 | 17.90 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 6 | 32997.44 | 60.81 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 6 | 155054.82 | 265.07 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 486.79 | 3.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 784.03 | 12.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 3228.48 | 47.35 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 6362.65 | 82.66 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.90 | 2.30 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 6.50 | 10.14 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 29.23 | 113.68 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 51.31 | 59.86 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.26 | 0.29 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 1.04 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 4.28 | 6.25 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 180.62 | 182.34 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.44 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 0.92 | 1.00 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2.30 | 3.02 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 3.79 | 3.99 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 12.78 | 12.94 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 20.26 | 43.56 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 199.59 | 309.85 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 2.19 | 2.34 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 4.16 | 6.78 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 29.15 | 33.17 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 176.67 | 182.41 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 247.12 | 2.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 327.91 | 5.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 1240.08 | 14.18 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 7111.04 | 158.66 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 4.88 | 7.08 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 5.66 | 7.73 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 22.66 | 80.11 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 181.84 | 587.93 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.20 | 0.23 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.47 | 0.52 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.65 | 1.77 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 164.98 | 167.27 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 0.92 | 0.97 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2.83 | 7.97 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 3.24 | 3.63 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 23.98 | 26.06 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 255.78 | 294.65 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.65 | 0.68 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.60 | 1.65 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 41.10 | 45.75 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 189.79 | 192.00 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 810.30 | 6.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 752.55 | 15.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 8243.10 | 119.83 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 7198.87 | 131.76 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 18.18 | 21.48 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 35.31 | 139.82 | 100% | 39.00 | -235.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 71.76 | 196.22 | 100% | 6.00 | -268.20 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 75.37 | 246.87 | 100% | 274.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.23 | 0.29 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 1.27 | 2.22 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 10.83 | 20.86 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 188.85 | 191.41 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.16 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.46 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 0.92 | 0.99 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2.91 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 13.47 | 15.53 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 24.06 | 42.72 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 208.11 | 212.36 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 511.72 | 973.29 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.76 | 1.95 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 3.80 | 12.41 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 10.34 | 13.44 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 189.15 | 194.63 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 321.56 | 1.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 851.95 | 17.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 3080.47 | 44.09 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 5978.07 | 77.15 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 4.11 | 8.46 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 8.09 | 11.05 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 34.71 | 54.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 72.64 | 279.41 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.37 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 1.22 | 1.39 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2.89 | 3.38 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 303.27 | 309.38 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.17 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 0.92 | 0.99 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 1.85 | 2.92 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.88 | 2.30 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 7.32 | 22.53 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 23.27 | 23.71 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 128.53 | 167.30 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.53 | 0.58 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.59 | 1.83 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 23.58 | 24.15 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 82.22 | 90.66 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1493.04 | 3.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 3435.74 | 79.48 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 15936.10 | 130.87 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 124628.48 | 1082.38 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 12.20 | 13.78 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 52.11 | 84.66 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 117.15 | 121.48 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 382.92 | 1409.75 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.16 | 0.19 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.43 | 0.50 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 1876.33 | 1950.48 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.26 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.33 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.39 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 1584.82 | 1654.48 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 2.30 | 2.47 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 3.72 | 4.65 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 4.27 | 12.94 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 6.78 | 9.46 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 2.88 | 2.93 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 9.73 | 30.92 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 594.69 | 625.59 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | no | 1831.32 | 1878.23 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 329.62 | 2.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 1269.22 | 8.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 669.25 | 9.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 3775.70 | 57.83 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 4.78 | 8.15 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 6.33 | 9.31 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 21.91 | 29.68 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 38.32 | 136.90 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.52 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 4.20 | 10.97 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 11.57 | 13.19 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.30 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 0.47 | 0.58 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 0.76 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 1.90 | 1.97 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2.46 | 5.10 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 3.16 | 3.47 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 5.26 | 6.04 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 84.57 | 86.46 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260617T074225Z.json) | yes | 1.39 | 1.42 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 3.41 | 6.03 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260617T074225Z.json) | yes | 31.56 | 34.40 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260617T074225Z.json) | yes | 169.20 | 170.34 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 201.34 | 0.28 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.93 | 1.14 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.28 | 0.57 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.18 | 0.22 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 0.17 | 0.19 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 2158.18 | 12.14 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 21.10 | 40.51 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 8.90 | 9.16 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260617T074225Z.json) | yes | 6.44 | 6.76 | 100% | 75.00 | 0.00 | pass |
