# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260815T060439Z.json`

- Generated at: 20260815T060439Z
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
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 6 | 3223.00 | 2.93 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | no | 8 | 7695.68 | 16.96 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 6 | 31642.00 | 54.19 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 6 | 170092.38 | 257.99 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 500.00 | 2.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 625.12 | 9.30 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 3518.18 | 58.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 6671.37 | 75.04 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 1.79 | 1.99 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 6.52 | 10.13 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 28.64 | 111.78 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 75.45 | 146.94 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.26 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 1.41 | 2.13 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2.00 | 2.30 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 151.59 | 154.61 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 0.76 | 0.80 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 3.76 | 4.09 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 7.88 | 9.78 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 13.48 | 16.25 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 259.44 | 364.49 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2.23 | 3.06 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.71 | 2.95 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 24.83 | 28.81 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 143.64 | 145.04 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 216.03 | 1.86 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 262.87 | 4.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 1260.22 | 12.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 6342.13 | 138.30 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 3.72 | 6.08 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 4.87 | 6.88 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 16.85 | 66.50 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 152.30 | 448.58 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.16 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.46 | 0.52 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.74 | 2.44 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 137.30 | 145.70 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.35 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 0.77 | 0.80 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 1.06 | 2.52 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.69 | 3.03 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 3.50 | 6.45 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 22.83 | 26.02 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 198.31 | 228.03 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.62 | 0.66 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 1.43 | 1.47 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 35.41 | 40.26 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 202.80 | 205.92 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 725.22 | 6.34 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 601.31 | 10.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 7708.82 | 90.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 6654.25 | 112.04 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 17.46 | 20.55 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 34.45 | 136.74 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 47.48 | 60.03 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 63.74 | 214.21 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.22 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.67 | 0.73 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2.37 | 2.50 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 165.24 | 166.99 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 0.76 | 0.82 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 11.70 | 12.41 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 13.19 | 20.37 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 184.77 | 187.63 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 382.30 | 890.96 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.81 | 0.83 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.19 | 2.26 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 7.74 | 9.47 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 161.96 | 169.31 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 295.50 | 1.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 731.50 | 14.98 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 2943.40 | 41.36 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 6831.01 | 97.65 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 3.40 | 7.60 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 6.52 | 10.85 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 60.21 | 235.68 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 150.71 | 317.68 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.31 | 0.38 | 100% | 10628.00 | +56.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.95 | 1.03 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 1.15 | 1.31 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 276.61 | 292.05 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.15 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.38 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 0.93 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 1.81 | 1.98 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 4.07 | 14.30 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 29.63 | 30.27 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 121.59 | 155.42 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 1.62 | 1.76 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 9.52 | 16.21 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 30.35 | 31.60 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 77.17 | 94.83 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 1210.52 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2335.02 | 49.60 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 14973.27 | 113.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 139393.58 | 1042.55 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 10.93 | 12.11 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 49.15 | 76.72 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 123.44 | 126.58 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 233.73 | 934.25 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.18 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.27 | 0.55 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.51 | 0.67 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 1874.40 | 1977.60 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.25 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.68 | 1.15 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 1419.07 | 1478.33 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 2.17 | 2.26 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.80 | 2.99 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 5.99 | 7.67 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 8.54 | 15.37 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.55 | 2.61 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 5.37 | 10.60 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 512.46 | 553.76 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | no | 1793.69 | 1834.07 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 275.73 | 2.01 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 1238.11 | 7.98 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 565.83 | 9.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 4200.04 | 82.35 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 4.18 | 7.25 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 6.00 | 9.06 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 38.12 | 129.89 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 49.76 | 79.41 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.53 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2.60 | 9.16 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 54.00 | 109.41 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.36 | 0.52 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.47 | 0.54 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 0.80 | 1.06 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 46.68 | 74.73 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 2.51 | 2.70 | 100% | 225.00 | +20.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 3.25 | 4.11 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 4.20 | 5.79 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 67.43 | 70.23 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260815T060439Z.json) | yes | 0.91 | 0.95 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 1.42 | 1.44 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260815T060439Z.json) | yes | 30.17 | 33.48 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260815T060439Z.json) | yes | 193.87 | 198.67 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | no | 170.97 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 1.23 | 2.65 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.18 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.15 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 2403.06 | 68.10 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 21.77 | 35.41 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 128.04 | 136.47 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260815T060439Z.json) | yes | 54.48 | 61.52 | 100% | 75.00 | 0.00 | pass |
