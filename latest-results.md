# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261111T060330Z.json`

- Generated at: 20261111T060330Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.100 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.100/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 6 | 3688.61 | 4.12 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | no | 8 | 7704.05 | 8.25 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 6 | 39989.80 | 75.50 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 6 | 268428.81 | 363.76 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 507.56 | 4.16 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 717.39 | 5.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 4643.23 | 77.28 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 7895.66 | 110.44 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 1.98 | 2.23 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 5.05 | 8.26 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 5.47 | 8.69 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 191.88 | 415.02 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.28 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 1.15 | 1.46 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 2.64 | 3.05 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 182.97 | 185.07 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.38 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 1.10 | 1.17 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 4.72 | 4.84 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 13.22 | 15.83 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 14.25 | 20.67 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 348.17 | 464.48 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 3.43 | 4.40 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 5.14 | 5.32 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 31.24 | 34.11 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 171.55 | 172.31 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 284.22 | 1.85 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 255.16 | 2.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 1513.00 | 14.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 7754.36 | 171.35 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 3.49 | 5.20 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 5.11 | 8.49 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 5.13 | 8.83 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 190.78 | 535.16 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.21 | 0.26 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.51 | 0.55 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 1.05 | 2.25 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 159.54 | 160.26 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 1.13 | 1.22 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 1.70 | 2.84 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 3.63 | 3.91 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 27.01 | 28.24 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 255.06 | 294.00 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 1.95 | 1.98 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 2.79 | 4.36 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 40.48 | 47.34 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 250.22 | 252.79 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 723.50 | 5.65 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 805.71 | 8.33 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 7939.18 | 137.06 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 11765.93 | 183.75 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 4.51 | 8.07 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 19.44 | 23.56 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 60.12 | 78.78 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 89.53 | 298.37 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.24 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.67 | 0.74 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 6.22 | 8.80 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 194.66 | 196.50 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.24 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.40 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 1.10 | 1.13 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 10.37 | 10.80 | 100% | 274.00 | -166.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 17.60 | 18.11 | 100% | 448.00 | +8.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 244.29 | 276.42 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 815.70 | 1282.53 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 4.21 | 4.61 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 6.92 | 11.35 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 12.42 | 15.56 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 185.11 | 186.81 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 586.99 | 1.90 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 394.10 | 2.80 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 3940.34 | 53.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 7270.42 | 101.45 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 2.10 | 6.96 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 3.75 | 9.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 18.69 | 22.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 96.51 | 166.69 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.36 | 0.39 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 1.10 | 1.16 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 1.53 | 1.99 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 330.18 | 340.19 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.19 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 1.19 | 1.29 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 5.41 | 6.61 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 5.49 | 11.17 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 40.43 | 40.76 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 146.75 | 185.82 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.54 | 0.57 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 4.26 | 4.30 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 38.96 | 40.27 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 101.60 | 115.86 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 1559.80 | 3.77 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 1348.99 | 3.96 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 16558.89 | 113.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 232799.11 | 1560.50 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 6.53 | 25.37 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 12.13 | 14.78 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 53.39 | 84.79 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 148.85 | 157.51 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.20 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.51 | 0.58 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 2932.09 | 2978.91 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.43 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 2118.47 | 2145.49 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 2.82 | 3.01 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 3.79 | 4.21 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 6.85 | 8.84 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 8.05 | 15.34 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 3.45 | 3.57 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 3.87 | 9.16 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 507.60 | 528.12 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | no | 2600.28 | 2626.55 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 377.09 | 3.27 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 722.55 | 4.79 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 1568.42 | 9.70 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 4770.08 | 101.74 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 5.31 | 10.03 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 6.76 | 10.65 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 15.98 | 28.72 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 68.54 | 111.18 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 0.19 | 0.24 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.51 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 2.81 | 10.57 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 109.86 | 223.61 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.33 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 0.94 | 1.57 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 1.52 | 1.87 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 4.16 | 5.20 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 1.42 | 3.55 | 100% | 54.00 | -151.00 | pass |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 4.79 | 5.07 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 4.97 | 5.76 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 88.53 | 89.12 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261111T060330Z.json) | yes | 3.08 | 3.13 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 3.42 | 4.86 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261111T060330Z.json) | yes | 36.76 | 44.49 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261111T060330Z.json) | yes | 237.60 | 240.55 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | no | 240.22 | 0.31 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.96 | 1.02 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 0.29 | 0.42 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 2869.38 | 73.43 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 37.72 | 75.19 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 141.51 | 157.33 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261111T060330Z.json) | yes | 41.05 | 49.08 | 100% | 75.00 | 0.00 | pass |
