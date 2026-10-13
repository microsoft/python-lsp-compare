# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261013T060740Z.json`

- Generated at: 20261013T060740Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.86 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.86/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.2 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 6 | 3497.60 | 4.08 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | no | 8 | 16467.52 | 34.91 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 6 | 38833.23 | 73.76 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 6 | 268277.62 | 375.52 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 498.14 | 4.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 1272.90 | 27.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 4566.98 | 75.23 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 7749.95 | 108.30 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 1.59 | 1.72 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 6.03 | 11.25 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 93.06 | 358.19 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 189.16 | 304.14 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.31 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 1.05 | 1.32 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 5.10 | 6.65 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 180.40 | 181.31 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 4.70 | 7.43 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 4.20 | 4.38 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 13.24 | 15.88 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 32.11 | 76.73 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 338.28 | 447.50 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 3.13 | 5.05 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 5.63 | 5.70 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 30.36 | 34.10 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 166.70 | 167.40 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 258.50 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 292.83 | 4.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 1461.94 | 14.21 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 7653.86 | 165.04 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.28 | 6.67 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 4.98 | 8.42 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 17.76 | 60.42 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 167.17 | 450.91 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.23 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.28 | 0.34 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.59 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 158.12 | 159.34 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.39 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 1.06 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 1.95 | 2.04 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.74 | 4.95 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 26.33 | 27.98 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 254.05 | 288.94 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 3.28 | 3.31 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 4.25 | 12.79 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 38.77 | 46.09 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 244.78 | 246.94 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 840.27 | 7.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 1273.95 | 30.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 7721.10 | 145.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 11565.14 | 179.91 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 17.45 | 20.69 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 88.85 | 305.71 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 89.82 | 356.37 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 130.86 | 355.42 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.29 | 0.33 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.94 | 1.41 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 2.78 | 3.74 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 190.72 | 194.26 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.45 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 1.10 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 17.32 | 19.05 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 46.42 | 71.77 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 221.69 | 225.04 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 797.71 | 1233.44 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.66 | 4.73 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 10.84 | 19.94 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 11.59 | 14.40 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 181.64 | 184.58 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 374.30 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 877.99 | 19.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 3799.51 | 50.88 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 7104.31 | 113.71 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 2.98 | 6.94 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 14.45 | 25.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 88.69 | 353.81 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 162.89 | 385.32 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.40 | 0.41 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 1.64 | 1.82 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 2.60 | 3.68 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 326.76 | 330.90 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.44 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 1.25 | 1.78 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 1.84 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 3.67 | 12.26 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 5.73 | 6.07 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 37.98 | 38.77 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 135.03 | 170.82 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.50 | 0.54 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 5.28 | 5.31 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 39.69 | 40.50 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 102.87 | 110.63 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 1175.94 | 4.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 15894.47 | 113.00 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 5332.63 | 167.55 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 230958.32 | 1615.08 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 10.38 | 12.52 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 53.92 | 86.27 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 144.40 | 150.76 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 830.98 | 3302.28 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.24 | 0.27 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.28 | 0.35 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.49 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 3007.38 | 3051.73 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.20 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.38 | 0.77 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.45 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 2251.31 | 2277.96 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.68 | 0.77 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 2.66 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.77 | 4.86 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 7.82 | 10.95 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.49 | 4.55 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 5.46 | 20.02 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 502.29 | 533.87 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | no | 2669.67 | 2705.76 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 350.45 | 2.81 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 1545.19 | 9.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 950.02 | 13.14 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 7090.08 | 105.80 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 5.41 | 9.05 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 5.73 | 8.09 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 54.05 | 191.45 | 100% | 207.20 | +193.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 71.57 | 122.36 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.54 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 6.90 | 26.98 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 59.18 | 69.01 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.33 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 0.58 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 0.78 | 1.00 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 73.43 | 103.29 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 2.15 | 4.57 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 4.53 | 4.74 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 4.71 | 5.96 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 90.29 | 92.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 2.28 | 4.52 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261013T060740Z.json) | yes | 3.01 | 3.04 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261013T060740Z.json) | yes | 35.23 | 37.87 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261013T060740Z.json) | yes | 234.52 | 235.82 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 207.20, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | no | 220.07 | 0.33 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 1.03 | 1.10 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 6247.14 | 38.43 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 12.58 | 17.69 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 95.65 | 147.49 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261013T060740Z.json) | yes | 7.08 | 7.28 | 100% | 75.00 | 0.00 | pass |
