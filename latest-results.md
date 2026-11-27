# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261127T060330Z.json`

- Generated at: 20261127T060330Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.112 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.112/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 6 | 2559.20 | 2.51 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | no | 8 | 4452.49 | 3.48 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 6 | 28371.42 | 44.51 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 6 | 188693.28 | 277.63 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 320.71 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 535.56 | 4.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 3504.69 | 57.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 5784.18 | 80.29 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.49 | 1.75 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 4.01 | 5.52 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 5.15 | 8.93 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 128.57 | 269.59 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.21 | 0.23 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 1.19 | 1.43 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.47 | 1.65 | 100% | 7910.00 | +3891.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 140.00 | 142.28 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.33 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 0.77 | 0.80 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 3.35 | 3.50 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 6.96 | 9.25 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 14.89 | 36.03 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 255.92 | 362.51 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.73 | 1.76 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 3.07 | 3.60 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 25.03 | 28.61 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 128.78 | 130.08 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4232.00, 7910.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 177.47 | 1.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 156.58 | 1.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 1123.25 | 10.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 5577.43 | 122.77 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 2.17 | 5.14 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 3.65 | 6.20 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 3.82 | 6.09 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 125.79 | 350.65 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.12 | 0.13 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.41 | 0.46 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.03 | 1.90 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 121.48 | 124.71 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 0.79 | 0.81 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.75 | 3.97 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 2.27 | 2.43 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 19.70 | 22.88 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 178.01 | 214.46 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.10 | 1.13 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 2.23 | 2.79 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 30.26 | 34.84 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 187.77 | 191.44 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 428.81 | 4.58 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 568.70 | 5.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 6480.47 | 56.43 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 5979.41 | 107.96 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.91 | 5.16 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 13.89 | 17.26 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 61.92 | 207.32 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 77.29 | 189.93 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.18 | 0.19 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.51 | 0.57 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.49 | 1.70 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 146.12 | 149.92 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.30 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 0.78 | 0.79 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 10.08 | 10.89 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 13.65 | 23.35 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 173.43 | 181.77 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 211.68 | 243.06 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.48 | 1.52 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 5.68 | 8.20 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 7.74 | 9.89 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 142.19 | 144.15 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 270.56 | 1.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 366.82 | 1.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 2935.00 | 39.96 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 5178.62 | 70.43 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.45 | 5.12 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 2.72 | 6.99 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 15.11 | 17.21 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 59.62 | 132.98 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.26 | 0.27 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.94 | 0.96 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 1.76 | 2.56 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 234.89 | 237.01 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.13 | 0.14 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.30 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 0.92 | 1.04 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.22 | 1.50 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.81 | 2.05 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 27.82 | 29.82 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 105.01 | 135.83 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.44 | 1.46 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 3.47 | 9.31 | 100% | 2249.00 | +1356.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 28.89 | 29.52 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 77.62 | 84.04 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2249.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1071.95 | 1.30 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 959.62 | 2.76 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 13162.50 | 95.28 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 162553.83 | 1206.00 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 5.35 | 20.87 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 8.65 | 11.18 | 100% | 788.00 | +665.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 48.57 | 73.11 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 104.70 | 117.64 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.15 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.21 | 0.46 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.36 | 0.39 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 2278.07 | 2341.13 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.15 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.32 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 1675.24 | 1750.37 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.37 | 0.56 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 2.15 | 2.35 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 2.57 | 2.82 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 5.44 | 6.30 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.44 | 0.49 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 2.28 | 2.32 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 421.72 | 440.52 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | no | 1969.82 | 2023.82 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 788.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 262.15 | 2.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 298.74 | 2.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 1165.51 | 6.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 3619.79 | 78.36 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 4.35 | 7.24 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 5.08 | 8.21 | 100% | 497.00 | +483.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 9.58 | 13.83 | 100% | 276.60 | +262.60 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 56.42 | 104.35 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.19 | 0.21 | 100% | 217.00 | +191.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.39 | 0.44 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 37.61 | 74.46 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 0.57 | 0.68 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 0.96 | 1.06 | 100% | 2.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 2.72 | 4.43 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 50.87 | 116.06 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.93 | 0.96 | 100% | 57.00 | -148.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 3.26 | 4.28 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 3.49 | 3.90 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 63.12 | 64.55 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1.07 | 1.93 | 100% | 2884.00 | +2464.00 | pass |
| [Ty](latest-results/ty-20261127T060330Z.json) | yes | 1.91 | 1.94 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261127T060330Z.json) | yes | 26.29 | 29.21 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261127T060330Z.json) | yes | 183.75 | 191.28 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 276.60, 497.00).
- client session hover: result differences detected (217.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 2884.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | no | 126.11 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.73 | 0.86 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.13 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.17 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.16 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.15 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 0.14 | 0.16 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 1467.92 | 19.62 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 7.61 | 7.75 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 46.24 | 47.54 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261127T060330Z.json) | yes | 5.02 | 5.12 | 100% | 75.00 | 0.00 | pass |
