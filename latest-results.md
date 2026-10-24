# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261024T060509Z.json`

- Generated at: 20261024T060509Z
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
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 6 | 2195.06 | 2.48 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | no | 8 | 3792.55 | 3.12 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 6 | 21390.53 | 29.42 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 6 | 165440.76 | 231.05 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 337.56 | 2.50 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 435.92 | 3.87 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 2632.47 | 39.99 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 4741.85 | 61.82 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 1.05 | 1.28 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.73 | 3.81 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 3.84 | 6.58 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 92.26 | 218.97 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.17 | 0.20 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.79 | 1.06 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.92 | 1.10 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 109.92 | 111.65 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.09 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.10 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.20 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 0.56 | 0.61 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 2.27 | 2.45 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 7.84 | 9.85 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 14.44 | 35.31 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 178.62 | 278.46 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.15 | 3.24 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 3.36 | 3.41 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 16.48 | 17.02 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 104.07 | 107.67 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 157.11 | 0.95 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 162.94 | 1.51 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 937.48 | 9.33 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 4249.72 | 94.16 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.58 | 3.27 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.60 | 4.31 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 2.84 | 4.45 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 90.58 | 241.32 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.11 | 0.13 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.13 | 0.16 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.36 | 0.40 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 95.10 | 95.42 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.10 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.25 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 0.58 | 0.64 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.80 | 0.83 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.83 | 3.12 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 17.37 | 18.10 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 140.82 | 170.79 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.17 | 2.35 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 1.89 | 1.90 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 25.86 | 29.64 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 143.70 | 144.44 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 383.94 | 4.05 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 521.54 | 4.70 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 5031.00 | 42.17 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 4367.79 | 79.55 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.35 | 4.66 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 10.38 | 12.10 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 48.35 | 162.07 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 55.41 | 128.83 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.15 | 0.18 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.44 | 0.49 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.85 | 5.57 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 114.66 | 115.90 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.10 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.27 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 0.60 | 0.65 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 3.55 | 5.35 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 10.21 | 11.75 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 12.13 | 22.32 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 117.75 | 120.64 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 155.93 | 185.88 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.40 | 0.45 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.69 | 2.73 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 5.86 | 6.71 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 109.32 | 109.65 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 302.37 | 0.81 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 241.86 | 1.80 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 2444.34 | 33.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 4050.10 | 49.88 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.05 | 5.06 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.17 | 4.54 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 12.54 | 16.71 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 25.45 | 32.87 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.22 | 0.26 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.61 | 0.63 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 1.17 | 1.22 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 181.94 | 188.55 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.10 | 0.12 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.11 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.34 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 0.62 | 0.66 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.90 | 0.98 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 3.50 | 4.05 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 19.49 | 19.67 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 89.10 | 111.59 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.28 | 0.29 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 3.13 | 3.16 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 21.92 | 27.04 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 64.97 | 74.85 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 705.84 | 2.47 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 872.51 | 4.38 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 9405.12 | 45.76 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 145330.79 | 1052.54 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 4.99 | 19.51 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 6.43 | 7.93 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 38.71 | 55.67 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 84.98 | 94.47 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.32 | 0.34 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.83 | 3.87 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 1979.34 | 2109.48 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.26 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.95 | 3.71 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 1479.89 | 1580.16 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 1.67 | 1.79 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.92 | 3.21 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 4.04 | 4.78 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 11.78 | 22.51 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.34 | 0.39 | 100% | 33.00 | +3.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.74 | 2.82 | 100% | 7.00 | -23.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 185.49 | 197.72 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | no | 1716.80 | 1775.46 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 225.33 | 1.90 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 449.03 | 2.85 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 940.14 | 5.63 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 2700.50 | 48.34 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 3.32 | 5.49 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 3.63 | 5.63 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 8.96 | 19.52 | 100% | 253.80 | +239.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 32.31 | 56.12 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.11 | 0.13 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.33 | 0.37 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 2.08 | 8.01 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 5.58 | 8.20 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.17 | 0.20 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 0.49 | 0.62 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 0.98 | 1.09 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 1.87 | 2.44 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.72 | 2.70 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 2.56 | 3.31 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 2.95 | 3.23 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 58.63 | 74.15 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1.31 | 2.51 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261024T060509Z.json) | yes | 1.84 | 1.87 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261024T060509Z.json) | yes | 21.43 | 23.82 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261024T060509Z.json) | yes | 143.31 | 145.36 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 253.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | no | 130.78 | 0.16 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.54 | 0.67 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.09 | 0.09 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.12 | 0.15 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.11 | 0.11 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.11 | 0.11 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 0.13 | 0.14 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 1060.90 | 14.03 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 5.98 | 7.53 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 32.75 | 35.29 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261024T060509Z.json) | yes | 3.34 | 3.58 | 100% | 75.00 | 0.00 | pass |
