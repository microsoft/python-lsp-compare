# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260821T060731Z.json`

- Generated at: 20260821T060731Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.73 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.73/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 6 | 3267.02 | 3.10 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | no | 8 | 7797.84 | 15.82 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 6 | 37523.18 | 72.01 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 6 | 219129.78 | 369.46 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 412.41 | 2.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 757.87 | 10.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 4476.63 | 79.94 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 7831.82 | 114.04 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 1.59 | 1.69 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 6.49 | 9.24 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 30.11 | 116.80 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 220.70 | 414.05 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 1.55 | 2.00 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.44 | 2.69 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 179.34 | 186.81 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.48 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 4.36 | 4.82 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 8.10 | 9.52 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 14.99 | 17.59 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 358.16 | 455.64 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.89 | 2.90 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 3.03 | 4.50 | 100% | 1909.00 | +1631.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 33.00 | 35.66 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 164.77 | 165.36 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 239.26 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 282.88 | 5.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 1466.95 | 14.85 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 7671.99 | 172.03 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 4.54 | 7.81 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 4.78 | 7.34 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 19.57 | 72.16 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 209.82 | 646.30 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.28 | 0.32 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.50 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 152.85 | 153.28 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.69 | 5.78 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.82 | 2.90 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 25.74 | 27.81 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 252.85 | 279.55 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 1.99 | 2.10 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.32 | 3.46 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 43.10 | 47.18 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 243.54 | 244.52 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 780.56 | 6.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 828.84 | 18.12 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 7741.65 | 133.54 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 10187.48 | 144.79 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 19.00 | 22.72 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 36.17 | 143.57 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 75.14 | 155.13 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 79.40 | 263.82 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.26 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.65 | 0.73 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.74 | 2.91 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 188.39 | 191.67 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 12.20 | 13.14 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 31.03 | 56.73 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 222.89 | 228.52 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 633.01 | 1301.79 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.28 | 2.30 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 10.47 | 12.62 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 20.43 | 46.56 | 100% | 794.00 | -3498.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 180.25 | 180.98 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 312.75 | 1.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 822.72 | 17.42 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 3452.48 | 47.96 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 7162.22 | 122.88 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 3.32 | 7.43 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 6.82 | 11.36 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 65.77 | 261.99 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 204.32 | 479.61 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.37 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 1.18 | 1.30 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 3.18 | 4.74 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 332.75 | 344.02 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.22 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.45 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 1.27 | 1.70 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.35 | 3.60 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.20 | 2.68 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 11.07 | 15.29 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 38.51 | 39.82 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 143.73 | 191.23 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.43 | 2.48 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 4.72 | 8.78 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 37.57 | 37.89 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 87.62 | 97.94 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 1235.19 | 3.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2414.29 | 50.20 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 16462.91 | 135.43 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 183672.12 | 1562.08 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 10.81 | 11.94 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 47.11 | 76.66 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 146.16 | 152.95 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 240.98 | 945.01 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.22 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.48 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 1.93 | 2.93 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 2781.33 | 2842.59 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.28 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.45 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 2215.98 | 2263.19 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 2.79 | 3.10 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.90 | 2.96 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 6.11 | 6.31 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 7.22 | 15.11 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.57 | 0.68 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.74 | 2.79 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 622.99 | 642.07 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | no | 2664.11 | 2685.05 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 286.84 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 1476.75 | 9.09 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 753.89 | 9.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 5049.98 | 112.20 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 4.60 | 7.91 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 6.00 | 9.02 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 43.24 | 133.09 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 88.16 | 144.44 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 2.55 | 8.47 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 134.77 | 209.53 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.36 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 0.52 | 0.60 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 0.75 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 4.85 | 5.86 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.56 | 0.57 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 2.76 | 3.49 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 4.99 | 6.38 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 89.72 | 92.05 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260821T060731Z.json) | yes | 1.04 | 1.05 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 1.96 | 3.63 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260821T060731Z.json) | yes | 34.59 | 39.95 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260821T060731Z.json) | yes | 243.49 | 254.66 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | no | 185.27 | 0.27 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.92 | 0.97 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.16 | 0.16 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.19 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 1752.08 | 31.13 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 23.30 | 35.03 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 63.24 | 69.18 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260821T060731Z.json) | yes | 6.83 | 7.13 | 100% | 75.00 | 0.00 | pass |
