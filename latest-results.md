# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260916T060523Z.json`

- Generated at: 20260916T060523Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.81 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.81/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 6 | 4989.74 | 4.01 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | no | 8 | 16242.67 | 35.39 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 6 | 36449.51 | 65.04 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 6 | 207157.00 | 361.16 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 402.02 | 3.43 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 1089.58 | 23.73 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 4493.34 | 76.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 7862.22 | 109.48 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 1.78 | 1.99 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 6.31 | 9.60 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 82.61 | 326.77 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 184.15 | 420.20 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.29 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 1.15 | 1.60 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 2.83 | 3.69 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 185.25 | 186.92 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.34 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.41 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 0.99 | 1.03 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 3.96 | 4.12 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 11.19 | 12.54 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 32.46 | 46.19 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 343.27 | 430.02 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.39 | 0.42 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 3.69 | 3.82 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 30.92 | 33.45 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 173.04 | 174.80 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 262.34 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 266.41 | 3.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 1454.06 | 13.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 7522.96 | 169.15 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 4.87 | 7.35 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 5.35 | 8.13 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 15.81 | 62.32 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 194.26 | 580.73 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.19 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.24 | 0.27 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.50 | 0.54 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 165.23 | 168.03 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.20 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 1.69 | 1.79 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 4.67 | 5.24 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 25.07 | 27.06 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 237.99 | 278.96 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.47 | 0.53 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 2.88 | 2.92 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 37.31 | 43.01 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 247.26 | 250.28 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 857.94 | 7.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 1234.48 | 30.58 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 7757.14 | 131.91 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 9669.88 | 134.05 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 18.41 | 21.78 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 51.93 | 69.96 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 73.59 | 250.03 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 86.02 | 343.32 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.24 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.72 | 0.82 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 4.83 | 6.61 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 195.78 | 198.21 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.17 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.44 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 2.72 | 2.92 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 17.32 | 18.27 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 30.23 | 33.24 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 220.41 | 230.74 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 584.93 | 1156.02 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 2.83 | 2.88 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 10.58 | 14.56 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 29.07 | 91.89 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 190.42 | 193.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 366.66 | 2.51 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 783.43 | 15.87 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 3494.28 | 46.68 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 6949.82 | 116.80 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 3.58 | 8.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 7.38 | 11.48 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 76.98 | 307.13 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 194.00 | 522.55 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.40 | 0.42 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.99 | 1.04 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 1.22 | 1.43 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 319.60 | 325.33 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.19 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 1.07 | 1.27 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.70 | 0.75 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 4.40 | 5.04 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 34.58 | 34.76 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 135.35 | 202.52 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.46 | 0.48 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 3.96 | 4.03 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 34.75 | 34.98 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 89.04 | 102.72 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 2774.40 | 5.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 15814.46 | 110.45 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 5142.65 | 159.36 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 172270.83 | 1533.34 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 11.67 | 12.26 | 100% | 776.00 | +653.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 55.13 | 78.09 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 133.11 | 141.20 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 768.52 | 3073.32 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.19 | 0.20 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.24 | 0.36 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.49 | 0.56 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 2717.94 | 2753.59 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.28 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.44 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 2213.10 | 2239.11 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 2.45 | 2.58 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 6.37 | 8.10 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 7.45 | 7.91 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 11.51 | 23.18 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 5.84 | 5.93 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 16.39 | 38.84 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 489.84 | 505.37 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | no | 2600.12 | 2659.59 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 776.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 326.38 | 2.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 1523.50 | 8.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 900.61 | 15.12 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 4794.03 | 106.25 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 5.70 | 9.73 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 6.19 | 8.65 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 65.30 | 178.49 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 71.29 | 98.16 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.57 | 0.67 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 5.49 | 19.22 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 132.00 | 242.84 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.31 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 0.54 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 0.85 | 0.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 3.68 | 4.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 2.97 | 4.84 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 4.16 | 4.35 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 4.62 | 6.18 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 86.30 | 87.00 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 1.52 | 1.56 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260916T060523Z.json) | yes | 2.50 | 2.56 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260916T060523Z.json) | yes | 32.85 | 36.37 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260916T060523Z.json) | yes | 237.99 | 244.08 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | no | 223.33 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.95 | 1.06 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 0.31 | 0.61 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 6602.17 | 68.98 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 18.08 | 32.61 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 139.58 | 150.07 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260916T060523Z.json) | yes | 49.27 | 55.88 | 100% | 75.00 | 0.00 | pass |
