# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261116T060532Z.json`

- Generated at: 20261116T060532Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.104 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.104/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.4.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 6 | 3468.23 | 3.93 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | no | 8 | 6789.26 | 6.89 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 6 | 33424.45 | 55.28 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 6 | 206028.15 | 301.28 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 621.98 | 4.37 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 568.92 | 4.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 3953.68 | 61.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 6948.51 | 96.43 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 1.79 | 2.18 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.50 | 5.05 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 6.48 | 11.02 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 143.31 | 298.29 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.23 | 0.25 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 1.06 | 1.52 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.13 | 2.47 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 174.54 | 178.66 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.37 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 0.85 | 0.86 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 3.56 | 3.75 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 15.62 | 17.62 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 16.62 | 22.20 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 269.27 | 420.21 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.39 | 0.44 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 5.58 | 6.13 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 27.96 | 33.26 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 159.91 | 162.20 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 267.24 | 1.98 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 232.18 | 2.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 1237.33 | 12.50 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 6851.87 | 151.10 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.66 | 3.78 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 4.47 | 7.36 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 5.17 | 7.74 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 146.32 | 393.72 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.16 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.46 | 0.53 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 1.62 | 3.11 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 149.90 | 152.47 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.32 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 0.85 | 0.92 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.40 | 5.98 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.91 | 4.50 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 22.52 | 25.75 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 230.20 | 298.76 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 1.57 | 1.61 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 3.02 | 3.78 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 34.71 | 39.66 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 228.23 | 235.42 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 633.00 | 6.77 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 724.98 | 7.32 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 7734.94 | 93.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 7115.30 | 123.33 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 4.10 | 8.26 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 16.08 | 20.14 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 51.35 | 69.81 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 66.47 | 216.95 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.20 | 0.23 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.59 | 0.62 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 4.24 | 5.77 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 172.63 | 180.82 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.31 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 0.91 | 0.96 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.90 | 3.01 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 16.81 | 16.97 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 17.98 | 27.25 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 217.29 | 223.82 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 392.15 | 931.10 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.40 | 3.71 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 4.61 | 10.70 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 10.03 | 12.01 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 174.46 | 180.77 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 358.97 | 2.34 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 555.35 | 2.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 3444.50 | 45.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 6140.04 | 86.08 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.81 | 7.26 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.20 | 7.75 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 17.95 | 36.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 76.19 | 155.60 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.32 | 0.35 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 1.04 | 1.13 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 1.16 | 1.33 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 286.59 | 301.99 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.14 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 0.96 | 1.20 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 4.66 | 5.96 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 5.93 | 13.96 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 34.36 | 37.13 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 122.39 | 156.03 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.59 | 3.39 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.41 | 3.50 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 32.28 | 34.72 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 87.09 | 96.99 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 1443.86 | 3.39 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 1216.12 | 3.53 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 15656.81 | 110.17 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 175241.71 | 1282.68 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 5.97 | 23.19 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 11.06 | 13.50 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 58.48 | 87.14 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 113.99 | 119.28 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.13 | 0.14 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.56 | 0.69 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 2408.79 | 2492.22 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.15 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.43 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 1795.32 | 1951.36 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 1.99 | 2.08 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.23 | 3.54 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 7.44 | 10.27 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 10.25 | 16.55 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.44 | 0.49 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.02 | 3.20 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 483.95 | 507.95 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | no | 2093.31 | 2210.62 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 367.06 | 3.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 634.49 | 3.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 1397.19 | 8.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 3730.72 | 68.04 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 4.98 | 8.25 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 6.75 | 9.94 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 7.06 | 12.76 | 100% | 253.80 | +239.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 52.23 | 90.96 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 0.14 | 0.17 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.40 | 0.47 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2.73 | 10.46 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 16.47 | 21.24 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.26 | 0.29 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 0.78 | 1.07 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 1.25 | 1.41 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 16.29 | 30.22 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 3.23 | 4.12 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 5.33 | 6.31 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 6.29 | 6.90 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 66.98 | 69.53 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261116T060532Z.json) | yes | 3.18 | 3.42 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 4.35 | 4.43 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261116T060532Z.json) | yes | 30.05 | 36.91 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261116T060532Z.json) | yes | 188.21 | 194.27 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 253.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | no | 212.21 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.74 | 0.87 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 2421.14 | 56.08 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 9.49 | 12.23 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 116.04 | 141.64 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261116T060532Z.json) | yes | 42.70 | 56.60 | 100% | 75.00 | 0.00 | pass |
