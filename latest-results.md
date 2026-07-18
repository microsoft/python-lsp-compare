# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260718T063555Z.json`

- Generated at: 20260718T063555Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.61 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.61/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 6 | 3732.22 | 3.77 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 8 | 8903.47 | 16.96 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 6 | 36552.80 | 63.94 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 6 | 213950.73 | 357.98 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 525.69 | 3.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 757.51 | 10.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 3930.14 | 62.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 7446.65 | 115.36 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 2.37 | 2.49 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 6.44 | 11.19 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 31.75 | 123.73 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 212.82 | 318.63 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.41 | 0.50 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 1.01 | 1.12 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 2.67 | 3.22 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 172.63 | 174.37 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.45 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 1.01 | 1.04 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 4.26 | 4.59 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 12.45 | 14.07 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 15.25 | 18.26 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 276.88 | 392.37 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.57 | 0.67 | 100% | 2075.00 | +1797.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 3.85 | 4.48 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 29.45 | 32.48 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 186.06 | 193.10 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 235.71 | 2.23 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 333.50 | 5.55 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 1562.25 | 14.96 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 8333.59 | 185.25 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 4.81 | 8.23 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 5.75 | 8.06 | 100% | 259.00 | +249.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 20.91 | 80.29 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 224.65 | 712.27 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.30 | 0.31 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.56 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 3.27 | 4.49 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 168.58 | 170.60 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.80 | 4.86 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.10 | 1.19 | 100% | 83.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 3.22 | 3.55 | 100% | 104.00 | -1.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 27.44 | 32.91 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 331.44 | 398.32 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.66 | 0.70 | 100% | 1190.00 | +1107.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 1.63 | 1.70 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 41.57 | 51.19 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 200.54 | 211.77 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 810.50 | 7.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 745.53 | 14.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 8363.42 | 94.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 8142.03 | 148.35 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 18.82 | 21.73 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 42.24 | 157.26 | 100% | 39.00 | -232.20 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 73.12 | 243.51 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 107.41 | 317.10 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.32 | 0.39 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.70 | 0.78 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 3.14 | 3.84 | 100% | 3121.00 | +2771.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 198.28 | 203.04 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.48 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 13.26 | 14.33 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 23.41 | 38.65 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 245.44 | 257.83 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 387.18 | 863.07 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.08 | 1.21 | 100% | 2481.00 | -1811.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 2.37 | 2.38 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 13.40 | 18.07 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 189.57 | 191.13 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 271.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 3121.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4441.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 319.27 | 1.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 818.50 | 16.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 3489.82 | 48.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 6718.58 | 86.74 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 3.87 | 9.01 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 7.58 | 13.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 46.76 | 77.76 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 73.42 | 284.20 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.43 | 0.48 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.36 | 1.98 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 1.56 | 1.84 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 331.07 | 343.71 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.24 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.49 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 1.23 | 1.49 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.76 | 0.82 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 2.13 | 2.26 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 27.47 | 27.78 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 142.20 | 183.21 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 1.86 | 1.89 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 4.45 | 6.99 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 27.15 | 27.64 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 93.03 | 105.04 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 1480.07 | 4.96 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 3000.48 | 62.24 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 17609.04 | 151.78 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 178800.60 | 1546.05 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 16.15 | 18.98 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 60.29 | 94.05 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 138.35 | 140.11 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 299.75 | 1177.55 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.57 | 0.65 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.84 | 2.62 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 3.06 | 5.36 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 2731.83 | 2911.55 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.32 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.63 | 0.98 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.50 | 2.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 2325.79 | 2471.01 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 3.14 | 3.63 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 4.41 | 4.73 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 6.36 | 22.95 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 7.13 | 8.05 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.55 | 0.60 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 3.10 | 3.16 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 690.29 | 725.05 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | no | 2531.13 | 2711.98 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 360.97 | 2.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 1598.13 | 10.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 862.44 | 11.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 4509.28 | 66.13 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 4.96 | 8.63 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 8.72 | 12.86 | 100% | 454.00 | +440.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 26.87 | 35.22 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 52.55 | 163.43 | 100% | 274.40 | +260.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.27 | 0.29 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 0.59 | 0.90 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 2.94 | 10.29 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 9.47 | 16.72 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.35 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 0.65 | 0.81 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 1.00 | 1.55 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 12.40 | 32.82 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.22 | 3.01 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 3.23 | 3.75 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 5.73 | 7.99 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 101.71 | 103.10 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260718T063555Z.json) | yes | 1.43 | 1.52 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 1.43 | 1.53 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260718T063555Z.json) | yes | 38.36 | 53.90 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260718T063555Z.json) | yes | 180.20 | 222.16 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 274.40, 454.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3585.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 212.63 | 0.29 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.90 | 0.98 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.26 | 0.27 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 0.22 | 0.23 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 2172.87 | 31.58 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 23.49 | 32.35 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 62.00 | 68.29 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260718T063555Z.json) | yes | 9.26 | 10.44 | 100% | 75.00 | 0.00 | pass |
