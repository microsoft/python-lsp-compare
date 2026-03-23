# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260323T065805Z.json`

- Generated at: 20260323T065805Z
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
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 6 | 7259.02 | 3.44 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 6 | 11024.96 | 24.24 | 150 | 87% | 4 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | no | 6 | 92711.47 | 64.60 | 150 | 93% | 2 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 6 | 270761.67 | 623.66 | 150 | 80% | 6 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — not just measured requests.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1078.43 | 4.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 1607.06 | 16.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 15333.94 | 49.38 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 8026.14 | 92.35 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.86 | 2.24 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 6.47 | 10.52 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 42.61 | 168.24 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 42.72 | 46.21 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.28 | 0.32 | 100% | 3908.00 | -111.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 1.11 | 1.34 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 4.45 | 13.60 | 100% | 8341.00 | +4322.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 209.41 | 246.58 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.30 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.42 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 1.05 | 1.08 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 4.33 | 4.46 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 18.92 | 19.67 | 100% | 167.00 | -2.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 35.03 | 39.57 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 210.35 | 313.98 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.68 | 1.83 | 100% | 354.00 | +76.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.97 | 2.00 | 100% | 376.00 | +98.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 28.55 | 31.97 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 204.26 | 248.49 | 100% | 5644.00 | +5366.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4134.00, 8341.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 167.00, 169.00).
- edit array then hover (edit+hover): result differences detected (278.00, 354.00, 376.00, 5644.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 771.77 | 1.56 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 963.39 | 7.74 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | no | 7619.05 | 22.11 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 7099.85 | 162.58 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 5.14 | 7.95 | 100% | 237.00 | +218.20 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 7.34 | 15.68 | 100% | 18.80 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 36.75 | 145.30 | 100% | 38.00 | +19.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 268.26 | 549.66 | 100% | 2.00 | -16.80 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.21 | 0.23 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.26 | 0.27 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.60 | 0.66 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 181.88 | 183.01 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.18 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.23 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.44 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 1.11 | 1.14 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 1.17 | 3.23 | 0% | 0.00 | 0.00 | fail (10) |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.24 | 1.30 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | no | 58.06 | 62.04 | 0% | 0.00 | 0.00 | fail (10) |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 156.21 | 160.09 | 100% | 94.00 | +94.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.28 | 0.34 | 100% | 21.00 | -7.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.01 | 1.03 | 100% | 7.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 44.10 | 48.33 | 100% | 28.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 205.42 | 207.03 | 100% | 49.00 | +21.00 | pass |

### Result Differences

- queryset completion: result differences detected (18.80, 2.00, 237.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (0.00, 23.00, 94.00).
- edit queryset then hover (edit+hover): result differences detected (21.00, 28.00, 49.00, 7.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1410.73 | 6.57 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 1477.08 | 18.50 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 19846.22 | 117.51 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 8829.08 | 151.96 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 17.89 | 22.21 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 47.55 | 188.85 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 92.39 | 309.69 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 115.81 | 303.96 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.26 | 0.27 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.78 | 0.94 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 2.47 | 2.88 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 210.76 | 215.01 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.47 | 0.60 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 1.06 | 1.09 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 13.11 | 13.65 | 100% | 448.00 | +7.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 41.98 | 62.16 | 100% | 256.00 | -185.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 230.74 | 240.56 | 100% | 442.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 483.25 | 921.56 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.27 | 0.38 | 100% | 328.00 | -3964.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.38 | 1.40 | 100% | 281.00 | -4011.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 10.64 | 12.57 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 201.46 | 203.97 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 442.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 281.00, 328.00, 4292.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 870.98 | 1.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 1518.92 | 19.42 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 8690.42 | 46.03 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 7878.91 | 98.25 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 4.36 | 10.56 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 6.49 | 11.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 75.70 | 126.76 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 84.43 | 329.53 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.38 | 0.40 | 100% | 10580.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.79 | 0.88 | 100% | 13682.00 | +3110.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 1.36 | 1.84 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 357.41 | 393.88 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.24 | 0.26 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.81 | 1.91 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 1.09 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.99 | 2.21 | 100% | 23.00 | -16.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 11.29 | 15.38 | 100% | 17.00 | -22.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 29.05 | 30.46 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 138.89 | 195.17 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 0.30 | 0.32 | 0% | 0.00 | -900.00 | fail (10) |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 1.54 | 1.56 | 100% | 304.00 | -596.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 27.99 | 28.40 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 82.59 | 89.35 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10580.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 304.00, 900.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 2248.56 | 4.07 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 4024.38 | 72.11 | 5 | 25 | 80% | 1 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | no | 35017.86 | 143.90 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 233637.72 | 3163.10 | 5 | 25 | 40% | 3 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 12.55 | 14.94 | 100% | 767.00 | +644.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 53.93 | 89.18 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 145.88 | 149.68 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 354.03 | 1370.27 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.24 | 0.26 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.52 | 0.66 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 2693.45 | 2744.71 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 1.12 | 3.13 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 2312.84 | 2399.10 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 2.67 | 2.76 | 0% | 0.00 | 0.00 | fail (10) |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 4.52 | 5.79 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 4.89 | 13.30 | 0% | 0.00 | 0.00 | fail (10) |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | no | 6.11 | 6.68 | 0% | 0.00 | 0.00 | fail (10) |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 1.18 | 1.24 | 100% | 43.00 | +13.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 2.81 | 3.00 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 657.81 | 689.29 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | no | 10660.64 | 10830.27 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 767.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 43.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 878.55 | 2.09 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 6203.98 | 8.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 1434.12 | 11.04 | 5 | 25 | 80% | 1 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 5289.98 | 73.74 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 5.14 | 10.17 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 6.59 | 10.33 | 100% | 441.00 | +425.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 25.87 | 33.95 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 48.90 | 167.42 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.50 | 0.58 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 3.69 | 12.22 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 29.27 | 51.32 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.37 | 0.39 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.47 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 0.73 | 0.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 25.80 | 51.52 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | no | 2.07 | 4.62 | 0% | 0.00 | -205.00 | fail (10) |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 2.44 | 2.75 | 100% | 227.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 5.55 | 7.97 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 96.52 | 104.75 | 100% | 56.00 | -149.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260323T065805Z.json) | yes | 0.19 | 0.20 | 100% | 31.00 | -731.00 | pass |
| [Ty](latest-results/ty-20260323T065805Z.json) | yes | 0.75 | 0.76 | 100% | 304.00 | -458.00 | pass |
| [Pyright](latest-results/pyright-20260323T065805Z.json) | yes | 31.51 | 36.33 | 100% | 762.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260323T065805Z.json) | yes | 191.25 | 192.96 | 100% | 257.00 | -505.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 441.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (0.00, 205.00, 227.00, 56.00).
- edit response then hover (edit+hover): result differences detected (257.00, 304.00, 31.00, 762.00).
