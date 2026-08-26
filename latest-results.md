# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260826T060727Z.json`

- Generated at: 20260826T060727Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.74 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.74/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.2.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 6 | 4787.94 | 3.68 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | no | 8 | 7686.35 | 15.53 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 6 | 37706.69 | 74.96 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 6 | 213844.23 | 370.01 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 456.73 | 3.37 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 777.58 | 11.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 4164.70 | 70.88 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 7740.90 | 113.08 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 1.62 | 1.79 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 6.62 | 12.79 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 33.52 | 122.19 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 221.85 | 437.71 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.30 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 1.02 | 1.07 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2.01 | 2.37 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 174.91 | 176.12 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.45 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 1.03 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 4.18 | 4.31 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 10.46 | 12.11 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 16.99 | 38.60 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 314.76 | 442.86 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 3.09 | 4.61 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 4.25 | 4.26 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 31.54 | 35.47 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 163.41 | 164.66 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 234.27 | 2.04 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 283.32 | 5.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 1452.76 | 13.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 7593.77 | 173.37 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 4.17 | 8.19 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 4.69 | 7.32 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 20.29 | 72.28 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 219.65 | 534.43 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.21 | 0.22 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.50 | 0.56 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 1.51 | 3.47 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 152.38 | 154.21 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 1.05 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2.30 | 4.28 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.25 | 3.40 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 26.00 | 30.51 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 251.36 | 284.25 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 1.81 | 3.52 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 1.87 | 1.89 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 38.90 | 47.72 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 242.38 | 245.43 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 811.24 | 7.53 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 799.57 | 16.61 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 7621.16 | 141.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 10905.38 | 176.85 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 18.93 | 22.19 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 38.53 | 143.75 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 78.82 | 260.38 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 118.35 | 316.09 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.25 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.70 | 0.83 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2.66 | 2.84 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 188.13 | 190.11 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.41 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 14.76 | 16.13 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 34.70 | 58.52 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 219.91 | 222.40 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 792.27 | 1264.82 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.53 | 3.61 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 6.92 | 11.80 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 12.04 | 15.44 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 179.00 | 180.30 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 338.91 | 2.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 682.59 | 12.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 3425.89 | 46.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 6898.97 | 121.37 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.36 | 7.77 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 6.61 | 11.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 61.24 | 243.96 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 209.59 | 425.35 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.40 | 0.42 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 1.01 | 1.05 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 1.24 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 320.50 | 321.03 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.26 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.86 | 2.21 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.74 | 0.83 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.30 | 3.63 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 37.20 | 37.95 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 135.28 | 164.36 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.48 | 0.50 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.36 | 4.37 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 38.50 | 39.21 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 89.22 | 101.87 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 2645.18 | 4.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2403.00 | 51.23 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 16319.07 | 132.12 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 179144.48 | 1560.12 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 12.29 | 13.42 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 48.86 | 80.34 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 143.33 | 144.32 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 238.43 | 952.83 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.30 | 0.51 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.44 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 2761.34 | 2819.29 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.43 | 0.89 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.44 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 2228.76 | 2249.37 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 2.62 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 5.11 | 5.31 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 6.27 | 7.26 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 16.73 | 27.07 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.57 | 0.61 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 4.78 | 4.88 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 604.59 | 635.02 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | no | 2664.55 | 2712.24 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 301.62 | 2.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 1438.88 | 9.26 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 761.42 | 10.54 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 4844.95 | 110.85 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 4.66 | 7.98 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 6.21 | 9.27 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 43.71 | 138.99 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 77.34 | 119.87 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 0.55 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2.63 | 8.76 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 150.95 | 233.88 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.36 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 0.51 | 0.57 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 1.11 | 2.08 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 4.74 | 5.00 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 3.45 | 3.62 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 3.55 | 5.05 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 4.82 | 5.76 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 88.85 | 92.42 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260826T060727Z.json) | yes | 1.58 | 1.62 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 2.57 | 4.28 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260826T060727Z.json) | yes | 35.17 | 39.34 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260826T060727Z.json) | yes | 232.37 | 243.12 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | no | 188.67 | 0.38 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 1.70 | 4.14 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 0.20 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 1790.19 | 32.04 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 31.04 | 61.96 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 58.33 | 59.66 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260826T060727Z.json) | yes | 6.75 | 6.90 | 100% | 75.00 | 0.00 | pass |
