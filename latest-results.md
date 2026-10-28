# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261028T060413Z.json`

- Generated at: 20261028T060413Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.93 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.93/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 6 | 3344.33 | 3.94 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | no | 8 | 7084.95 | 8.71 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 6 | 42032.54 | 85.12 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 6 | 270474.13 | 380.35 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 507.46 | 3.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 732.24 | 4.44 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 4983.01 | 86.37 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 7769.97 | 107.63 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 1.69 | 1.94 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.22 | 5.89 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 6.59 | 11.99 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 180.07 | 387.47 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1.18 | 1.63 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.49 | 2.78 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 184.49 | 187.94 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.24 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.39 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 1.05 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 4.18 | 4.27 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 12.88 | 14.76 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 12.93 | 14.56 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 387.75 | 473.11 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.34 | 5.05 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 4.89 | 5.02 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 35.91 | 36.97 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 168.36 | 171.59 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 256.30 | 1.72 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 243.34 | 2.23 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1536.18 | 14.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 7757.58 | 162.40 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.06 | 3.98 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 4.52 | 7.07 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 5.18 | 8.24 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 153.08 | 397.46 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.25 | 0.28 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.54 | 0.64 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1.27 | 3.40 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 157.89 | 159.15 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 1.11 | 1.18 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.68 | 6.68 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 3.88 | 4.17 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 27.53 | 29.21 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 250.50 | 254.02 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1.37 | 3.52 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 2.27 | 2.31 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 40.58 | 47.67 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 249.42 | 251.36 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 770.50 | 7.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 719.49 | 8.05 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 7838.89 | 142.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 13710.06 | 229.76 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1.79 | 6.18 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 17.73 | 21.24 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 84.18 | 282.92 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 94.93 | 208.80 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.27 | 0.32 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.74 | 0.85 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.06 | 4.92 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 194.44 | 198.22 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.41 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.79 | 2.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 1.10 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 15.81 | 17.02 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 19.49 | 35.20 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 234.71 | 237.07 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1048.99 | 1356.33 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 3.92 | 4.16 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 14.49 | 17.78 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 15.13 | 45.11 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 186.26 | 188.91 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 503.65 | 1.65 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 369.40 | 2.91 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 4087.81 | 56.60 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 7218.34 | 101.00 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1.69 | 5.74 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 3.22 | 7.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 19.59 | 26.24 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 96.80 | 166.58 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.43 | 0.44 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1.81 | 2.96 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.42 | 3.47 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 328.03 | 333.90 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.24 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.44 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 1.25 | 1.59 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.30 | 8.13 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 6.12 | 6.76 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 40.35 | 43.23 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 150.33 | 189.20 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.57 | 0.61 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 4.54 | 5.06 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 38.59 | 38.83 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 110.83 | 127.06 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1317.89 | 3.59 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 1097.15 | 3.86 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 16134.85 | 113.61 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 234724.83 | 1662.41 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 6.50 | 25.11 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 11.19 | 12.97 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 54.85 | 88.79 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 146.94 | 149.34 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.23 | 0.25 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.26 | 0.32 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.48 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 3087.04 | 3164.77 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1.19 | 2.88 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 2314.21 | 2430.28 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.81 | 4.16 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 2.99 | 3.13 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 4.07 | 4.70 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 6.23 | 6.65 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 3.55 | 3.63 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 8.18 | 18.45 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 505.29 | 530.44 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | no | 2760.87 | 2823.60 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 356.47 | 3.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 682.55 | 4.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 1580.63 | 9.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 5164.52 | 106.40 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 5.34 | 9.82 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 5.96 | 8.27 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 14.67 | 26.00 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 81.56 | 152.48 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.54 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.72 | 10.23 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 86.58 | 116.16 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.35 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 0.72 | 0.81 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 1.34 | 1.41 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 11.28 | 29.55 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 3.71 | 3.79 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 4.59 | 4.82 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 5.02 | 6.81 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 98.57 | 103.27 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2.67 | 4.44 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261028T060413Z.json) | yes | 3.11 | 3.26 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261028T060413Z.json) | yes | 35.95 | 40.93 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261028T060413Z.json) | yes | 253.99 | 262.71 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | no | 214.31 | 0.42 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 1.81 | 4.39 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.21 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 2658.51 | 77.48 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 35.84 | 67.22 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 134.03 | 156.16 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261028T060413Z.json) | yes | 62.57 | 75.82 | 100% | 75.00 | 0.00 | pass |
