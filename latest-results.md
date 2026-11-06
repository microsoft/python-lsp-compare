# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261106T060351Z.json`

- Generated at: 20261106T060351Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.98 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.98/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 6 | 4196.09 | 4.88 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | no | 8 | 7195.27 | 5.59 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 6 | 46282.66 | 96.88 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 6 | 272062.97 | 372.50 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 633.62 | 5.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 775.88 | 5.70 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 5474.69 | 93.54 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 8870.74 | 117.31 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.83 | 4.72 | 100% | 250.00 | +49.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 2.25 | 2.61 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 8.15 | 11.68 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 194.56 | 412.40 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.32 | 0.35 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 1.50 | 2.00 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.94 | 3.45 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 196.21 | 198.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 1.10 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 4.93 | 5.04 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 18.62 | 21.18 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 21.68 | 28.96 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 422.93 | 585.44 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.77 | 3.84 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 6.11 | 6.49 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 34.69 | 40.10 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 189.78 | 199.44 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 325.89 | 2.35 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 285.10 | 2.59 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 1599.69 | 15.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 8524.49 | 188.28 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 3.14 | 4.96 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 5.64 | 8.36 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 5.79 | 9.09 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 206.86 | 502.54 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.26 | 0.31 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.61 | 0.70 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.59 | 3.69 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 174.93 | 181.95 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.38 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 1.11 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.93 | 6.94 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 4.83 | 5.35 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 29.49 | 32.71 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 282.62 | 326.13 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 2.03 | 2.12 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 3.83 | 4.80 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 41.00 | 48.64 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 275.88 | 284.21 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 718.99 | 7.62 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 907.87 | 9.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 8724.01 | 149.13 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 14190.45 | 272.81 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.99 | 7.29 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 20.30 | 23.97 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 69.00 | 88.95 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 90.76 | 305.67 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.88 | 1.06 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.62 | 2.89 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 209.69 | 213.97 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 1.10 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 20.52 | 21.25 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 28.35 | 38.00 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 259.51 | 265.03 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 1258.06 | 1386.53 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 3.92 | 13.53 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 4.73 | 5.27 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 13.98 | 16.86 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 206.34 | 212.60 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 648.07 | 2.80 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 458.26 | 3.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 4349.89 | 61.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 8000.18 | 120.79 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.65 | 7.97 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 4.10 | 9.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 19.88 | 22.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 154.41 | 371.02 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.41 | 0.44 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.27 | 1.35 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 1.99 | 2.72 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 357.40 | 367.56 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 1.31 | 1.53 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 4.62 | 6.43 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 6.96 | 7.52 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 46.52 | 47.41 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 161.89 | 196.54 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 5.20 | 12.69 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 5.56 | 5.94 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 44.28 | 44.87 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 123.42 | 142.85 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1600.37 | 2.23 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 1460.85 | 4.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 18946.62 | 127.52 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 232975.84 | 1556.01 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 8.30 | 32.25 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 13.11 | 15.39 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 62.56 | 91.71 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 151.74 | 161.35 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.19 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.59 | 0.70 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 2911.55 | 2957.85 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.54 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 2124.59 | 2182.33 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.69 | 0.76 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 2.69 | 2.85 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 4.11 | 4.36 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 8.19 | 9.65 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.78 | 3.71 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 3.85 | 4.21 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 565.70 | 608.28 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | no | 2589.48 | 2625.72 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 450.38 | 4.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 755.16 | 5.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 1721.32 | 10.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 4967.71 | 103.47 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 5.71 | 9.24 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 8.08 | 11.27 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 18.12 | 34.10 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 75.81 | 123.72 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.58 | 0.68 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2.89 | 10.91 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 98.09 | 186.81 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 0.79 | 0.87 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 1.46 | 1.67 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 4.53 | 5.49 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 4.18 | 4.50 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 6.24 | 7.52 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 7.43 | 7.95 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 92.10 | 95.57 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 3.45 | 4.87 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261106T060351Z.json) | yes | 4.00 | 4.26 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261106T060351Z.json) | yes | 38.94 | 44.14 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261106T060351Z.json) | yes | 246.82 | 256.20 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | no | 256.93 | 0.33 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 1.09 | 1.20 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 0.24 | 0.28 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 2113.99 | 31.43 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 13.19 | 17.62 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 73.70 | 92.41 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261106T060351Z.json) | yes | 7.41 | 7.52 | 100% | 75.00 | 0.00 | pass |
