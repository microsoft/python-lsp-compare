# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260912T060455Z.json`

- Generated at: 20260912T060455Z
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
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 6 | 4824.55 | 3.90 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | no | 8 | 16364.27 | 36.72 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 6 | 38374.25 | 73.80 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 6 | 220485.23 | 374.47 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 395.80 | 3.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 1147.19 | 25.89 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 4628.09 | 80.21 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 7859.90 | 113.79 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 1.60 | 1.70 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 6.32 | 9.74 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 94.67 | 375.82 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 213.77 | 460.56 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.32 | 0.33 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 1.05 | 1.40 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 2.48 | 2.70 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 180.72 | 185.18 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.23 | 0.26 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.39 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 1.09 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 4.41 | 4.65 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 10.51 | 13.49 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 25.91 | 32.01 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 361.56 | 479.82 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 3.88 | 4.57 | 100% | 267.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 6.16 | 15.50 | 100% | 2546.00 | +2268.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 31.72 | 34.84 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 168.93 | 174.50 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 248.94 | 2.52 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 306.30 | 4.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 1459.34 | 14.44 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 7778.46 | 175.05 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 4.61 | 7.30 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 4.91 | 7.42 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 15.62 | 61.00 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 213.00 | 655.62 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.23 | 0.24 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.27 | 0.30 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.53 | 0.57 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 157.06 | 161.96 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.22 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 4.36 | 4.68 | 100% | 104.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 5.85 | 13.77 | 100% | 83.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 27.34 | 31.19 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 257.37 | 300.16 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 1.45 | 3.83 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 2.88 | 2.95 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 39.32 | 47.01 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 246.74 | 248.11 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 818.88 | 7.58 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 1150.11 | 28.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 8014.60 | 141.28 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 11474.68 | 183.83 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 18.36 | 21.26 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 84.49 | 283.35 | 100% | 271.20 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 84.52 | 333.25 | 100% | 16.00 | -255.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 100.14 | 242.49 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.25 | 0.27 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.74 | 0.80 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 4.07 | 5.88 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 190.93 | 192.50 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.21 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 1.07 | 1.12 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 2.93 | 2.95 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 16.29 | 17.43 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 41.12 | 69.75 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 229.87 | 237.94 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 821.30 | 1310.67 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 2.79 | 2.85 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 8.64 | 14.98 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 12.22 | 14.93 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 184.39 | 186.14 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 352.19 | 2.48 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 1018.57 | 24.68 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 3638.99 | 47.93 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 7036.37 | 116.73 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 3.33 | 7.63 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 7.42 | 13.09 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 112.02 | 437.36 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 177.63 | 461.49 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.39 | 0.40 | 100% | 10621.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 1.17 | 1.30 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 2.28 | 2.65 | 100% | 15232.00 | +4660.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 328.74 | 331.91 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.24 | 0.27 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.42 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.52 | 1.21 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 1.11 | 1.21 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 4.36 | 4.70 | 100% | 23.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 6.39 | 21.52 | 100% | 17.00 | -21.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 37.97 | 38.24 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 139.30 | 199.54 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 2.19 | 3.44 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 4.09 | 4.25 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 38.20 | 39.06 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 91.32 | 97.81 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 2698.40 | 4.82 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 15610.64 | 106.85 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 5812.15 | 185.94 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 184732.86 | 1586.31 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 11.47 | 12.12 | 100% | 775.00 | +652.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 47.92 | 78.50 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 150.79 | 153.99 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 904.16 | 3586.61 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.24 | 0.27 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.50 | 0.57 | 100% | 34.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 2.20 | 2.95 | 100% | 48.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 2809.23 | 2850.44 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.30 | 0.31 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.42 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 2257.56 | 2292.89 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 2.66 | 2.85 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 6.23 | 7.12 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 6.41 | 7.46 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 8.53 | 26.32 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 5.69 | 5.90 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 14.55 | 24.89 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 479.17 | 503.08 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | no | 2711.33 | 2735.50 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 775.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 310.34 | 2.69 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 1562.52 | 9.54 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 898.79 | 14.92 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 5063.03 | 113.63 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 5.90 | 8.69 | 100% | 467.00 | +453.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 6.01 | 10.63 | 100% | 14.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 65.24 | 184.65 | 100% | 487.80 | +473.80 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 80.83 | 137.57 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.54 | 0.59 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 5.39 | 19.00 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 154.96 | 225.17 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.33 | 0.35 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 0.56 | 0.64 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 0.81 | 0.96 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 3.48 | 4.14 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.58 | 0.61 | 100% | 32.00 | -173.00 | pass |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 4.10 | 4.48 | 100% | 225.00 | +20.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 4.82 | 7.54 | 100% | 205.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 90.53 | 91.46 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260912T060455Z.json) | yes | 2.64 | 2.93 | 100% | 1613.00 | +1193.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 3.06 | 5.55 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20260912T060455Z.json) | yes | 35.54 | 39.37 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260912T060455Z.json) | yes | 238.36 | 244.55 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1613.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | no | 227.58 | 0.33 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 1.01 | 1.07 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.23 | 0.24 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 0.25 | 0.27 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 5803.59 | 27.00 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 15.97 | 26.50 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 57.78 | 59.06 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260912T060455Z.json) | yes | 7.26 | 8.03 | 100% | 75.00 | 0.00 | pass |
