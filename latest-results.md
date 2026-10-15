# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261015T060556Z.json`

- Generated at: 20261015T060556Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.87 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.87/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 6 | 3629.06 | 4.37 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | no | 8 | 17288.06 | 39.31 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 6 | 41208.84 | 78.67 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 6 | 252804.95 | 384.46 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 579.67 | 4.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 1256.05 | 25.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 4998.57 | 87.66 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 8282.26 | 109.21 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 1.72 | 1.99 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 6.76 | 12.35 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 85.46 | 338.27 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 176.13 | 372.28 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.31 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 1.23 | 1.52 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.52 | 2.77 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 187.77 | 192.37 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.43 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 1.04 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 4.36 | 4.56 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 15.29 | 16.44 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 33.77 | 49.23 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 391.73 | 497.68 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 4.19 | 6.47 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 6.19 | 6.45 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 38.16 | 40.66 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 176.74 | 180.92 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 269.55 | 2.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 303.97 | 4.77 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 1549.40 | 15.27 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 7972.35 | 173.21 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 4.56 | 7.02 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 5.05 | 8.05 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 16.15 | 63.55 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 177.22 | 486.60 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.24 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.27 | 0.35 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.62 | 0.68 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 162.46 | 164.68 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.34 | 2.82 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 5.32 | 5.78 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 28.24 | 31.74 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 269.90 | 317.65 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 3.31 | 3.40 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 4.87 | 14.69 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 42.01 | 49.04 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 255.34 | 258.29 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 870.46 | 8.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 1261.81 | 30.23 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 8027.73 | 150.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 12439.54 | 186.69 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 17.56 | 20.70 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 81.54 | 321.94 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 83.78 | 280.60 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 106.63 | 253.67 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.69 | 0.78 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 4.29 | 6.80 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 200.21 | 202.27 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 1.07 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.73 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 19.24 | 20.03 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 32.21 | 66.51 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 254.07 | 258.80 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 837.31 | 1310.86 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 5.58 | 5.99 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 11.30 | 13.17 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 30.37 | 82.14 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 190.31 | 193.36 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 383.18 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 884.05 | 18.98 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 4099.96 | 56.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 7431.45 | 118.28 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 3.01 | 6.98 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 19.12 | 26.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 87.65 | 349.58 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 169.94 | 372.93 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.41 | 0.43 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 1.11 | 1.20 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 1.68 | 1.93 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 334.93 | 340.77 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.22 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.65 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 1.19 | 1.30 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 3.01 | 3.71 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 5.76 | 6.29 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 43.65 | 44.28 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 152.17 | 192.07 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.89 | 3.59 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 5.21 | 5.30 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 41.69 | 43.07 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 109.55 | 126.83 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 1154.04 | 4.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 16481.43 | 116.03 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 5884.06 | 189.59 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 216077.55 | 1652.80 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 11.00 | 13.20 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 53.89 | 87.98 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 144.83 | 145.72 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 934.96 | 3738.84 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.27 | 0.41 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.48 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 3048.66 | 3091.99 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.58 | 0.86 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 2343.12 | 2429.69 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.70 | 9.58 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 2.79 | 3.01 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 4.75 | 4.85 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 8.34 | 10.66 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 4.48 | 4.66 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 9.86 | 18.30 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 516.87 | 546.27 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | no | 2724.59 | 2740.46 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 372.16 | 3.13 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 1639.95 | 9.75 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 921.05 | 14.71 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 5013.60 | 102.79 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 6.23 | 8.61 | 100% | 496.00 | +482.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 6.40 | 11.43 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 62.71 | 193.26 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 81.02 | 125.95 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.54 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 5.65 | 19.89 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 89.53 | 189.52 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.33 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 0.64 | 0.81 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 0.75 | 0.85 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 7.61 | 15.39 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.42 | 5.18 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 4.69 | 5.72 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 5.36 | 6.11 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 93.37 | 95.48 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 2.41 | 4.82 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261015T060556Z.json) | yes | 3.17 | 3.27 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261015T060556Z.json) | yes | 36.37 | 40.27 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261015T060556Z.json) | yes | 242.42 | 251.88 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 487.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | no | 223.29 | 0.32 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 1.02 | 1.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 0.25 | 0.28 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 6553.78 | 63.78 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 17.99 | 32.60 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 115.57 | 168.72 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261015T060556Z.json) | yes | 57.78 | 60.39 | 100% | 75.00 | 0.00 | pass |
