# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260510T065052Z.json`

- Generated at: 20260510T065052Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.34 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.34/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.64.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 6 | 4064.05 | 3.63 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 8 | 10121.55 | 19.78 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 6 | 35399.82 | 63.44 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 6 | 198324.17 | 342.51 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 531.17 | 4.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 843.95 | 11.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 3512.35 | 52.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 7051.85 | 90.62 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 1.71 | 1.92 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 6.21 | 12.95 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 31.27 | 121.83 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 63.11 | 68.69 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.32 | 0.36 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 1.09 | 1.18 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 2.88 | 3.37 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 197.58 | 201.55 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.24 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.49 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 1.12 | 1.31 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 4.62 | 4.91 | 0% | 0.00 | -169.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 18.63 | 44.85 | 100% | 149.00 | -20.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 18.72 | 19.07 | 100% | 167.00 | -2.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 226.21 | 307.42 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 2.01 | 2.06 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 3.30 | 3.38 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 30.84 | 35.83 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 186.68 | 188.04 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 253.60 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 362.45 | 5.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 1442.21 | 16.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 8094.47 | 182.89 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 5.40 | 8.71 | 100% | 256.00 | +246.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 5.59 | 8.19 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 24.87 | 91.94 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 224.78 | 597.21 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.32 | 0.55 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.57 | 0.68 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.94 | 2.30 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 177.64 | 178.52 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.50 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 1.08 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.81 | 3.75 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 2.73 | 2.98 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 26.22 | 29.05 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 302.30 | 337.11 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 1.43 | 1.47 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.54 | 3.90 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 47.94 | 49.55 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 208.64 | 211.15 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 883.97 | 6.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 798.48 | 16.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 8661.92 | 119.12 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 8066.49 | 152.15 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 18.04 | 22.26 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 36.32 | 143.86 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 79.19 | 262.61 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 114.91 | 353.71 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.27 | 0.29 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.91 | 1.25 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 11.02 | 20.18 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 207.78 | 210.38 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.46 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.91 | 4.39 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 14.31 | 16.72 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 23.22 | 31.71 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 235.22 | 259.45 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 505.68 | 970.37 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 1.52 | 1.53 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 7.88 | 14.10 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 9.33 | 11.30 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 201.78 | 206.21 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 354.42 | 1.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 862.18 | 17.23 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 3439.44 | 47.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 6973.16 | 86.69 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 4.36 | 10.60 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 18.88 | 22.16 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 33.84 | 57.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 75.72 | 301.07 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.78 | 0.83 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 1.67 | 2.31 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 339.82 | 350.16 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.46 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 1.10 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 2.01 | 2.26 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 5.13 | 17.40 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 29.63 | 30.11 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 130.52 | 167.55 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 1.62 | 1.84 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 4.23 | 8.53 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 29.09 | 29.79 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 83.60 | 90.41 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 1653.14 | 4.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 3668.33 | 85.71 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 17025.86 | 136.75 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 164071.60 | 1480.87 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 15.29 | 18.56 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 51.87 | 77.16 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 141.93 | 144.81 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 416.58 | 1665.05 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.48 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 2525.19 | 2590.26 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.38 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.58 | 1.66 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 2241.48 | 2322.70 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 2.68 | 2.82 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 3.35 | 3.51 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 7.06 | 9.79 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 9.37 | 20.98 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.78 | 4.70 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 3.14 | 3.24 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 623.97 | 635.14 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | no | 2493.09 | 2508.71 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 387.75 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 1318.04 | 8.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 832.03 | 10.49 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 4066.60 | 61.85 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 5.52 | 10.09 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 6.29 | 10.35 | 100% | 443.00 | +427.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 24.01 | 30.06 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 41.47 | 147.22 | 100% | 267.40 | +251.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.24 | 0.28 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.53 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 4.80 | 13.50 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 11.27 | 15.87 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.39 | 0.41 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.60 | 0.77 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 0.71 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 2.36 | 2.43 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 2.46 | 2.59 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 4.23 | 5.49 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 5.15 | 7.30 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 88.74 | 91.66 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260510T065052Z.json) | yes | 0.92 | 1.10 | 100% | 304.00 | -458.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.56 | 1.64 | 100% | 3486.00 | +2724.00 | pass |
| [Pyright](latest-results/pyright-20260510T065052Z.json) | yes | 31.11 | 36.12 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260510T065052Z.json) | yes | 182.86 | 185.42 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 267.40, 443.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 3486.00, 762.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 209.02 | 0.42 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 1.84 | 4.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.30 | 0.57 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.21 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.21 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 2545.11 | 24.80 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 13.98 | 19.82 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 11.98 | 17.79 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260510T065052Z.json) | yes | 48.45 | 53.61 | 100% | 75.00 | 0.00 | pass |
