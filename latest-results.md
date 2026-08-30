# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260830T060523Z.json`

- Generated at: 20260830T060523Z
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
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 6 | 3770.47 | 2.93 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | no | 8 | 5512.55 | 11.01 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 6 | 24658.56 | 41.67 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 6 | 134760.46 | 203.70 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 362.94 | 2.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 467.02 | 7.81 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 2954.83 | 51.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 5562.29 | 74.68 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 1.45 | 1.58 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 4.86 | 7.45 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 23.40 | 91.53 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 125.84 | 346.25 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.27 | 0.31 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 1.13 | 1.37 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 1.52 | 1.82 | 100% | 2589.00 | -1430.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 123.76 | 124.44 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.34 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 0.58 | 0.65 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 3.18 | 3.42 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 7.95 | 9.33 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 13.39 | 17.24 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 228.80 | 302.94 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.65 | 1.71 | 100% | 1909.00 | +1631.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 3.31 | 3.38 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 24.34 | 26.98 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 120.06 | 121.64 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (2589.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (1909.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 183.21 | 1.68 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 200.54 | 3.36 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 1000.74 | 10.86 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 5203.67 | 112.69 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 3.13 | 5.26 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 3.87 | 5.55 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 13.32 | 52.49 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 108.47 | 305.56 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.14 | 0.20 | 100% | 298.00 | +241.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.19 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.45 | 0.54 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 110.39 | 112.39 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.12 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.32 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 0.69 | 0.75 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.66 | 2.91 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 2.81 | 4.63 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 20.00 | 22.57 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 168.98 | 207.63 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.43 | 0.46 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 1.52 | 1.57 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 30.39 | 34.03 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 174.94 | 186.51 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 626.44 | 5.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 523.81 | 9.75 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 5747.60 | 56.11 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 5039.74 | 85.22 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 14.01 | 16.16 | 100% | 1000.00 | +728.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 28.39 | 111.19 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 36.79 | 51.30 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 74.94 | 262.92 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.19 | 0.28 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.60 | 0.68 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 1.73 | 2.05 | 100% | 2588.00 | +2238.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 128.31 | 130.51 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.14 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.34 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 0.59 | 0.65 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 11.94 | 13.48 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 14.63 | 21.26 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 138.64 | 144.62 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 198.43 | 231.53 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.89 | 2.99 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 3.93 | 6.23 | 100% | 794.00 | -3498.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 6.26 | 7.33 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 121.76 | 123.05 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2588.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 794.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 259.93 | 1.63 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 530.61 | 9.99 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 2490.22 | 35.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 4811.34 | 79.23 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.74 | 6.08 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 4.95 | 7.75 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 48.28 | 191.27 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 119.50 | 250.25 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.28 | 0.33 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.74 | 0.80 | 100% | 13188.00 | +2616.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 1.22 | 1.76 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 227.57 | 234.96 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.14 | 0.16 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.31 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 0.73 | 0.77 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.47 | 0.49 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.59 | 2.90 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 24.58 | 25.92 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 105.23 | 134.56 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.34 | 0.38 | 100% | 2137.00 | +1237.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.39 | 2.42 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 23.78 | 24.41 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 68.22 | 75.74 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 13188.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2137.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2089.96 | 3.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 1913.12 | 39.99 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 11435.06 | 88.82 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 111039.48 | 816.10 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 9.50 | 10.34 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 38.61 | 59.75 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 93.80 | 95.97 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 187.85 | 745.77 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.10 | 0.12 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.24 | 0.56 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.39 | 0.43 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 1444.45 | 1534.38 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.12 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.20 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.39 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 1110.33 | 1188.97 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 1.95 | 2.17 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 4.22 | 5.09 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 5.06 | 7.32 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 5.84 | 22.29 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 3.91 | 3.94 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 6.04 | 19.64 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 400.49 | 421.44 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | no | 1429.96 | 1477.70 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 248.00 | 2.00 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 1030.11 | 6.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 449.65 | 7.39 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 3103.93 | 54.26 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 3.61 | 6.33 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 5.22 | 7.56 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 32.05 | 107.30 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 34.45 | 63.23 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.42 | 0.45 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 2.58 | 9.15 | 100% | 149.00 | +123.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 11.26 | 16.98 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.23 | 0.27 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 0.39 | 0.45 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 0.75 | 0.86 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 1.53 | 1.61 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.94 | 2.55 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 2.87 | 3.77 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 3.75 | 5.13 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 56.74 | 59.04 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 1.14 | 1.20 | 100% | 3585.00 | +3165.00 | pass |
| [Ty](latest-results/ty-20260830T060523Z.json) | yes | 1.37 | 1.43 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260830T060523Z.json) | yes | 23.10 | 26.62 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260830T060523Z.json) | yes | 167.31 | 204.47 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 467.00).
- client session hover: result differences detected (149.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 3585.00, 420.00, 880.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | no | 144.54 | 0.20 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.72 | 0.85 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.15 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 1283.25 | 19.40 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 20.45 | 45.75 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 34.04 | 36.80 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260830T060523Z.json) | yes | 3.70 | 3.95 | 100% | 75.00 | 0.00 | pass |
