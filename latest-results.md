# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261020T060523Z.json`

- Generated at: 20261020T060523Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.89 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.89/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 6 | 3479.69 | 4.15 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | no | 8 | 6983.32 | 9.13 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 6 | 38068.09 | 72.67 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 6 | 243987.82 | 368.02 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 511.00 | 4.35 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 721.61 | 6.96 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 4467.97 | 73.23 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 7790.70 | 106.99 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 1.63 | 1.81 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 5.02 | 7.15 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 6.16 | 11.32 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 185.67 | 370.07 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.30 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 1.13 | 1.35 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 4.87 | 6.60 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 178.79 | 181.79 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.38 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 1.08 | 1.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 1.18 | 2.71 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 4.26 | 4.41 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 13.75 | 15.58 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 21.57 | 44.54 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 327.20 | 449.57 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 2.15 | 2.19 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 5.87 | 5.97 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 31.27 | 37.01 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 165.17 | 166.78 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 242.38 | 1.18 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 260.89 | 2.59 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 1455.81 | 13.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 7473.27 | 166.70 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 1.46 | 4.75 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.40 | 6.93 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 4.74 | 7.90 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 187.24 | 399.27 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.28 | 0.29 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.55 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 155.73 | 158.21 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.25 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.36 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 1.12 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 3.29 | 5.12 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.87 | 5.09 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 25.70 | 28.01 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 247.20 | 278.42 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.62 | 0.66 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 3.26 | 3.28 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 38.14 | 44.38 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 242.21 | 243.60 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 632.51 | 7.79 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 851.02 | 8.20 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 7473.14 | 132.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 11275.01 | 182.85 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 3.29 | 6.37 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 17.75 | 20.73 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 68.47 | 94.30 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 77.81 | 261.19 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.27 | 0.32 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.65 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 3.03 | 4.68 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 188.78 | 191.30 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.39 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 1.11 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 18.25 | 23.10 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 26.16 | 32.64 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 224.26 | 233.07 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 825.04 | 1313.95 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.54 | 4.59 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 6.28 | 15.46 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 10.35 | 11.85 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 180.50 | 182.06 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 373.55 | 2.92 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 535.89 | 3.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 3762.81 | 51.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 7143.16 | 102.04 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 2.92 | 6.74 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 3.01 | 7.01 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 18.79 | 22.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 117.41 | 246.38 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.42 | 0.43 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 1.15 | 2.24 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 1.96 | 2.72 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 317.20 | 320.52 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.23 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.76 | 2.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 1.35 | 1.76 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 5.73 | 6.22 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 7.13 | 12.38 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 37.00 | 37.25 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 138.82 | 176.68 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 4.10 | 5.14 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 5.20 | 5.20 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 37.24 | 37.31 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 97.35 | 112.85 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 1130.00 | 3.98 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 1340.65 | 4.30 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 15567.28 | 105.28 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 209436.73 | 1596.71 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 6.53 | 25.19 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 10.03 | 12.09 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 52.94 | 85.69 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 146.74 | 156.14 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.22 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.49 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 2953.13 | 2985.30 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 1.31 | 2.87 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 2222.67 | 2250.44 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 2.63 | 2.75 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.98 | 6.11 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 7.06 | 15.49 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 7.72 | 10.03 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.46 | 4.58 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 7.45 | 16.36 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 463.93 | 493.77 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | no | 2658.38 | 2671.62 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 353.23 | 2.88 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 656.28 | 3.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 1539.21 | 9.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 4670.82 | 103.06 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 4.96 | 9.42 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 5.75 | 8.19 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 13.42 | 22.56 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 67.02 | 93.85 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.54 | 0.62 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 2.43 | 9.05 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 56.74 | 64.46 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.33 | 0.34 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 0.61 | 0.65 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 0.76 | 0.87 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 70.86 | 113.06 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.73 | 0.73 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 4.75 | 5.02 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 4.91 | 6.46 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 88.11 | 90.50 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 2.05 | 3.83 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261020T060523Z.json) | yes | 3.08 | 3.13 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261020T060523Z.json) | yes | 35.37 | 41.90 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261020T060523Z.json) | yes | 232.56 | 235.20 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | no | 212.11 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.95 | 1.00 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.21 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 2641.90 | 78.52 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 26.53 | 48.90 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 147.03 | 149.65 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261020T060523Z.json) | yes | 62.00 | 68.88 | 100% | 75.00 | 0.00 | pass |
