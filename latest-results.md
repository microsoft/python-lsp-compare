# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260828T090257Z.json`

- Generated at: 20260828T090257Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.412 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.412/package/dist/pyright-langserver.js |
| Ty | 0.0.75 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.75/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 6 | 4759.21 | 3.61 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | no | 8 | 7973.50 | 15.74 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 6 | 37428.75 | 70.71 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 6 | 217031.19 | 370.44 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 466.80 | 3.39 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 813.81 | 11.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 4236.91 | 72.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 7859.57 | 113.37 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 1.68 | 1.82 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 7.25 | 12.35 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 30.91 | 117.64 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 217.01 | 462.34 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.33 | 0.36 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 1.07 | 1.20 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 11.53 | 36.99 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 178.72 | 181.78 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.36 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 1.02 | 1.05 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 4.54 | 4.73 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 8.96 | 10.88 | 100% | 149.00 | -19.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 10.55 | 11.18 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 322.13 | 427.39 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 3.66 | 5.24 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 4.19 | 4.27 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 31.37 | 34.11 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 165.56 | 166.85 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 237.65 | 2.07 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 282.58 | 5.05 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 1460.38 | 14.19 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 7710.99 | 173.14 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 4.11 | 7.50 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 4.76 | 7.35 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 19.33 | 72.76 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 210.99 | 649.99 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.22 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.39 | 0.48 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.53 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 156.41 | 158.84 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.20 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.39 | 0.40 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.41 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 1.07 | 1.11 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2.69 | 5.26 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.29 | 3.47 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 25.89 | 28.56 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 251.08 | 281.37 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 1.90 | 1.96 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2.46 | 3.73 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 40.00 | 44.29 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 246.14 | 248.85 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 813.43 | 7.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 739.22 | 11.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 7820.15 | 139.62 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 10105.74 | 146.05 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 19.12 | 22.82 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 37.07 | 145.58 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 72.90 | 236.67 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 100.40 | 233.64 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.25 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.73 | 0.79 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2.70 | 2.96 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 190.70 | 194.78 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.46 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 1.08 | 1.16 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 14.24 | 22.39 | 100% | 256.00 | -184.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 15.16 | 16.72 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 224.92 | 228.99 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 644.99 | 1333.50 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.49 | 3.59 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 5.27 | 8.40 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 11.17 | 13.67 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 181.03 | 182.41 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 333.02 | 2.04 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 727.31 | 13.95 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 3470.24 | 47.95 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 7004.81 | 123.63 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.34 | 7.52 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 7.54 | 13.07 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 64.03 | 246.03 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 213.94 | 441.13 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.38 | 0.40 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 1.12 | 1.23 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 1.27 | 1.56 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 323.05 | 325.44 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.42 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 1.09 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.25 | 3.50 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 3.82 | 8.59 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 39.69 | 43.70 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 143.35 | 190.29 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.51 | 0.55 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.01 | 3.13 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 40.39 | 42.00 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 87.20 | 96.69 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 2609.37 | 4.21 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2342.19 | 48.37 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 16673.19 | 134.47 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 181829.66 | 1567.53 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 10.93 | 12.13 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 48.91 | 76.74 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 148.67 | 153.95 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 240.06 | 941.75 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.23 | 0.26 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.41 | 0.83 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.47 | 0.52 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 2780.02 | 2831.11 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.26 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.28 | 0.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.45 | 0.52 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 2226.88 | 2272.83 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.61 | 0.62 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 2.55 | 2.67 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 4.93 | 5.06 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 6.46 | 7.44 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.51 | 0.53 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 4.70 | 4.77 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 616.04 | 641.00 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | no | 2679.55 | 2719.53 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 298.93 | 2.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 1482.30 | 9.18 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 818.37 | 11.07 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 4806.01 | 105.36 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 5.46 | 9.72 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 6.04 | 9.05 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 48.30 | 147.39 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 67.13 | 88.98 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.22 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.57 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2.71 | 8.98 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 94.73 | 182.73 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.38 | 0.40 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 0.51 | 0.59 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 0.84 | 0.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 48.04 | 119.38 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 1.20 | 3.02 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 3.07 | 3.59 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 5.27 | 7.01 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 88.25 | 89.68 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260828T090257Z.json) | yes | 1.56 | 1.59 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2.75 | 4.54 | 100% | 3585.00 | +3165.00 | pass |
| [Pyright](latest-results/pyright-20260828T090257Z.json) | yes | 33.78 | 40.46 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260828T090257Z.json) | yes | 228.63 | 229.53 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | no | 187.69 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.96 | 1.01 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.17 | 0.18 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.21 | 0.21 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 2062.34 | 45.36 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 26.13 | 49.13 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 101.43 | 158.89 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260828T090257Z.json) | yes | 8.52 | 8.92 | 100% | 75.00 | 0.00 | pass |
