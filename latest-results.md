# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261029T060415Z.json`

- Generated at: 20261029T060415Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.94 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.94/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 6 | 3724.32 | 3.97 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | no | 8 | 7280.88 | 6.87 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 6 | 37265.51 | 66.15 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 6 | 257363.74 | 345.00 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 555.48 | 4.07 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 787.79 | 6.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 4460.76 | 72.84 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 7990.71 | 99.62 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 1.62 | 2.73 | 100% | 250.00 | +49.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 1.87 | 2.11 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 6.54 | 11.28 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 155.13 | 304.37 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.29 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 1.11 | 1.35 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.31 | 2.57 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 174.85 | 175.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.19 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.19 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.38 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 1.04 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 4.16 | 4.29 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 12.83 | 14.96 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 15.53 | 17.79 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 324.54 | 445.40 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 5.18 | 5.68 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 12.40 | 36.78 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 31.65 | 37.21 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 162.92 | 164.44 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 259.11 | 2.28 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 278.99 | 2.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 1452.06 | 13.61 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 7358.87 | 160.57 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 3.30 | 5.13 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 4.61 | 7.59 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.70 | 7.58 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 165.24 | 453.68 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.20 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.53 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 1.87 | 3.16 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 152.62 | 153.29 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.16 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.39 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.06 | 4.42 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 3.92 | 4.08 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 26.07 | 28.59 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 243.17 | 276.38 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 2.40 | 2.42 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 3.96 | 4.23 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 36.45 | 42.46 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 240.72 | 244.30 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 697.19 | 5.64 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 812.65 | 7.72 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 7466.52 | 127.16 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 10587.76 | 145.93 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.24 | 6.90 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 18.55 | 22.37 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 57.85 | 77.85 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 95.18 | 320.18 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.26 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.70 | 0.86 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.42 | 2.58 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 186.11 | 187.43 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.18 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 1.08 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 15.32 | 16.95 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 18.51 | 33.83 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 213.09 | 216.37 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 622.21 | 1243.04 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.31 | 5.44 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 4.78 | 10.95 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 11.18 | 15.09 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 177.67 | 178.36 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 544.43 | 1.82 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 389.80 | 2.70 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 3804.22 | 51.75 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 7567.30 | 95.68 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 1.66 | 5.79 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 3.54 | 8.58 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 18.62 | 24.28 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 87.35 | 178.70 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.37 | 0.39 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 1.05 | 1.06 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 1.48 | 1.92 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 315.11 | 319.15 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.19 | 0.23 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.25 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 1.13 | 1.29 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.87 | 5.07 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 5.61 | 11.80 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 37.40 | 38.12 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 137.19 | 170.99 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.53 | 0.54 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.53 | 4.59 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 37.41 | 38.33 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 101.06 | 122.35 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 1338.80 | 3.84 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 1565.49 | 3.90 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 15444.66 | 103.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 222408.86 | 1494.94 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 6.56 | 25.42 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 10.90 | 13.43 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 47.44 | 77.43 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 148.23 | 160.83 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.19 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.21 | 0.26 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.43 | 0.47 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 2786.58 | 2829.72 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.42 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 2048.76 | 2094.58 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 2.58 | 2.78 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.11 | 4.71 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 7.17 | 17.32 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 7.68 | 8.79 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 3.79 | 3.80 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 5.38 | 13.15 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 462.81 | 479.57 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | no | 2488.53 | 2517.41 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 368.48 | 3.17 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 703.34 | 3.98 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 1516.06 | 9.02 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 4571.48 | 92.07 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 4.70 | 8.52 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 6.35 | 9.67 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 10.91 | 22.23 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 61.16 | 99.21 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 0.18 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.50 | 0.54 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.67 | 10.10 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 47.07 | 62.94 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.34 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 0.76 | 0.93 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 1.39 | 1.62 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 42.55 | 87.11 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2.73 | 4.20 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 4.66 | 6.14 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 4.89 | 5.94 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 84.08 | 85.76 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261029T060415Z.json) | yes | 3.07 | 3.10 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 3.27 | 4.56 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261029T060415Z.json) | yes | 34.47 | 40.81 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261029T060415Z.json) | yes | 225.47 | 225.80 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | no | 230.64 | 0.30 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.99 | 1.04 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.21 | 0.27 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 2473.01 | 52.96 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 21.80 | 29.92 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 75.98 | 125.00 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261029T060415Z.json) | yes | 61.09 | 69.15 | 100% | 75.00 | 0.00 | pass |
