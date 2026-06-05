# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260605T072341Z.json`

- Generated at: 20260605T072341Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.410 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.410/package/dist/pyright-langserver.js |
| Ty | 0.0.44 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.44/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 6 | 3995.88 | 3.38 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 8 | 10235.12 | 20.20 | 205 | 98% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 6 | 37169.78 | 70.98 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 6 | 215859.87 | 354.49 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 583.32 | 3.59 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 874.35 | 13.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 3502.61 | 51.42 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 7159.89 | 93.61 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 1.80 | 2.03 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 6.63 | 10.11 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 39.17 | 146.46 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 58.79 | 68.60 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.33 | 0.39 | 100% | 4244.00 | +225.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 1.12 | 1.21 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 1.96 | 2.13 | 100% | 3604.00 | -415.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 208.08 | 220.44 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.51 | 0.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 1.06 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 4.63 | 4.89 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 13.21 | 13.52 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 21.24 | 47.22 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 218.25 | 306.20 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 2.42 | 2.59 | 100% | 376.00 | +98.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 4.30 | 6.77 | 100% | 2075.00 | +1797.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 30.60 | 36.50 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 195.50 | 209.82 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3604.00, 4019.00, 4134.00, 4244.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (2075.00, 278.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 257.56 | 2.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 467.35 | 9.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 1404.13 | 15.58 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 8354.56 | 186.88 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 5.51 | 8.34 | 100% | 259.00 | +249.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 6.06 | 11.91 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 36.38 | 134.67 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 214.21 | 683.43 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.59 | 0.67 | 100% | 57.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.71 | 2.03 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 2.63 | 2.92 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 184.21 | 189.50 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.23 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.49 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 1.01 | 2.63 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 1.09 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 3.49 | 3.86 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 5.85 | 13.80 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 25.87 | 29.86 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 323.16 | 374.54 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 2.00 | 2.07 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 2.47 | 4.98 | 100% | 1190.00 | +1107.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 44.87 | 49.87 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 211.75 | 217.08 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 259.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 1190.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 888.41 | 6.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 800.96 | 16.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 9629.64 | 155.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 8255.84 | 156.05 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 18.18 | 21.46 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 40.39 | 160.17 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 80.86 | 267.95 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 125.77 | 385.95 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.27 | 0.29 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 1.48 | 3.33 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 8.44 | 19.79 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 208.59 | 209.36 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.29 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.50 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 11.89 | 12.46 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 26.01 | 55.02 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 240.68 | 242.86 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 684.53 | 1091.96 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 1.66 | 1.69 | 100% | 4378.00 | +86.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 6.52 | 14.85 | 100% | 2481.00 | -1811.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 11.90 | 16.79 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 204.16 | 207.21 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 2481.00, 4292.00, 4378.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 349.52 | 1.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 898.79 | 18.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 3337.86 | 46.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 7259.40 | 89.31 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 3.90 | 8.60 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 8.48 | 13.97 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 29.59 | 43.34 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 81.43 | 323.00 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.42 | 0.45 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.82 | 0.88 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 1.26 | 1.44 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 353.66 | 361.65 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.24 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.28 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.40 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 1.18 | 1.28 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 2.30 | 2.49 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 3.11 | 7.76 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 31.31 | 32.32 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 140.27 | 200.65 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 1.82 | 1.86 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 4.55 | 9.31 | 100% | 1869.00 | +969.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 30.80 | 31.06 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 81.57 | 87.99 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 1869.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 1543.18 | 3.84 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 3727.41 | 87.73 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 17931.63 | 147.74 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 180439.73 | 1534.75 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 12.37 | 14.14 | 100% | 771.00 | +648.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 61.69 | 103.46 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 155.48 | 159.21 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 421.61 | 1684.72 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.23 | 0.24 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.60 | 0.69 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 2619.34 | 2669.28 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.26 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.46 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.53 | 1.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 2314.58 | 2372.61 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 2.51 | 2.62 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 3.30 | 3.46 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 7.54 | 9.70 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 13.60 | 14.88 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 2.66 | 8.40 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 3.07 | 3.07 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 668.42 | 692.43 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | no | 2581.84 | 2596.16 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 771.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 373.89 | 2.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 1363.92 | 8.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 873.60 | 12.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 4390.46 | 66.35 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 5.59 | 10.08 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 6.04 | 9.16 | 100% | 453.00 | +439.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 24.70 | 31.08 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 50.18 | 173.07 | 100% | 275.40 | +261.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.63 | 0.68 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 4.37 | 11.42 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 13.27 | 18.84 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.43 | 0.46 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 0.58 | 0.70 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 0.82 | 0.93 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 3.23 | 3.33 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 2.45 | 6.44 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 3.01 | 3.22 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 4.71 | 6.04 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 100.41 | 101.72 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260605T072341Z.json) | yes | 1.61 | 1.66 | 100% | 1650.00 | +1230.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 3.32 | 6.16 | 100% | 3606.00 | +3186.00 | pass |
| [Pyright](latest-results/pyright-20260605T072341Z.json) | yes | 32.62 | 36.75 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260605T072341Z.json) | yes | 190.13 | 192.83 | 100% | 363.00 | -57.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 275.40, 453.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 227.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1650.00, 3606.00, 363.00, 420.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 240.17 | 0.34 | 8 | 40 | 100% | 0 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 1.15 | 1.28 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.31 | 0.63 | 100% | 8.00 | 0.00 | pass |

### flow narrowed branch type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.22 | 0.24 | 100% | 8.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### edited narrowing recomputes type (edit+getComputedType)

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 0.23 | 0.24 | 100% | 5.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 2352.46 | 13.01 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 20.64 | 50.15 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 10.14 | 10.83 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260605T072341Z.json) | yes | 8.26 | 8.62 | 100% | 75.00 | 0.00 | pass |
