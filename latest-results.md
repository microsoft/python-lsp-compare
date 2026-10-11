# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261011T060530Z.json`

- Generated at: 20261011T060530Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.86 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.86/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 6 | 3578.85 | 4.30 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | no | 8 | 16805.82 | 36.21 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 6 | 39211.13 | 76.20 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 6 | 221281.17 | 373.65 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 525.71 | 4.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 1285.90 | 24.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 4859.53 | 86.35 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 8028.76 | 111.19 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 1.70 | 1.89 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 6.87 | 11.97 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 98.38 | 387.96 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 195.48 | 296.64 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.30 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 1.27 | 1.88 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 2.38 | 2.61 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 184.04 | 185.64 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.39 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 1.10 | 1.19 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 5.03 | 5.45 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 15.28 | 18.35 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 20.16 | 35.49 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 388.08 | 509.74 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.49 | 0.52 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 5.74 | 5.82 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 35.12 | 38.50 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 170.31 | 172.25 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 262.29 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 295.34 | 4.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 1460.21 | 14.05 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 7779.30 | 174.62 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 4.52 | 6.86 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 4.83 | 7.91 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 18.29 | 71.90 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 192.16 | 497.44 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.25 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.37 | 0.41 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.57 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 164.20 | 166.50 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.34 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 1.08 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 1.88 | 2.01 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 4.90 | 5.27 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 25.89 | 27.70 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 262.87 | 303.86 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.77 | 0.86 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 3.28 | 3.32 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 38.56 | 43.50 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 252.80 | 257.12 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 852.79 | 8.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 1379.51 | 31.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 8038.62 | 151.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 11226.35 | 180.96 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 17.80 | 21.00 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 79.91 | 269.01 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 99.65 | 394.63 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 133.86 | 358.27 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.28 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.66 | 0.74 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 5.00 | 7.29 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 200.49 | 207.59 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.45 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 1.10 | 1.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 3.11 | 3.66 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 18.19 | 18.85 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 39.37 | 68.14 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 233.78 | 239.23 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 811.95 | 1285.71 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 4.53 | 4.57 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 11.79 | 15.51 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 12.83 | 18.80 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 186.78 | 189.13 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 382.85 | 2.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 872.50 | 18.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 3890.99 | 52.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 7469.23 | 116.34 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 3.11 | 7.52 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 15.23 | 26.91 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 91.97 | 366.94 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 167.81 | 368.85 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.40 | 0.41 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 1.05 | 1.16 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 2.20 | 2.77 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 334.04 | 344.77 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.24 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.67 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 1.09 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.83 | 0.88 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 5.67 | 6.26 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 39.59 | 40.87 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 145.56 | 182.23 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.51 | 0.53 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 5.31 | 5.43 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 39.17 | 39.79 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 101.18 | 112.63 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 1187.17 | 4.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 16164.53 | 113.35 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 5309.30 | 166.46 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 185222.66 | 1583.84 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 11.56 | 13.27 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 53.03 | 84.62 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 155.81 | 167.39 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 830.26 | 3300.94 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.24 | 0.26 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.45 | 1.07 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.51 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 2791.53 | 2812.15 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.26 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.48 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 2257.18 | 2296.22 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.63 | 0.69 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 2.60 | 2.77 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 4.83 | 5.24 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 7.93 | 10.97 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.93 | 2.25 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 4.45 | 4.48 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 504.81 | 529.45 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | no | 2712.07 | 2749.24 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 368.05 | 3.09 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 1609.52 | 9.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 905.34 | 13.66 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 4742.60 | 104.70 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 4.96 | 9.15 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 6.15 | 8.95 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 57.05 | 183.57 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 63.60 | 102.94 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.53 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 5.56 | 19.58 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 57.36 | 86.44 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.35 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 0.60 | 0.69 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 0.86 | 1.09 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 72.72 | 100.62 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 3.07 | 4.75 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 5.21 | 6.61 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 5.35 | 5.92 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 92.88 | 94.32 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 2.28 | 4.54 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261011T060530Z.json) | yes | 3.11 | 3.14 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261011T060530Z.json) | yes | 36.13 | 40.99 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261011T060530Z.json) | yes | 236.94 | 241.99 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 487.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | no | 223.44 | 0.32 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.99 | 1.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.22 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 0.25 | 0.28 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 6534.50 | 61.25 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 17.19 | 28.91 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 97.72 | 143.08 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261011T060530Z.json) | yes | 68.85 | 88.48 | 100% | 75.00 | 0.00 | pass |
