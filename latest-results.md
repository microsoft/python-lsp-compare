# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261003T060754Z.json`

- Generated at: 20261003T060754Z
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
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 6 | 4971.80 | 4.11 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | no | 8 | 16895.41 | 36.91 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 6 | 37606.04 | 72.15 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 6 | 213483.70 | 350.45 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 488.31 | 3.98 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 1286.10 | 28.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 4542.54 | 77.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 7407.31 | 80.58 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 1.67 | 1.75 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 6.06 | 9.46 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 63.14 | 76.46 | 100% | 188.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 93.39 | 361.77 | 100% | 250.00 | +49.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.31 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 1.18 | 1.39 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 5.68 | 5.89 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 173.51 | 173.92 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.45 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 1.03 | 1.05 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 3.52 | 5.33 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 4.37 | 4.53 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 12.06 | 12.85 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 34.20 | 80.87 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 353.25 | 477.16 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 4.48 | 5.90 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.64 | 5.76 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 28.98 | 30.65 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 160.85 | 162.35 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 251.88 | 2.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 295.08 | 4.64 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 1432.37 | 13.52 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 7327.94 | 164.71 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 4.67 | 7.06 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 4.70 | 7.56 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 15.72 | 59.95 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 185.61 | 421.69 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.24 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.36 | 0.45 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.54 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 150.93 | 154.21 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.36 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.38 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 1.32 | 1.52 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 2.05 | 2.08 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 4.51 | 4.60 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 24.76 | 27.07 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 245.96 | 276.18 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 3.08 | 3.09 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 4.69 | 11.27 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 37.24 | 44.40 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 239.74 | 241.26 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 824.04 | 7.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 1269.66 | 29.83 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 7413.72 | 129.48 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 10963.44 | 178.76 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 18.01 | 21.49 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 64.44 | 103.81 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 75.35 | 251.85 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 85.52 | 341.17 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.27 | 0.29 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.66 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 2.36 | 2.54 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 185.54 | 187.65 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.30 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.39 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 15.65 | 16.91 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 45.25 | 68.33 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 217.05 | 220.33 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 803.25 | 1229.44 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 4.40 | 4.42 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 14.16 | 17.39 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 15.73 | 16.74 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 179.31 | 184.87 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 378.37 | 2.97 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 883.51 | 19.77 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 3809.92 | 51.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 6742.68 | 92.77 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 3.47 | 7.99 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 14.15 | 25.83 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 70.87 | 153.69 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 87.53 | 349.20 | 100% | 15.00 | +14.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.40 | 0.43 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 2.53 | 3.43 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 3.34 | 7.85 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 316.16 | 318.09 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.22 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.47 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 1.23 | 1.50 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 1.35 | 3.25 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.63 | 6.14 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 7.83 | 18.69 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 37.10 | 37.63 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 136.28 | 172.85 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.50 | 0.52 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.11 | 5.14 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 38.50 | 39.41 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 101.15 | 114.34 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 2681.81 | 4.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 15318.87 | 102.27 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 5262.71 | 165.82 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 180062.01 | 1549.30 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 10.88 | 12.28 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 50.96 | 89.80 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 141.88 | 144.19 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 813.71 | 3253.91 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.44 | 0.49 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.61 | 1.72 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 2744.67 | 2770.38 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.22 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.45 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 2215.58 | 2268.24 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 2.48 | 2.59 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.93 | 6.04 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 7.52 | 10.71 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 14.44 | 34.05 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.51 | 0.55 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.74 | 5.80 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 451.98 | 480.79 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | no | 2641.89 | 2678.81 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 347.39 | 2.80 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 1538.91 | 9.12 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 889.92 | 13.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 4530.05 | 85.87 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 5.27 | 8.89 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 5.82 | 8.85 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 58.73 | 183.29 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 59.59 | 100.10 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.59 | 0.70 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 5.15 | 17.99 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 45.70 | 66.31 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.32 | 0.37 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 0.59 | 0.67 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 0.82 | 0.89 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 12.60 | 24.38 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.55 | 0.58 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 4.35 | 6.24 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 4.41 | 4.45 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 85.32 | 88.32 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 1.47 | 1.47 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261003T060754Z.json) | yes | 2.95 | 3.01 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261003T060754Z.json) | yes | 34.57 | 39.37 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261003T060754Z.json) | yes | 226.12 | 227.52 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | no | 215.54 | 0.31 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.95 | 0.97 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 0.23 | 0.23 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 6792.90 | 67.72 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 15.63 | 20.40 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 129.54 | 148.32 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261003T060754Z.json) | yes | 57.98 | 60.56 | 100% | 75.00 | 0.00 | pass |
