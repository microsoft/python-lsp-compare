# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260923T060603Z.json`

- Generated at: 20260923T060603Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.83 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.83/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 6 | 5198.53 | 4.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | no | 8 | 16768.31 | 37.61 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 6 | 38479.60 | 73.51 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 6 | 220891.00 | 373.99 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 487.88 | 3.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 1182.44 | 27.11 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 4675.40 | 77.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 7874.03 | 116.42 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 1.60 | 1.78 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 6.18 | 9.45 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 90.82 | 357.79 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 230.81 | 441.98 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 1.12 | 1.40 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 2.54 | 2.69 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 178.78 | 180.19 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.41 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.65 | 1.89 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 1.06 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 4.75 | 5.00 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 11.98 | 13.74 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 38.12 | 51.86 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 350.49 | 462.58 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 3.44 | 3.71 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 5.40 | 5.45 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 31.64 | 34.64 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 166.68 | 170.25 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 258.81 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 313.46 | 4.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 1474.28 | 14.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 8005.21 | 177.64 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 4.61 | 6.71 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 4.64 | 7.36 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 16.93 | 65.37 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 216.71 | 660.78 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.24 | 0.30 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.55 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 155.55 | 157.46 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 1.07 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 3.78 | 8.14 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 4.56 | 4.69 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 26.56 | 29.55 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 257.40 | 301.61 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 1.39 | 3.64 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 3.14 | 3.16 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 39.71 | 46.27 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 257.47 | 285.24 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 843.20 | 7.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 1320.46 | 34.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 7811.16 | 141.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 11332.22 | 183.45 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 18.08 | 21.72 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 76.86 | 256.74 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 93.24 | 372.01 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 108.83 | 275.74 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.77 | 0.87 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 5.34 | 6.17 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 189.68 | 191.82 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 1.08 | 1.29 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 2.91 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 16.31 | 17.64 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 43.24 | 69.97 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 226.14 | 229.22 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 828.25 | 1281.23 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 4.48 | 4.51 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 10.93 | 12.30 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 26.77 | 89.93 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 181.56 | 183.95 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 364.13 | 2.64 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 891.61 | 19.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 3611.04 | 47.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 7031.44 | 124.37 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 3.38 | 7.73 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 6.76 | 12.61 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 85.00 | 339.11 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 216.59 | 494.07 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.41 | 0.44 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 1.19 | 1.59 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 1.21 | 1.33 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 328.22 | 329.92 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.23 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 1.14 | 1.30 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 2.19 | 3.64 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 4.75 | 5.02 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 38.12 | 38.54 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 139.54 | 181.06 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 4.43 | 4.49 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 9.60 | 25.27 | 100% | 2246.00 | +1346.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 37.79 | 38.09 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 89.63 | 101.97 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 2845.03 | 5.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 15845.60 | 108.42 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 5500.90 | 173.44 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 185199.04 | 1575.76 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 13.10 | 14.79 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 48.63 | 79.28 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 144.00 | 145.52 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 852.12 | 3372.89 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.48 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.96 | 2.24 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 2809.34 | 2883.19 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 2234.02 | 2299.54 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 2.63 | 2.74 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 6.18 | 6.55 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 7.39 | 10.32 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 13.32 | 24.55 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.54 | 0.59 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 5.94 | 6.05 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 485.18 | 516.75 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | no | 2688.82 | 2733.40 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 399.48 | 3.42 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 1541.06 | 9.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 885.35 | 12.93 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 4970.13 | 108.30 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 5.45 | 9.49 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 6.98 | 10.73 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 55.87 | 183.34 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 71.96 | 94.04 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.55 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 5.33 | 18.61 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 112.70 | 209.34 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.35 | 0.43 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 0.61 | 0.67 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 0.78 | 0.88 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 30.35 | 69.85 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.55 | 0.57 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 4.50 | 6.16 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 5.45 | 6.40 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 94.23 | 105.90 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 2.52 | 5.39 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260923T060603Z.json) | yes | 3.83 | 3.87 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20260923T060603Z.json) | yes | 35.55 | 39.47 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260923T060603Z.json) | yes | 232.26 | 233.89 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | no | 216.79 | 0.44 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 1.81 | 4.29 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.26 | 0.31 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.26 | 0.27 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 0.24 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 6457.30 | 59.63 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 14.41 | 21.66 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 112.34 | 144.09 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260923T060603Z.json) | yes | 52.12 | 65.83 | 100% | 75.00 | 0.00 | pass |
