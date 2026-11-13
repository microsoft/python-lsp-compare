# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261113T060330Z.json`

- Generated at: 20261113T060330Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.102 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.102/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.4.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 6 | 3923.98 | 4.67 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | no | 8 | 7170.34 | 6.78 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 6 | 42687.41 | 85.93 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 6 | 263820.71 | 375.89 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 719.49 | 4.38 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 580.14 | 5.46 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 4922.15 | 84.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 8032.84 | 111.63 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 2.24 | 2.58 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.70 | 7.81 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 6.52 | 12.25 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 187.11 | 397.90 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.31 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 1.18 | 1.53 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 4.12 | 5.40 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 188.28 | 191.46 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.19 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.48 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 1.06 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 4.59 | 4.71 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 12.96 | 16.32 | 100% | 168.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 17.64 | 19.49 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 382.50 | 500.36 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 1.93 | 3.07 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 6.92 | 7.64 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 34.05 | 35.03 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 177.11 | 181.97 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 274.21 | 1.92 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 280.12 | 2.65 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 1507.69 | 15.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 7956.37 | 174.54 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 3.66 | 6.21 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 5.04 | 8.46 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 5.65 | 8.82 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 201.30 | 587.77 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.23 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.55 | 0.59 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.64 | 1.76 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 158.14 | 159.06 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.23 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 3.75 | 5.41 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 5.00 | 5.50 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 27.01 | 29.43 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 263.12 | 314.21 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 1.30 | 3.32 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 2.21 | 2.34 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 43.52 | 50.87 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 249.08 | 253.84 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 818.87 | 8.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 820.85 | 12.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 8297.43 | 155.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 13020.49 | 229.41 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 4.16 | 8.04 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 19.20 | 23.03 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 84.99 | 283.21 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 133.39 | 358.70 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.26 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.84 | 0.96 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 4.60 | 8.02 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 197.62 | 202.46 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.41 | 0.61 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 1.04 | 1.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.33 | 2.93 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 18.12 | 18.62 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 27.67 | 41.37 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 247.70 | 251.57 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 1048.79 | 1412.71 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 4.15 | 4.58 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 12.02 | 16.19 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 21.99 | 56.25 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 196.05 | 203.38 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 406.37 | 3.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 621.50 | 3.74 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 4037.10 | 55.45 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 7433.28 | 104.44 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 3.88 | 6.92 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 4.02 | 9.62 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 17.96 | 24.76 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 97.98 | 201.12 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.39 | 0.40 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 1.78 | 2.03 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.84 | 5.74 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 336.34 | 342.89 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.20 | 0.21 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.52 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 1.26 | 1.52 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.72 | 2.97 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 6.18 | 7.06 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 8.63 | 23.66 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 42.57 | 44.08 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 144.86 | 186.85 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.63 | 0.68 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 4.73 | 4.81 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 44.05 | 45.12 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 112.12 | 125.25 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 1417.32 | 4.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 1613.59 | 4.77 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 17581.96 | 120.62 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 227174.99 | 1603.00 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 7.87 | 30.60 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 13.00 | 15.46 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 50.27 | 82.53 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 146.66 | 160.71 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.22 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.46 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 3036.89 | 3113.02 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.43 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 2212.28 | 2309.86 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 2.85 | 3.08 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 4.42 | 4.79 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 7.43 | 8.57 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 10.77 | 35.25 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 3.71 | 3.90 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 4.80 | 7.06 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 544.49 | 565.26 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | no | 2616.30 | 2663.35 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 421.17 | 4.10 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 728.35 | 5.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 1618.03 | 9.87 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 4925.80 | 106.56 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 4.90 | 8.56 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 9.18 | 11.98 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 15.72 | 29.65 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 81.84 | 155.74 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.58 | 0.66 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.90 | 10.97 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 110.39 | 250.35 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.31 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 0.79 | 0.94 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 1.47 | 1.63 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 3.69 | 4.50 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2.89 | 4.74 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 6.12 | 6.71 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 6.27 | 6.72 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 95.85 | 99.09 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261113T060330Z.json) | yes | 3.36 | 3.55 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 4.64 | 4.74 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261113T060330Z.json) | yes | 36.95 | 45.81 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261113T060330Z.json) | yes | 241.00 | 249.38 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | no | 237.13 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.92 | 0.95 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.19 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.22 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 2155.23 | 38.12 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 18.99 | 27.82 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 88.08 | 123.02 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261113T060330Z.json) | yes | 7.29 | 7.39 | 100% | 75.00 | 0.00 | pass |
