# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261006T060557Z.json`

- Generated at: 20261006T060557Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.84 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.84/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.2 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 6 | 5406.15 | 4.84 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | no | 8 | 16786.44 | 36.25 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 6 | 43670.70 | 94.08 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 6 | 223712.55 | 370.31 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 540.87 | 4.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 1175.99 | 24.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 5023.43 | 86.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 8539.29 | 109.59 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 1.77 | 1.89 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 7.19 | 10.54 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 91.52 | 362.15 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 172.07 | 315.34 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.34 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 1.41 | 1.84 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.55 | 2.81 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 190.79 | 194.87 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.49 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 1.07 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 4.57 | 4.81 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 14.27 | 15.08 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 26.29 | 40.46 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 390.97 | 506.99 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.47 | 4.14 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 5.94 | 6.36 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 34.86 | 36.57 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 179.43 | 187.12 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 263.55 | 2.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 328.73 | 5.54 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 1614.91 | 16.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 7796.88 | 173.27 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 4.75 | 6.81 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 5.82 | 8.62 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 17.54 | 66.53 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 197.24 | 572.21 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.24 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.57 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.56 | 5.32 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 160.56 | 161.63 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 1.10 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 4.67 | 10.47 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 4.84 | 5.50 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 29.88 | 32.77 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 257.66 | 292.43 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.67 | 5.94 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 3.22 | 3.30 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 43.70 | 52.95 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 249.81 | 252.99 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 918.35 | 9.73 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 1361.99 | 33.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 7886.59 | 137.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 14226.37 | 276.43 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 19.01 | 22.12 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 62.48 | 80.85 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 87.19 | 292.12 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 93.14 | 370.11 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.92 | 1.15 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.47 | 2.67 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 201.92 | 210.06 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.41 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 1.02 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 22.04 | 23.10 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 57.56 | 81.91 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 232.34 | 235.58 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 1279.23 | 1497.38 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 7.14 | 7.50 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 11.70 | 21.18 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 14.42 | 15.73 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 187.50 | 194.11 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 430.80 | 3.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 937.06 | 20.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 4094.52 | 54.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 7537.68 | 102.57 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 3.54 | 8.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 16.71 | 31.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 88.27 | 352.22 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 94.88 | 177.88 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.42 | 0.44 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 1.11 | 1.21 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 4.19 | 10.41 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 336.81 | 347.37 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.72 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 1.14 | 1.35 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 6.03 | 6.65 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 8.33 | 26.99 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 39.84 | 40.62 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 144.91 | 182.47 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.17 | 3.63 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 5.20 | 5.28 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 40.16 | 41.18 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 106.63 | 116.68 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 2876.69 | 5.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 17041.23 | 120.48 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 5553.51 | 174.91 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 187189.36 | 1594.80 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 12.13 | 13.19 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 58.92 | 92.98 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 155.22 | 162.21 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 847.44 | 3388.81 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.55 | 0.65 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.68 | 1.97 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 2848.88 | 2947.38 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.34 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.49 | 0.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 2300.94 | 2387.34 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 2.75 | 2.80 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 7.99 | 9.61 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 8.60 | 10.34 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 11.47 | 22.61 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 7.83 | 8.02 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 15.17 | 34.79 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 534.45 | 573.30 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | no | 2666.23 | 2707.26 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 375.90 | 3.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 1670.24 | 9.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 974.10 | 13.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 4762.74 | 104.58 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 5.14 | 8.82 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 6.22 | 8.81 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 58.02 | 192.87 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 63.67 | 97.94 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.59 | 0.72 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 5.96 | 20.86 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 59.36 | 74.50 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.36 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 0.62 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 0.77 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 70.91 | 97.34 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.65 | 0.70 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 5.52 | 5.85 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 5.65 | 6.89 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 89.11 | 91.30 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 2.36 | 4.81 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261006T060557Z.json) | yes | 3.24 | 3.36 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261006T060557Z.json) | yes | 37.17 | 43.64 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261006T060557Z.json) | yes | 239.82 | 244.07 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | no | 226.61 | 0.33 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 1.01 | 1.11 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.24 | 0.27 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.25 | 0.26 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 6228.45 | 41.97 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 12.76 | 19.96 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 64.37 | 68.48 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261006T060557Z.json) | yes | 48.79 | 54.87 | 100% | 75.00 | 0.00 | pass |
