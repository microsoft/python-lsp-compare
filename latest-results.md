# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261125T060347Z.json`

- Generated at: 20261125T060347Z
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
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 6 | 3416.42 | 4.06 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | no | 8 | 5208.55 | 4.53 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 6 | 34939.56 | 64.09 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 6 | 201367.78 | 268.43 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 494.99 | 5.28 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 565.78 | 5.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 4242.42 | 73.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 6498.97 | 89.69 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 2.05 | 2.33 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 3.31 | 5.47 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 6.10 | 10.46 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 135.00 | 268.20 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.37 | 0.39 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 1.27 | 1.53 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.36 | 4.17 | 100% | 7910.00 | +3891.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 158.91 | 159.51 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.17 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.45 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 0.87 | 0.94 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 3.79 | 4.07 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 10.42 | 10.71 | 100% | 168.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 17.81 | 22.48 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 327.81 | 437.73 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 5.99 | 7.47 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 11.68 | 31.87 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 33.58 | 42.81 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 149.88 | 152.35 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4232.00, 7910.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 184.93 | 2.13 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 246.27 | 2.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 1397.57 | 13.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 6622.36 | 145.67 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.89 | 4.24 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 4.77 | 7.56 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 5.08 | 7.71 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 151.53 | 411.22 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.18 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.56 | 0.72 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1.81 | 4.43 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 139.04 | 139.41 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.37 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 1.04 | 1.39 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.88 | 5.55 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.85 | 4.42 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 24.47 | 25.59 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 216.89 | 260.06 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 1.83 | 1.90 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.90 | 3.62 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 38.06 | 44.81 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 219.85 | 232.50 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 495.54 | 5.37 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 759.72 | 7.54 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 6720.71 | 116.74 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 9379.83 | 132.47 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1.81 | 5.80 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 17.91 | 21.59 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 50.32 | 67.96 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 70.67 | 239.03 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.23 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.87 | 1.02 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.00 | 2.24 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 166.97 | 169.57 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.28 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 0.79 | 0.82 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 15.74 | 16.62 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 16.91 | 24.02 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 203.57 | 206.80 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 580.09 | 1141.01 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.67 | 3.80 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 5.99 | 9.66 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 10.44 | 13.65 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 162.06 | 163.52 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 427.58 | 1.80 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 366.02 | 2.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 3548.87 | 49.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 6160.15 | 90.76 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 3.42 | 7.53 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.53 | 8.48 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 17.66 | 20.59 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 102.90 | 213.83 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.33 | 0.40 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 2.21 | 3.32 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 3.59 | 5.26 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 285.42 | 303.04 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.22 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.48 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 1.12 | 1.55 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1.32 | 1.36 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 4.55 | 5.37 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 32.20 | 32.54 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 134.55 | 168.55 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.47 | 0.50 | 100% | 2249.00 | +1356.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.75 | 3.77 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 32.16 | 32.44 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 93.22 | 107.78 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2249.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1305.44 | 2.18 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 1196.82 | 3.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 14960.97 | 106.05 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 171328.83 | 1082.19 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 6.52 | 25.23 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 11.24 | 13.60 | 100% | 788.00 | +665.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 51.48 | 75.80 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 120.39 | 126.21 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.32 | 0.60 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.32 | 0.61 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.40 | 0.51 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 2043.94 | 2096.88 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.20 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.22 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.84 | 2.15 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 1451.31 | 1507.41 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.32 | 7.82 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 2.38 | 2.63 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.45 | 3.84 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 6.34 | 8.88 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1.53 | 4.85 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 3.17 | 3.28 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 471.19 | 497.39 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | no | 1792.95 | 1846.71 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 788.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 352.60 | 3.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 415.58 | 5.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 1409.89 | 8.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 4036.76 | 85.51 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 5.39 | 8.61 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 6.62 | 9.83 | 100% | 497.00 | +483.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 15.77 | 25.95 | 100% | 276.60 | +262.60 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 66.86 | 127.85 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 0.15 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.21 | 0.45 | 100% | 217.00 | +191.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.51 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 81.18 | 163.79 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 0.88 | 1.09 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 1.39 | 1.51 | 100% | 2.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 3.07 | 3.60 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 3.56 | 4.64 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 4.42 | 6.43 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 4.85 | 5.25 | 100% | 225.00 | +20.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 5.25 | 13.42 | 100% | 57.00 | -148.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 75.39 | 78.70 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 2.76 | 3.36 | 100% | 2884.00 | +2464.00 | pass |
| [Ty](latest-results/ty-20261125T060347Z.json) | yes | 2.86 | 2.87 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261125T060347Z.json) | yes | 33.22 | 36.91 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261125T060347Z.json) | yes | 200.58 | 202.31 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 276.60, 497.00).
- client session hover: result differences detected (217.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 2884.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | no | 127.40 | 0.27 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.88 | 0.96 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.20 | 0.26 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 1686.29 | 23.67 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 12.46 | 20.94 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 53.08 | 60.33 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261125T060347Z.json) | yes | 5.48 | 5.75 | 100% | 75.00 | 0.00 | pass |
