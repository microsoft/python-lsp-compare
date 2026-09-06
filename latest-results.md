# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260906T060451Z.json`

- Generated at: 20260906T060451Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.78 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.78/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 6 | 4817.67 | 3.86 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | no | 8 | 7932.25 | 16.24 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 6 | 37935.49 | 74.41 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 6 | 207334.55 | 367.36 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 375.38 | 3.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 775.10 | 10.48 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 4360.23 | 74.64 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 7885.11 | 115.69 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 1.68 | 1.84 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 7.28 | 10.49 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 34.57 | 125.36 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 206.50 | 376.58 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.28 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 1.18 | 1.38 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 2.26 | 2.63 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 191.63 | 201.23 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 1.02 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 4.10 | 4.52 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 9.72 | 10.84 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 12.70 | 15.16 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 331.84 | 451.96 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 2.68 | 2.71 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 3.58 | 3.64 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 32.46 | 37.24 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 175.20 | 178.30 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 251.80 | 2.42 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 281.43 | 4.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 1389.54 | 13.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 7693.25 | 171.57 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 3.87 | 6.59 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 4.75 | 7.40 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 19.51 | 74.52 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 196.62 | 586.71 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.19 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.23 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.51 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 165.85 | 167.37 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 1.13 | 1.21 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 2.34 | 6.23 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 4.27 | 4.62 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 23.05 | 24.73 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 245.17 | 287.43 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1.85 | 3.75 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 2.73 | 2.75 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 37.74 | 43.17 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 249.08 | 257.21 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 829.67 | 7.64 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 781.35 | 14.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 7859.85 | 135.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 10629.21 | 171.51 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 18.25 | 21.90 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 39.99 | 149.37 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 57.06 | 83.56 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 71.61 | 235.72 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.25 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.73 | 0.86 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 2.49 | 2.74 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 195.73 | 197.92 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.19 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.40 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 1.03 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 15.81 | 23.93 | 100% | 256.00 | -184.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 16.79 | 18.50 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 226.25 | 231.24 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 771.76 | 1222.68 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 2.73 | 2.78 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 13.06 | 15.85 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 15.98 | 51.40 | 100% | 794.00 | -3498.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 195.33 | 201.11 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 349.16 | 2.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 756.41 | 15.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 3613.83 | 48.46 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 7254.52 | 120.49 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 3.69 | 8.81 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 11.70 | 19.53 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 65.28 | 252.50 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 195.34 | 378.45 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.38 | 0.40 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1.19 | 1.90 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 1.58 | 2.06 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 331.02 | 341.87 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.19 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.43 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 1.10 | 1.25 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 3.44 | 7.65 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 4.19 | 4.54 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 37.47 | 37.80 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 141.42 | 173.53 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 3.89 | 3.92 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 5.73 | 11.77 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 37.49 | 37.74 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 87.20 | 96.56 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 2692.29 | 4.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 2416.76 | 50.94 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 16516.76 | 129.96 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 171954.81 | 1560.21 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 10.51 | 11.60 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 55.87 | 88.57 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 137.92 | 142.64 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 242.08 | 967.53 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.18 | 0.20 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.42 | 0.46 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 2771.31 | 2824.18 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 2264.24 | 2347.29 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 2.67 | 2.75 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 5.53 | 5.70 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 6.09 | 6.42 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 11.13 | 27.17 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1.11 | 2.94 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 5.86 | 6.12 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 587.54 | 616.14 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | no | 2624.90 | 2691.45 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 319.37 | 2.98 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 1425.92 | 8.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 747.90 | 10.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 4687.00 | 101.12 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 4.86 | 8.06 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 6.64 | 9.34 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 40.70 | 143.33 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 67.81 | 115.51 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.61 | 0.74 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 4.06 | 14.47 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 119.60 | 266.93 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 0.51 | 0.60 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 0.74 | 0.87 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 4.47 | 5.54 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1.19 | 3.02 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 4.82 | 6.24 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 5.01 | 6.84 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 80.27 | 83.17 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260906T060451Z.json) | yes | 2.56 | 2.60 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 3.79 | 4.47 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260906T060451Z.json) | yes | 32.90 | 37.74 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260906T060451Z.json) | yes | 233.48 | 242.16 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | no | 199.51 | 0.37 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1.78 | 4.58 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 1973.78 | 43.68 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 19.74 | 30.31 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 100.01 | 130.02 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260906T060451Z.json) | yes | 11.30 | 19.52 | 100% | 75.00 | 0.00 | pass |
