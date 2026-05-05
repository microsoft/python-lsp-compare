# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260505T002234Z.json`

- Generated at: 20260505T002234Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.34 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.34/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.63.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 6 | 3870.14 | 3.28 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | no | 8 | 9896.53 | 19.14 | 200 | 98% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 6 | 33291.91 | 56.42 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 6 | 208087.78 | 342.19 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 517.06 | 4.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1001.96 | 16.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 3538.76 | 53.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 7435.80 | 88.77 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.68 | 1.80 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 7.03 | 14.23 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 37.92 | 149.24 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 60.01 | 76.34 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.31 | 0.33 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.98 | 1.03 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 6.16 | 14.98 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 188.88 | 190.46 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.51 | 0.64 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 1.04 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 3.56 | 4.61 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 4.35 | 4.73 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 17.62 | 17.87 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 32.49 | 50.98 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 229.87 | 313.96 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.98 | 2.05 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 2.95 | 3.01 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 31.14 | 36.27 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 189.56 | 200.97 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 243.28 | 1.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 358.71 | 5.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 1327.60 | 13.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 7714.96 | 171.48 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 4.96 | 7.69 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 5.18 | 8.57 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 22.97 | 90.32 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 194.81 | 622.42 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.25 | 0.27 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.38 | 0.81 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.55 | 0.65 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 171.54 | 175.09 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.45 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1.43 | 1.67 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 2.59 | 2.69 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 22.47 | 24.82 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 290.77 | 320.32 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.33 | 1.37 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 3.68 | 4.73 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 41.07 | 46.89 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 199.23 | 199.77 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 841.72 | 6.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 749.39 | 12.34 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 7695.82 | 90.67 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 7754.40 | 140.05 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 16.83 | 21.72 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 42.71 | 169.15 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 78.03 | 258.34 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 87.34 | 255.61 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.27 | 0.28 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.83 | 0.88 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 2.03 | 2.10 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 201.68 | 204.60 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.46 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 1.04 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 11.88 | 12.35 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 15.43 | 24.91 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 211.99 | 216.31 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 363.63 | 814.22 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1.34 | 1.44 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.46 | 1.48 | 100% | 4378.00 | +86.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 10.41 | 14.05 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 198.19 | 207.73 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 342.56 | 1.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 907.62 | 18.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 3242.63 | 43.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 6835.68 | 92.30 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 4.26 | 10.59 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 18.26 | 23.70 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 64.69 | 105.64 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 82.30 | 310.72 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.75 | 0.78 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 1.33 | 1.56 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 339.51 | 372.64 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 1.06 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.86 | 1.94 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 6.90 | 16.11 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 28.07 | 28.33 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 118.91 | 156.42 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1.53 | 1.55 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 2.05 | 6.68 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 28.16 | 28.65 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 76.94 | 83.11 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 1556.98 | 3.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 3552.97 | 82.20 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 16229.26 | 129.10 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 174166.11 | 1498.01 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 11.21 | 13.73 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 46.56 | 75.89 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 140.10 | 142.16 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 406.88 | 1454.21 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.46 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1.63 | 3.08 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 2559.19 | 2599.62 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.37 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1.44 | 2.73 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 2239.03 | 2320.63 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.58 | 0.62 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 2.59 | 2.70 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 3.36 | 3.58 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 6.16 | 7.12 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.48 | 0.50 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 3.00 | 3.14 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 591.92 | 618.01 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | no | 2549.13 | 2585.97 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 368.54 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 1257.84 | 7.81 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 854.47 | 11.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 4180.84 | 62.56 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 4.33 | 7.97 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 6.03 | 10.05 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 22.26 | 25.63 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 47.73 | 161.11 | 100% | 565.00 | +549.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.30 | 0.41 | 100% | 314.00 | +288.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.52 | 0.58 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 13.69 | 18.47 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.36 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.57 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 0.70 | 0.75 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 13.65 | 36.56 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 2.33 | 2.51 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 4.32 | 4.51 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 4.45 | 6.25 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 84.87 | 86.37 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260505T002234Z.json) | yes | 0.81 | 0.82 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 2.94 | 5.08 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260505T002234Z.json) | yes | 29.02 | 32.46 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260505T002234Z.json) | yes | 178.36 | 182.82 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 443.00, 565.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | no | 214.51 | 0.36 | 8 | 35 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 1.18 | 1.26 | 100% | 30.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.19 | 0.19 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.28 | 0.54 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 0.22 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 2256.90 | 10.24 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 13.42 | 18.90 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 9.61 | 9.85 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260505T002234Z.json) | yes | 7.70 | 7.88 | 100% | 75.00 | 0.00 | pass |
