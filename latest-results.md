# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261027T060537Z.json`

- Generated at: 20261027T060537Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.92 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.92/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 6 | 2250.65 | 2.56 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | no | 8 | 3859.48 | 3.26 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 6 | 24008.17 | 34.88 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 6 | 168861.10 | 236.67 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 362.18 | 2.71 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 427.86 | 2.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 2709.19 | 40.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 4716.90 | 61.21 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 1.15 | 1.50 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.62 | 3.36 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 3.70 | 6.14 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 77.03 | 185.35 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.17 | 0.20 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.82 | 1.13 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.78 | 4.92 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 114.56 | 115.58 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.11 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.17 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.22 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 0.56 | 0.61 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 2.57 | 2.75 | 0% | 0.00 | -168.00 | fail (10) |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 8.22 | 8.44 | 100% | 168.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 9.32 | 10.50 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 179.76 | 285.95 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.72 | 2.08 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.82 | 2.92 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 17.69 | 21.13 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 111.32 | 116.54 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 163.89 | 0.95 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 161.42 | 1.42 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 1038.75 | 11.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 4624.27 | 102.08 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1.40 | 2.80 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.98 | 4.77 | 100% | 262.00 | +252.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 3.83 | 5.87 | 100% | 10.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 101.31 | 276.97 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.11 | 0.13 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.38 | 0.43 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.79 | 2.65 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 106.61 | 110.17 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.09 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.12 | 0.14 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.30 | 0.39 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 0.64 | 0.69 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1.65 | 4.25 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.57 | 3.21 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 23.08 | 25.96 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 150.94 | 187.22 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.79 | 2.18 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 1.36 | 1.40 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 28.90 | 33.73 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 150.90 | 156.17 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 377.84 | 4.06 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 526.86 | 5.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 5897.06 | 48.30 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 4837.62 | 80.55 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.70 | 5.57 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 11.16 | 13.12 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 34.54 | 48.31 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 60.10 | 202.70 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.15 | 0.19 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.65 | 0.81 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1.37 | 1.54 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 119.13 | 122.36 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.10 | 0.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.11 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.24 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 0.59 | 0.64 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 11.57 | 12.26 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 15.74 | 25.47 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 132.20 | 147.63 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 173.03 | 199.62 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.40 | 0.47 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.18 | 2.23 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 7.46 | 8.49 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 116.27 | 118.06 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 241.67 | 1.60 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 348.27 | 1.91 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 2437.68 | 33.80 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 4334.54 | 55.96 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.13 | 5.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 3.32 | 5.13 | 100% | 15.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 12.20 | 13.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 27.76 | 34.81 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.23 | 0.27 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1.02 | 2.23 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 1.32 | 1.66 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 200.32 | 215.52 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.11 | 0.12 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.24 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.30 | 0.80 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 0.67 | 0.71 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.75 | 4.33 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 3.05 | 3.89 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 27.28 | 33.37 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 88.88 | 114.85 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.17 | 4.70 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.46 | 2.51 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 23.76 | 24.63 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 66.34 | 75.34 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 719.50 | 2.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 827.66 | 2.95 | 5 | 25 | 80% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 10914.87 | 69.16 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 147605.12 | 1071.33 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 4.73 | 18.46 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 7.43 | 8.49 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 43.97 | 64.31 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 81.25 | 90.29 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.09 | 0.10 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.15 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.32 | 0.38 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 2012.66 | 2071.88 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.09 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.12 | 0.13 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.31 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 1557.07 | 1676.29 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 1.50 | 1.58 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.53 | 3.00 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.82 | 9.48 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 4.65 | 5.75 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 2.18 | 2.33 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 7.02 | 16.98 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 296.55 | 400.01 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | no | 1704.17 | 1732.02 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 420.16 | 1.87 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 239.02 | 2.10 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 1010.61 | 6.32 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 2742.65 | 48.92 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 4.11 | 6.12 | 100% | 496.00 | +482.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 4.28 | 7.18 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 5.44 | 9.70 | 100% | 253.80 | +239.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 32.15 | 60.49 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.11 | 0.12 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.40 | 0.48 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 2.09 | 8.03 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 4.21 | 4.64 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.16 | 0.18 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 0.80 | 1.51 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 0.87 | 0.98 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 4.50 | 8.65 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.41 | 0.45 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 3.17 | 4.09 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 3.44 | 3.87 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 59.24 | 76.35 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1.26 | 2.49 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20261027T060537Z.json) | yes | 1.97 | 2.02 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20261027T060537Z.json) | yes | 22.95 | 25.69 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261027T060537Z.json) | yes | 144.48 | 147.22 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 253.80, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | no | 138.85 | 0.16 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.54 | 0.64 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.10 | 0.12 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.12 | 0.15 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.11 | 0.11 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.12 | 0.13 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 0.12 | 0.14 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 1154.95 | 19.74 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 9.39 | 21.41 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 41.66 | 57.79 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261027T060537Z.json) | yes | 8.18 | 12.87 | 100% | 75.00 | 0.00 | pass |
