# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260618T073500Z.json`

- Generated at: 20260618T073500Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.50 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.50/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.1.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 6 | 3510.79 | 3.33 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 8 | 8559.77 | 16.07 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 6 | 32844.98 | 55.22 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 6 | 195882.66 | 335.79 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 493.74 | 3.30 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 753.33 | 11.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 3230.51 | 45.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 6953.06 | 88.17 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.66 | 1.85 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 6.01 | 9.99 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 32.19 | 123.86 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 41.71 | 51.08 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.27 | 0.28 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.92 | 1.01 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 2.28 | 2.58 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 204.83 | 220.47 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 0.98 | 1.02 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 4.35 | 4.57 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 12.13 | 12.46 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 17.29 | 42.58 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 187.97 | 236.33 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 2.26 | 2.31 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 3.82 | 5.44 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 31.22 | 36.30 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 188.97 | 189.83 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 247.62 | 2.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 328.22 | 5.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 1270.00 | 14.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 7821.56 | 180.94 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 4.74 | 7.19 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 6.12 | 9.28 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 20.42 | 80.17 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 224.04 | 602.61 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.25 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.25 | 0.36 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.48 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 183.26 | 187.25 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.19 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.76 | 1.58 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 1.02 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 3.98 | 4.45 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 4.15 | 8.82 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 22.63 | 25.50 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 288.24 | 340.34 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 1.22 | 3.00 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.66 | 1.69 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 42.25 | 47.81 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 208.12 | 211.22 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 791.42 | 6.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 721.21 | 13.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 7294.90 | 85.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 7668.06 | 141.22 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 18.34 | 22.05 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 38.45 | 150.82 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 72.05 | 240.19 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 89.32 | 257.39 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.24 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 1.19 | 2.40 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 2.55 | 2.84 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 207.27 | 212.85 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 1.02 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 13.59 | 14.13 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 19.44 | 27.57 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 207.90 | 212.18 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 341.84 | 755.29 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.85 | 1.89 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 7.31 | 12.51 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 10.44 | 12.81 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 200.57 | 202.84 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3120.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 313.43 | 1.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 802.10 | 14.87 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 3065.10 | 41.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 6500.80 | 82.05 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 3.81 | 8.73 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 7.39 | 12.69 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 31.76 | 56.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 68.69 | 272.85 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.37 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.90 | 0.94 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 1.25 | 1.52 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 323.27 | 334.05 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.18 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.39 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.85 | 2.04 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 4.12 | 8.20 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 27.46 | 28.10 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 125.28 | 168.13 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.45 | 0.49 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.60 | 1.64 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 26.70 | 27.88 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 75.55 | 83.79 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1344.46 | 3.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 3014.54 | 61.85 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 16744.48 | 136.95 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 162959.90 | 1460.68 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 11.68 | 13.18 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 64.13 | 85.53 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 132.12 | 136.29 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 301.73 | 1192.39 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.24 | 0.26 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.45 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 2524.76 | 2562.96 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.33 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 2182.34 | 2263.27 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 2.41 | 2.54 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 2.94 | 3.03 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 5.47 | 20.02 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 7.64 | 10.74 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 1.55 | 3.44 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 2.71 | 2.75 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 612.20 | 641.36 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | no | 2461.79 | 2531.22 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 320.12 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 1239.99 | 7.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 773.91 | 9.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 3979.27 | 61.68 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 4.57 | 7.84 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 6.21 | 9.60 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 20.77 | 26.26 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 41.53 | 147.52 | 100% | 273.40 | +259.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.56 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 2.90 | 10.23 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 12.04 | 14.83 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.34 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 0.52 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 0.78 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 2.14 | 2.20 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 2.57 | 4.12 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 2.93 | 3.09 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 4.06 | 5.36 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 85.19 | 85.67 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 1.33 | 1.40 | 100% | 3585.00 | +3165.00 | pass |
| [Ty](latest-results/ty-20260618T073500Z.json) | yes | 1.54 | 1.57 | 100% | 1650.00 | +1230.00 | pass |
| [Pyright](latest-results/pyright-20260618T073500Z.json) | yes | 28.58 | 33.48 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260618T073500Z.json) | yes | 188.26 | 198.81 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 273.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 212.04 | 0.28 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.93 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.25 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 0.18 | 0.20 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 1954.42 | 24.71 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 20.01 | 27.11 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 47.38 | 51.04 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260618T073500Z.json) | yes | 6.74 | 6.97 | 100% | 75.00 | 0.00 | pass |
