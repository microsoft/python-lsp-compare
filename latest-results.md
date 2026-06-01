# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260601T073807Z.json`

- Generated at: 20260601T073807Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.40 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.40/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 6 | 3799.98 | 3.32 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 8 | 10417.25 | 21.20 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 6 | 34789.07 | 64.30 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 6 | 207251.96 | 344.89 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 548.94 | 3.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 862.28 | 12.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 3405.73 | 50.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 7164.45 | 88.05 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1.80 | 1.97 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 6.27 | 9.71 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 37.67 | 140.86 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 47.05 | 52.04 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.32 | 0.37 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.98 | 1.02 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 1.95 | 2.20 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 199.42 | 213.81 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.49 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 4.34 | 4.61 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 14.18 | 15.42 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 17.38 | 43.20 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 216.66 | 300.41 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 2.09 | 2.11 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 4.08 | 6.29 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 29.55 | 33.59 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 188.36 | 190.66 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 242.56 | 2.14 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 379.52 | 6.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 1304.22 | 14.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 8109.56 | 181.26 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 5.06 | 8.01 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 5.21 | 7.37 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 28.76 | 108.44 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 210.19 | 662.07 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.26 | 0.32 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.54 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.74 | 1.81 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 178.23 | 181.58 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 1.09 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 1.83 | 3.78 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 3.24 | 3.54 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 24.79 | 28.34 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 306.64 | 354.76 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.76 | 0.79 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1.94 | 2.00 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 41.82 | 48.22 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 210.14 | 216.34 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 847.06 | 6.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 729.64 | 14.76 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 8608.52 | 123.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 7876.33 | 150.30 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 17.88 | 21.87 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 39.60 | 156.69 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 75.34 | 250.45 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 125.49 | 394.96 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.27 | 0.29 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.88 | 1.02 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 7.41 | 17.21 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 203.98 | 206.25 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.50 | 0.67 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 1.05 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 11.08 | 11.83 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 17.79 | 29.30 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 223.59 | 227.84 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 531.25 | 1033.60 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1.62 | 1.63 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 8.79 | 16.58 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 11.24 | 13.42 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 197.41 | 201.96 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 331.82 | 1.75 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 909.42 | 17.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 3359.14 | 46.96 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 6915.74 | 86.56 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 4.14 | 9.55 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 9.20 | 14.19 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 38.40 | 74.66 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 78.38 | 308.48 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.39 | 0.41 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.77 | 0.85 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 1.26 | 1.42 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 336.51 | 338.51 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.22 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 2.20 | 2.39 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 2.90 | 5.40 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 28.70 | 29.05 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 141.02 | 196.73 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1.82 | 1.85 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 7.10 | 24.29 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 28.13 | 28.71 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 82.91 | 99.64 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1461.28 | 3.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 3664.13 | 85.32 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 16803.51 | 140.82 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 172942.14 | 1499.68 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 11.81 | 13.85 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 53.82 | 87.33 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 144.97 | 149.65 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 417.07 | 1666.98 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.21 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.51 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 2584.90 | 2633.23 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.40 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.67 | 2.02 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 2247.61 | 2295.11 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 2.68 | 2.76 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 3.30 | 3.40 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 6.12 | 21.02 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 7.39 | 10.56 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 2.54 | 3.30 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 3.14 | 3.21 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 641.99 | 657.24 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | no | 2518.27 | 2550.73 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 368.31 | 2.35 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 1307.95 | 8.80 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 857.13 | 11.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 4243.73 | 63.47 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 5.32 | 9.96 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 6.17 | 9.64 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 22.63 | 27.77 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 50.32 | 168.21 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 0.52 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 4.24 | 11.52 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 11.68 | 15.57 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 0.56 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 1.33 | 3.13 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 2.74 | 3.28 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 1.53 | 4.04 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 3.21 | 3.31 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 4.41 | 5.70 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 95.98 | 96.90 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260601T073807Z.json) | yes | 1.61 | 1.65 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 3.28 | 5.76 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260601T073807Z.json) | yes | 32.45 | 37.81 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260601T073807Z.json) | yes | 184.34 | 186.84 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 226.93 | 0.41 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 1.74 | 4.12 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.28 | 0.54 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.22 | 0.25 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 0.21 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 2788.20 | 40.86 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 19.87 | 43.97 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 44.26 | 55.05 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260601T073807Z.json) | yes | 58.43 | 78.39 | 100% | 75.00 | 0.00 | pass |
