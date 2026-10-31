# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261031T060309Z.json`

- Generated at: 20261031T060309Z
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
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 6 | 3785.91 | 4.03 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | no | 8 | 7524.23 | 8.62 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 6 | 39175.54 | 75.78 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 6 | 266114.90 | 359.72 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 537.95 | 4.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 729.56 | 5.74 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 5040.67 | 88.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 7808.21 | 110.04 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.75 | 4.08 | 100% | 250.00 | +49.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 1.93 | 2.21 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 6.99 | 12.29 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 191.01 | 345.07 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.31 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 1.15 | 1.52 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.70 | 2.92 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 183.50 | 188.44 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.19 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 1.10 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 4.69 | 4.88 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 12.85 | 14.32 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 21.75 | 31.78 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 397.47 | 549.79 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.23 | 3.80 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 5.19 | 5.26 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 35.48 | 37.56 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 169.89 | 171.12 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 276.17 | 1.78 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 268.08 | 2.35 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 1461.98 | 13.94 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 7646.26 | 172.54 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.59 | 5.71 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 4.76 | 7.66 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 4.90 | 7.83 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 195.04 | 408.70 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.20 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.54 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.91 | 2.94 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 158.23 | 159.71 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.16 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.83 | 2.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 1.11 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.36 | 1.38 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 4.06 | 4.30 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 26.15 | 28.54 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 260.11 | 297.99 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.17 | 4.58 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 2.43 | 2.47 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 37.88 | 44.55 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 248.21 | 249.39 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 826.99 | 7.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 739.96 | 10.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 7713.06 | 133.44 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 11310.65 | 180.79 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.08 | 6.70 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 18.83 | 22.77 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 61.13 | 77.20 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 77.32 | 257.78 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.23 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.64 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.59 | 2.81 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 192.90 | 194.71 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 15.76 | 17.01 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 38.23 | 56.94 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 228.08 | 231.63 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 814.15 | 1273.55 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 3.93 | 3.98 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 7.00 | 11.61 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 11.44 | 15.25 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 184.00 | 185.91 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 535.52 | 1.09 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 407.11 | 2.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 3939.51 | 53.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 7080.02 | 98.20 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.95 | 6.17 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 3.47 | 8.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 18.29 | 25.10 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 91.88 | 174.57 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.38 | 0.40 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.05 | 1.10 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 1.65 | 2.55 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 319.73 | 324.05 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.19 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 1.15 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.71 | 1.83 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 5.32 | 6.11 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 38.73 | 39.84 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 144.23 | 181.00 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.52 | 0.53 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 4.79 | 4.84 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 39.50 | 40.02 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 103.60 | 124.52 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 1363.45 | 3.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1582.91 | 4.63 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 15864.60 | 108.55 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 231111.84 | 1541.40 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 6.67 | 25.94 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 11.45 | 13.71 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 50.07 | 80.96 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 146.19 | 156.93 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.19 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.49 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 2883.79 | 2920.04 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.19 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.47 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 2089.21 | 2155.16 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 3.28 | 3.44 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 3.93 | 4.09 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 7.25 | 8.13 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 14.56 | 22.71 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 1.53 | 2.64 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 3.77 | 3.80 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 484.48 | 525.51 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | no | 2584.52 | 2603.43 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 382.32 | 3.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 700.54 | 4.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 1558.14 | 9.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 4755.50 | 102.70 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 4.92 | 8.17 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 6.66 | 10.03 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 13.44 | 25.27 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 64.09 | 106.62 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.57 | 0.66 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.73 | 10.33 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 55.97 | 75.45 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.31 | 0.34 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 0.86 | 0.99 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 1.33 | 1.40 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 71.93 | 150.76 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.76 | 4.18 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 4.89 | 5.23 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 5.14 | 6.16 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 87.73 | 88.85 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2.80 | 4.83 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261031T060309Z.json) | yes | 3.12 | 3.14 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261031T060309Z.json) | yes | 35.75 | 43.57 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261031T060309Z.json) | yes | 233.80 | 234.75 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | no | 231.13 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.95 | 1.02 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 2728.44 | 70.92 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 14.41 | 24.34 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 145.68 | 162.92 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261031T060309Z.json) | yes | 52.68 | 70.06 | 100% | 75.00 | 0.00 | pass |
