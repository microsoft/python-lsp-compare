# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261120T060335Z.json`

- Generated at: 20261120T060335Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.107 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.107/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.5.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 6 | 2814.61 | 2.92 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | no | 8 | 5314.91 | 7.06 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 6 | 27358.33 | 42.31 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 6 | 184717.73 | 271.45 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 369.01 | 2.80 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 508.53 | 3.59 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 3514.96 | 57.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 5694.59 | 80.95 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 1.50 | 1.73 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.42 | 5.58 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 4.09 | 6.87 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 126.66 | 271.76 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.21 | 0.23 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.99 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 1.44 | 1.58 | 100% | 7910.00 | +3891.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 141.54 | 143.87 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 0.76 | 0.78 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 2.95 | 3.06 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 8.80 | 10.40 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 10.55 | 12.99 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 259.04 | 378.14 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 3.39 | 3.42 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 3.43 | 3.60 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 25.41 | 27.86 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 132.82 | 134.81 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4232.00, 7910.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 158.98 | 1.13 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 186.89 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 1104.14 | 10.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 5573.37 | 125.83 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.93 | 2.52 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 3.68 | 6.32 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 3.76 | 6.36 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 140.91 | 292.35 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.14 | 0.15 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.17 | 0.19 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.37 | 0.42 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 124.47 | 127.38 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.31 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 0.82 | 0.84 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.14 | 3.35 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.72 | 2.98 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 18.69 | 20.07 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 176.88 | 212.22 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 1.41 | 1.46 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.27 | 2.83 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 29.45 | 34.28 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 186.09 | 188.00 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 407.47 | 4.27 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 612.52 | 5.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 6257.30 | 54.91 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 5726.50 | 100.98 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 1.48 | 4.77 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 14.36 | 17.75 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 43.40 | 56.60 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 56.64 | 192.53 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.17 | 0.22 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.50 | 0.58 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 3.98 | 4.22 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 150.39 | 152.18 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.11 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.28 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 0.78 | 0.80 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.89 | 3.22 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 9.41 | 14.90 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 12.06 | 13.23 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 167.22 | 171.46 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 209.33 | 238.53 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.80 | 2.89 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 3.59 | 7.80 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 7.79 | 9.17 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 143.11 | 146.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 317.91 | 1.96 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 412.58 | 2.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 2882.80 | 38.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 5095.48 | 73.49 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.80 | 7.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 4.09 | 6.34 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 12.75 | 17.13 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 63.88 | 127.86 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.27 | 0.28 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.03 | 3.57 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 2.49 | 5.94 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 243.22 | 248.46 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.12 | 0.13 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.29 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 0.80 | 0.89 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.84 | 2.17 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.75 | 4.15 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 3.51 | 3.95 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 27.54 | 29.49 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 103.24 | 129.33 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 1.89 | 2.87 | 100% | 2249.00 | +1356.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 3.08 | 3.11 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 32.02 | 37.96 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 73.96 | 81.57 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2249.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 1045.81 | 2.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 1102.74 | 2.91 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 12446.76 | 85.05 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 159226.26 | 1186.36 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 5.45 | 21.35 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 8.40 | 10.96 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 45.90 | 70.88 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 98.29 | 106.95 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.20 | 0.48 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.21 | 0.45 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.34 | 0.42 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 2212.97 | 2277.20 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.14 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.33 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 1637.36 | 1696.95 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 1.90 | 1.97 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.67 | 2.76 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 4.86 | 5.55 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 8.27 | 18.57 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.47 | 0.48 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.54 | 2.58 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 373.84 | 405.40 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | no | 1981.28 | 2010.46 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 282.47 | 2.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 290.11 | 2.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 1152.37 | 6.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 3401.54 | 61.10 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 4.32 | 7.46 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 5.13 | 8.11 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 7.82 | 11.56 | 100% | 276.20 | +262.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 37.81 | 65.67 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 0.12 | 0.15 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.38 | 0.44 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.59 | 1.82 | 100% | 217.00 | +191.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 6.35 | 7.72 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 0.64 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.83 | 1.79 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 1.01 | 1.08 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 3.16 | 6.02 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.16 | 3.52 | 100% | 57.00 | -148.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 3.33 | 4.44 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 3.68 | 3.92 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 66.84 | 79.31 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2.02 | 3.83 | 100% | 2884.00 | +2464.00 | pass |
| [Ty](latest-results/ty-20261120T060335Z.json) | yes | 2.33 | 2.35 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261120T060335Z.json) | yes | 24.99 | 27.66 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261120T060335Z.json) | yes | 191.34 | 223.98 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 276.20, 496.00).
- client session hover: result differences detected (217.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 2884.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | no | 111.28 | 0.21 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.69 | 0.74 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.14 | 0.16 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.16 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 2323.22 | 67.97 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 12.69 | 16.83 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 122.20 | 141.39 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261120T060335Z.json) | yes | 69.01 | 81.19 | 100% | 75.00 | 0.00 | pass |
