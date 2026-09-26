# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260926T060531Z.json`

- Generated at: 20260926T060531Z
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
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 6 | 4065.46 | 3.35 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | no | 8 | 12524.01 | 28.00 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 6 | 29443.84 | 49.42 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 6 | 159910.95 | 281.49 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 425.71 | 3.80 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 839.22 | 15.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 3699.08 | 60.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 5884.32 | 84.97 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 1.34 | 1.56 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 5.54 | 9.84 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 67.14 | 254.30 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 145.98 | 351.17 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.23 | 0.24 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.87 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.80 | 2.04 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 142.53 | 144.38 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.33 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 0.78 | 0.81 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 3.11 | 3.31 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 8.81 | 10.47 | 100% | 149.00 | -19.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 12.33 | 13.34 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 269.22 | 399.02 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.61 | 2.55 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 4.99 | 5.16 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 25.15 | 29.69 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 132.42 | 133.95 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 209.70 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 214.25 | 2.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 1141.11 | 11.06 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 5829.22 | 129.86 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 3.73 | 5.80 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 3.75 | 5.79 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 11.79 | 45.89 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 149.01 | 452.79 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.17 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.21 | 0.25 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.39 | 0.42 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 125.17 | 126.02 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.13 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 0.78 | 0.81 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.39 | 1.50 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 3.65 | 4.06 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 19.49 | 20.63 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 183.95 | 217.58 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.20 | 3.32 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 2.42 | 2.51 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 31.43 | 37.15 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 190.42 | 192.90 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 669.71 | 6.19 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 846.75 | 19.64 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 7387.63 | 86.14 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 6108.94 | 104.43 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 13.75 | 16.72 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 43.45 | 55.75 | 100% | 6.00 | -265.20 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 62.71 | 250.20 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 66.22 | 223.18 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.18 | 0.21 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.63 | 0.81 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.72 | 1.83 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 153.23 | 157.33 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.13 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.30 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 0.75 | 0.80 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 13.47 | 14.90 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 31.26 | 49.99 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 177.02 | 193.31 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 354.89 | 823.83 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 2.33 | 8.06 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 3.42 | 3.49 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 8.65 | 9.91 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 147.68 | 149.59 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 295.14 | 2.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 664.28 | 14.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 2932.35 | 39.21 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 5799.35 | 91.02 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 2.71 | 6.48 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 12.30 | 22.46 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 66.32 | 264.68 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 152.31 | 283.26 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.29 | 0.32 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.75 | 0.77 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 1.41 | 1.80 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 245.69 | 250.24 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.14 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.67 | 1.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 0.86 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.58 | 0.60 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 4.11 | 4.36 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 28.76 | 30.43 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 104.08 | 131.24 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 3.12 | 7.03 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 3.81 | 3.87 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 27.47 | 27.85 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 77.59 | 82.41 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 2192.82 | 3.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 13076.17 | 92.78 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 4090.89 | 127.38 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 132528.61 | 1205.75 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 8.60 | 9.60 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 50.54 | 69.48 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 109.56 | 111.70 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 627.50 | 2509.34 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.14 | 0.15 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.22 | 0.45 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.35 | 0.43 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 2126.26 | 2186.45 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.14 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.33 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 1725.39 | 1767.49 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.36 | 0.39 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 1.98 | 2.05 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 4.91 | 5.01 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 5.16 | 5.86 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 4.66 | 4.81 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 8.76 | 23.55 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 407.55 | 430.49 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | no | 2065.58 | 2115.60 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 272.38 | 2.17 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 1207.50 | 7.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 664.02 | 9.97 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 3760.51 | 72.92 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 4.53 | 6.90 | 100% | 467.00 | +453.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 4.74 | 8.29 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 41.38 | 133.83 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 46.60 | 69.66 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.39 | 0.44 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 4.73 | 16.75 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 36.17 | 64.27 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.23 | 0.25 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 0.42 | 0.48 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 0.62 | 0.78 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 29.26 | 95.67 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.65 | 3.58 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 3.47 | 3.55 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 3.51 | 4.41 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 67.29 | 68.89 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 1.86 | 3.90 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260926T060531Z.json) | yes | 2.27 | 2.30 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20260926T060531Z.json) | yes | 26.40 | 29.41 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260926T060531Z.json) | yes | 185.26 | 188.34 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | no | 175.13 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.72 | 0.77 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.14 | 0.16 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 5029.46 | 65.35 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 17.32 | 34.98 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 118.64 | 130.44 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260926T060531Z.json) | yes | 60.09 | 72.95 | 100% | 75.00 | 0.00 | pass |
