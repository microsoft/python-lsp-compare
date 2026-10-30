# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261030T060358Z.json`

- Generated at: 20261030T060358Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.95 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.95/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 6 | 2591.56 | 2.82 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | no | 8 | 5430.14 | 7.42 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 6 | 23683.93 | 32.81 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 6 | 156240.83 | 214.57 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 493.40 | 2.78 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 384.19 | 3.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 2809.42 | 42.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 4501.50 | 59.95 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 1.27 | 1.59 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.48 | 3.82 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 3.56 | 5.59 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 90.56 | 172.73 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.16 | 0.19 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.99 | 1.33 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.22 | 1.35 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 106.52 | 109.44 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.10 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.30 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 0.59 | 0.61 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 2.37 | 2.50 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 7.73 | 7.97 | 100% | 168.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 11.82 | 13.39 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 187.59 | 292.43 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.37 | 5.40 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 3.68 | 4.32 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 18.78 | 23.93 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 99.71 | 102.35 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 180.57 | 1.14 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 172.65 | 1.52 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 983.04 | 10.15 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 4255.23 | 95.80 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.75 | 2.06 | 100% | 15.00 | +5.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 3.37 | 5.04 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 3.46 | 5.54 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 94.56 | 210.04 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.10 | 0.11 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.22 | 0.47 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.35 | 0.40 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 92.81 | 95.51 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.08 | 0.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.27 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 0.59 | 0.62 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.60 | 3.11 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 3.33 | 7.39 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 18.89 | 20.33 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 144.83 | 183.91 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.31 | 2.65 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 1.34 | 1.38 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 27.89 | 33.38 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 146.18 | 149.24 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 569.76 | 5.38 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 592.55 | 8.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 5522.90 | 48.78 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 4366.32 | 74.50 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 3.54 | 5.72 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 12.25 | 14.67 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 31.56 | 43.33 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 59.99 | 204.73 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.14 | 0.17 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.62 | 0.71 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.88 | 2.93 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 116.60 | 136.19 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.09 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.27 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 0.56 | 0.62 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.95 | 2.96 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 12.03 | 12.95 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 21.18 | 46.76 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 117.00 | 120.92 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 175.50 | 189.81 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.36 | 2.68 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 7.53 | 9.88 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 10.49 | 10.77 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 106.77 | 109.31 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 277.50 | 1.83 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 436.17 | 2.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 2613.11 | 34.50 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 4046.06 | 53.14 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.86 | 5.22 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.62 | 6.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 14.22 | 19.25 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 37.28 | 74.77 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.22 | 0.27 | 100% | 10621.00 | +42.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 1.29 | 1.62 | 100% | 10579.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.75 | 3.45 | 100% | 15239.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 186.04 | 194.86 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.10 | 0.11 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.36 | 0.42 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.66 | 2.20 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 0.68 | 0.79 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 3.62 | 4.91 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 7.04 | 16.80 | 100% | 40.00 | +2.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 21.29 | 22.11 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 90.83 | 119.47 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.86 | 2.86 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.60 | 2.71 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 20.43 | 20.78 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 65.77 | 73.62 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 937.02 | 2.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1008.92 | 2.92 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 10735.17 | 54.61 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 136363.65 | 954.19 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 4.86 | 19.02 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 7.99 | 9.64 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 41.43 | 56.77 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 74.72 | 80.99 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.08 | 0.09 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.12 | 0.15 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.35 | 0.42 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 1798.96 | 1858.14 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 1349.92 | 1409.74 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.26 | 2.64 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 1.57 | 1.84 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.56 | 3.06 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 3.80 | 4.29 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 2.19 | 2.21 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 8.33 | 14.84 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 227.20 | 243.49 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | no | 1545.79 | 1617.15 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 250.43 | 2.22 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 462.36 | 3.07 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 1020.28 | 6.55 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 2708.07 | 49.82 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 3.93 | 6.28 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 4.64 | 7.35 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 10.40 | 21.99 | 100% | 253.80 | +239.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 41.77 | 95.34 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.10 | 0.11 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.37 | 0.43 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2.21 | 8.50 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 6.55 | 9.13 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.17 | 0.20 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 0.53 | 0.68 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 0.84 | 0.98 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 1.72 | 2.13 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.85 | 2.28 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 3.30 | 4.32 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 3.67 | 4.16 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 47.34 | 53.17 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 1.73 | 2.99 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261030T060358Z.json) | yes | 1.85 | 1.91 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261030T060358Z.json) | yes | 24.61 | 30.03 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261030T060358Z.json) | yes | 151.69 | 188.19 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 253.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | no | 143.58 | 0.15 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.51 | 0.62 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.09 | 0.09 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.10 | 0.12 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.09 | 0.10 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 0.09 | 0.11 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 2112.60 | 66.02 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 53.71 | 82.87 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 105.29 | 117.99 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261030T060358Z.json) | yes | 39.07 | 45.70 | 100% | 75.00 | 0.00 | pass |
