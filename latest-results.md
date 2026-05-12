# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260512T065328Z.json`

- Generated at: 20260512T065328Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.409 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.409/package/dist/pyright-langserver.js |
| Ty | 0.0.35 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.35/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.64.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 6 | 3940.81 | 3.27 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 8 | 9915.09 | 18.76 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 6 | 33194.52 | 58.61 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 6 | 194302.75 | 333.62 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 491.80 | 3.43 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 805.06 | 11.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 3087.50 | 42.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 6901.68 | 88.19 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.67 | 1.84 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 5.44 | 9.56 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 33.35 | 123.92 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 45.45 | 61.37 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.28 | 0.30 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 1.04 | 1.11 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 1.89 | 2.14 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 199.80 | 205.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.48 | 0.63 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 0.98 | 1.03 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 4.20 | 4.60 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 13.26 | 13.47 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 17.44 | 42.17 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 179.42 | 220.70 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.79 | 1.90 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 4.70 | 6.62 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 25.46 | 28.79 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 190.55 | 192.90 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 240.51 | 1.88 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 386.22 | 6.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 1254.83 | 13.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 7611.66 | 172.74 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 4.62 | 7.39 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 5.11 | 8.75 | 100% | 256.00 | +246.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 26.19 | 100.05 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 204.03 | 432.65 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.22 | 0.31 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.23 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.53 | 0.61 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 179.61 | 180.12 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 1.06 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 2.64 | 3.06 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 4.32 | 11.70 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 22.83 | 24.70 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 271.77 | 310.08 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.26 | 1.28 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 2.83 | 4.27 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 37.93 | 42.26 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 207.24 | 211.36 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 256.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 847.99 | 6.25 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 709.01 | 13.13 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 8093.21 | 114.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 7537.32 | 138.37 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 17.73 | 22.81 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 36.62 | 145.16 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 72.39 | 236.00 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 74.27 | 197.99 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.22 | 0.25 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.91 | 1.04 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 7.44 | 8.85 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 208.72 | 215.28 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.55 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 1.03 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 3.31 | 5.29 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 11.76 | 12.19 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 13.14 | 13.31 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 206.39 | 208.58 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 491.70 | 932.24 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.37 | 1.41 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 5.16 | 12.54 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 9.34 | 12.48 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 201.45 | 203.05 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 348.92 | 1.70 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 850.40 | 16.40 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 3141.68 | 42.76 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 6419.36 | 81.30 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 4.62 | 11.43 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 18.11 | 22.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 32.26 | 55.27 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 75.40 | 299.21 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.37 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.74 | 0.78 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 1.73 | 1.90 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 322.07 | 325.55 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.19 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.46 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 1.03 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.89 | 2.10 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 2.67 | 2.85 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 25.70 | 25.99 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 116.26 | 148.85 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.42 | 1.45 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 2.95 | 7.48 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 25.41 | 25.66 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 77.26 | 89.00 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1676.83 | 4.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 3699.25 | 85.55 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 16331.30 | 130.09 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 161855.27 | 1459.69 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 14.61 | 16.09 | 100% | 770.00 | +647.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 53.71 | 77.72 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 132.21 | 140.20 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 409.80 | 1638.00 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.18 | 0.20 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.45 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 2503.88 | 2600.01 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.35 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 2187.18 | 2242.15 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 1.94 | 5.69 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 2.47 | 2.60 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 3.51 | 3.77 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 6.09 | 6.95 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 3.13 | 3.16 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 15.62 | 25.93 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 589.85 | 603.34 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | no | 2472.72 | 2511.84 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 770.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 334.76 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 1286.01 | 8.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 815.74 | 10.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 3977.46 | 61.44 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 5.23 | 9.81 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 5.94 | 9.80 | 100% | 443.00 | +429.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 23.02 | 29.52 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 44.45 | 153.03 | 100% | 267.40 | +253.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.52 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 4.41 | 11.59 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 12.13 | 14.43 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.35 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 0.54 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 0.74 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 2.09 | 2.18 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 2.39 | 2.53 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 3.25 | 5.05 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 4.76 | 7.05 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 85.50 | 85.82 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260512T065328Z.json) | yes | 1.05 | 1.07 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 2.51 | 5.07 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260512T065328Z.json) | yes | 29.59 | 33.06 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260512T065328Z.json) | yes | 184.43 | 187.33 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 267.40, 443.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 210.04 | 0.29 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 1.00 | 1.10 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.24 | 0.51 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.19 | 0.22 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.17 | 0.21 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 0.20 | 0.22 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 2439.37 | 15.09 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 28.60 | 53.90 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 10.18 | 14.91 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260512T065328Z.json) | yes | 6.49 | 6.54 | 100% | 75.00 | 0.00 | pass |
