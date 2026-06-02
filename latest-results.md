# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260602T073229Z.json`

- Generated at: 20260602T073229Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.42 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.42/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 6 | 3787.07 | 3.21 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 8 | 10504.09 | 21.45 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 6 | 34968.03 | 63.61 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 6 | 203582.69 | 341.11 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 519.98 | 3.23 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 847.39 | 12.40 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 3341.07 | 48.80 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 7470.11 | 91.75 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1.74 | 1.87 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 5.61 | 10.04 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 37.04 | 140.66 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 52.19 | 67.96 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.33 | 0.34 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 1.02 | 1.12 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 1.87 | 2.07 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 207.42 | 221.49 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.25 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 4.92 | 5.01 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 11.77 | 12.56 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 19.56 | 45.14 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 207.33 | 248.61 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 2.07 | 2.12 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 3.27 | 3.29 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 29.64 | 31.73 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 193.17 | 197.01 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 246.35 | 2.11 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 389.11 | 7.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 1306.00 | 14.32 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 8201.98 | 182.28 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 4.65 | 7.28 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 4.95 | 7.88 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 27.77 | 106.75 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 212.83 | 667.17 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.25 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.54 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 1.86 | 3.57 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 181.84 | 184.31 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.67 | 1.94 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 1.86 | 3.98 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 3.16 | 3.46 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 23.45 | 25.43 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 305.77 | 351.26 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1.96 | 1.99 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 2.90 | 4.44 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 42.56 | 48.33 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 209.92 | 214.13 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 844.89 | 6.04 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 764.14 | 15.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 8569.85 | 118.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 8023.94 | 153.22 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 17.14 | 21.13 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 38.41 | 152.29 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 74.32 | 251.90 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 119.17 | 371.98 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.26 | 0.30 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.77 | 0.87 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 7.88 | 17.95 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 208.23 | 209.02 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.49 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 2.90 | 3.01 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 10.97 | 11.59 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 24.35 | 41.19 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 236.62 | 254.20 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 506.35 | 988.79 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1.62 | 1.66 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 4.76 | 10.76 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 9.79 | 11.58 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 201.01 | 208.96 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 343.53 | 1.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 867.03 | 17.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 3268.27 | 46.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 6756.14 | 83.50 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 4.05 | 9.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 7.39 | 11.66 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 31.55 | 54.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 79.54 | 309.13 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.40 | 0.43 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 2.13 | 4.35 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 2.37 | 3.49 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 330.58 | 332.02 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.46 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 2.30 | 2.56 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 3.49 | 3.74 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 27.62 | 27.77 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 139.01 | 190.33 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.85 | 1.78 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1.87 | 1.89 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 26.69 | 26.76 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 82.48 | 90.17 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1463.08 | 3.75 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 3655.21 | 86.02 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 17190.20 | 145.74 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 169035.59 | 1474.41 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 11.84 | 13.86 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 55.33 | 96.19 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 139.66 | 144.17 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 419.40 | 1676.23 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.22 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.49 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 2501.07 | 2533.83 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.31 | 0.59 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 2225.56 | 2303.52 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 2.66 | 2.83 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 3.35 | 3.44 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 6.49 | 7.08 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 7.74 | 19.08 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 2.43 | 7.86 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 3.11 | 3.14 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 665.96 | 690.79 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | no | 2503.09 | 2537.79 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 369.25 | 2.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 1292.64 | 8.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 883.84 | 12.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 4094.93 | 61.50 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 4.50 | 7.89 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 6.40 | 9.81 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 22.95 | 26.81 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 51.01 | 174.51 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 0.51 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 4.33 | 11.77 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 10.65 | 17.46 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.37 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 0.60 | 0.67 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 1.43 | 3.63 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 2.34 | 2.43 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 3.02 | 3.22 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 3.28 | 5.17 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 4.12 | 6.13 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 92.19 | 92.77 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260602T073229Z.json) | yes | 1.64 | 1.70 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 1.67 | 1.74 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260602T073229Z.json) | yes | 29.94 | 33.95 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260602T073229Z.json) | yes | 179.35 | 181.90 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 229.00 | 0.42 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 1.77 | 4.16 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.30 | 0.59 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.22 | 0.26 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 0.22 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 2868.37 | 41.30 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 14.11 | 22.87 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 52.18 | 56.70 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260602T073229Z.json) | yes | 57.62 | 62.22 | 100% | 75.00 | 0.00 | pass |
