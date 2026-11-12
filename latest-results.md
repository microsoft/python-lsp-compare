# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261112T060339Z.json`

- Generated at: 20261112T060339Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.101 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.101/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 6 | 2945.03 | 3.25 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | no | 8 | 5255.79 | 4.15 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 6 | 28041.67 | 47.08 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 6 | 184683.55 | 232.97 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 415.19 | 3.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 595.13 | 6.89 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 3706.11 | 63.05 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 5899.00 | 76.90 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 1.73 | 1.96 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 3.24 | 4.71 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 6.42 | 11.20 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 112.41 | 213.82 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.24 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 1.37 | 1.95 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 5.48 | 5.90 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 138.65 | 139.70 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.37 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 0.68 | 0.72 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 5.72 | 5.92 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 3.14 | 3.38 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 9.92 | 11.36 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 17.33 | 18.76 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 277.65 | 416.99 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.69 | 3.37 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 4.00 | 4.01 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 29.44 | 33.78 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 129.61 | 131.39 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 201.60 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 241.24 | 1.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 1174.35 | 11.76 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 5582.84 | 123.24 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 1.83 | 4.47 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 4.11 | 6.49 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 4.43 | 7.17 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 121.04 | 330.84 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.15 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.46 | 0.54 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 3.90 | 5.92 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 121.91 | 122.62 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.12 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.14 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.35 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 0.88 | 1.02 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 1.44 | 1.63 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 3.18 | 3.28 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 20.99 | 24.04 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 179.42 | 206.04 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 1.75 | 1.83 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.63 | 4.09 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 32.58 | 38.11 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 192.94 | 208.02 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 651.07 | 6.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 599.25 | 6.37 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 7265.20 | 85.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 5655.89 | 100.13 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.17 | 5.12 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 15.18 | 18.46 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 41.75 | 58.58 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 62.85 | 209.96 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.20 | 0.25 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.64 | 0.67 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 6.66 | 9.57 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 150.98 | 155.95 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.35 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 0.76 | 0.80 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 4.31 | 7.35 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 12.64 | 13.43 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 16.19 | 25.50 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 160.66 | 162.88 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 356.10 | 834.16 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.52 | 8.46 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 3.43 | 3.57 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 8.15 | 10.65 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 146.50 | 148.00 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 317.06 | 2.28 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 477.21 | 2.57 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 2968.65 | 40.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 5357.81 | 77.58 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 3.10 | 7.28 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 3.20 | 6.58 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 13.69 | 16.89 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 89.51 | 205.86 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.30 | 0.35 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.86 | 0.88 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 1.48 | 1.62 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 244.66 | 252.60 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.13 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.14 | 0.14 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.50 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 0.87 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 3.14 | 3.69 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 4.18 | 4.41 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 26.71 | 27.33 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 111.48 | 140.12 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 3.66 | 3.69 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 5.53 | 13.62 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 26.16 | 26.35 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 75.66 | 86.78 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 1206.48 | 2.01 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 1058.78 | 3.14 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 11746.45 | 74.14 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 158657.78 | 955.93 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 5.08 | 19.71 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 9.13 | 11.26 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 35.90 | 58.67 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 105.49 | 110.11 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.13 | 0.15 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.37 | 0.47 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 1812.72 | 1854.34 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.17 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.52 | 0.89 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 1234.01 | 1279.63 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 2.34 | 2.70 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 3.26 | 3.56 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 4.32 | 5.71 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 5.38 | 7.00 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.39 | 0.41 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 2.98 | 3.05 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 328.53 | 363.18 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | no | 1625.07 | 1668.56 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 301.32 | 2.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 449.08 | 3.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 1180.90 | 7.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 3530.24 | 64.05 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 4.71 | 8.14 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 5.42 | 8.31 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 8.27 | 14.47 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 47.48 | 72.83 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.63 | 0.70 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.03 | 7.79 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 9.43 | 12.59 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.25 | 0.30 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 0.74 | 0.84 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 1.15 | 1.37 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 4.55 | 9.48 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.52 | 3.88 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 3.68 | 4.65 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 4.21 | 4.47 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 63.88 | 65.06 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 2.54 | 4.44 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261112T060339Z.json) | yes | 2.66 | 2.70 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261112T060339Z.json) | yes | 26.96 | 30.10 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261112T060339Z.json) | yes | 194.91 | 232.73 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | no | 204.36 | 0.25 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.82 | 0.97 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 1483.03 | 17.82 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 7.59 | 9.24 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 41.15 | 42.52 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261112T060339Z.json) | yes | 4.71 | 4.89 | 100% | 75.00 | 0.00 | pass |
