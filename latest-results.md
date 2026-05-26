# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260526T070607Z.json`

- Generated at: 20260526T070607Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.39 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.39/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 6 | 3743.99 | 3.28 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 8 | 10712.51 | 21.73 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 6 | 33024.56 | 55.84 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 6 | 189760.07 | 338.33 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 553.37 | 3.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 855.53 | 12.97 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 3056.32 | 42.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 7024.81 | 89.60 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.77 | 2.00 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 5.99 | 10.69 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 39.97 | 145.73 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 41.44 | 48.68 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.29 | 0.30 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.98 | 1.02 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 1.88 | 2.04 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 204.85 | 216.22 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.46 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 0.96 | 1.02 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 4.38 | 4.89 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 14.39 | 14.78 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 18.13 | 46.79 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 178.55 | 225.98 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.90 | 1.92 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 4.71 | 6.79 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 26.84 | 31.06 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 196.37 | 202.99 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 231.28 | 1.88 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 404.05 | 7.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 1277.70 | 13.78 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 7742.68 | 179.82 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 5.00 | 8.02 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 5.03 | 8.12 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 31.59 | 121.23 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 226.41 | 609.73 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.22 | 0.29 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.55 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 1.17 | 2.76 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 183.63 | 186.14 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.44 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 2.54 | 4.80 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 2.68 | 3.01 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 22.73 | 26.86 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 276.80 | 312.04 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.73 | 0.79 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.33 | 1.38 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 40.14 | 43.66 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 211.23 | 216.42 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 837.08 | 6.49 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 757.63 | 14.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 7639.27 | 90.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 7623.48 | 144.03 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 17.63 | 21.82 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 40.71 | 161.24 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 76.00 | 254.79 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 91.43 | 266.72 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.24 | 0.27 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.82 | 0.94 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 8.06 | 18.31 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 210.09 | 215.50 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.51 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 12.98 | 13.82 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 19.70 | 30.06 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 215.63 | 229.79 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 361.69 | 798.89 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.43 | 1.54 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 3.61 | 11.53 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 11.13 | 12.79 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 202.00 | 204.53 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 334.03 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 864.36 | 16.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 3159.03 | 43.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 6463.52 | 80.87 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 4.07 | 9.72 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 7.25 | 11.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 24.15 | 35.32 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 80.22 | 316.76 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.36 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 1.38 | 1.68 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 1.70 | 2.88 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 327.88 | 332.56 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.18 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.34 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 0.97 | 1.00 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 1.75 | 4.60 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.92 | 2.13 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 26.23 | 27.02 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 129.93 | 172.37 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.50 | 0.51 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.50 | 1.52 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 25.13 | 26.47 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 81.00 | 86.36 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1458.96 | 3.89 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 3622.47 | 83.24 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 16609.70 | 136.44 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 156685.61 | 1472.52 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 12.70 | 15.02 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 59.53 | 88.63 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 128.17 | 132.48 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 410.04 | 1638.96 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.18 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.18 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.51 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 2533.09 | 2554.36 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.20 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.41 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 2216.74 | 2313.30 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 2.45 | 2.61 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 3.31 | 3.46 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 3.38 | 11.73 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 6.91 | 10.68 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 2.39 | 7.71 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 3.02 | 3.04 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 614.82 | 643.41 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | no | 2482.13 | 2498.79 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 329.26 | 2.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 1282.54 | 8.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 848.46 | 11.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 4219.96 | 63.16 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 5.08 | 8.17 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 6.07 | 9.47 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 22.79 | 30.51 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 47.24 | 165.39 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.57 | 0.66 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 4.25 | 11.26 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 10.73 | 16.13 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.35 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 0.51 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 0.79 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 2.07 | 2.12 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 2.46 | 5.42 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 2.74 | 2.97 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 4.68 | 5.57 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 90.00 | 92.07 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260526T070607Z.json) | yes | 1.09 | 1.12 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 4.96 | 5.98 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260526T070607Z.json) | yes | 30.21 | 34.24 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260526T070607Z.json) | yes | 190.20 | 194.33 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 237.62 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 1.11 | 1.26 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.25 | 0.53 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.18 | 0.20 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 0.20 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 3122.38 | 51.78 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 49.74 | 85.06 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 55.00 | 67.52 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260526T070607Z.json) | yes | 50.60 | 53.93 | 100% | 75.00 | 0.00 | pass |
