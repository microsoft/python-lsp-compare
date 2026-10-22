# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261022T060527Z.json`

- Generated at: 20261022T060527Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.90 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.90/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.4.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 6 | 2310.55 | 2.69 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | no | 8 | 3966.67 | 3.66 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 6 | 22767.67 | 31.54 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 6 | 170355.70 | 232.50 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 396.70 | 2.68 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 337.70 | 2.81 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 2738.49 | 41.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 4878.58 | 63.45 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 1.07 | 1.31 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 1.09 | 2.38 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 3.60 | 5.39 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 86.29 | 215.40 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.16 | 0.20 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.97 | 1.48 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 1.39 | 1.55 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 117.20 | 118.56 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.21 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 0.61 | 0.66 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 2.45 | 2.71 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 9.36 | 12.38 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 9.92 | 16.32 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 182.75 | 290.94 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.90 | 1.93 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.39 | 3.45 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 17.48 | 17.72 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 110.71 | 112.49 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 160.46 | 1.02 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 172.79 | 1.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 971.22 | 10.05 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 4757.79 | 102.96 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.66 | 2.22 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 2.80 | 4.19 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 3.12 | 4.78 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 105.24 | 245.49 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.11 | 0.13 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.12 | 0.14 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.39 | 0.43 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 102.44 | 103.33 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 0.63 | 0.66 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.09 | 3.69 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 3.43 | 7.03 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 17.66 | 19.89 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 149.92 | 190.77 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.77 | 2.06 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 2.01 | 2.05 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 28.82 | 34.83 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 156.57 | 160.06 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 487.02 | 5.11 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 566.39 | 5.22 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 5195.32 | 42.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 4769.42 | 82.24 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 3.46 | 5.03 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 10.90 | 12.95 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 36.34 | 51.28 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 48.93 | 164.01 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.14 | 0.18 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.61 | 0.80 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 3.33 | 4.66 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 125.14 | 126.14 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.27 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 0.91 | 1.71 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 2.34 | 2.96 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 10.63 | 16.62 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 12.16 | 13.00 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 130.95 | 131.96 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 159.56 | 186.00 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 2.83 | 2.88 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 5.15 | 5.88 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 5.76 | 10.10 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 117.84 | 118.69 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 329.55 | 1.66 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 261.27 | 1.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 2484.30 | 36.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 4253.45 | 59.22 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 2.13 | 5.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 3.46 | 5.19 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 12.34 | 13.85 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 49.97 | 111.01 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.20 | 0.23 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.63 | 0.74 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 1.64 | 2.88 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 200.40 | 202.38 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.27 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 0.61 | 0.64 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 1.73 | 4.15 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.62 | 4.39 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 23.25 | 24.27 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 98.85 | 126.82 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 2.35 | 6.24 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.13 | 3.25 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 21.86 | 22.03 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 67.05 | 75.80 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 818.70 | 2.57 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 734.72 | 2.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 10368.33 | 53.10 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 149302.95 | 1042.39 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 5.06 | 19.70 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 7.02 | 8.24 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 41.99 | 61.11 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 81.36 | 88.72 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.11 | 0.12 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.31 | 0.36 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 1932.27 | 1995.05 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.14 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.33 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 1471.20 | 1530.85 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 1.64 | 1.80 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.07 | 3.57 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 4.03 | 4.96 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 7.28 | 15.50 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.30 | 0.36 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 2.74 | 2.76 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 218.84 | 234.28 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | no | 1725.47 | 1748.83 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 237.67 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 458.57 | 3.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 1010.00 | 6.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 2393.51 | 44.73 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 3.03 | 5.42 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.57 | 5.29 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 13.53 | 25.88 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 28.89 | 50.31 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 0.11 | 0.14 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.13 | 0.23 | 100% | 167.00 | +141.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.35 | 0.40 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 4.17 | 4.34 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.17 | 0.20 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 0.55 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 1.02 | 1.19 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 1.16 | 1.25 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.43 | 0.47 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 3.33 | 3.92 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 3.53 | 4.61 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 49.03 | 55.26 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 1.34 | 2.53 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261022T060527Z.json) | yes | 1.97 | 2.04 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261022T060527Z.json) | yes | 23.19 | 27.55 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261022T060527Z.json) | yes | 140.38 | 141.06 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | no | 135.07 | 0.15 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.51 | 0.60 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.09 | 0.11 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.10 | 0.10 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 1180.59 | 22.75 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 7.00 | 10.63 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 57.45 | 84.93 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261022T060527Z.json) | yes | 3.80 | 3.97 | 100% | 75.00 | 0.00 | pass |
