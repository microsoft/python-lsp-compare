# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261016T060539Z.json`

- Generated at: 20261016T060539Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.88 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.88/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.4.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 6 | 2875.38 | 3.19 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | no | 8 | 4798.74 | 4.38 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 6 | 27318.29 | 41.93 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 6 | 196497.05 | 283.21 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 389.30 | 3.19 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 497.38 | 3.63 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 3546.22 | 56.06 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 6081.35 | 81.68 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 1.30 | 1.45 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.52 | 4.02 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 5.75 | 10.00 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 126.91 | 246.06 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.21 | 0.24 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.92 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 2.33 | 4.08 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 143.26 | 145.24 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.13 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.33 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 0.72 | 0.76 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 3.04 | 3.12 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 9.55 | 11.58 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 13.44 | 19.55 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 249.04 | 369.72 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.75 | 2.10 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.74 | 5.35 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 24.27 | 29.98 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 134.46 | 135.46 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 197.44 | 1.29 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 197.60 | 1.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 1096.90 | 10.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 5604.80 | 122.01 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 3.19 | 5.19 | 100% | 262.00 | +252.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 3.28 | 5.23 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 3.65 | 5.96 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 117.62 | 317.86 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.14 | 0.16 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.19 | 0.22 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.42 | 0.44 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 124.95 | 126.20 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.16 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 0.75 | 0.77 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.87 | 4.45 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 3.58 | 3.71 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 19.20 | 20.42 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 178.28 | 209.17 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.98 | 2.44 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 2.46 | 2.52 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 28.84 | 33.24 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 188.48 | 189.66 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 721.14 | 5.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 573.61 | 9.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 6222.36 | 55.10 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 5776.46 | 101.22 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.59 | 4.98 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 12.81 | 15.63 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 43.73 | 59.69 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 60.22 | 204.40 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.17 | 0.20 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.56 | 0.64 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 2.00 | 2.60 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 151.67 | 153.00 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.18 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.34 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 0.74 | 0.78 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 13.02 | 14.34 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 28.17 | 49.89 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 165.98 | 171.71 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 206.95 | 227.94 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 3.45 | 3.48 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 7.41 | 9.84 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 14.58 | 45.32 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 144.00 | 145.49 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 361.47 | 2.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 490.62 | 4.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 2915.90 | 39.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 5620.10 | 71.58 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.93 | 5.28 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 2.32 | 5.50 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 11.60 | 21.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 61.90 | 139.86 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.29 | 0.31 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.91 | 1.21 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 3.67 | 9.12 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 242.39 | 245.56 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.14 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.53 | 0.86 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 0.78 | 0.82 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.09 | 4.26 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 9.66 | 24.92 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 26.41 | 27.74 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 106.70 | 133.32 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 3.93 | 3.99 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 7.84 | 16.46 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 26.41 | 26.75 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 75.29 | 87.63 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1025.83 | 2.65 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 897.01 | 3.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 12370.03 | 83.38 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 169707.43 | 1242.44 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 5.33 | 20.73 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 8.02 | 9.75 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 44.51 | 67.11 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 107.75 | 118.53 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.14 | 0.16 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.38 | 0.43 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.51 | 0.65 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 2259.70 | 2306.71 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.34 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 1799.07 | 1872.71 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.19 | 3.13 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 1.97 | 2.01 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.31 | 4.90 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 4.45 | 4.83 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.76 | 4.91 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 6.44 | 11.05 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 367.24 | 377.38 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | no | 2043.71 | 2106.48 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 308.86 | 2.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 519.32 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 1166.88 | 7.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 3706.92 | 80.33 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 4.44 | 7.83 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.68 | 6.94 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 10.79 | 14.43 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 55.95 | 101.06 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.39 | 0.44 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 2.23 | 8.42 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 42.55 | 66.79 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.24 | 0.26 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 0.47 | 0.58 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 0.61 | 0.80 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 46.49 | 122.62 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 2.39 | 2.87 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 3.24 | 3.95 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 4.20 | 4.81 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 69.88 | 71.69 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1.16 | 1.20 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261016T060539Z.json) | yes | 2.44 | 2.50 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261016T060539Z.json) | yes | 26.47 | 30.38 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261016T060539Z.json) | yes | 186.76 | 189.30 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | no | 171.81 | 0.21 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.70 | 0.78 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 0.15 | 0.15 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 1322.74 | 18.73 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 8.50 | 10.09 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 42.60 | 47.34 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261016T060539Z.json) | yes | 5.09 | 5.23 | 100% | 75.00 | 0.00 | pass |
