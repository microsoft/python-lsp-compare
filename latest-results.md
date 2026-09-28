# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260928T060730Z.json`

- Generated at: 20260928T060730Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.84 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.84/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 6 | 5088.02 | 4.16 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | no | 8 | 16436.19 | 37.77 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 6 | 38514.36 | 74.14 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 6 | 217566.56 | 364.51 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 504.17 | 4.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 1053.90 | 22.73 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 4500.42 | 73.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 7688.41 | 114.99 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 1.65 | 1.89 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 6.12 | 8.84 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 83.23 | 329.24 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 227.50 | 468.36 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.33 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 1.16 | 1.49 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 2.23 | 2.33 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 175.42 | 175.90 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 1.03 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 4.29 | 4.36 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 12.59 | 14.17 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 19.64 | 22.45 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 329.85 | 464.42 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 5.66 | 5.79 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 8.36 | 16.17 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 32.34 | 35.77 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 166.71 | 168.72 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 257.86 | 2.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 285.29 | 4.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 1461.00 | 13.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 7736.99 | 172.00 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 4.73 | 7.80 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 4.81 | 7.16 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 17.74 | 68.20 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 209.10 | 640.39 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.42 | 0.47 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.52 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 151.88 | 152.92 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.37 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 1.94 | 2.02 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 4.73 | 5.04 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 25.85 | 28.51 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 255.91 | 289.24 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.79 | 0.85 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 3.16 | 3.20 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 38.27 | 43.63 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 242.02 | 243.47 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 832.64 | 7.82 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 1129.21 | 29.57 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 7632.92 | 136.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 11274.25 | 185.99 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 18.28 | 21.81 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 79.07 | 266.94 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 87.86 | 347.62 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 92.23 | 216.42 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.68 | 0.75 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 3.85 | 5.74 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 191.16 | 192.67 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.40 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 1.03 | 1.05 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 2.92 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 15.86 | 17.41 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 47.65 | 80.12 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 215.62 | 216.90 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 838.49 | 1379.15 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 4.47 | 4.48 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 5.57 | 13.19 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 11.32 | 13.29 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 181.45 | 183.44 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 374.41 | 2.88 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 926.41 | 20.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 3867.76 | 53.42 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 7086.84 | 120.64 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 3.33 | 7.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 14.42 | 26.58 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 88.10 | 351.56 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 208.83 | 460.44 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.44 | 0.51 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 2.49 | 3.32 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 4.25 | 7.79 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 318.44 | 321.94 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.21 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.75 | 1.65 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 2.20 | 3.67 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 5.36 | 5.56 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 7.20 | 22.84 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 37.64 | 38.27 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 145.72 | 176.38 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 4.60 | 12.11 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 5.06 | 5.10 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 37.18 | 37.55 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 101.94 | 110.98 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 2761.66 | 4.78 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 15845.34 | 108.00 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 5609.51 | 178.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 182639.34 | 1538.47 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 11.44 | 12.58 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 51.53 | 81.65 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 149.07 | 151.99 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 877.67 | 3509.79 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.22 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.48 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 2741.08 | 2774.28 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.28 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 2180.97 | 2209.83 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 2.60 | 2.66 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 6.12 | 6.49 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 6.98 | 9.93 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 12.67 | 23.94 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 3.05 | 3.70 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 5.81 | 5.92 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 480.54 | 505.46 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | no | 2618.62 | 2658.80 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 357.27 | 2.78 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 1565.58 | 9.53 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 864.84 | 12.83 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 4782.06 | 104.69 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 4.71 | 7.83 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 5.74 | 8.14 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 54.96 | 182.88 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 70.75 | 96.72 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.58 | 0.67 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 5.19 | 18.16 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 102.40 | 193.33 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.34 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 0.58 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 0.81 | 0.85 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 33.42 | 84.02 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.58 | 0.62 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 4.44 | 4.57 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 4.80 | 5.89 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 88.43 | 88.72 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260928T060730Z.json) | yes | 2.95 | 2.98 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 3.07 | 5.50 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20260928T060730Z.json) | yes | 36.75 | 39.79 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260928T060730Z.json) | yes | 228.47 | 230.60 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | no | 223.27 | 0.43 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 1.85 | 4.39 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.25 | 0.26 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 6343.76 | 66.56 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 17.65 | 36.64 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 122.07 | 150.74 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260928T060730Z.json) | yes | 59.96 | 73.59 | 100% | 75.00 | 0.00 | pass |
