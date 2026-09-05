# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260905T060452Z.json`

- Generated at: 20260905T060452Z
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
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 6 | 4084.81 | 3.20 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | no | 8 | 6320.79 | 12.72 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 6 | 26941.05 | 47.14 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 6 | 153767.57 | 224.85 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 306.18 | 2.55 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 567.12 | 8.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 3375.32 | 59.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 5726.42 | 78.98 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 1.45 | 1.55 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 5.18 | 8.51 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 28.09 | 101.33 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 129.51 | 288.90 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.20 | 0.22 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 1.03 | 1.25 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1.91 | 3.01 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 133.79 | 136.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.26 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 0.79 | 0.83 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 3.26 | 3.43 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 7.92 | 9.09 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 9.93 | 10.23 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 264.06 | 378.30 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1.99 | 2.51 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 3.04 | 3.07 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 26.25 | 31.31 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 127.53 | 130.05 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 207.43 | 2.06 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 228.45 | 4.04 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 1087.84 | 11.14 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 5492.42 | 123.80 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 3.19 | 5.28 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 4.04 | 5.93 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 17.19 | 58.24 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 147.28 | 448.98 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.15 | 0.19 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.18 | 0.23 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.49 | 0.54 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 118.43 | 120.11 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 0.69 | 0.70 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.74 | 2.33 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.98 | 1.06 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 3.60 | 3.70 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 19.86 | 22.01 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 172.95 | 198.16 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1.10 | 2.71 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 2.39 | 2.41 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 31.79 | 35.84 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 179.65 | 182.56 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 683.08 | 6.14 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 572.80 | 10.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 6684.76 | 77.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 5619.36 | 95.92 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 15.45 | 18.38 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 30.20 | 120.03 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 40.79 | 52.62 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 52.62 | 174.52 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.21 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.60 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 2.13 | 2.24 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 143.76 | 146.26 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 0.84 | 0.92 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 12.51 | 13.48 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 18.97 | 24.04 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 157.10 | 159.35 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 326.50 | 743.66 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 2.39 | 2.44 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 2.66 | 8.55 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 7.12 | 9.03 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 137.12 | 139.34 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 303.70 | 2.08 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 676.25 | 13.84 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 2538.87 | 34.87 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 5153.93 | 85.74 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 2.93 | 6.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 5.48 | 9.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 55.21 | 213.51 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 130.10 | 265.89 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.32 | 0.37 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 1.29 | 1.55 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 2.73 | 2.78 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 246.06 | 265.52 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.15 | 0.17 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 0.88 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1.32 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 3.62 | 3.70 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 9.04 | 24.03 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 26.12 | 27.55 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 104.19 | 127.51 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.89 | 2.40 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 3.39 | 3.41 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 25.57 | 26.15 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 62.98 | 70.18 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 2317.31 | 4.11 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 2125.98 | 44.99 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 12158.73 | 92.75 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 128323.06 | 906.82 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 9.31 | 10.26 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 34.38 | 62.25 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 100.13 | 102.00 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 211.04 | 843.36 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.17 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.35 | 0.72 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.43 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 1622.56 | 1677.26 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.25 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 1289.40 | 1343.40 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 2.30 | 2.57 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 5.48 | 6.15 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 5.54 | 6.52 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 6.95 | 18.11 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 5.14 | 5.23 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 6.63 | 22.09 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 423.00 | 438.61 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | no | 1519.71 | 1535.39 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 267.11 | 2.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 1095.53 | 7.30 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 533.29 | 8.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 3452.37 | 57.82 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 4.51 | 8.70 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 5.06 | 7.61 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 36.05 | 116.33 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 39.16 | 62.76 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.19 | 0.35 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.50 | 0.53 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 2.28 | 7.81 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 7.02 | 8.26 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.29 | 0.34 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 0.47 | 0.56 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 0.88 | 1.04 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 11.28 | 20.18 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1.05 | 2.92 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 3.45 | 4.07 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 3.50 | 3.78 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 60.92 | 63.00 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260905T060452Z.json) | yes | 2.18 | 2.20 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 3.14 | 4.46 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260905T060452Z.json) | yes | 27.16 | 31.01 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260905T060452Z.json) | yes | 170.71 | 172.35 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | no | 184.01 | 0.23 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.81 | 0.91 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.20 | 0.36 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.15 | 0.15 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 1432.88 | 22.07 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 16.84 | 41.57 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 44.93 | 57.65 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260905T060452Z.json) | yes | 4.43 | 4.65 | 100% | 75.00 | 0.00 | pass |
