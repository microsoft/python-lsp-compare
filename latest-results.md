# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261017T060433Z.json`

- Generated at: 20261017T060433Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.89 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.89/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 6 | 2272.02 | 2.62 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | no | 8 | 4539.10 | 5.24 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 6 | 23116.08 | 32.30 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 6 | 175841.06 | 241.08 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 357.67 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 437.06 | 3.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 2809.62 | 45.87 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 4886.03 | 65.66 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 1.08 | 1.32 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.35 | 2.67 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 3.93 | 6.98 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 98.25 | 181.29 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.17 | 0.19 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.78 | 1.12 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.41 | 1.60 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 116.80 | 118.43 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.10 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.23 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 0.59 | 0.64 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 2.37 | 2.51 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 9.93 | 13.14 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 11.63 | 15.71 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 205.27 | 336.97 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 2.08 | 3.08 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.33 | 3.40 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 19.14 | 21.69 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 110.27 | 112.49 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 290.08 | 0.51 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 172.53 | 1.61 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 986.23 | 10.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 4818.32 | 105.66 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.69 | 1.77 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 2.79 | 4.66 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 3.35 | 5.43 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 105.27 | 283.22 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.11 | 0.14 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.21 | 0.32 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.36 | 0.41 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 102.81 | 107.39 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.09 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.43 | 0.73 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 0.71 | 0.82 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.84 | 0.94 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.12 | 3.70 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 19.00 | 21.51 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 164.57 | 208.58 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.39 | 0.46 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 1.92 | 1.95 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 28.36 | 32.74 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 154.95 | 156.74 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 450.41 | 3.99 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 552.48 | 5.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 5279.27 | 45.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 5110.41 | 88.18 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.09 | 3.43 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 11.10 | 13.13 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 36.55 | 50.40 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 54.06 | 175.71 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.16 | 0.21 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.54 | 0.65 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.37 | 1.57 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 127.79 | 132.54 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.11 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.28 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 0.59 | 0.64 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 11.26 | 13.09 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 12.36 | 17.91 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 151.47 | 157.22 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 165.82 | 194.73 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 2.76 | 2.85 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 5.04 | 8.79 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 6.35 | 8.98 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 124.51 | 125.62 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 247.27 | 1.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 348.59 | 1.81 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 2540.66 | 33.72 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 4466.13 | 60.07 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.11 | 3.88 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 2.06 | 5.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 14.09 | 19.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 50.70 | 108.71 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.19 | 0.22 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.60 | 0.66 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 1.24 | 1.61 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 206.38 | 232.76 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.10 | 0.10 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.11 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.28 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 0.69 | 0.89 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.41 | 3.80 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 5.23 | 12.97 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 21.67 | 22.26 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 88.20 | 111.03 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.99 | 3.34 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.05 | 3.07 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 20.92 | 21.10 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 64.80 | 75.75 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 805.58 | 2.31 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 719.07 | 2.54 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 10502.06 | 51.78 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 153599.60 | 1072.64 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 4.70 | 18.42 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 6.75 | 8.17 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 44.52 | 62.04 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 83.34 | 90.50 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.09 | 0.12 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.14 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.26 | 0.32 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 1998.83 | 2147.20 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 1515.15 | 1579.83 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 1.61 | 1.83 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.00 | 3.31 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 4.32 | 5.38 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 5.09 | 19.66 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.58 | 5.61 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 2.72 | 2.79 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 209.57 | 221.80 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | no | 1764.26 | 1849.43 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 223.00 | 1.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 437.13 | 2.57 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 998.25 | 6.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 2960.58 | 54.27 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 3.22 | 5.72 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.47 | 5.25 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 7.99 | 13.56 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 44.40 | 104.44 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.11 | 0.13 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.36 | 0.42 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 2.12 | 8.20 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 5.91 | 7.37 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.16 | 0.17 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 0.36 | 0.48 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 0.51 | 0.56 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 2.51 | 4.75 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.89 | 2.18 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 3.15 | 3.63 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 3.34 | 4.08 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 52.31 | 54.37 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1.68 | 2.88 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261017T060433Z.json) | yes | 1.87 | 1.90 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261017T060433Z.json) | yes | 26.28 | 30.95 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261017T060433Z.json) | yes | 166.22 | 211.97 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | no | 135.22 | 0.15 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.56 | 0.69 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.12 | 0.15 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 0.11 | 0.13 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 1635.03 | 47.08 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 8.89 | 14.92 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 72.83 | 121.49 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261017T060433Z.json) | yes | 59.52 | 69.04 | 100% | 75.00 | 0.00 | pass |
