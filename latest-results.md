# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260904T060510Z.json`

- Generated at: 20260904T060510Z
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
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 6 | 4731.84 | 3.81 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | no | 8 | 8368.35 | 18.15 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 6 | 38050.72 | 76.54 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 6 | 217507.91 | 367.08 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 371.86 | 3.20 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 752.12 | 11.61 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 4338.90 | 74.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 7708.56 | 112.07 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 1.63 | 1.79 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 6.67 | 9.96 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 33.43 | 121.78 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 209.96 | 487.49 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.31 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 1.11 | 1.31 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2.58 | 3.17 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 180.25 | 186.72 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.45 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 1.04 | 2.61 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 4.48 | 4.79 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 10.19 | 13.38 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 17.35 | 39.72 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 329.75 | 448.42 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 3.63 | 5.20 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 3.64 | 3.83 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 32.12 | 35.14 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 164.60 | 165.28 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 249.85 | 2.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 290.82 | 4.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 1443.34 | 13.74 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 7693.57 | 172.11 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 3.95 | 6.76 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 4.82 | 7.39 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 18.09 | 71.36 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 216.27 | 664.67 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.21 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.52 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2.28 | 2.97 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 156.46 | 163.01 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.80 | 2.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 1.02 | 1.06 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 4.26 | 4.47 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 24.79 | 26.63 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 246.38 | 279.52 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 1.22 | 3.09 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 2.82 | 2.86 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 39.03 | 44.62 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 240.38 | 241.79 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 806.02 | 7.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 679.06 | 12.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 7828.03 | 139.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 10849.00 | 177.19 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 18.70 | 22.32 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 36.44 | 144.22 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 72.05 | 243.50 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 101.72 | 255.34 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.26 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.60 | 0.68 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2.68 | 2.99 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 189.31 | 190.04 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 14.82 | 16.27 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 15.23 | 22.41 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 222.72 | 224.66 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 800.11 | 1236.40 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 2.70 | 2.74 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 5.43 | 9.16 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 12.79 | 15.32 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 183.30 | 185.90 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 357.13 | 2.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 756.25 | 15.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 3453.26 | 46.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 7087.61 | 121.54 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 3.50 | 8.03 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 7.05 | 11.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 62.42 | 243.10 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 195.28 | 455.37 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.39 | 0.40 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 1.16 | 1.26 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 3.32 | 5.17 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 333.33 | 344.93 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.41 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 1.11 | 1.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2.92 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 4.44 | 5.08 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 6.09 | 17.33 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 39.47 | 40.64 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 136.57 | 168.38 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.39 | 0.42 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 3.97 | 4.00 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 38.52 | 39.25 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 88.65 | 98.01 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 2632.68 | 4.67 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2401.94 | 51.24 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 16531.13 | 138.49 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 182302.86 | 1551.70 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 11.23 | 12.29 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 49.16 | 83.77 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 143.62 | 144.21 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 237.48 | 949.03 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.21 | 0.21 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.24 | 0.29 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.50 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 2738.18 | 2772.67 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.30 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.55 | 0.95 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 2214.81 | 2266.21 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 2.48 | 2.61 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 5.89 | 5.97 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 6.37 | 7.64 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 14.47 | 19.84 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 3.84 | 10.21 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 5.66 | 5.68 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 635.87 | 661.56 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | no | 2659.43 | 2681.71 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 314.30 | 2.71 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 1435.10 | 9.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 759.53 | 10.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 4887.28 | 105.43 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 4.78 | 8.09 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 5.89 | 8.74 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 44.69 | 134.24 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 72.26 | 97.11 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 0.51 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2.73 | 9.18 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 121.86 | 196.47 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.36 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 0.54 | 0.61 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 1.03 | 1.89 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 14.06 | 41.01 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.60 | 0.63 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 4.36 | 5.20 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 4.55 | 5.65 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 89.74 | 92.20 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260904T060510Z.json) | yes | 2.53 | 2.55 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 3.15 | 4.36 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260904T060510Z.json) | yes | 34.38 | 39.74 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260904T060510Z.json) | yes | 229.24 | 230.82 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | no | 187.58 | 0.28 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.94 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 2541.06 | 72.57 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 20.94 | 53.32 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 141.02 | 145.84 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260904T060510Z.json) | yes | 55.75 | 63.14 | 100% | 75.00 | 0.00 | pass |
