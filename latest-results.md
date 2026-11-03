# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261103T060341Z.json`

- Generated at: 20261103T060341Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.96 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.96/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 6 | 3448.28 | 3.78 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | no | 8 | 6029.19 | 5.06 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 6 | 36190.55 | 68.37 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 6 | 220570.20 | 279.37 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 478.03 | 3.82 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 592.53 | 4.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 4054.48 | 66.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 6654.97 | 94.52 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1.69 | 3.37 | 100% | 250.00 | +49.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 1.81 | 2.04 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 6.42 | 11.48 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 156.38 | 338.26 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.26 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 1.08 | 1.39 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 2.38 | 2.64 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 161.41 | 164.81 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.38 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 1.00 | 1.19 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 3.86 | 4.37 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 12.25 | 14.45 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 17.47 | 20.28 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 297.31 | 427.48 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.32 | 0.35 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 4.61 | 4.75 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 29.70 | 33.54 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 149.93 | 151.40 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 251.31 | 1.88 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 238.86 | 2.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 1347.05 | 13.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 6593.00 | 146.94 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 2.60 | 3.65 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 4.59 | 7.05 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 4.63 | 7.70 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 155.41 | 316.52 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.16 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.24 | 0.25 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.50 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 141.64 | 143.29 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.18 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.39 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 1.03 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.18 | 8.74 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.39 | 3.62 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 24.49 | 26.33 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 217.33 | 248.21 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 1.88 | 1.93 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.19 | 3.93 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 36.56 | 42.52 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 219.29 | 222.59 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 656.37 | 6.95 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 778.62 | 7.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 6718.36 | 116.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 11279.26 | 171.17 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.63 | 7.88 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 17.52 | 20.94 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 50.55 | 68.75 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 70.22 | 234.27 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.21 | 0.23 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.78 | 1.05 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 5.46 | 8.29 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 170.86 | 171.82 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.15 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.40 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 1.09 | 1.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 2.92 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 15.49 | 18.30 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 16.80 | 33.94 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 197.52 | 200.33 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 774.96 | 1198.10 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.87 | 3.93 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 5.95 | 15.54 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 9.47 | 10.92 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 163.92 | 167.13 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 525.08 | 2.23 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 373.08 | 2.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 3559.25 | 49.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 5961.81 | 94.37 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.47 | 7.97 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.70 | 10.16 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 17.41 | 22.58 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 131.73 | 308.61 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.31 | 0.34 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1.42 | 2.56 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 1.74 | 1.89 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 277.23 | 285.43 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.16 | 0.17 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.23 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.48 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 1.00 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 4.28 | 5.94 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 4.57 | 4.93 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 30.85 | 32.31 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 133.74 | 176.16 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1.54 | 3.38 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 4.03 | 4.03 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 31.05 | 32.31 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 92.72 | 105.93 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 1223.12 | 3.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1413.25 | 4.34 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 14540.84 | 100.78 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 190518.19 | 1134.59 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 5.63 | 21.78 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 10.83 | 13.49 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 47.33 | 78.03 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 121.85 | 129.72 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.16 | 0.18 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.20 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.42 | 0.51 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 2160.45 | 2185.62 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 1531.19 | 1603.52 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 2.48 | 2.64 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.46 | 5.25 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.64 | 3.95 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 6.81 | 10.68 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.41 | 3.43 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 12.24 | 24.03 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 448.96 | 471.01 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | no | 1856.98 | 1885.93 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 356.57 | 3.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 555.08 | 4.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 1409.66 | 8.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 4123.87 | 89.00 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 4.27 | 7.52 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 6.10 | 9.18 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 13.49 | 23.77 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 65.21 | 116.04 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.51 | 0.58 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 2.54 | 8.77 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 49.40 | 72.15 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.30 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 0.78 | 0.95 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 1.25 | 1.30 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 45.12 | 78.53 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.65 | 0.75 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 4.17 | 5.34 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 5.52 | 6.73 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 76.85 | 77.95 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261103T060341Z.json) | yes | 3.00 | 3.03 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 3.43 | 4.98 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261103T060341Z.json) | yes | 33.94 | 38.73 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261103T060341Z.json) | yes | 208.43 | 213.98 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | no | 214.70 | 0.33 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1.06 | 1.40 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.29 | 0.59 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.26 | 0.37 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 1820.87 | 28.44 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 16.10 | 33.93 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 62.51 | 74.53 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261103T060341Z.json) | yes | 6.70 | 6.87 | 100% | 75.00 | 0.00 | pass |
