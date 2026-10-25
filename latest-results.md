# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261025T060448Z.json`

- Generated at: 20261025T060448Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.91 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.91/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 6 | 2829.41 | 3.35 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | no | 8 | 5478.04 | 6.99 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 6 | 29057.31 | 43.76 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 6 | 199756.11 | 284.36 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 419.23 | 3.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 559.19 | 6.38 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 3364.88 | 52.22 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 6091.51 | 80.48 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 1.37 | 1.60 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.97 | 5.00 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 4.86 | 8.62 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 115.83 | 243.48 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.23 | 0.24 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.91 | 1.25 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.83 | 2.00 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 146.87 | 149.30 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.31 | 0.36 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 0.79 | 0.83 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 3.38 | 3.55 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 10.07 | 11.37 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 15.58 | 21.16 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 231.98 | 345.40 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 4.23 | 4.28 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 12.34 | 37.61 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 23.03 | 25.54 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 135.52 | 137.12 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 213.04 | 1.31 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 205.71 | 1.96 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 1143.82 | 11.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 5891.06 | 128.30 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.27 | 5.61 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.32 | 5.42 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 4.07 | 6.33 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 122.41 | 332.08 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.17 | 0.18 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.41 | 0.46 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.72 | 2.42 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 130.47 | 135.30 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.26 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 0.78 | 0.84 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.01 | 1.06 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.75 | 4.10 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 20.09 | 21.96 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 193.18 | 240.22 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.39 | 2.95 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 2.44 | 2.49 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 30.99 | 36.60 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 194.67 | 197.36 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 682.40 | 6.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 589.01 | 8.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 6980.04 | 60.33 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 6169.93 | 107.64 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.83 | 5.80 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 13.42 | 16.05 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 46.68 | 58.36 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 73.40 | 241.97 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.19 | 0.22 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.60 | 0.77 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 3.44 | 5.31 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 155.85 | 158.92 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.30 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 0.79 | 0.83 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.94 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 15.98 | 16.64 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 25.01 | 48.75 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 183.15 | 190.35 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 218.10 | 246.90 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.94 | 4.59 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 6.97 | 11.94 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 9.23 | 12.49 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 151.72 | 154.26 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 419.94 | 1.61 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 301.21 | 2.26 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 3018.60 | 40.32 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 5479.45 | 74.74 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.83 | 5.36 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 2.43 | 5.76 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 15.68 | 19.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 67.43 | 134.32 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.31 | 0.32 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.77 | 0.81 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 1.27 | 1.41 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 249.85 | 253.69 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.15 | 0.15 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.44 | 0.71 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 0.82 | 0.86 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 3.31 | 4.45 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 4.45 | 5.12 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 27.61 | 27.83 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 105.37 | 133.43 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.96 | 3.30 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.97 | 3.99 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 27.97 | 28.45 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 78.86 | 89.43 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1036.38 | 2.25 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 928.51 | 3.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 13346.20 | 91.51 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 172374.64 | 1235.28 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 5.21 | 20.31 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 9.42 | 11.27 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 50.46 | 68.46 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 109.09 | 112.67 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.14 | 0.15 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.17 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.42 | 0.53 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 2303.59 | 2338.74 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.13 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.32 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 1742.01 | 1826.91 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.38 | 0.63 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 2.11 | 2.30 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.74 | 3.84 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 4.85 | 5.24 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 3.57 | 3.63 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 5.38 | 15.82 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 401.50 | 423.67 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | no | 2019.61 | 2054.04 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 292.34 | 2.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 535.25 | 3.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 1203.77 | 7.04 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 3749.50 | 79.72 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 3.72 | 6.39 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 4.57 | 6.40 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 12.58 | 24.08 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 54.44 | 94.07 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 0.13 | 0.15 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.39 | 0.46 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.36 | 9.01 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 88.94 | 200.86 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.24 | 0.25 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 0.56 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 1.09 | 1.20 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 3.40 | 3.90 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 2.92 | 3.02 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 3.94 | 5.01 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 4.31 | 4.56 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 65.15 | 66.77 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1.17 | 1.24 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261025T060448Z.json) | yes | 2.37 | 2.40 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261025T060448Z.json) | yes | 26.60 | 31.77 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261025T060448Z.json) | yes | 186.66 | 190.68 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | no | 175.02 | 0.22 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.74 | 0.77 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.13 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.15 | 0.15 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 0.15 | 0.15 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 1950.21 | 55.48 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 9.02 | 13.04 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 106.10 | 118.24 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261025T060448Z.json) | yes | 51.34 | 58.36 | 100% | 75.00 | 0.00 | pass |
