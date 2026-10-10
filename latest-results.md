# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261010T060530Z.json`

- Generated at: 20261010T060530Z
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
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 6 | 3498.87 | 4.09 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | no | 8 | 16145.87 | 35.48 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 6 | 39745.24 | 74.97 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 6 | 217417.73 | 364.66 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 517.74 | 4.26 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 1262.42 | 29.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 4722.21 | 81.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 7926.10 | 107.41 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 1.66 | 1.80 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 5.16 | 8.32 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 99.39 | 386.10 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 178.78 | 378.09 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.33 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 1.20 | 1.55 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 2.63 | 3.12 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 183.01 | 184.97 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.42 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 1.00 | 1.03 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 4.60 | 4.80 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 13.35 | 14.42 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 23.91 | 36.20 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 366.34 | 459.58 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 5.74 | 5.86 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 19.95 | 69.21 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 36.80 | 40.36 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 169.67 | 173.89 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 258.10 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 293.66 | 4.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 1478.81 | 14.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 7698.04 | 172.38 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.17 | 6.22 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 4.66 | 7.63 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 15.24 | 59.71 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 193.46 | 401.33 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.24 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.25 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.52 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 159.01 | 160.85 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.23 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 1.07 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.89 | 5.20 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 7.27 | 14.37 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 26.79 | 28.35 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 260.00 | 301.50 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.62 | 0.65 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 3.26 | 3.29 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 40.03 | 44.69 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 248.38 | 249.93 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 839.61 | 7.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 1160.03 | 27.75 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 7913.44 | 149.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 11993.37 | 180.07 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 17.06 | 20.34 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 79.18 | 263.34 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 93.40 | 372.58 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 127.70 | 335.04 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.26 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.64 | 0.68 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 2.34 | 2.59 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 194.70 | 196.97 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 1.02 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 17.43 | 18.39 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 40.46 | 63.71 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 237.97 | 257.14 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 808.98 | 1269.81 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 2.31 | 3.71 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.74 | 4.86 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 11.14 | 12.69 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 183.89 | 186.71 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 377.08 | 2.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 1063.67 | 25.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 3869.80 | 53.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 7242.59 | 98.40 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 3.00 | 6.99 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 15.67 | 17.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 90.02 | 193.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 114.68 | 446.04 | 100% | 15.00 | +14.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.39 | 0.43 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 2.01 | 3.65 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 4.39 | 10.30 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 324.85 | 329.85 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.24 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.46 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 1.12 | 1.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 1.32 | 2.56 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 1.91 | 3.54 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 5.54 | 5.97 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 38.35 | 38.54 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 141.98 | 176.66 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 5.20 | 5.26 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 6.18 | 15.11 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 37.65 | 37.86 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 104.04 | 117.99 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 1144.92 | 4.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 16119.25 | 110.40 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 5458.01 | 172.80 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 181878.52 | 1565.73 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 10.32 | 12.27 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 50.89 | 82.88 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 152.83 | 159.18 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 847.56 | 3389.17 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.24 | 0.30 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.50 | 0.60 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 2773.36 | 2849.81 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.45 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 2223.14 | 2282.77 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 2.53 | 2.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.79 | 4.93 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 6.22 | 6.61 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 7.65 | 20.83 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.52 | 4.63 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 8.37 | 20.45 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 493.92 | 518.62 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | no | 2676.80 | 2695.78 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 361.43 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 1561.81 | 9.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 916.32 | 14.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 4759.04 | 95.00 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 4.63 | 8.10 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 5.96 | 8.57 | 100% | 496.00 | +482.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 66.61 | 109.94 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 70.85 | 199.14 | 100% | 487.80 | +473.80 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.24 | 0.30 | 100% | 167.00 | +141.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.51 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 49.44 | 74.64 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.31 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 0.58 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 0.76 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 37.12 | 91.01 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.57 | 0.60 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 4.80 | 5.63 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 4.81 | 6.14 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 87.65 | 88.18 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 2.28 | 4.64 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261010T060530Z.json) | yes | 3.06 | 3.10 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261010T060530Z.json) | yes | 36.32 | 40.84 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261010T060530Z.json) | yes | 234.17 | 235.33 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 487.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | no | 218.04 | 0.31 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.96 | 1.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 5773.72 | 26.79 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 11.67 | 14.34 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 59.17 | 60.08 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261010T060530Z.json) | yes | 9.51 | 9.99 | 100% | 75.00 | 0.00 | pass |
