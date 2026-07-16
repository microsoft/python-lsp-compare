# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260716T064540Z.json`

- Generated at: 20260716T064540Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.59 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.59/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 6 | 3350.21 | 3.03 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 8 | 9299.65 | 19.21 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 6 | 34666.65 | 60.33 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 6 | 202004.71 | 333.72 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 426.16 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 766.11 | 10.97 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 4344.22 | 72.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 7393.30 | 98.94 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1.69 | 1.87 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 6.41 | 9.95 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 31.82 | 119.57 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 152.20 | 292.45 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 1.72 | 3.61 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 3.24 | 4.25 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 171.91 | 174.03 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.42 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.99 | 2.98 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 4.72 | 5.00 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 7.79 | 9.74 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 16.78 | 18.80 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 322.35 | 459.44 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.00 | 2.44 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.71 | 2.75 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 31.89 | 36.77 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 164.83 | 170.44 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 218.10 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 316.05 | 5.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 1368.76 | 12.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 7464.91 | 164.87 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 4.00 | 7.37 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 4.73 | 7.43 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 22.84 | 81.28 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 197.03 | 625.00 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.24 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.52 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.07 | 2.66 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 153.15 | 154.85 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 1.06 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.88 | 3.92 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.61 | 2.72 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 22.55 | 26.13 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 286.73 | 315.47 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.66 | 0.70 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1.52 | 1.55 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 36.79 | 42.17 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 186.40 | 189.29 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 792.10 | 6.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 760.25 | 14.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 7982.73 | 91.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 7364.68 | 134.28 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 18.98 | 21.93 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 40.09 | 150.29 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 72.66 | 244.15 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 98.24 | 294.41 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.26 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.61 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 5.64 | 7.40 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 183.69 | 187.63 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 1.09 | 1.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 2.91 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 13.14 | 14.65 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 22.89 | 31.63 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 209.74 | 216.99 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 374.47 | 866.15 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.69 | 0.74 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.05 | 2.08 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 10.09 | 11.50 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 178.66 | 181.83 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 311.92 | 1.53 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 774.56 | 14.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 3313.57 | 44.38 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 6948.73 | 84.36 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 3.67 | 8.52 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 6.56 | 11.86 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 44.24 | 77.50 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 65.90 | 261.66 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.40 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.12 | 1.69 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 1.26 | 1.58 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 314.76 | 318.82 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 1.16 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1.80 | 1.99 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 5.27 | 11.35 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 29.27 | 29.52 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 132.17 | 162.36 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1.52 | 1.53 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.96 | 6.34 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 32.37 | 37.33 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 81.48 | 86.01 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1308.42 | 3.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 2917.02 | 60.23 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 16243.39 | 132.04 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 168963.66 | 1462.80 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 10.49 | 11.99 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 49.98 | 81.88 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 146.20 | 148.27 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 291.54 | 1154.58 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.26 | 0.37 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.45 | 0.49 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.53 | 1.41 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 2488.48 | 2545.46 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 2199.17 | 2261.35 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 2.65 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.76 | 2.90 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 6.30 | 7.81 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 7.30 | 16.13 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 1.57 | 2.53 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.55 | 2.59 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 603.03 | 626.09 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | no | 2477.48 | 2515.01 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 293.51 | 2.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 1413.98 | 8.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 810.64 | 9.76 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 3869.43 | 57.06 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 4.76 | 7.70 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 5.97 | 9.20 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 21.97 | 25.50 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 43.02 | 141.98 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.59 | 0.67 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 2.78 | 9.59 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 9.15 | 13.71 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.38 | 0.40 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 0.52 | 0.55 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 0.78 | 0.93 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 2.34 | 2.49 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.59 | 0.61 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 2.48 | 2.67 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 5.73 | 9.03 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 93.35 | 96.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260716T064540Z.json) | yes | 1.05 | 1.08 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 2.00 | 4.03 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260716T064540Z.json) | yes | 30.67 | 34.44 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260716T064540Z.json) | yes | 158.50 | 159.30 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 247.06 | 0.31 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.97 | 1.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.30 | 0.32 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 0.26 | 0.29 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 2707.97 | 69.00 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 19.97 | 27.64 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 126.12 | 138.11 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260716T064540Z.json) | yes | 60.91 | 74.04 | 100% | 75.00 | 0.00 | pass |
