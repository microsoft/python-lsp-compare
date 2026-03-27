# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260327T065650Z.json`

- Generated at: 20260327T065650Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.408 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.408/package/dist/pyright-langserver.js |
| Ty | 0.0.26 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.26/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 6 | 6653.60 | 3.27 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | no | 6 | 9408.11 | 20.29 | 150 | 90% | 2 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 6 | 82385.16 | 58.04 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 6 | 206360.09 | 497.57 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — not just measured requests.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 962.21 | 4.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 1391.01 | 14.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 12741.42 | 45.82 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 7160.74 | 83.90 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.69 | 1.94 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 6.18 | 10.53 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 37.52 | 147.72 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 48.13 | 59.27 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.22 | 0.23 | 100% | 3908.00 | -111.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 1.06 | 1.13 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 3.86 | 12.22 | 100% | 8341.00 | +4322.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 190.30 | 243.48 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.39 | 0.67 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 0.87 | 0.92 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 3.57 | 3.75 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 17.21 | 18.10 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 31.02 | 36.62 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 194.86 | 302.97 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.64 | 1.75 | 100% | 354.00 | +76.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.76 | 1.86 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 26.64 | 31.72 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 176.63 | 202.88 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4134.00, 8341.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (278.00, 354.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 705.23 | 2.06 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 786.42 | 5.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 6115.69 | 13.96 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 7536.23 | 149.84 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 4.73 | 7.49 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 5.94 | 8.52 | 100% | 254.00 | +244.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 22.24 | 87.56 | 100% | 38.00 | +28.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 153.00 | 423.27 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.17 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.20 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.54 | 0.60 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 158.24 | 161.53 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.14 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.15 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 0.87 | 0.90 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 2.80 | 3.17 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 2.81 | 4.75 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 22.37 | 25.98 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 254.99 | 293.99 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.19 | 0.21 | 100% | 144.00 | +61.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.25 | 1.31 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 41.73 | 49.28 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 182.11 | 183.08 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 2.00, 254.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 144.00, 71.00, 83.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1317.86 | 6.35 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 1257.16 | 14.57 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 17144.42 | 108.93 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 7464.29 | 122.33 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 17.69 | 21.64 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 41.90 | 166.23 | 100% | 39.00 | -235.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 60.49 | 112.21 | 100% | 6.00 | -268.20 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 86.80 | 291.90 | 100% | 274.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.23 | 0.30 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.89 | 1.08 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 1.78 | 2.09 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 182.58 | 184.59 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.18 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.43 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 0.97 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 12.38 | 12.66 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 28.78 | 55.55 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 192.78 | 195.13 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 448.18 | 858.35 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.23 | 0.25 | 100% | 328.00 | -3964.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.27 | 1.32 | 100% | 281.00 | -4011.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 8.34 | 10.15 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 174.85 | 175.31 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 281.00, 328.00, 4292.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 801.85 | 1.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | no | 1292.77 | 15.94 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 7402.83 | 42.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 6499.17 | 83.31 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 4.29 | 9.89 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 10.18 | 13.79 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 67.37 | 109.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 70.83 | 276.31 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.35 | 0.37 | 100% | 10580.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 2.25 | 2.69 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 3.15 | 3.77 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 302.06 | 329.52 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.84 | 1.85 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 1.03 | 1.17 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 1.08 | 1.19 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.89 | 2.17 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 5.63 | 8.09 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 23.26 | 24.38 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 117.77 | 148.47 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | no | 0.16 | 0.19 | 0% | 0.00 | -900.00 | fail (10) |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 1.43 | 1.47 | 100% | 304.00 | -596.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 22.76 | 23.34 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 78.41 | 86.94 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10580.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 304.00, 900.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 2085.72 | 3.42 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 3513.06 | 61.83 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 29928.98 | 129.78 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 173216.24 | 2486.32 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 11.34 | 13.26 | 100% | 767.00 | +644.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 52.41 | 81.53 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 118.36 | 125.58 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 306.99 | 1226.79 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.16 | 0.17 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.17 | 0.19 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.55 | 0.69 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 1887.54 | 1918.84 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.17 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.20 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.48 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 1613.52 | 1649.71 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.59 | 0.95 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 2.46 | 2.71 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 2.82 | 3.03 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 6.86 | 9.79 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 1.25 | 1.29 | 100% | 43.00 | +13.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 2.58 | 2.68 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 588.58 | 594.42 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | no | 8809.73 | 8871.77 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 767.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 43.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 780.73 | 1.94 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 9051.83 | 7.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | no | 1167.69 | 9.61 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 4483.42 | 59.72 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 4.81 | 7.95 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 6.11 | 9.67 | 100% | 441.00 | +425.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 21.40 | 28.65 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 41.34 | 136.86 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.15 | 0.17 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.55 | 0.71 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 3.41 | 11.58 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 17.56 | 28.44 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.28 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.41 | 0.49 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 0.74 | 0.80 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 11.10 | 30.91 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 2.32 | 2.54 | 100% | 227.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | no | 2.90 | 4.84 | 0% | 0.00 | -205.00 | fail (10) |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 4.89 | 6.99 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 78.86 | 82.79 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260327T065650Z.json) | yes | 0.14 | 0.18 | 100% | 31.00 | -731.00 | pass |
| [Ty](latest-results/ty-20260327T065650Z.json) | yes | 0.72 | 0.74 | 100% | 304.00 | -458.00 | pass |
| [Pyright](latest-results/pyright-20260327T065650Z.json) | yes | 27.24 | 32.10 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260327T065650Z.json) | yes | 169.67 | 172.63 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 441.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (0.00, 205.00, 227.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 31.00, 762.00).
