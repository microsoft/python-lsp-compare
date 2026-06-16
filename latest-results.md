# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260616T075050Z.json`

- Generated at: 20260616T075050Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.49 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.49/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 6 | 3582.39 | 3.10 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 8 | 9842.43 | 19.14 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 6 | 32769.43 | 56.73 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 6 | 201204.56 | 335.56 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 466.61 | 3.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 801.73 | 10.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 3301.57 | 49.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 7094.71 | 86.08 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.64 | 1.81 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 6.10 | 10.13 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 30.21 | 115.10 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 51.01 | 58.32 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.29 | 0.30 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.98 | 1.05 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.16 | 3.75 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 190.69 | 192.87 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.94 | 2.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 1.01 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 4.36 | 4.70 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 11.40 | 11.83 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 17.74 | 43.15 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 209.15 | 293.86 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 2.33 | 2.36 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.24 | 3.28 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 29.39 | 35.42 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 183.34 | 184.39 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 231.64 | 2.01 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 365.53 | 6.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 1287.30 | 14.59 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 7768.12 | 172.33 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 4.77 | 7.57 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 4.85 | 7.24 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 26.70 | 98.77 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 201.62 | 638.08 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.27 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.53 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 173.23 | 175.99 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.44 | 1.02 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.54 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 2.94 | 3.10 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.38 | 10.11 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 23.66 | 27.24 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 286.58 | 327.14 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.76 | 0.80 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.82 | 1.84 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 43.47 | 48.68 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 199.16 | 201.42 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 792.57 | 6.26 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 794.39 | 16.43 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 7578.73 | 90.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 7663.14 | 148.26 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 16.92 | 20.58 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 34.48 | 136.22 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 72.08 | 235.05 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 128.01 | 410.51 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.24 | 0.28 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 1.20 | 2.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 11.23 | 19.52 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 201.84 | 203.79 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.44 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 1.06 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 2.92 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 12.06 | 13.85 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 22.74 | 30.14 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 216.00 | 223.98 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 365.14 | 790.03 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.88 | 1.90 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 10.77 | 10.83 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 12.40 | 13.59 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 194.40 | 196.96 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 324.12 | 1.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 863.78 | 16.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 3179.18 | 44.06 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 6671.83 | 82.89 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 3.80 | 8.69 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 7.19 | 11.96 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 30.98 | 52.82 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 72.51 | 286.79 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.40 | 0.40 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 1.59 | 2.00 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.28 | 5.16 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 328.38 | 332.87 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.35 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.63 | 1.65 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.88 | 2.03 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 6.62 | 17.61 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 26.91 | 27.18 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 129.88 | 180.69 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.55 | 0.59 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.70 | 1.74 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 27.13 | 27.29 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 81.30 | 87.33 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1436.04 | 3.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3673.62 | 86.09 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 16144.42 | 133.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 167915.19 | 1462.34 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 10.91 | 12.48 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 51.85 | 85.47 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 140.84 | 146.67 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 409.66 | 1637.42 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.20 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.46 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 2509.41 | 2540.14 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.40 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 2188.04 | 2209.30 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.55 | 0.58 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 2.49 | 2.56 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 3.08 | 3.15 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 6.83 | 8.69 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 2.86 | 2.87 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 19.84 | 26.55 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 609.26 | 631.93 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | no | 2470.91 | 2493.25 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 331.41 | 2.11 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 1278.23 | 8.40 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 813.96 | 10.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 4091.57 | 61.45 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 4.90 | 8.16 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 5.56 | 8.76 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 22.46 | 27.90 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 40.92 | 143.38 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.52 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.98 | 10.67 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 10.80 | 15.37 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.36 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 0.48 | 0.53 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 0.68 | 0.73 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 2.31 | 2.38 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 2.81 | 2.92 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 3.48 | 4.64 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 4.44 | 5.62 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 92.48 | 93.04 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260616T075050Z.json) | yes | 1.52 | 1.54 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 2.57 | 5.31 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260616T075050Z.json) | yes | 31.45 | 34.19 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260616T075050Z.json) | yes | 179.18 | 180.85 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 203.52 | 0.30 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.96 | 1.06 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.28 | 0.51 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.20 | 0.23 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 2325.91 | 16.25 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 23.94 | 41.78 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 16.09 | 22.82 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260616T075050Z.json) | yes | 8.72 | 8.87 | 100% | 75.00 | 0.00 | pass |
