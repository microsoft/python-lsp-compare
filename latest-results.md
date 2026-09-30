# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260930T060542Z.json`

- Generated at: 20260930T060542Z
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
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 6 | 4078.73 | 3.35 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | no | 8 | 11984.60 | 26.44 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 6 | 28396.97 | 46.61 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 6 | 161201.93 | 281.12 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 384.82 | 2.99 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 842.80 | 17.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 3304.93 | 52.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 6030.06 | 86.74 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 1.27 | 1.37 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 4.64 | 8.35 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 66.52 | 259.58 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 153.20 | 390.72 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.21 | 0.22 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.92 | 1.30 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 1.73 | 1.92 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 142.76 | 143.67 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.16 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.29 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 0.77 | 0.80 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 2.96 | 3.11 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 9.23 | 10.46 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 18.13 | 24.35 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 231.84 | 353.98 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.24 | 3.09 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 4.14 | 4.17 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 22.31 | 25.48 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 134.02 | 136.03 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 205.35 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 247.14 | 4.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 1102.41 | 10.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 5831.17 | 131.04 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 3.67 | 6.04 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 3.71 | 5.76 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 14.19 | 47.38 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 153.41 | 477.02 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.14 | 0.17 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.40 | 0.45 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 3.53 | 5.49 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 125.84 | 128.85 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.29 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 0.77 | 0.80 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.06 | 4.22 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 3.65 | 3.90 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 19.21 | 20.78 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 184.84 | 224.60 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 1.10 | 3.05 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 2.38 | 2.41 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 29.08 | 34.84 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 190.32 | 195.35 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 678.02 | 6.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 1023.89 | 27.14 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 7042.04 | 83.41 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 6097.87 | 102.85 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 14.21 | 17.01 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 42.41 | 57.98 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 66.25 | 220.28 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 74.00 | 295.35 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.18 | 0.20 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.55 | 0.61 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 3.91 | 5.72 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 155.48 | 158.20 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.27 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 0.73 | 0.78 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 3.53 | 5.34 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 14.52 | 15.65 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 27.44 | 44.67 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 170.57 | 177.04 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 341.73 | 778.90 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 3.37 | 3.41 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 8.22 | 10.26 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 26.84 | 75.84 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 145.03 | 147.57 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 299.40 | 2.24 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 682.08 | 14.20 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 2865.11 | 39.18 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 5604.81 | 91.01 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 2.64 | 5.98 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 5.24 | 9.16 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 64.73 | 258.31 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 148.43 | 397.71 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.30 | 0.33 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.75 | 0.77 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.86 | 0.98 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 248.59 | 257.96 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.14 | 0.15 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 0.83 | 0.95 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.81 | 2.89 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 4.25 | 4.81 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 28.28 | 28.92 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 114.41 | 171.84 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.56 | 3.48 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 3.85 | 3.89 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 28.90 | 29.05 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 75.07 | 80.82 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 2229.32 | 4.08 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 12874.15 | 87.61 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 4166.56 | 130.98 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 133992.30 | 1210.62 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 9.58 | 10.16 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 46.34 | 71.00 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 108.27 | 114.03 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 646.66 | 2586.03 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.14 | 0.14 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.37 | 0.42 | 100% | 34.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.38 | 1.03 | 100% | 7.00 | -27.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 2131.40 | 2191.37 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.19 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.32 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 1721.67 | 1777.96 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.31 | 0.34 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 1.99 | 2.14 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 4.59 | 5.02 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 5.57 | 6.51 | 100% | 23.00 | +23.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 4.70 | 4.76 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 7.63 | 10.42 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 386.40 | 393.51 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | no | 2089.76 | 2152.90 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 281.82 | 2.31 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 1208.33 | 6.93 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 669.77 | 10.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 3645.72 | 64.47 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 3.51 | 6.20 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 5.03 | 7.16 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 41.26 | 132.13 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 42.41 | 68.23 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.14 | 0.16 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.39 | 0.45 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 5.12 | 18.33 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 13.73 | 34.87 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.23 | 0.25 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 0.44 | 0.55 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 0.58 | 0.71 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 11.30 | 27.94 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.30 | 3.75 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 3.60 | 3.85 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 3.62 | 4.58 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 62.18 | 65.23 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260930T060542Z.json) | yes | 2.35 | 2.56 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 2.35 | 4.27 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20260930T060542Z.json) | yes | 26.55 | 30.56 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260930T060542Z.json) | yes | 192.72 | 223.43 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | no | 177.63 | 0.21 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.70 | 0.78 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.12 | 0.12 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 4174.74 | 19.87 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 10.13 | 17.62 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 44.35 | 48.91 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260930T060542Z.json) | yes | 5.13 | 5.28 | 100% | 75.00 | 0.00 | pass |
