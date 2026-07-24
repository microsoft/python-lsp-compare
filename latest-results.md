# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260724T064712Z.json`

- Generated at: 20260724T064712Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.63 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.63/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.1.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 6 | 3446.00 | 3.11 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 8 | 8488.14 | 16.44 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 6 | 35089.30 | 61.18 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 6 | 203114.86 | 339.53 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 512.53 | 3.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 748.57 | 10.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 4285.45 | 71.86 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 7355.35 | 109.56 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1.74 | 1.97 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 7.37 | 13.76 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 30.25 | 117.48 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 201.52 | 345.89 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.32 | 0.37 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 1.73 | 3.69 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2.38 | 2.44 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 174.04 | 174.60 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.45 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 1.03 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 4.52 | 4.80 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 9.58 | 11.57 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 18.41 | 23.96 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 316.73 | 427.14 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.51 | 0.55 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 3.20 | 3.33 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 33.01 | 39.67 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 166.69 | 168.98 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 219.48 | 1.96 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 312.15 | 4.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 1423.52 | 13.09 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 7566.02 | 166.53 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 4.56 | 7.82 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 4.83 | 7.61 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 20.34 | 77.85 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 191.55 | 599.07 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.26 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.49 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 156.22 | 157.48 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 1.09 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2.50 | 6.42 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 2.85 | 3.14 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 24.17 | 26.84 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 297.51 | 334.62 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 1.26 | 3.05 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1.69 | 1.76 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 35.85 | 39.82 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 186.27 | 188.35 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 780.84 | 6.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 706.10 | 13.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 8187.86 | 94.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 7336.36 | 133.08 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 17.57 | 20.88 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 36.78 | 145.30 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 75.16 | 249.97 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 90.50 | 259.24 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.26 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.67 | 0.79 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2.73 | 2.97 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 185.04 | 187.84 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 1.05 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 12.75 | 13.55 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 20.90 | 30.81 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 212.06 | 215.57 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 384.67 | 881.88 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 2.24 | 2.31 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 4.73 | 10.80 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 11.93 | 12.82 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 176.74 | 178.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 297.23 | 1.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 834.63 | 16.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 3373.75 | 44.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 6660.94 | 83.35 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 3.53 | 8.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 6.71 | 11.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 37.76 | 85.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 65.98 | 260.90 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.40 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 1.03 | 1.04 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 1.20 | 1.35 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 319.60 | 323.68 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 1.27 | 1.55 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1.93 | 2.00 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 6.61 | 11.37 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 29.68 | 30.55 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 134.08 | 158.34 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1.69 | 1.72 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 9.60 | 22.63 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 28.45 | 29.54 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 81.23 | 89.82 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1342.26 | 3.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2927.38 | 61.69 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 16379.02 | 134.35 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 170150.73 | 1484.41 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 10.77 | 11.54 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 48.79 | 74.39 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 141.06 | 142.72 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 287.45 | 1148.54 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.21 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.37 | 0.82 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.46 | 0.49 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 2583.74 | 2645.71 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.29 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.44 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 2225.43 | 2287.52 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 2.82 | 3.14 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 3.17 | 3.25 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 6.22 | 7.01 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 14.82 | 36.43 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 2.97 | 3.04 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 5.76 | 18.16 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 615.84 | 633.17 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | no | 2469.00 | 2505.98 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 293.65 | 2.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 1439.71 | 8.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 807.94 | 11.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 4045.47 | 60.27 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 5.29 | 8.59 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 5.70 | 8.86 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 22.75 | 28.11 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 50.06 | 153.05 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.22 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.53 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2.78 | 9.71 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 9.30 | 14.52 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.35 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 0.54 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 0.88 | 1.35 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 2.51 | 3.21 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.58 | 0.62 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 2.52 | 2.73 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 4.59 | 6.18 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 96.36 | 98.40 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260724T064712Z.json) | yes | 1.16 | 1.17 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 2.57 | 4.43 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260724T064712Z.json) | yes | 31.03 | 35.57 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260724T064712Z.json) | yes | 170.46 | 198.55 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 205.90 | 0.30 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.95 | 1.00 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.28 | 0.30 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 0.23 | 0.26 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 1945.47 | 27.16 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 21.65 | 36.21 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 52.64 | 57.42 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260724T064712Z.json) | yes | 7.20 | 7.38 | 100% | 75.00 | 0.00 | pass |
