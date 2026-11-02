# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261102T060408Z.json`

- Generated at: 20261102T060408Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.95 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.95/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 6 | 3795.83 | 4.12 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | no | 8 | 6849.18 | 5.36 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 6 | 37072.39 | 67.55 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 6 | 257100.72 | 354.39 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 525.30 | 4.01 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 730.03 | 4.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 4530.98 | 76.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 7541.20 | 106.37 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 1.86 | 2.11 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.07 | 3.67 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 6.10 | 11.49 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 185.76 | 374.66 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.29 | 0.29 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 1.09 | 1.32 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2.90 | 3.98 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 176.61 | 177.17 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.40 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 1.08 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 4.70 | 4.84 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 12.64 | 14.74 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 14.75 | 17.98 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 345.17 | 461.47 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.17 | 3.82 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 5.10 | 5.19 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 31.85 | 35.57 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 163.71 | 164.41 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 252.87 | 2.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 278.65 | 2.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 1434.79 | 13.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 7450.60 | 166.01 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.39 | 5.22 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 4.49 | 7.05 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 4.65 | 7.52 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 185.14 | 528.65 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.19 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.50 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.52 | 1.06 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 152.57 | 152.83 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 1.08 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 3.91 | 4.04 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 4.63 | 9.72 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 25.01 | 26.68 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 249.79 | 282.63 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 2.41 | 2.46 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2.74 | 4.17 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 37.18 | 44.78 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 241.48 | 243.40 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 807.26 | 7.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 788.16 | 10.67 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 7519.66 | 142.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 10338.19 | 148.41 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 1.93 | 6.63 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 18.50 | 22.14 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 77.03 | 259.12 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 126.41 | 337.33 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.25 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.66 | 0.72 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2.50 | 2.60 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 191.61 | 202.46 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.43 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 1.10 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 14.77 | 16.03 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 33.61 | 53.15 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 216.92 | 220.05 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 652.04 | 1350.45 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 3.90 | 3.93 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 11.91 | 14.17 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 15.05 | 42.11 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 177.24 | 177.88 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 557.58 | 1.99 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 390.17 | 2.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 3828.81 | 52.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 6892.56 | 100.92 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 3.44 | 8.31 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 4.36 | 7.35 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 18.13 | 21.11 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 112.03 | 188.70 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.39 | 0.42 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 1.30 | 1.94 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 1.62 | 1.98 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 314.21 | 324.04 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.20 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 1.14 | 1.26 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 1.69 | 1.73 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 4.94 | 5.24 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 38.50 | 39.05 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 142.23 | 177.11 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2.37 | 7.85 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 4.61 | 4.69 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 38.70 | 39.22 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 101.10 | 109.67 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 1517.01 | 2.21 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 1398.27 | 4.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 15400.46 | 104.68 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 223102.80 | 1515.29 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 6.42 | 24.90 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 12.08 | 14.65 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 50.58 | 90.80 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 141.30 | 152.87 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.20 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.49 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.85 | 2.33 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 2825.38 | 2859.31 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.75 | 0.95 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 2092.14 | 2146.33 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 2.64 | 2.79 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.72 | 12.93 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 4.05 | 4.15 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 7.49 | 11.00 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.51 | 0.56 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 4.59 | 5.54 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 464.39 | 488.25 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | no | 2514.96 | 2546.80 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 421.97 | 3.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 716.29 | 4.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 1539.16 | 9.09 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 4593.90 | 95.08 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 5.19 | 9.28 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 7.74 | 11.65 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 15.10 | 25.30 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 64.50 | 101.21 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.52 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2.56 | 9.62 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 56.07 | 68.39 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.33 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 0.77 | 1.02 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 1.66 | 1.79 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 40.45 | 100.47 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.35 | 4.11 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 4.74 | 6.17 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 5.76 | 6.32 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 86.42 | 88.78 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261102T060408Z.json) | yes | 3.21 | 3.35 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 3.42 | 4.85 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261102T060408Z.json) | yes | 34.25 | 41.89 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261102T060408Z.json) | yes | 227.96 | 228.70 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | no | 230.58 | 0.31 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.95 | 0.98 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 2030.88 | 27.61 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 14.04 | 18.50 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 61.97 | 65.76 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261102T060408Z.json) | yes | 6.82 | 7.04 | 100% | 75.00 | 0.00 | pass |
