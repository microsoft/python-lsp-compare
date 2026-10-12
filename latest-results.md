# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261012T061044Z.json`

- Generated at: 20261012T061044Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.86 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.86/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 6 | 3125.94 | 3.50 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | no | 8 | 14337.30 | 32.40 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 6 | 34990.89 | 65.50 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 6 | 190627.13 | 329.03 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 427.41 | 3.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 1054.86 | 22.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 3925.98 | 62.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 6679.70 | 91.39 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 1.32 | 1.45 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 6.33 | 11.71 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 77.86 | 298.59 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 146.00 | 309.62 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.23 | 0.25 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 1.02 | 1.54 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 2.00 | 2.38 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 162.24 | 167.27 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.36 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 0.88 | 0.91 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 3.38 | 3.54 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 11.56 | 14.64 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 29.56 | 75.85 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 278.50 | 415.39 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 2.65 | 4.55 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.86 | 5.00 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 27.28 | 29.76 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 144.46 | 149.23 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 233.31 | 2.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 293.60 | 3.55 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 1335.06 | 13.23 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 6579.93 | 146.26 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 3.74 | 6.16 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 4.64 | 6.89 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 14.56 | 54.57 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 151.52 | 421.39 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.17 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.20 | 0.25 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.47 | 0.54 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 141.13 | 143.26 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.34 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 0.81 | 0.86 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 2.31 | 4.90 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.17 | 4.51 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 25.22 | 26.54 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 222.27 | 270.27 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.53 | 0.58 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 2.81 | 2.84 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 35.48 | 42.47 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 215.58 | 221.95 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 761.52 | 6.91 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 1070.35 | 27.08 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 6994.16 | 128.47 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 9842.35 | 158.63 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 14.47 | 17.40 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 69.66 | 235.78 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 72.62 | 289.85 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 93.71 | 237.03 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.21 | 0.23 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.56 | 0.61 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 4.66 | 5.90 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 171.04 | 176.02 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.34 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 0.86 | 0.93 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 4.14 | 5.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 15.74 | 16.43 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 47.75 | 96.43 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 208.82 | 217.32 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 713.18 | 1097.66 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 3.97 | 4.02 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 6.23 | 11.37 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 9.43 | 11.17 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 167.92 | 174.23 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 371.88 | 2.45 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 798.20 | 18.15 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 3468.81 | 46.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 6024.83 | 83.35 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 2.65 | 6.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 18.51 | 20.37 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 68.89 | 274.84 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 72.65 | 155.98 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.34 | 0.37 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 1.71 | 2.31 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 3.30 | 5.00 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 274.49 | 283.09 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.16 | 0.17 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.34 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 0.94 | 1.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 1.06 | 2.55 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.82 | 5.34 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 9.32 | 14.95 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 34.44 | 34.85 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 127.39 | 150.57 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.27 | 4.39 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 8.19 | 14.17 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 34.23 | 34.35 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 85.17 | 96.96 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 1028.00 | 3.45 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 15077.27 | 104.05 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 4490.74 | 140.63 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 160043.34 | 1430.28 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 9.11 | 11.84 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 56.69 | 79.11 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 127.44 | 133.02 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 687.62 | 2749.72 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.15 | 0.16 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.39 | 0.47 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 2574.48 | 2679.15 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 2059.27 | 2120.68 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 2.45 | 2.70 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 2.48 | 8.89 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.04 | 4.16 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 5.98 | 7.52 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 3.74 | 3.84 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 12.75 | 23.88 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 456.82 | 490.84 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | no | 2387.76 | 2418.81 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 303.83 | 2.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 1341.41 | 7.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 800.74 | 13.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 4305.17 | 94.41 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.82 | 6.95 | 100% | 496.00 | +482.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 5.40 | 9.32 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 60.50 | 170.07 | 100% | 394.00 | +380.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 72.58 | 148.04 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.15 | 0.18 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.45 | 0.50 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.84 | 2.89 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 44.60 | 62.66 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.26 | 0.28 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 0.47 | 0.55 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 0.70 | 0.85 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 58.66 | 143.35 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 1.81 | 3.82 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 3.96 | 5.03 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 4.01 | 4.61 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 77.19 | 80.25 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261012T061044Z.json) | yes | 2.47 | 2.49 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 2.85 | 5.19 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261012T061044Z.json) | yes | 28.42 | 32.06 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261012T061044Z.json) | yes | 219.03 | 221.82 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 394.00, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | no | 204.70 | 0.37 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 1.75 | 4.43 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.17 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 5624.11 | 66.61 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 18.44 | 32.77 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 145.75 | 160.38 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261012T061044Z.json) | yes | 35.63 | 54.29 | 100% | 75.00 | 0.00 | pass |
