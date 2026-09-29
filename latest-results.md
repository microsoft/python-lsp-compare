# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260929T060553Z.json`

- Generated at: 20260929T060553Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.84 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.84/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.2 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 6 | 4105.65 | 3.45 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | no | 8 | 11731.81 | 24.66 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 6 | 28362.29 | 47.03 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 6 | 165606.66 | 284.74 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 390.23 | 3.03 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 819.48 | 17.23 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 3302.06 | 51.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 6331.52 | 92.29 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 1.28 | 1.42 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 4.15 | 6.45 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 69.14 | 272.10 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 165.83 | 393.66 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.23 | 0.24 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.94 | 1.33 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 1.82 | 1.94 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 151.47 | 153.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.22 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.31 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 0.77 | 0.82 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 3.39 | 3.54 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 9.33 | 10.83 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 14.51 | 17.24 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 227.49 | 336.93 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.44 | 0.70 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 4.17 | 4.19 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 22.64 | 23.85 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 140.00 | 147.20 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 205.50 | 1.98 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 206.08 | 2.84 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 1137.26 | 11.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 6039.29 | 134.50 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.68 | 5.81 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 3.80 | 6.13 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 11.75 | 45.41 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 162.20 | 508.28 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.16 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.20 | 0.21 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.41 | 0.46 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 128.24 | 128.90 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.13 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.30 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 0.75 | 0.78 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 1.49 | 1.57 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.56 | 3.71 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 20.27 | 21.67 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 189.08 | 228.11 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.61 | 0.63 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 2.40 | 2.41 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 30.20 | 35.72 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 192.22 | 194.27 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 663.86 | 6.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 852.25 | 21.32 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 7157.04 | 86.18 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 6286.28 | 106.88 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 14.11 | 17.17 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 45.97 | 69.02 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 57.90 | 196.85 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 64.19 | 256.12 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.20 | 0.23 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.57 | 0.63 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 4.08 | 7.34 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 157.66 | 159.48 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.33 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 0.80 | 0.82 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 3.53 | 5.36 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 13.32 | 14.49 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 27.39 | 34.46 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 182.54 | 187.66 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 363.89 | 832.46 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.43 | 3.46 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 7.44 | 10.21 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 8.22 | 10.27 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 147.43 | 150.63 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 300.87 | 2.18 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 765.03 | 17.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 2925.76 | 39.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 5987.46 | 92.43 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 2.60 | 6.00 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 15.68 | 20.85 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 64.92 | 259.08 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 153.24 | 420.86 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.30 | 0.31 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 1.55 | 2.11 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 2.92 | 3.44 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 248.87 | 253.96 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.14 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.34 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 0.83 | 0.94 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 2.73 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 4.10 | 4.51 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 9.44 | 23.85 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 29.67 | 30.00 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 107.69 | 134.29 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.79 | 3.84 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 8.34 | 23.59 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 29.53 | 30.42 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 74.33 | 81.44 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 2234.16 | 4.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 12671.18 | 86.95 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 3904.83 | 119.91 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 137062.20 | 1200.13 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 11.06 | 12.12 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 46.54 | 70.06 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 102.33 | 104.37 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 591.03 | 2363.48 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.14 | 0.17 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.38 | 0.46 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 2152.58 | 2240.50 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.33 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 1731.78 | 1781.61 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 2.11 | 2.35 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 2.12 | 7.61 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 5.20 | 6.65 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 6.24 | 8.57 | 100% | 23.00 | +23.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 5.75 | 6.64 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 6.12 | 13.95 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 382.31 | 397.67 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | no | 2011.86 | 2032.58 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 311.04 | 2.57 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 1168.98 | 7.01 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 681.26 | 10.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 3899.92 | 82.22 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 3.61 | 6.61 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 5.27 | 7.37 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 41.28 | 134.26 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 59.36 | 123.69 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.13 | 0.15 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 0.39 | 0.45 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 4.97 | 17.71 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 99.53 | 306.62 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.25 | 0.29 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 0.47 | 0.56 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 1.05 | 2.51 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 3.02 | 4.00 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.42 | 0.44 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.82 | 4.43 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 3.91 | 5.13 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 62.77 | 64.23 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 3.08 | 4.69 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260929T060553Z.json) | yes | 3.14 | 3.61 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20260929T060553Z.json) | yes | 26.10 | 29.43 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260929T060553Z.json) | yes | 186.41 | 188.66 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | no | 177.36 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.74 | 0.78 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.16 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 4325.51 | 21.44 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 9.57 | 18.50 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 45.62 | 47.40 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260929T060553Z.json) | yes | 9.12 | 21.59 | 100% | 75.00 | 0.00 | pass |
