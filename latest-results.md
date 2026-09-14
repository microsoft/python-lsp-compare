# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260914T060721Z.json`

- Generated at: 20260914T060721Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.80 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.80/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 6 | 4055.76 | 3.07 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | no | 8 | 10484.73 | 22.09 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 6 | 23634.45 | 34.07 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 6 | 135299.19 | 203.50 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 321.26 | 2.40 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 779.81 | 16.41 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 2937.88 | 47.34 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 5703.23 | 75.47 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 1.50 | 1.62 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 4.22 | 7.23 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 64.70 | 255.52 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 134.11 | 286.84 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.26 | 0.30 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.94 | 1.07 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 1.75 | 2.11 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 124.16 | 124.82 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.11 | 0.12 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.17 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.27 | 0.37 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 0.64 | 0.73 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 3.12 | 3.32 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 7.32 | 7.76 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 13.61 | 14.46 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 211.06 | 324.96 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 1.90 | 6.58 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2.76 | 2.83 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 20.23 | 22.18 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 115.30 | 116.39 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 192.42 | 1.95 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 219.65 | 3.56 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 961.98 | 9.68 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 5075.83 | 114.27 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 3.65 | 5.65 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 3.83 | 5.64 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 11.24 | 42.53 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 136.12 | 409.45 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.19 | 0.21 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.27 | 0.33 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.44 | 0.49 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 107.90 | 109.19 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.26 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 0.59 | 0.63 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 2.65 | 6.74 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 3.36 | 3.63 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 18.09 | 21.29 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 161.85 | 195.00 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2.19 | 2.22 | 100% | 100.00 | +17.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 3.44 | 10.54 | 100% | 858.00 | +775.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 25.96 | 31.88 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 164.91 | 165.34 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 630.72 | 5.61 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 691.67 | 16.90 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 5742.46 | 53.07 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 5057.94 | 85.50 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 13.77 | 16.23 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 38.47 | 52.12 | 100% | 6.00 | -265.20 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 55.15 | 189.22 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 62.97 | 251.26 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.18 | 0.26 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.59 | 0.62 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 1.45 | 1.58 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 131.50 | 133.82 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.09 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.13 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.33 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 0.65 | 0.70 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 11.79 | 12.71 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 19.47 | 36.30 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 134.03 | 140.66 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 200.58 | 224.47 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.52 | 0.57 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2.17 | 2.21 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 8.68 | 12.12 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 122.83 | 124.88 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 272.66 | 1.89 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 564.90 | 11.39 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 2400.24 | 34.12 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 4635.06 | 81.31 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2.82 | 6.18 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 5.14 | 8.33 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 55.35 | 220.83 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 123.05 | 238.11 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.29 | 0.33 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.70 | 0.74 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 1.04 | 1.27 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 229.25 | 240.02 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.10 | 0.11 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.14 | 0.17 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.27 | 0.35 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 0.92 | 1.19 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.47 | 0.55 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 3.22 | 3.59 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 26.56 | 27.66 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 100.55 | 137.55 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.32 | 0.34 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 3.01 | 3.06 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 26.79 | 27.88 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 63.60 | 76.81 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2370.24 | 4.21 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 10532.41 | 53.68 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 3652.55 | 112.12 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 111682.83 | 809.20 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 9.72 | 11.03 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 39.12 | 59.97 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 91.63 | 94.39 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 540.72 | 2162.28 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.12 | 0.13 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.39 | 1.08 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.41 | 0.48 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 1473.63 | 1498.48 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.16 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.21 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.33 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 1094.71 | 1153.78 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 1.85 | 2.06 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 4.02 | 4.40 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 5.57 | 6.77 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 7.08 | 14.66 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 5.16 | 5.27 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 12.51 | 29.97 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 224.50 | 234.15 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | no | 1384.17 | 1414.73 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 268.46 | 2.34 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 1059.48 | 6.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 577.95 | 11.35 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 3144.30 | 55.26 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 4.18 | 6.17 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 5.25 | 7.75 | 100% | 467.00 | +453.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 34.16 | 58.47 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 45.98 | 138.99 | 100% | 487.80 | +473.80 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.18 | 0.21 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.50 | 0.56 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 5.29 | 19.36 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 11.79 | 19.60 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.26 | 0.32 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 0.55 | 0.83 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 0.66 | 0.73 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 1.96 | 2.05 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 3.30 | 4.14 | 100% | 205.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 3.32 | 4.31 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 3.60 | 4.01 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 53.69 | 54.57 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 1.91 | 3.99 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260914T060721Z.json) | yes | 2.13 | 2.18 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260914T060721Z.json) | yes | 24.05 | 27.23 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260914T060721Z.json) | yes | 174.70 | 206.65 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | no | 163.34 | 0.28 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 1.01 | 2.14 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.14 | 0.15 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.18 | 0.18 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.18 | 0.19 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 0.20 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 3834.86 | 14.95 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 8.49 | 15.07 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 32.24 | 34.47 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260914T060721Z.json) | yes | 4.12 | 4.62 | 100% | 75.00 | 0.00 | pass |
