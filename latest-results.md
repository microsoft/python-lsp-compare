# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261108T060314Z.json`

- Generated at: 20261108T060314Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.99 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.99/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 6 | 2412.94 | 2.51 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | no | 8 | 4229.69 | 3.43 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 6 | 22161.99 | 30.03 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 6 | 156872.29 | 206.67 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 356.02 | 2.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 394.85 | 2.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 2589.61 | 38.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 4336.88 | 50.87 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 1.15 | 1.44 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.94 | 6.07 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 3.27 | 5.13 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 45.39 | 73.15 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.16 | 0.19 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 1.01 | 1.35 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.39 | 1.66 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 107.03 | 110.60 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.30 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 0.58 | 0.62 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 2.25 | 2.41 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 8.32 | 9.29 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 9.23 | 11.28 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 171.74 | 267.19 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.22 | 0.24 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.58 | 2.73 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 18.19 | 19.89 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 99.07 | 99.58 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 171.59 | 1.05 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 170.05 | 1.42 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 914.64 | 9.31 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 4350.08 | 95.23 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.80 | 4.98 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 3.32 | 5.42 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 3.43 | 5.27 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 94.90 | 239.30 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.10 | 0.13 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.11 | 0.14 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.33 | 0.36 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 100.98 | 122.26 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.24 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 0.63 | 0.65 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.07 | 1.86 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.50 | 3.16 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 17.02 | 18.73 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 135.99 | 169.78 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 1.08 | 1.12 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.21 | 2.50 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 25.52 | 29.39 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 143.68 | 146.44 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 438.73 | 3.26 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 525.69 | 5.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 5139.55 | 44.47 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 4661.82 | 84.10 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.62 | 5.12 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 11.46 | 14.28 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 46.76 | 91.32 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 50.36 | 169.91 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.13 | 0.16 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.47 | 0.56 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.33 | 1.53 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 115.93 | 117.55 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.22 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 0.56 | 0.62 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 10.49 | 14.98 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 11.45 | 11.72 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 125.65 | 132.16 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 163.12 | 191.00 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.73 | 5.71 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.15 | 2.21 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 8.17 | 13.27 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 131.58 | 189.70 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 373.12 | 1.66 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 259.07 | 1.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 2416.67 | 32.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 3943.79 | 51.56 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.15 | 4.06 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.33 | 5.87 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 12.82 | 16.19 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 33.92 | 62.96 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.19 | 0.21 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 2.03 | 3.64 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.72 | 3.27 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 180.76 | 186.79 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.09 | 0.10 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.31 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 0.59 | 0.64 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.12 | 2.98 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.98 | 5.06 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 3.39 | 4.54 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 21.13 | 22.23 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 85.92 | 108.52 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.33 | 0.35 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.30 | 2.32 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 21.38 | 22.38 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 60.87 | 71.80 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 870.46 | 2.49 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 950.66 | 3.05 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 10115.34 | 49.01 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 137205.84 | 912.81 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 4.37 | 17.13 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 7.79 | 9.34 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 40.71 | 58.56 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 77.69 | 87.66 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.08 | 0.08 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.12 | 0.14 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.31 | 0.37 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 1687.29 | 1738.88 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.12 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.48 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 1292.75 | 1367.83 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 1.53 | 1.68 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.12 | 5.63 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 2.51 | 3.18 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 4.08 | 5.26 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 1.90 | 1.95 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 8.61 | 17.36 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 199.45 | 205.72 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | no | 1504.79 | 1560.58 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 231.64 | 1.97 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 429.21 | 2.43 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 986.19 | 6.13 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 2373.89 | 45.44 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 4.03 | 6.41 | 100% | 496.00 | +482.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 4.09 | 7.06 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 6.56 | 10.51 | 100% | 253.80 | +239.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 34.65 | 71.12 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.09 | 0.11 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.33 | 0.39 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.10 | 8.10 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 4.50 | 5.36 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 0.54 | 0.66 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 0.85 | 0.97 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 1.01 | 1.08 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1.25 | 2.64 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 2.99 | 3.92 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 3.15 | 3.72 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 48.24 | 57.27 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261108T060314Z.json) | yes | 1.75 | 1.80 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 2.09 | 3.02 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261108T060314Z.json) | yes | 22.70 | 25.05 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261108T060314Z.json) | yes | 138.80 | 146.19 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 253.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | no | 145.44 | 0.16 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.55 | 0.64 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 1326.08 | 23.08 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 7.28 | 10.30 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 38.59 | 64.11 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261108T060314Z.json) | yes | 23.36 | 47.16 | 100% | 75.00 | 0.00 | pass |
