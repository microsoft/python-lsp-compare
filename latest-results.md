# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261118T060337Z.json`

- Generated at: 20261118T060337Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.105 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.105/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 6 | 2828.65 | 2.87 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | no | 8 | 6035.48 | 7.11 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 6 | 27414.98 | 41.61 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 6 | 185105.28 | 269.98 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 373.53 | 2.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 616.73 | 5.34 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 3402.55 | 55.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 5779.55 | 80.73 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 1.52 | 1.78 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 4.59 | 8.68 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 4.66 | 7.26 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 126.13 | 242.36 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.20 | 0.22 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.93 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 1.22 | 1.40 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 142.09 | 144.73 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.29 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 0.71 | 0.75 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 2.94 | 3.04 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 8.66 | 9.78 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 8.99 | 10.46 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 248.56 | 344.28 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 3.32 | 3.36 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 11.79 | 34.99 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 24.25 | 27.30 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 131.78 | 134.20 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 196.36 | 1.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 230.74 | 2.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 1099.75 | 10.49 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 5478.21 | 122.56 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 3.49 | 5.48 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 3.64 | 6.31 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 4.21 | 6.43 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 129.85 | 261.73 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.13 | 0.14 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.19 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.40 | 0.44 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 124.47 | 126.95 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.11 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.29 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 0.82 | 0.86 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.79 | 3.20 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 3.26 | 3.98 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 18.64 | 22.20 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 173.90 | 203.75 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 1.42 | 1.44 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2.98 | 3.15 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 28.91 | 33.37 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 183.76 | 184.79 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 604.73 | 5.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 642.69 | 9.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 6311.15 | 54.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 5752.85 | 101.10 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 3.15 | 6.05 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 13.72 | 17.17 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 42.49 | 57.74 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 59.00 | 201.38 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.17 | 0.20 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.57 | 0.65 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 4.70 | 7.22 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 148.07 | 150.68 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.33 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 0.78 | 0.82 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2.35 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 11.37 | 12.82 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 16.84 | 37.77 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 167.86 | 170.13 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 205.40 | 231.87 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.88 | 3.22 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 8.91 | 13.06 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 20.78 | 44.07 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 146.31 | 147.95 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 441.94 | 0.89 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 299.49 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 2888.91 | 39.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 5035.41 | 69.38 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 1.92 | 6.91 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.79 | 7.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 12.05 | 14.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 53.69 | 114.06 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.26 | 0.28 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.81 | 0.84 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 4.79 | 10.21 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 236.62 | 239.65 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.12 | 0.14 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.83 | 0.95 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 0.88 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 1.16 | 1.21 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 3.52 | 3.98 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 27.74 | 27.88 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 104.62 | 131.12 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.39 | 0.41 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 3.05 | 3.08 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 27.97 | 28.00 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 72.77 | 83.24 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 1071.53 | 2.80 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 1205.31 | 2.94 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 12567.10 | 82.85 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 159683.53 | 1186.32 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 5.53 | 21.60 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 8.30 | 10.88 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 45.30 | 69.17 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 99.64 | 116.62 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.13 | 0.14 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.33 | 0.39 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.43 | 1.30 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 2248.98 | 2314.78 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.13 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 1641.31 | 1667.04 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 2.02 | 2.12 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.69 | 2.77 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 5.09 | 10.77 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 5.30 | 6.86 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.48 | 2.51 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 3.80 | 9.38 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 363.01 | 387.13 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | no | 1939.67 | 1972.39 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 283.02 | 2.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 532.32 | 3.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 1145.52 | 6.75 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 3375.74 | 59.78 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 4.18 | 7.13 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 5.08 | 8.23 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 7.55 | 12.93 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 36.20 | 61.60 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.41 | 0.45 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2.30 | 8.80 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 7.09 | 10.75 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 0.61 | 0.82 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 1.02 | 1.13 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 3.54 | 6.76 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2.59 | 3.22 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 3.22 | 3.99 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 3.66 | 3.88 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 63.00 | 71.44 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261118T060337Z.json) | yes | 2.32 | 2.34 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2.53 | 3.46 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261118T060337Z.json) | yes | 25.35 | 28.55 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261118T060337Z.json) | yes | 189.08 | 224.51 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | no | 182.42 | 0.21 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.68 | 0.75 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.14 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 2183.31 | 56.93 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 15.84 | 28.20 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 106.55 | 118.49 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261118T060337Z.json) | yes | 48.40 | 60.31 | 100% | 75.00 | 0.00 | pass |
