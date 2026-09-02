# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260902T060558Z.json`

- Generated at: 20260902T060558Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.77 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.77/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 6 | 4876.68 | 3.96 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | no | 8 | 7786.94 | 15.79 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 6 | 37143.86 | 70.16 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 6 | 215787.11 | 366.18 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 484.96 | 3.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 817.66 | 11.47 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 4268.89 | 72.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 7688.52 | 113.74 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 1.60 | 1.68 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 6.31 | 8.71 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 33.96 | 123.60 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 226.06 | 425.80 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.30 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 1.02 | 1.17 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 2.09 | 2.42 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 174.30 | 175.49 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.23 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 4.60 | 4.89 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 11.14 | 12.46 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 17.72 | 40.59 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 323.46 | 435.82 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 3.37 | 4.40 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 5.16 | 5.19 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 31.20 | 36.28 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 162.70 | 163.37 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 251.30 | 2.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 288.36 | 4.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 1436.69 | 14.59 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 7632.41 | 171.72 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 3.95 | 6.73 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 4.62 | 7.18 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 18.28 | 72.04 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 212.15 | 650.76 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.22 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.31 | 0.41 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.53 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 152.47 | 153.26 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 3.31 | 8.73 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 4.26 | 4.41 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 24.70 | 26.93 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 249.69 | 277.99 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 1.23 | 3.04 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 2.97 | 3.21 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 43.37 | 53.39 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 243.23 | 247.35 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 810.78 | 7.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 716.71 | 14.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 7635.19 | 138.59 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 9999.39 | 142.78 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 18.33 | 21.97 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 36.77 | 143.95 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 75.86 | 243.05 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 103.65 | 265.89 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.27 | 0.31 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.59 | 0.67 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 2.76 | 3.01 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 190.87 | 194.25 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.39 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 1.04 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 15.45 | 16.78 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 30.05 | 44.22 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 220.33 | 226.05 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 626.42 | 1296.35 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.82 | 0.91 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 4.37 | 4.39 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 10.61 | 12.54 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 177.08 | 177.57 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 349.98 | 2.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 739.19 | 14.93 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 3458.73 | 47.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 6898.65 | 121.23 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 3.43 | 8.00 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 7.89 | 13.30 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 62.49 | 248.86 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 205.96 | 478.87 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.40 | 0.41 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 1.20 | 1.34 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 1.21 | 1.63 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 322.16 | 323.78 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.20 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 1.04 | 3.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 1.13 | 1.34 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 4.27 | 4.48 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 4.54 | 7.19 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 38.43 | 39.21 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 138.58 | 172.13 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 4.01 | 4.12 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 5.37 | 9.30 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 38.47 | 39.16 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 88.01 | 97.15 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 2658.12 | 4.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 2410.74 | 50.88 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 16538.98 | 134.88 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 181088.76 | 1547.39 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 11.04 | 11.98 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 48.92 | 77.92 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 148.44 | 149.65 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 245.11 | 979.47 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.44 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.70 | 2.07 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 2744.53 | 2772.96 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.30 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.44 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 2189.08 | 2244.19 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 2.45 | 2.55 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 6.46 | 7.92 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 6.72 | 8.22 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 8.36 | 23.35 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.51 | 0.53 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 5.67 | 5.71 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 617.88 | 641.59 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | no | 2652.42 | 2675.80 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 321.54 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 1441.17 | 9.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 731.14 | 9.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 4843.59 | 104.44 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 4.48 | 7.98 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 5.93 | 8.71 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 36.62 | 128.95 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 71.35 | 101.42 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 2.67 | 9.01 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 98.43 | 208.93 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 0.55 | 0.60 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 0.83 | 0.99 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 29.71 | 92.34 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 3.45 | 3.54 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 3.99 | 4.20 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 4.60 | 5.89 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 87.43 | 89.78 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 1.99 | 3.71 | 100% | 3585.00 | +3165.00 | pass |
| [Ty](latest-results/ty-20260902T060558Z.json) | yes | 2.48 | 2.51 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260902T060558Z.json) | yes | 34.58 | 37.57 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260902T060558Z.json) | yes | 235.27 | 242.51 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | no | 183.60 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.94 | 1.01 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.19 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 1899.53 | 39.88 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 52.97 | 84.31 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 59.96 | 63.74 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260902T060558Z.json) | yes | 6.72 | 6.96 | 100% | 75.00 | 0.00 | pass |
