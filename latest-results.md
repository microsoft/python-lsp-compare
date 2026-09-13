# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260913T060637Z.json`

- Generated at: 20260913T060637Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.80 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.80/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 6 | 4873.13 | 3.82 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | no | 8 | 15468.71 | 35.87 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 6 | 35098.62 | 64.82 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 6 | 167484.73 | 282.33 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 388.14 | 3.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 1148.36 | 28.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 4617.76 | 81.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 6969.36 | 98.45 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 1.65 | 1.82 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 6.56 | 10.28 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 81.93 | 317.24 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 176.29 | 389.01 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.25 | 0.28 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 1.24 | 1.51 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 3.64 | 7.29 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 159.73 | 162.36 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.20 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.44 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 1.03 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 3.84 | 4.18 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 10.21 | 12.06 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 39.35 | 46.11 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 365.89 | 525.78 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 3.50 | 3.79 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 19.16 | 62.96 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 30.99 | 34.13 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 151.36 | 153.20 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 246.31 | 2.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 295.57 | 4.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 1342.03 | 13.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 6720.81 | 147.25 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 4.46 | 7.08 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 4.83 | 6.89 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 15.04 | 59.18 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 167.82 | 514.12 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.18 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.22 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.54 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 141.14 | 143.18 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.15 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.32 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 1.01 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 4.35 | 4.89 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 6.55 | 20.85 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 26.13 | 29.58 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 213.85 | 243.54 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 1.49 | 4.30 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 2.57 | 2.59 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 35.38 | 41.33 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 212.42 | 213.65 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 831.76 | 7.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 1055.64 | 25.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 7050.15 | 119.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 9583.78 | 136.53 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 19.16 | 23.04 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 47.06 | 63.83 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 73.09 | 242.60 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 84.31 | 336.34 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.23 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.67 | 0.74 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 2.39 | 2.57 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 173.47 | 176.20 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 1.07 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 16.24 | 16.61 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 41.10 | 43.52 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 210.72 | 214.72 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 597.36 | 1179.55 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 1.29 | 2.80 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 2.58 | 2.63 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 11.14 | 16.07 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 166.45 | 167.31 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 358.25 | 2.35 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 755.29 | 15.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 3320.94 | 46.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 6201.92 | 105.58 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 3.32 | 7.42 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 6.57 | 10.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 76.93 | 306.93 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 179.95 | 382.86 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.34 | 0.41 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.98 | 1.01 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 1.23 | 1.61 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 284.80 | 286.17 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.16 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.36 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 0.95 | 1.02 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.63 | 0.66 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 4.14 | 4.68 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 31.50 | 33.18 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 134.93 | 189.58 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.46 | 0.47 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 3.78 | 3.83 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 30.69 | 30.87 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 87.31 | 100.29 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 2739.29 | 4.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 14765.21 | 102.69 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 5226.98 | 164.31 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 136282.99 | 1127.60 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 11.05 | 11.93 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 49.07 | 79.84 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 117.85 | 119.26 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 804.41 | 3216.77 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.17 | 0.17 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.40 | 1.07 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.47 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 2016.25 | 2061.51 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.45 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 1591.60 | 1649.14 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.41 | 0.46 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 2.30 | 2.41 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 5.87 | 6.71 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 6.73 | 8.11 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 5.80 | 6.83 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 16.39 | 27.94 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 456.71 | 472.09 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | no | 1909.99 | 1963.39 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 309.38 | 2.64 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 1468.90 | 9.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 758.68 | 15.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 4259.49 | 95.32 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 5.91 | 8.59 | 100% | 467.00 | +453.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 6.38 | 10.39 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 65.32 | 186.10 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 72.26 | 128.63 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.53 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 5.08 | 18.01 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 121.37 | 174.71 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.27 | 0.30 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 0.50 | 0.58 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 0.83 | 1.19 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 2.74 | 3.33 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 1.52 | 4.55 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 4.08 | 4.34 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 4.24 | 5.18 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 72.74 | 74.82 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260913T060637Z.json) | yes | 2.36 | 2.40 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 3.34 | 6.47 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20260913T060637Z.json) | yes | 34.23 | 38.38 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260913T060637Z.json) | yes | 207.48 | 209.46 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | no | 214.17 | 0.28 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.85 | 0.94 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.25 | 0.26 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 6014.01 | 65.02 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 18.50 | 42.72 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 126.48 | 150.49 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260913T060637Z.json) | yes | 50.07 | 56.86 | 100% | 75.00 | 0.00 | pass |
