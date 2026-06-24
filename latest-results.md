# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260624T070549Z.json`

- Generated at: 20260624T070549Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.52 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.52/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 6 | 3501.13 | 3.18 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 8 | 8999.33 | 17.51 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 6 | 34546.55 | 59.59 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 6 | 198390.41 | 337.25 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 466.93 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 740.86 | 10.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 3626.02 | 59.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 6985.51 | 88.60 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1.72 | 1.99 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 6.25 | 9.39 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 32.13 | 123.67 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 44.39 | 56.00 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.27 | 0.28 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.94 | 0.99 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2.23 | 2.52 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 204.18 | 221.25 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 0.97 | 1.03 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 4.15 | 4.78 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 8.15 | 9.13 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 16.47 | 18.58 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 259.36 | 383.15 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 1.86 | 3.03 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 2.84 | 2.86 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 27.98 | 28.92 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 189.29 | 190.57 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 227.35 | 2.01 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 333.88 | 5.44 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 1262.23 | 14.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 7828.79 | 176.77 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 4.86 | 7.50 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 5.81 | 12.03 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 21.17 | 82.01 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 214.57 | 536.02 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.26 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.32 | 0.66 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.54 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 182.89 | 184.31 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.43 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 0.98 | 1.02 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 3.02 | 3.45 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 4.92 | 12.13 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 23.42 | 26.46 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 277.13 | 321.60 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.62 | 0.68 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1.67 | 1.72 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 41.04 | 43.35 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 208.29 | 210.58 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 821.54 | 7.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 911.28 | 17.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 8200.66 | 93.12 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 7643.70 | 138.93 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 18.55 | 22.48 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 44.65 | 172.74 | 100% | 39.00 | -232.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 74.93 | 200.89 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 84.43 | 286.23 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.23 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.92 | 1.26 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 3.68 | 5.58 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 206.68 | 207.75 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.49 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 3.52 | 5.34 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 14.04 | 15.07 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 30.20 | 56.94 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 209.08 | 211.26 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 368.85 | 856.05 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 2.25 | 2.29 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 6.36 | 10.45 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 10.92 | 13.82 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 202.95 | 211.91 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 316.45 | 1.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 855.36 | 16.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 3188.17 | 44.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 6542.51 | 82.39 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 3.99 | 9.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 7.68 | 12.06 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 31.81 | 55.59 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 72.15 | 278.35 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.38 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 1.42 | 1.80 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 1.87 | 3.30 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 325.63 | 331.62 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.19 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.39 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 1.04 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2.90 | 4.47 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1.86 | 2.10 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2.56 | 7.89 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 26.31 | 27.18 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 132.35 | 185.94 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1.59 | 1.61 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 3.76 | 10.40 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 27.16 | 27.75 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 78.18 | 85.16 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1357.71 | 3.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 3106.63 | 65.23 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 16987.77 | 138.84 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 165298.91 | 1474.67 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 11.70 | 13.13 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 62.18 | 96.82 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 135.75 | 141.38 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 306.47 | 1205.19 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.49 | 0.59 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 1.68 | 2.94 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 2529.84 | 2568.06 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.24 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.39 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.51 | 0.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 2214.85 | 2295.61 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 2.57 | 2.77 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 2.90 | 2.98 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 7.39 | 10.57 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 9.05 | 23.49 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 2.75 | 2.80 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 8.43 | 16.64 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 623.74 | 639.88 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | no | 2490.34 | 2510.29 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 311.15 | 2.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 1281.70 | 8.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 823.73 | 10.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 4090.99 | 62.12 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 4.46 | 7.61 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 6.10 | 9.21 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 22.23 | 29.92 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 47.00 | 149.53 | 100% | 273.40 | +259.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 1.43 | 3.32 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2.90 | 10.24 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 10.98 | 14.61 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.35 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 0.54 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 0.99 | 1.36 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 2.12 | 2.16 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 1.87 | 3.80 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 2.99 | 3.19 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 5.09 | 6.42 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 87.37 | 88.08 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260624T070549Z.json) | yes | 1.49 | 1.52 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2.62 | 4.51 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260624T070549Z.json) | yes | 29.82 | 34.91 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260624T070549Z.json) | yes | 187.89 | 189.18 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 273.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 211.00 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 1.80 | 4.49 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.37 | 0.76 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 0.20 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 2016.60 | 27.39 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 23.75 | 52.11 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 52.04 | 67.30 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260624T070549Z.json) | yes | 6.37 | 6.56 | 100% | 75.00 | 0.00 | pass |
