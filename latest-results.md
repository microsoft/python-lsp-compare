# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261114T060312Z.json`

- Generated at: 20261114T060312Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.104 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.104/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 6 | 3618.48 | 3.82 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | no | 8 | 6908.37 | 6.01 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 6 | 35352.44 | 62.35 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 6 | 234935.89 | 346.60 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 475.65 | 3.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 685.34 | 5.09 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 4119.67 | 65.54 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 7350.63 | 98.21 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 1.93 | 2.20 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.15 | 5.31 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 6.09 | 10.68 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 138.19 | 286.96 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.27 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 1.19 | 1.54 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 3.43 | 5.24 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 180.66 | 185.64 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.15 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 0.95 | 1.02 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 3.52 | 5.33 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 3.73 | 3.89 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 11.45 | 13.22 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 14.81 | 21.14 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 291.41 | 417.87 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 1.57 | 3.43 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 4.44 | 4.54 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 28.58 | 30.84 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 167.53 | 171.29 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 280.54 | 1.81 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 247.57 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 1476.60 | 16.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 7070.44 | 158.20 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 1.18 | 3.82 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 4.53 | 7.28 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 4.84 | 8.26 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 164.07 | 334.02 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.18 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.50 | 0.98 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.53 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 162.11 | 164.45 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.32 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.48 | 3.75 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 3.80 | 6.82 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 32.32 | 34.60 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 222.04 | 257.51 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 1.86 | 1.89 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 3.26 | 3.96 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 42.19 | 50.72 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 241.76 | 247.03 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 773.58 | 7.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 806.54 | 12.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 7226.45 | 127.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 9445.11 | 131.06 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 4.05 | 7.56 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 18.11 | 22.47 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 53.58 | 68.84 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 74.62 | 246.74 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.22 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.61 | 0.68 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 4.43 | 5.00 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 191.35 | 193.84 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.38 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 0.97 | 1.01 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.93 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 14.46 | 15.77 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 28.42 | 60.99 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 210.35 | 211.82 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 568.27 | 1131.87 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.64 | 3.65 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 11.42 | 14.24 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 22.01 | 55.10 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 182.35 | 183.47 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 383.65 | 2.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 651.73 | 4.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 3604.68 | 48.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 6412.58 | 90.74 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.98 | 7.44 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.64 | 9.09 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 16.97 | 21.08 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 78.91 | 147.76 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.37 | 0.38 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.69 | 2.83 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 4.26 | 10.57 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 301.83 | 306.22 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.17 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.92 | 0.93 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 1.09 | 1.28 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.93 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.23 | 3.55 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 4.55 | 4.98 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 35.24 | 38.80 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 128.05 | 162.81 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.97 | 3.99 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 13.29 | 24.05 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 36.61 | 36.78 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 91.86 | 109.45 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 1571.07 | 3.90 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 1366.21 | 4.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 15258.49 | 104.61 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 202348.20 | 1507.89 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 6.68 | 26.01 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 12.05 | 14.59 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 57.06 | 100.50 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 123.23 | 125.96 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.17 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.31 | 0.61 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.46 | 0.49 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 2808.56 | 2845.55 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.21 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.40 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 2074.70 | 2147.42 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 1.70 | 5.19 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 2.54 | 2.61 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 4.55 | 5.04 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 7.01 | 9.13 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.49 | 3.89 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 10.80 | 16.78 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 458.10 | 494.69 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | no | 2530.42 | 2557.13 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 371.81 | 3.23 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 690.39 | 4.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 1447.89 | 8.48 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 4527.59 | 96.82 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 5.72 | 10.11 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 6.50 | 10.26 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 14.85 | 24.99 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 60.31 | 102.66 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 0.15 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.52 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.67 | 10.20 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 55.33 | 70.98 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.30 | 0.32 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 0.76 | 0.99 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 1.31 | 1.37 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 57.89 | 158.41 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.67 | 4.06 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 3.91 | 4.97 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 5.15 | 6.10 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 83.12 | 84.42 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 2.75 | 4.65 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261114T060312Z.json) | yes | 3.02 | 3.03 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261114T060312Z.json) | yes | 31.46 | 35.66 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261114T060312Z.json) | yes | 227.47 | 231.13 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | no | 231.60 | 0.27 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.85 | 0.93 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.14 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 1991.16 | 27.07 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 19.23 | 33.00 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 55.47 | 60.75 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261114T060312Z.json) | yes | 6.51 | 6.67 | 100% | 75.00 | 0.00 | pass |
