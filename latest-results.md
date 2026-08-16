# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260816T060453Z.json`

- Generated at: 20260816T060453Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.72 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.72/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 6 | 3254.86 | 3.03 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | no | 8 | 7711.17 | 15.68 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 6 | 39185.10 | 79.04 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 6 | 223488.15 | 374.53 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 440.35 | 2.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 786.42 | 12.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 4352.82 | 76.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 8186.93 | 114.60 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 1.66 | 1.77 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 7.10 | 12.16 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 34.86 | 132.67 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 214.11 | 446.13 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.31 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 1.03 | 1.12 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 2.25 | 2.73 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 183.44 | 185.66 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 1.06 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 4.69 | 4.91 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 8.40 | 9.97 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 22.85 | 43.91 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 338.84 | 456.99 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.81 | 2.89 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 3.05 | 4.55 | 100% | 1909.00 | +1631.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 33.86 | 37.24 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 169.68 | 174.90 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 226.12 | 1.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 275.67 | 4.89 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 1453.36 | 14.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 7983.03 | 178.75 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 4.60 | 7.84 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 4.75 | 6.75 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 20.30 | 72.28 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 220.46 | 680.68 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.48 | 0.53 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.48 | 1.06 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 158.49 | 160.81 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.36 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 2.29 | 6.10 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.52 | 2.60 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 24.54 | 26.66 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 264.79 | 301.96 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 1.19 | 2.93 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 1.43 | 1.47 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 40.83 | 45.36 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 248.92 | 253.56 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 761.17 | 6.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 737.14 | 13.89 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 7930.72 | 136.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 11130.83 | 183.08 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 18.74 | 21.98 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 37.82 | 146.63 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 77.72 | 265.21 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 80.45 | 167.74 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.73 | 0.86 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 7.57 | 10.33 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 191.84 | 193.99 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.40 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 3.51 | 6.23 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 12.15 | 13.40 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 12.89 | 17.19 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 224.74 | 231.98 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 824.66 | 1340.68 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.17 | 2.23 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 7.64 | 10.44 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 11.91 | 14.23 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 182.84 | 183.46 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 298.68 | 1.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 688.80 | 13.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 3451.99 | 47.07 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 7379.55 | 123.68 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 3.39 | 7.50 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 8.16 | 12.82 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 62.68 | 248.67 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 209.88 | 473.57 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.38 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 1.07 | 1.15 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 1.58 | 1.85 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 329.73 | 333.85 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.27 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.43 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 1.12 | 1.21 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.73 | 0.74 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 1.79 | 1.92 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 39.08 | 39.95 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 136.33 | 170.61 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.50 | 0.54 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 1.60 | 1.75 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 38.61 | 38.79 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 88.87 | 98.89 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 1244.47 | 3.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 2412.15 | 51.03 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 17300.27 | 144.11 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 187031.53 | 1582.42 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 11.20 | 12.24 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 52.71 | 85.32 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 148.92 | 154.06 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 241.93 | 959.29 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.29 | 0.54 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.48 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 2.94 | 2.96 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 2819.45 | 2865.59 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.25 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.50 | 0.72 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 2243.88 | 2285.25 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 2.63 | 2.69 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.85 | 2.94 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 3.65 | 9.41 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 7.00 | 9.34 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.67 | 2.70 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 6.39 | 17.09 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 659.87 | 684.02 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | no | 2697.22 | 2737.56 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 284.07 | 2.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 1495.82 | 9.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 769.47 | 10.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 4976.40 | 111.52 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 5.22 | 9.82 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 5.83 | 8.41 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 42.94 | 139.06 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 82.47 | 138.60 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.52 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 2.77 | 9.40 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 147.22 | 209.24 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.36 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.51 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 0.94 | 1.35 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 3.71 | 4.66 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 1.72 | 3.47 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 2.61 | 2.90 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 5.24 | 6.31 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 90.98 | 92.29 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260816T060453Z.json) | yes | 0.99 | 1.02 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 3.19 | 4.43 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260816T060453Z.json) | yes | 35.94 | 40.75 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260816T060453Z.json) | yes | 233.20 | 236.32 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | no | 189.32 | 0.28 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.95 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 1852.21 | 37.43 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 45.93 | 92.22 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 59.10 | 60.83 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260816T060453Z.json) | yes | 7.27 | 7.47 | 100% | 75.00 | 0.00 | pass |
