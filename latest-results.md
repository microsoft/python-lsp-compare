# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260321T063103Z.json`

- Generated at: 20260321T063103Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.408 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.408/package/dist/pyright-langserver.js |
| Ty | 0.0.24 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.24/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.57.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/0.57.1/pyrefly |
| pylsp-mypy | 1.14.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pylsp-mypy/venv/bin/pylsp |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Wall clock ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 6 | 6991.15 | 3.17 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 6 | 10688.83 | 23.78 | 150 | 87% | 4 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | no | 6 | 84291.97 | 57.06 | 150 | 93% | 2 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 6 | 256529.86 | 602.17 | 150 | 80% | 6 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — not just measured requests.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1020.11 | 4.18 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 1465.04 | 14.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 13991.91 | 50.88 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 7766.39 | 89.91 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.66 | 2.02 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 6.18 | 11.78 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 43.05 | 169.41 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 44.91 | 54.78 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.25 | 0.26 | 100% | 3908.00 | -111.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 1.10 | 1.18 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 3.41 | 11.68 | 100% | 8341.00 | +4322.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 204.22 | 243.84 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.26 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.38 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 1.06 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 4.18 | 4.25 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 16.91 | 17.31 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 26.61 | 36.63 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 215.68 | 310.43 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.30 | 0.32 | 100% | 354.00 | +76.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.89 | 1.91 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 31.07 | 34.28 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 195.17 | 227.32 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4134.00, 8341.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (278.00, 354.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 735.73 | 1.44 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 941.57 | 7.91 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | no | 7193.44 | 20.50 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 6890.37 | 157.46 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 4.68 | 7.54 | 100% | 237.00 | +218.20 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 6.86 | 13.82 | 100% | 18.80 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 35.95 | 142.05 | 100% | 38.00 | +19.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 267.17 | 524.46 | 100% | 2.00 | -16.80 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.24 | 0.27 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.67 | 0.73 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 172.64 | 173.73 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.36 | 0.86 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.49 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 1.09 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.16 | 1.19 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 2.79 | 4.71 | 0% | 0.00 | 0.00 | fail (10) |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | no | 53.47 | 59.07 | 0% | 0.00 | 0.00 | fail (10) |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 150.32 | 150.84 | 100% | 94.00 | +94.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.21 | 0.23 | 100% | 21.00 | -7.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.95 | 0.98 | 100% | 7.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 40.99 | 44.33 | 100% | 28.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 196.08 | 198.43 | 100% | 49.00 | +21.00 | pass |

### Result Differences

- queryset completion: result differences detected (18.80, 2.00, 237.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (0.00, 23.00, 94.00).
- edit queryset then hover (edit+hover): result differences detected (21.00, 28.00, 49.00, 7.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1337.01 | 6.05 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 1429.94 | 17.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 17619.37 | 87.81 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 8342.34 | 147.41 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 16.65 | 21.12 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 48.15 | 190.81 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 75.45 | 253.99 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 129.06 | 366.27 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.23 | 0.24 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.63 | 0.70 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 2.41 | 2.83 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 201.88 | 202.67 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.19 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.20 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.48 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 1.04 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 11.86 | 12.88 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 38.18 | 56.52 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 211.34 | 217.34 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 352.51 | 754.33 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.29 | 0.33 | 100% | 328.00 | -3964.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.34 | 1.37 | 100% | 281.00 | -4011.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 9.96 | 11.35 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 193.74 | 194.85 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 281.00, 328.00, 4292.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 834.22 | 1.62 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 1451.68 | 18.34 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 7987.97 | 43.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 7484.88 | 93.36 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 4.10 | 9.73 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 6.30 | 11.92 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 69.81 | 111.60 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 83.10 | 323.41 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.36 | 0.39 | 100% | 10580.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 1.20 | 2.34 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 1.86 | 3.14 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 338.28 | 373.67 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.22 | 0.25 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.40 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 1.08 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.91 | 2.08 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 6.87 | 15.26 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 30.09 | 31.68 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 130.20 | 191.50 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 0.27 | 0.29 | 0% | 0.00 | -900.00 | fail (10) |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 1.53 | 1.55 | 100% | 304.00 | -596.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 27.56 | 27.97 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 78.80 | 86.68 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10580.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 304.00, 900.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 2194.00 | 3.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 4003.77 | 72.92 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | no | 32131.73 | 131.73 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 221227.52 | 3059.44 | 5 | 25 | 40% | 3 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 12.13 | 14.46 | 100% | 767.00 | +644.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 47.30 | 77.81 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 143.43 | 146.43 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 347.29 | 1347.88 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.28 | 0.31 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.48 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 2585.53 | 2628.67 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.29 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 1.00 | 2.79 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 2286.72 | 2352.94 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 2.48 | 2.53 | 0% | 0.00 | 0.00 | fail (10) |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 3.19 | 3.46 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | no | 5.79 | 6.29 | 0% | 0.00 | 0.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 15.47 | 18.41 | 0% | 0.00 | 0.00 | fail (10) |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 1.25 | 1.32 | 100% | 43.00 | +13.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 2.72 | 2.73 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 604.10 | 620.08 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | no | 10279.02 | 10380.61 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 767.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 43.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 870.08 | 2.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 5367.54 | 7.96 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 1396.83 | 10.95 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 4818.35 | 65.42 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 4.87 | 9.87 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 6.24 | 9.74 | 100% | 441.00 | +425.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 21.80 | 25.56 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 47.78 | 155.75 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.49 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 3.62 | 11.98 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 20.18 | 39.35 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.35 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.49 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 0.69 | 0.75 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 20.65 | 39.95 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 2.45 | 2.72 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | no | 2.85 | 4.58 | 0% | 0.00 | -205.00 | fail (10) |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 4.74 | 7.54 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 85.72 | 92.31 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260321T063103Z.json) | yes | 0.18 | 0.19 | 100% | 31.00 | -731.00 | pass |
| [Ty](latest-results/ty-20260321T063103Z.json) | yes | 0.75 | 0.80 | 100% | 304.00 | -458.00 | pass |
| [Pyright](latest-results/pyright-20260321T063103Z.json) | yes | 28.99 | 32.77 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260321T063103Z.json) | yes | 178.75 | 181.63 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 441.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (0.00, 205.00, 227.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 31.00, 762.00).
