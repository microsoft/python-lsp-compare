# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260621T073314Z.json`

- Generated at: 20260621T073314Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.51 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.51/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 6 | 3572.69 | 3.26 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 8 | 9065.92 | 18.44 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 6 | 34008.39 | 58.92 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 6 | 202797.07 | 340.50 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 504.61 | 3.26 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 765.16 | 11.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 3720.65 | 58.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 7319.30 | 90.07 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1.81 | 2.11 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 7.42 | 11.18 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 31.94 | 115.13 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 55.11 | 63.82 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.30 | 0.34 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 1.21 | 1.59 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.46 | 2.66 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 202.27 | 205.61 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.29 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.47 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 4.78 | 4.93 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 11.62 | 11.91 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 18.69 | 44.20 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 249.27 | 390.68 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 2.35 | 2.40 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.68 | 2.71 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 32.06 | 42.21 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 187.13 | 189.84 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 231.90 | 2.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 331.82 | 5.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 1316.15 | 14.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 8002.05 | 184.56 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 4.71 | 7.60 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 4.89 | 7.34 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 23.26 | 83.52 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 244.74 | 689.94 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.23 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.31 | 0.46 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.54 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 181.01 | 183.26 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.45 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.26 | 5.46 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 3.03 | 3.20 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 24.06 | 26.38 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 292.97 | 330.04 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 1.24 | 3.02 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1.86 | 1.88 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 42.88 | 48.78 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 203.03 | 205.26 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 805.14 | 6.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 704.68 | 13.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 7718.37 | 90.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 7982.58 | 147.87 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 18.51 | 22.31 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 35.89 | 141.11 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 72.55 | 245.06 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 112.46 | 335.90 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.26 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.82 | 1.16 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.68 | 3.00 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 208.67 | 213.80 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.48 | 0.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 14.02 | 16.33 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 17.13 | 30.70 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 219.82 | 223.34 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 368.17 | 816.82 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1.96 | 2.04 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 9.39 | 14.68 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 10.61 | 13.41 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 197.35 | 198.85 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3120.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 326.73 | 1.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 830.23 | 16.09 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 3297.33 | 45.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 7006.11 | 87.44 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 3.80 | 8.71 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 6.66 | 11.18 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 36.10 | 61.00 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 67.44 | 262.34 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.40 | 0.42 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 1.30 | 1.62 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 1.60 | 3.06 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 341.81 | 344.12 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.22 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 1.04 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 2.08 | 2.30 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 10.01 | 20.87 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 29.46 | 30.18 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 134.39 | 182.59 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 1.12 | 2.90 | 100% | 1869.00 | +969.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1.76 | 1.78 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 28.80 | 29.07 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 85.51 | 93.47 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1381.00 | 3.34 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 3003.06 | 64.37 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 16648.18 | 136.15 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 168408.77 | 1471.92 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 10.63 | 12.26 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 51.17 | 84.82 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 140.12 | 143.98 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 290.28 | 1145.63 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.46 | 1.15 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.50 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 2515.24 | 2546.39 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.40 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.45 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 2202.16 | 2260.15 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 2.58 | 2.69 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 2.92 | 2.96 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 6.67 | 8.93 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 13.95 | 25.38 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 2.69 | 2.76 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 16.71 | 27.81 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 622.01 | 637.46 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | no | 2499.49 | 2522.09 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 323.32 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 1307.71 | 8.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 797.92 | 9.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 4078.25 | 61.15 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 5.24 | 9.58 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 6.15 | 9.92 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 21.96 | 25.45 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 42.86 | 148.74 | 100% | 273.40 | +259.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.57 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.90 | 10.16 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 11.28 | 15.10 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.37 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 0.55 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 0.74 | 0.82 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 2.27 | 2.40 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 1.38 | 3.71 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 2.89 | 3.01 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 5.10 | 7.78 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 93.84 | 96.85 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260621T073314Z.json) | yes | 1.53 | 1.58 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2.11 | 4.17 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260621T073314Z.json) | yes | 31.18 | 35.51 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260621T073314Z.json) | yes | 176.41 | 177.72 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 273.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 205.14 | 0.40 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 1.75 | 4.13 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.26 | 0.27 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 0.22 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 2427.92 | 50.68 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 26.28 | 37.85 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 118.73 | 136.15 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260621T073314Z.json) | yes | 7.04 | 7.26 | 100% | 75.00 | 0.00 | pass |
