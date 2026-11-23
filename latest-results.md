# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261123T060454Z.json`

- Generated at: 20261123T060454Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.108 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.108/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.5.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 6 | 2318.63 | 2.37 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | no | 8 | 3668.63 | 3.11 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 6 | 22682.68 | 30.92 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 6 | 154167.10 | 219.53 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 302.54 | 2.23 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 419.92 | 3.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 2684.66 | 41.82 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 4437.17 | 62.08 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 1.18 | 1.40 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.70 | 2.72 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 3.46 | 5.46 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 92.34 | 203.06 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.14 | 0.17 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.85 | 1.18 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.20 | 1.52 | 100% | 7910.00 | +3891.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 110.59 | 112.56 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.29 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 0.54 | 0.60 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 2.30 | 2.48 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 7.41 | 9.31 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 12.95 | 32.81 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 185.86 | 240.22 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 2.05 | 3.09 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.34 | 2.37 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 18.65 | 21.52 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 104.64 | 106.79 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (4019.00, 4134.00, 4232.00, 7910.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 116.22 | 0.83 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 156.20 | 1.32 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 888.98 | 8.83 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 4218.37 | 95.32 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.49 | 2.48 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 2.85 | 4.64 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 3.09 | 5.23 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 97.90 | 201.82 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.10 | 0.12 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.33 | 0.36 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.41 | 1.24 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 97.76 | 99.48 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.08 | 0.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.24 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 0.56 | 0.62 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.84 | 4.52 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.14 | 2.55 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 14.99 | 16.01 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 138.07 | 169.05 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.32 | 0.36 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 1.16 | 1.26 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 25.74 | 29.56 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 142.30 | 146.93 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 337.83 | 3.53 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 500.38 | 4.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 5271.89 | 44.98 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 4559.37 | 80.58 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 2.34 | 5.29 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 11.42 | 14.01 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 33.64 | 47.94 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 52.85 | 178.95 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.13 | 0.16 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.46 | 0.53 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 2.92 | 3.18 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 119.37 | 122.41 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.08 | 0.08 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.26 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 0.59 | 0.63 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 2.19 | 2.96 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 8.96 | 11.82 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 9.10 | 10.60 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 126.09 | 137.90 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 165.62 | 197.43 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.21 | 4.01 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.07 | 2.12 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 5.71 | 8.01 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 123.20 | 145.65 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 295.96 | 0.78 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 243.62 | 1.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 2452.51 | 33.54 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 4059.72 | 54.58 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.77 | 5.88 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.28 | 5.84 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 13.06 | 15.77 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 41.71 | 87.44 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.16 | 0.18 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.87 | 1.36 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 1.78 | 2.50 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 191.70 | 197.94 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.08 | 0.10 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.56 | 1.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 0.62 | 0.67 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.82 | 0.87 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.81 | 3.58 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 19.55 | 20.09 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 91.17 | 113.00 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.32 | 0.34 | 100% | 2249.00 | +1356.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.19 | 2.22 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 19.32 | 19.52 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 61.12 | 69.37 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2249.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 879.97 | 2.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 941.11 | 2.81 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 10389.04 | 50.66 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 134530.18 | 979.47 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 5.05 | 19.83 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 7.89 | 9.41 | 100% | 788.00 | +665.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 39.97 | 60.41 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 75.03 | 77.00 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.15 | 0.24 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.17 | 0.41 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.34 | 0.43 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 1855.10 | 1920.43 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.26 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 1388.71 | 1456.33 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 1.60 | 1.77 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 2.33 | 2.85 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 3.39 | 10.68 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 4.26 | 5.14 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 1.87 | 1.91 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 5.32 | 10.80 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 208.46 | 231.55 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | no | 1576.94 | 1638.71 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 788.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 235.92 | 2.13 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 271.42 | 3.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 995.60 | 5.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 2362.29 | 45.15 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 3.64 | 6.21 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 4.31 | 7.40 | 100% | 497.00 | +483.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 10.05 | 13.81 | 100% | 276.60 | +262.60 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 29.40 | 54.55 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.08 | 0.10 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.14 | 0.16 | 100% | 217.00 | +191.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.33 | 0.38 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 4.51 | 4.74 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 0.52 | 0.69 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 0.89 | 1.05 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 1.09 | 1.14 | 100% | 2.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.92 | 2.70 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 2.81 | 3.80 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 3.52 | 3.99 | 100% | 225.00 | +20.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 3.58 | 10.40 | 100% | 57.00 | -148.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 49.87 | 53.98 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1.37 | 2.02 | 100% | 2884.00 | +2464.00 | pass |
| [Ty](latest-results/ty-20261123T060454Z.json) | yes | 1.83 | 1.85 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261123T060454Z.json) | yes | 21.22 | 23.71 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261123T060454Z.json) | yes | 140.86 | 142.91 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 276.60, 497.00).
- client session hover: result differences detected (217.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 2884.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | no | 89.57 | 0.16 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.52 | 0.59 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.09 | 0.09 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.12 | 0.14 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.12 | 0.18 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 0.11 | 0.11 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 1196.60 | 17.09 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 10.78 | 22.19 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 34.52 | 35.82 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261123T060454Z.json) | yes | 5.99 | 9.77 | 100% | 75.00 | 0.00 | pass |
