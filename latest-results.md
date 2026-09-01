# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260901T060553Z.json`

- Generated at: 20260901T060553Z
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
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 6 | 4927.98 | 4.04 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | no | 8 | 7457.37 | 14.48 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 6 | 35078.76 | 60.31 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 6 | 204499.11 | 361.70 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 487.78 | 3.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 784.19 | 11.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 3939.23 | 64.58 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 7368.79 | 107.75 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 1.65 | 1.82 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 6.20 | 9.53 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 33.40 | 122.70 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 179.78 | 382.55 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.29 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 1.07 | 1.32 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 11.71 | 38.78 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 182.97 | 183.77 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.35 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 0.94 | 0.99 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 4.33 | 4.43 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 8.59 | 8.78 | 100% | 149.00 | -19.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 11.21 | 12.96 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 283.81 | 388.55 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 3.73 | 5.30 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 5.56 | 6.49 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 31.49 | 35.05 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 170.76 | 175.09 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 246.46 | 2.43 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 278.55 | 4.70 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 1361.02 | 13.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 7429.15 | 168.04 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 3.82 | 6.55 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 4.79 | 7.29 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 21.17 | 74.78 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 201.49 | 600.35 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.19 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.23 | 0.27 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.52 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 159.86 | 161.58 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 1.01 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 1.34 | 2.36 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 4.26 | 4.47 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 22.95 | 25.21 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 236.56 | 277.58 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.60 | 0.62 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 2.76 | 2.78 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 37.74 | 41.84 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 241.28 | 243.64 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 842.47 | 8.15 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 651.95 | 12.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 8523.39 | 99.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 7652.79 | 134.34 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 18.47 | 21.95 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 37.70 | 148.33 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 65.97 | 118.31 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 68.68 | 229.77 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.24 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.60 | 0.69 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 2.51 | 2.84 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 195.05 | 196.60 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 17.48 | 18.31 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 19.33 | 33.73 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 217.80 | 221.91 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 417.19 | 984.27 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.59 | 0.62 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 4.38 | 4.46 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 9.26 | 10.55 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 191.87 | 202.46 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 354.37 | 2.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 727.40 | 14.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 3266.94 | 43.73 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 6693.16 | 116.06 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 3.48 | 8.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 7.41 | 12.53 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 64.51 | 252.80 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 190.16 | 496.14 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.37 | 0.41 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.98 | 1.02 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 1.19 | 1.41 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 318.52 | 326.65 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.19 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.30 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.42 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 1.18 | 1.44 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.89 | 1.64 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 4.24 | 4.68 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 35.20 | 35.61 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 128.19 | 159.62 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 3.92 | 4.00 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 4.74 | 9.12 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 35.23 | 35.53 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 81.44 | 94.94 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 2673.97 | 4.76 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 2400.76 | 50.23 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 16570.68 | 132.65 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 170699.99 | 1541.30 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 11.17 | 12.06 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 56.65 | 84.61 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 129.04 | 130.09 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 242.92 | 970.91 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.18 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.42 | 0.46 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.53 | 1.53 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 2734.08 | 2804.78 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.89 | 2.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 2227.37 | 2349.55 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.39 | 0.42 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 2.55 | 2.64 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 5.35 | 5.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 6.09 | 6.42 | 100% | 23.00 | +23.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 5.76 | 5.80 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 7.46 | 19.41 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 599.94 | 624.02 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | no | 2613.47 | 2641.64 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 322.94 | 2.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 1417.51 | 8.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 726.22 | 9.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 4655.22 | 102.68 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 4.84 | 8.91 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 5.79 | 8.65 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 40.68 | 145.18 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 67.98 | 95.31 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.54 | 0.64 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 2.74 | 9.26 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 130.44 | 276.89 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.35 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 0.54 | 0.63 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 0.82 | 0.88 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 4.21 | 5.22 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.54 | 0.56 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 4.41 | 4.89 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 4.85 | 6.60 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 79.72 | 81.90 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260901T060553Z.json) | yes | 2.54 | 2.60 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 2.64 | 4.38 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260901T060553Z.json) | yes | 31.86 | 37.24 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260901T060553Z.json) | yes | 231.08 | 232.19 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | no | 191.87 | 0.25 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.87 | 0.99 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 1696.43 | 26.87 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 20.99 | 39.72 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 53.41 | 53.75 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260901T060553Z.json) | yes | 6.22 | 6.55 | 100% | 75.00 | 0.00 | pass |
