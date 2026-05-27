# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260527T072113Z.json`

- Generated at: 20260527T072113Z
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
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 6 | 3601.66 | 3.04 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 8 | 9582.74 | 18.10 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 6 | 32417.64 | 54.36 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 6 | 200786.42 | 337.13 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 470.80 | 3.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 810.64 | 12.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 3175.76 | 45.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 6684.44 | 85.68 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.60 | 1.77 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 6.07 | 10.86 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 34.71 | 135.76 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 51.90 | 56.74 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.30 | 0.32 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.96 | 1.01 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 1.85 | 2.00 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 190.55 | 197.23 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.47 | 0.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 1.08 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 4.31 | 4.68 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 12.52 | 12.74 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 19.22 | 40.22 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 189.80 | 235.60 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.92 | 1.94 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 4.50 | 6.45 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 29.93 | 33.75 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 180.57 | 181.75 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 229.58 | 1.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 374.56 | 6.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 1267.52 | 13.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 7699.08 | 175.06 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 4.62 | 7.03 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 4.82 | 7.70 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 28.57 | 111.85 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 216.95 | 474.86 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.25 | 0.31 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.54 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 2.06 | 2.95 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 170.52 | 172.83 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.44 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 1.81 | 3.73 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 2.61 | 2.70 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 22.16 | 25.36 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 289.63 | 319.12 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.73 | 0.78 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.45 | 1.49 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 40.95 | 47.00 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 197.13 | 198.71 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 795.16 | 5.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 724.04 | 12.49 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 7486.36 | 87.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 7504.11 | 142.20 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 16.82 | 20.95 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 38.57 | 153.00 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 69.42 | 236.16 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 114.22 | 358.07 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.24 | 0.25 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.80 | 0.94 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 7.13 | 17.39 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 195.61 | 196.21 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.20 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.49 | 0.58 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 1.09 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 10.92 | 12.93 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 15.58 | 36.32 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 207.88 | 210.95 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 354.86 | 792.10 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.92 | 1.15 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.38 | 1.42 | 100% | 4378.00 | +86.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 10.51 | 13.03 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 192.21 | 193.97 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 322.66 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 862.78 | 17.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 3141.68 | 43.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 6688.19 | 84.51 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 3.98 | 9.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 7.80 | 13.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 34.62 | 56.92 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 78.32 | 301.85 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.41 | 0.44 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.76 | 0.81 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 1.53 | 1.76 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 330.88 | 332.88 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.39 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 1.21 | 1.34 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.90 | 1.99 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 2.37 | 3.56 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 28.21 | 29.22 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 129.31 | 181.41 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.54 | 1.57 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 4.22 | 10.25 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 27.63 | 28.84 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 76.60 | 82.74 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1457.50 | 3.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 3527.33 | 81.93 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 16086.19 | 128.48 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 167965.06 | 1473.96 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 11.08 | 13.46 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 50.76 | 84.69 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 139.94 | 143.31 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 388.36 | 1551.79 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.23 | 0.25 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.48 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 2521.08 | 2579.74 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.24 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.40 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 2215.81 | 2269.14 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 2.51 | 2.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 3.17 | 3.22 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 6.92 | 7.96 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 20.16 | 35.01 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.68 | 0.69 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 3.00 | 3.03 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 583.83 | 603.67 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | no | 2490.45 | 2527.95 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 325.95 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 1260.14 | 8.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 834.71 | 11.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 4245.53 | 61.38 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 4.68 | 7.96 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 5.81 | 9.30 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 22.69 | 26.03 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 48.99 | 165.06 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 1.21 | 3.27 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 4.43 | 12.43 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 13.34 | 16.19 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.31 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 0.54 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 0.67 | 0.78 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 2.99 | 3.04 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 1.67 | 4.72 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 2.34 | 2.46 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 4.29 | 5.21 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 92.29 | 93.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260527T072113Z.json) | yes | 1.06 | 1.06 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 1.63 | 1.70 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260527T072113Z.json) | yes | 29.94 | 34.88 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260527T072113Z.json) | yes | 175.57 | 176.63 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 228.08 | 0.32 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 1.02 | 1.12 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.22 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.29 | 0.57 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.20 | 0.22 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 0.22 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 2220.60 | 10.15 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 13.90 | 24.33 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 9.92 | 13.45 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260527T072113Z.json) | yes | 6.64 | 6.89 | 100% | 75.00 | 0.00 | pass |
