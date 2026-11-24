# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261124T060329Z.json`

- Generated at: 20261124T060329Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.109 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.109/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 6 | 3609.27 | 4.09 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | no | 8 | 6843.99 | 9.13 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 6 | 41539.92 | 83.52 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 6 | 248300.93 | 354.68 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 495.27 | 4.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 681.07 | 5.50 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 4682.75 | 79.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 7863.86 | 106.11 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 1.87 | 2.17 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.13 | 3.21 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 5.84 | 9.56 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 180.20 | 389.83 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.26 | 0.29 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1.09 | 1.53 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.72 | 5.26 | 100% | 7910.00 | +3891.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 178.14 | 179.51 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.19 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.37 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 1.04 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 4.63 | 4.83 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 14.99 | 17.19 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 18.49 | 39.21 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 356.50 | 457.17 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 3.94 | 4.61 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 4.66 | 5.07 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 32.05 | 34.05 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 166.53 | 169.38 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4232.00, 7910.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 188.46 | 1.80 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 251.88 | 2.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1501.23 | 14.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 7707.80 | 168.36 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.92 | 3.97 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 4.80 | 7.74 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 4.87 | 8.00 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 191.97 | 550.15 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.19 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.54 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.17 | 3.03 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 154.30 | 159.44 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.24 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.36 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 1.05 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.36 | 5.36 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 3.74 | 4.32 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 26.84 | 30.59 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 254.93 | 297.53 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 1.83 | 1.88 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.33 | 3.64 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 39.68 | 46.01 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 239.56 | 243.45 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 528.23 | 4.90 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 801.54 | 8.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 7438.54 | 138.34 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 12835.35 | 226.65 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.62 | 5.51 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 18.63 | 22.39 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 83.86 | 270.93 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 124.72 | 341.80 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.24 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.67 | 0.75 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 4.06 | 4.72 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 181.01 | 183.80 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.49 | 0.70 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.69 | 2.83 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 14.59 | 16.65 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 17.79 | 18.58 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 213.57 | 216.10 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1035.23 | 1400.70 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 2.53 | 8.45 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 4.02 | 4.73 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 12.99 | 17.15 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 171.38 | 173.52 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 376.37 | 2.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 498.23 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 4013.31 | 55.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 6942.71 | 94.23 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 3.35 | 8.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 4.37 | 7.75 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 19.01 | 22.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 85.96 | 167.30 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.34 | 0.35 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1.35 | 1.74 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 3.26 | 5.15 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 309.69 | 319.64 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.18 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.42 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 1.14 | 1.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.34 | 2.90 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 5.10 | 9.09 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 5.16 | 6.00 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 37.79 | 40.24 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 148.15 | 179.58 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.56 | 0.59 | 100% | 2249.00 | +1356.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 3.89 | 3.92 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 36.54 | 37.57 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 107.64 | 123.19 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2249.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 1311.50 | 3.85 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1440.90 | 4.05 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 16931.48 | 115.95 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 213805.31 | 1526.17 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 7.19 | 28.04 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 11.70 | 13.95 | 100% | 788.00 | +665.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 52.08 | 75.18 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 137.72 | 147.57 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.25 | 0.50 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.38 | 0.90 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.47 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 2843.28 | 2890.65 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1.15 | 2.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 2079.21 | 2105.21 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 2.45 | 2.54 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 3.65 | 4.10 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 6.31 | 15.61 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 6.45 | 7.45 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 3.28 | 3.61 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 6.27 | 14.62 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 519.59 | 538.41 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | no | 2568.21 | 2601.08 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 788.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 348.96 | 2.84 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 372.70 | 3.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 1575.79 | 9.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 4542.70 | 94.84 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 4.93 | 8.72 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 7.05 | 10.63 | 100% | 497.00 | +483.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 10.77 | 15.32 | 100% | 276.60 | +262.60 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 61.37 | 99.14 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.27 | 0.29 | 100% | 217.00 | +191.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.53 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 53.01 | 70.94 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.82 | 1.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 0.83 | 0.99 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 1.47 | 1.64 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 52.76 | 103.43 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.27 | 1.46 | 100% | 57.00 | -148.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 5.38 | 5.96 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 5.50 | 7.71 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 88.06 | 89.15 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 1.07 | 1.09 | 100% | 2884.00 | +2464.00 | pass |
| [Ty](latest-results/ty-20261124T060329Z.json) | yes | 2.90 | 3.01 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261124T060329Z.json) | yes | 36.36 | 41.50 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261124T060329Z.json) | yes | 218.97 | 220.41 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 276.60, 497.00).
- client session hover: result differences detected (217.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 2884.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | no | 149.21 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.97 | 1.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.21 | 0.28 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 3008.92 | 87.25 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 12.93 | 16.85 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 211.92 | 262.67 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261124T060329Z.json) | yes | 36.91 | 61.35 | 100% | 75.00 | 0.00 | pass |
