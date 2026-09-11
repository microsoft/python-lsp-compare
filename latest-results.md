# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260911T060505Z.json`

- Generated at: 20260911T060505Z
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
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 6 | 4851.36 | 3.87 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | no | 8 | 16853.13 | 37.12 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 6 | 39165.06 | 74.28 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 6 | 223919.22 | 376.03 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 419.37 | 3.32 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 1235.87 | 26.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 4670.33 | 76.80 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 8076.25 | 114.94 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 1.88 | 2.22 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 5.97 | 8.56 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 87.27 | 337.96 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 218.00 | 524.67 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.35 | 0.40 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 1.17 | 1.50 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 5.12 | 6.04 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 181.33 | 183.09 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.38 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 1.10 | 1.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 5.72 | 5.95 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 4.52 | 4.82 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 10.59 | 13.61 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 32.20 | 74.85 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 345.47 | 453.18 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 3.13 | 5.12 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 3.57 | 3.63 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 30.98 | 32.47 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 169.75 | 176.81 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 246.86 | 2.41 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 267.58 | 4.03 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 1484.14 | 14.79 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 7862.39 | 175.92 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 4.53 | 6.60 | 100% | 261.00 | +251.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 4.85 | 8.03 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 16.36 | 63.45 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 220.62 | 630.65 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.40 | 0.45 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.55 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 156.60 | 158.45 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.21 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.41 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.41 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 1.08 | 1.15 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 2.06 | 2.27 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 4.25 | 4.48 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 26.58 | 29.29 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 254.05 | 283.26 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.90 | 1.09 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 2.82 | 2.84 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 41.58 | 46.91 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 247.27 | 248.79 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 825.48 | 7.72 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 1292.35 | 32.38 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 8029.37 | 138.88 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 11638.47 | 183.21 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 18.71 | 21.88 | 100% | 1000.00 | +728.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 81.14 | 172.80 | 100% | 6.00 | -265.20 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 91.19 | 361.96 | 100% | 16.00 | -255.20 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 93.34 | 310.33 | 100% | 271.20 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.27 | 0.30 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.82 | 0.92 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 5.07 | 5.88 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 193.30 | 195.33 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.21 | 0.22 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.45 | 0.54 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 1.04 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 3.92 | 5.80 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 16.67 | 17.25 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 48.87 | 77.16 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 231.23 | 244.19 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 810.14 | 1274.57 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 2.75 | 2.78 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 11.29 | 14.82 | 100% | 4292.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 12.85 | 18.84 | 100% | 943.00 | -3349.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 187.71 | 195.02 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 350.12 | 2.46 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 856.17 | 18.44 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 3643.25 | 48.90 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 7110.60 | 124.01 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 3.30 | 7.32 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 6.69 | 10.73 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 87.75 | 350.01 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 211.10 | 460.89 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.39 | 0.40 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 1.08 | 1.09 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 1.26 | 1.54 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 330.37 | 337.48 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.42 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 1.14 | 1.29 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 2.01 | 3.76 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 4.39 | 4.97 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 38.70 | 39.76 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 143.42 | 202.88 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 1.10 | 2.88 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 4.04 | 4.12 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 38.73 | 39.56 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 92.71 | 97.15 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 2693.83 | 4.61 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 16183.23 | 112.83 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 5364.81 | 168.29 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 187734.63 | 1584.76 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 10.90 | 11.91 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 51.16 | 82.91 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 148.41 | 150.25 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 827.56 | 3309.37 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.22 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.31 | 0.55 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.47 | 0.54 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 2795.79 | 2838.49 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.28 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.43 | 0.53 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 2236.93 | 2309.36 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 2.72 | 2.89 | 0% | 0.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 2.73 | 9.43 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 5.94 | 6.08 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 6.51 | 7.65 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 5.64 | 5.76 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 10.69 | 32.82 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 505.57 | 547.82 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | no | 2739.97 | 2775.78 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 315.70 | 2.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 1545.63 | 9.14 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 906.06 | 13.56 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 5105.97 | 117.66 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 4.54 | 8.17 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 5.86 | 8.82 | 100% | 467.00 | +453.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 56.03 | 184.37 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 104.05 | 169.67 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.53 | 0.61 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 5.41 | 18.99 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 152.06 | 211.30 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.34 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 0.56 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 0.86 | 1.05 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 4.10 | 5.34 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 3.75 | 4.67 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 4.27 | 5.06 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 4.59 | 6.15 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 90.69 | 93.72 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 2.28 | 4.47 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260911T060505Z.json) | yes | 2.51 | 2.51 | 100% | 1613.00 | +1193.00 | pass |
| [Pyright](latest-results/pyright-20260911T060505Z.json) | yes | 35.19 | 39.57 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260911T060505Z.json) | yes | 237.43 | 239.85 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | no | 220.52 | 0.42 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 1.78 | 4.24 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.20 | 0.22 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.24 | 0.26 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 0.24 | 0.24 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 6709.76 | 67.24 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 14.93 | 23.79 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 165.71 | 181.94 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260911T060505Z.json) | yes | 21.08 | 28.14 | 100% | 75.00 | 0.00 | pass |
