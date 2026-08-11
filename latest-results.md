# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260811T061537Z.json`

- Generated at: 20260811T061537Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.411 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.411/package/dist/pyright-langserver.js |
| Ty | 0.0.70 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.70/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.2.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 6 | 3495.47 | 3.07 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | no | 8 | 8590.23 | 18.38 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 6 | 33462.30 | 56.32 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 6 | 207196.53 | 362.70 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 467.33 | 2.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 811.95 | 10.25 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 3667.83 | 58.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 7637.99 | 109.16 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 1.70 | 1.92 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 5.90 | 10.48 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 32.40 | 123.38 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 183.75 | 437.41 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.29 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 1.66 | 3.81 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 2.23 | 2.51 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 185.43 | 190.24 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.40 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.59 | 1.27 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 1.00 | 1.04 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 4.03 | 4.44 | 0% | 0.00 | -169.00 | fail (10) |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 7.89 | 8.76 | 100% | 168.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 12.28 | 13.12 | 100% | 149.00 | -20.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 255.02 | 339.81 | 100% | 169.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 2.94 | 2.99 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 3.75 | 5.43 | 100% | 1909.00 | +1631.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 27.00 | 30.58 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 171.59 | 174.79 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00, 169.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 239.06 | 1.87 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 288.53 | 5.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 1363.62 | 12.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 7550.88 | 166.32 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 3.74 | 6.41 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 4.74 | 7.72 | 100% | 260.00 | +250.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 18.77 | 73.70 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 187.51 | 556.03 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.19 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.26 | 0.28 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.54 | 0.62 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 161.22 | 164.27 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.16 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 1.04 | 1.06 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 2.76 | 2.98 | 100% | 104.00 | -1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 4.81 | 10.97 | 100% | 83.00 | -22.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 22.85 | 24.15 | 100% | 105.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 242.43 | 293.85 | 100% | 143.00 | +38.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 1.25 | 3.19 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 1.52 | 1.56 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 36.96 | 45.38 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 239.42 | 242.58 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 260.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 105.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 802.42 | 6.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 693.23 | 12.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 7555.33 | 86.65 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 7897.64 | 135.10 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 18.41 | 22.33 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 40.24 | 149.96 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 54.55 | 71.47 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 68.10 | 226.30 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.24 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.70 | 0.79 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 5.03 | 5.90 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 193.59 | 197.41 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 1.02 | 1.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 2.93 | 2.94 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 11.20 | 20.67 | 100% | 256.00 | -185.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 12.24 | 13.02 | 100% | 448.00 | +7.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 236.01 | 239.15 | 100% | 441.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 354.02 | 786.58 | 100% | 441.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.62 | 0.70 | 100% | 794.00 | -3498.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 2.32 | 2.35 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 10.02 | 10.80 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 190.35 | 198.75 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 323.83 | 1.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 752.63 | 15.24 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 3151.08 | 41.43 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 7071.14 | 116.73 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 3.57 | 8.57 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 6.42 | 11.83 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 64.85 | 255.07 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 189.66 | 372.23 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.37 | 0.39 | 100% | 10628.00 | +56.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 1.25 | 1.51 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 1.49 | 2.38 | 100% | 13188.00 | +2616.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 322.01 | 325.59 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.18 | 0.20 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.38 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 1.11 | 1.40 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.54 | 0.59 | 100% | 17.00 | -22.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 2.01 | 2.19 | 100% | 23.00 | -16.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 35.84 | 37.22 | 0% | 0.00 | -39.00 | fail (10) |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 125.99 | 157.68 | 100% | 39.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 1.76 | 1.80 | 100% | 958.00 | +58.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 9.16 | 14.43 | 100% | 2137.00 | +1237.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 35.05 | 36.23 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 73.09 | 76.23 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10628.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 39.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 1338.50 | 3.69 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 2497.31 | 51.73 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 16349.00 | 130.93 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 172170.50 | 1543.08 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 11.41 | 13.22 | 100% | 774.00 | +651.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 55.41 | 82.28 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 131.30 | 134.43 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 248.16 | 991.76 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.18 | 0.19 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.42 | 0.46 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 2716.41 | 2765.20 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.26 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 2253.76 | 2296.87 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.48 | 0.55 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 2.46 | 2.59 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 3.45 | 3.81 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 6.64 | 9.39 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 3.12 | 3.15 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 9.66 | 26.06 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 591.78 | 604.40 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | no | 2611.45 | 2639.13 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 774.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 324.33 | 2.02 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 1375.43 | 8.00 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 734.86 | 8.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 4868.38 | 105.83 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 5.13 | 9.21 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 5.62 | 8.50 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 38.02 | 134.29 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 71.69 | 122.71 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.18 | 0.20 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.48 | 0.51 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 2.82 | 9.66 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 132.28 | 253.04 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 0.50 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 0.77 | 0.84 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 3.29 | 4.05 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.54 | 0.55 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 2.64 | 2.78 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 4.76 | 6.42 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 85.34 | 86.67 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260811T061537Z.json) | yes | 1.18 | 1.22 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 3.24 | 4.51 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260811T061537Z.json) | yes | 28.85 | 32.61 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260811T061537Z.json) | yes | 236.53 | 247.58 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | no | 190.57 | 0.37 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 1.78 | 4.55 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 0.16 | 0.18 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 2621.15 | 78.12 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 35.57 | 65.30 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 140.15 | 181.47 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260811T061537Z.json) | yes | 58.65 | 75.55 | 100% | 75.00 | 0.00 | pass |
