# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261008T060553Z.json`

- Generated at: 20261008T060553Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.85 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.85/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 6 | 3596.21 | 4.30 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | no | 8 | 16610.02 | 37.00 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 6 | 38539.97 | 74.25 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 6 | 218818.78 | 361.23 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 539.47 | 4.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 1296.48 | 25.33 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 4780.36 | 81.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 7628.56 | 100.84 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 1.79 | 2.03 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 6.24 | 11.47 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 90.68 | 353.17 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 157.61 | 304.65 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.32 | 0.34 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 1.14 | 1.38 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 1.99 | 2.22 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 176.68 | 177.53 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 4.64 | 4.84 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 14.21 | 15.43 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 28.70 | 71.96 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 365.71 | 487.16 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 5.06 | 5.93 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 5.81 | 5.88 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 34.29 | 40.29 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 164.23 | 165.59 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 263.93 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 259.90 | 3.73 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 1522.82 | 14.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 7452.01 | 167.55 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.51 | 6.73 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 4.76 | 7.67 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 15.65 | 61.65 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 190.13 | 396.97 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.25 | 0.27 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.28 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.53 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 153.05 | 153.64 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.37 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 1.82 | 1.87 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.87 | 5.27 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 26.34 | 30.03 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 251.29 | 281.78 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.67 | 0.69 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 3.29 | 3.34 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 39.25 | 44.71 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 242.21 | 245.28 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 877.72 | 8.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 1260.49 | 30.66 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 7575.59 | 136.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 11020.97 | 177.80 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 17.62 | 20.98 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 76.43 | 259.02 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 80.94 | 319.12 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 81.03 | 155.66 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.27 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.65 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 5.25 | 8.24 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 190.99 | 191.67 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.43 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 3.52 | 5.33 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 20.67 | 24.36 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 50.20 | 68.14 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 224.31 | 226.60 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 800.54 | 1248.56 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.65 | 4.73 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 10.96 | 12.17 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 13.39 | 19.40 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 183.87 | 192.38 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 385.35 | 2.94 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 927.45 | 21.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 3904.28 | 52.16 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 6818.95 | 93.28 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 3.12 | 7.51 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 14.91 | 26.89 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 74.07 | 159.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 91.28 | 362.27 | 100% | 15.00 | +14.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.43 | 0.46 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 2.64 | 3.99 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 3.23 | 8.21 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 315.81 | 317.52 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.23 | 0.24 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.61 | 1.67 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.84 | 2.04 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 1.14 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.79 | 0.82 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 5.61 | 6.26 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 38.05 | 38.55 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 139.50 | 172.70 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 5.32 | 5.49 | 100% | 951.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 10.68 | 27.43 | 100% | 2242.00 | +1349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 37.31 | 37.51 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 102.29 | 126.38 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 1174.88 | 4.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 15747.44 | 110.31 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 5323.38 | 167.91 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 184633.32 | 1570.90 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 10.87 | 12.98 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 48.95 | 83.45 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 153.54 | 157.70 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 826.22 | 3304.01 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.22 | 0.24 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.51 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.66 | 1.94 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 2779.18 | 2818.94 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.48 | 0.56 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 2235.77 | 2310.99 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 2.73 | 2.90 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.75 | 5.05 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 6.24 | 6.97 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 6.81 | 17.11 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.48 | 4.50 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 6.07 | 14.89 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 495.35 | 518.28 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | no | 2683.27 | 2707.18 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 354.88 | 2.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 1564.10 | 9.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 972.90 | 15.61 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 4710.35 | 98.54 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 4.68 | 8.65 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 5.88 | 8.65 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 64.01 | 216.64 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 67.38 | 109.08 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.56 | 0.66 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 6.29 | 22.36 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 50.04 | 69.97 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.33 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 0.60 | 0.71 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 0.77 | 0.92 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 52.35 | 98.90 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 3.68 | 4.58 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 4.56 | 4.82 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 4.87 | 6.32 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 89.83 | 92.37 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261008T060553Z.json) | yes | 3.00 | 3.03 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 3.75 | 5.64 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261008T060553Z.json) | yes | 36.19 | 41.48 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261008T060553Z.json) | yes | 233.07 | 234.86 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 487.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | no | 218.38 | 0.42 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 1.79 | 4.33 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.24 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 6351.04 | 63.84 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 17.60 | 25.89 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 146.29 | 167.65 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261008T060553Z.json) | yes | 27.64 | 32.67 | 100% | 75.00 | 0.00 | pass |
