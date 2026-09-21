# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260921T060722Z.json`

- Generated at: 20260921T060722Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.82 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.82/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 1.3.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/venv/bin/pyrefly |
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
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6 | 5565.98 | 4.82 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | no | 8 | 16900.74 | 37.50 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 6 | 39208.39 | 76.41 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 6 | 215805.28 | 369.78 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 548.30 | 5.04 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 1307.24 | 25.72 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 4951.62 | 86.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 8025.24 | 119.80 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 1.67 | 1.88 | 100% | 223.00 | +22.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 7.35 | 12.51 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 91.55 | 363.66 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 238.91 | 469.62 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.33 | 0.35 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 1.17 | 1.51 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.55 | 2.78 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 183.33 | 184.51 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.44 | 0.50 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 1.05 | 1.10 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 4.60 | 4.72 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 16.38 | 18.03 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 28.70 | 79.19 | 100% | 149.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 392.49 | 523.13 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 5.60 | 6.64 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6.61 | 7.15 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 29.83 | 32.52 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 171.10 | 173.17 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 149.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 272.79 | 2.74 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 319.39 | 5.58 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 1424.56 | 13.77 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 8147.20 | 179.58 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 4.74 | 7.86 | 100% | 10.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 5.22 | 7.46 | 100% | 261.00 | +251.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 18.47 | 64.82 | 100% | 15.00 | +5.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 225.31 | 689.91 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.54 | 0.63 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.89 | 5.34 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 162.24 | 163.33 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.20 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.39 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.83 | 6.67 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.14 | 4.89 | 100% | 83.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 4.87 | 5.46 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 25.53 | 27.57 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 259.81 | 304.33 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 1.57 | 4.31 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 3.20 | 3.27 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 37.65 | 43.63 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 249.46 | 260.02 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 261.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00, 83.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 909.36 | 9.33 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 1146.21 | 28.26 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 7988.09 | 140.12 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 11137.02 | 178.98 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 19.62 | 23.02 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 78.23 | 267.47 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 79.18 | 160.04 | 100% | 6.00 | -265.20 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 99.11 | 391.31 | 100% | 16.00 | -255.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.30 | 0.35 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.65 | 0.73 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 4.67 | 5.99 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 197.15 | 205.38 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.44 | 0.51 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 1.04 | 1.08 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.32 | 3.43 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 20.40 | 20.83 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 28.87 | 52.76 | 100% | 256.00 | -184.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 237.44 | 244.50 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 803.02 | 1258.21 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6.12 | 6.28 | 100% | 4441.00 | +149.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 6.36 | 22.05 | 100% | 943.00 | -3349.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 12.56 | 13.38 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 185.77 | 186.24 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (256.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 384.84 | 2.78 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 826.49 | 17.66 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 3678.16 | 50.00 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 7220.96 | 126.76 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 3.59 | 8.08 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 8.15 | 13.97 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 85.72 | 341.80 | 100% | 15.00 | +14.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 224.77 | 494.00 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.41 | 0.44 | 100% | 10621.00 | +49.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 1.04 | 1.06 | 100% | 15232.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 1.25 | 1.36 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 329.41 | 330.37 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.27 | 0.29 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.40 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 1.13 | 1.35 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.74 | 0.78 | 100% | 17.00 | -21.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 5.17 | 6.32 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 38.76 | 38.95 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 145.65 | 208.58 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.52 | 0.56 | 100% | 2246.00 | +1346.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 4.53 | 4.57 | 100% | 958.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 39.74 | 41.12 | 0% | 0.00 | -900.00 | fail (10) |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 94.56 | 103.53 | 100% | 900.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10621.00, 15232.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 17.00, 23.00, 38.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2246.00, 900.00, 958.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 3026.41 | 5.67 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 16424.65 | 119.67 | 5 | 25 | 80% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 5582.73 | 176.09 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 179571.21 | 1553.94 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 14.38 | 15.99 | 100% | 777.00 | +654.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 55.48 | 85.02 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 147.98 | 151.59 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 861.55 | 3445.27 | 100% | 15.00 | -108.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.21 | 0.22 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.38 | 0.81 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.48 | 0.59 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 2748.10 | 2786.14 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.22 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.45 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 2209.37 | 2244.61 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 2.51 | 2.58 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 7.24 | 8.70 | 100% | 23.00 | +23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 8.07 | 20.65 | 0% | 0.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 8.12 | 11.26 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6.05 | 6.13 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 10.38 | 23.80 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 533.80 | 550.81 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | no | 2661.74 | 2700.87 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 777.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 424.28 | 3.37 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 1592.40 | 9.79 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 953.66 | 15.53 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 4852.57 | 98.47 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 6.04 | 9.64 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6.34 | 8.82 | 100% | 467.00 | +453.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 59.15 | 101.14 | 100% | 1.00 | -13.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 70.81 | 192.34 | 100% | 487.80 | +473.80 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.22 | 0.26 | 100% | 7.00 | -19.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.25 | 0.31 | 100% | 167.00 | +141.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.53 | 0.60 | 100% | 26.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 54.63 | 124.00 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.34 | 0.36 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 0.63 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 0.82 | 0.90 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 61.10 | 69.33 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 3.89 | 5.02 | 100% | 32.00 | -173.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 5.34 | 6.48 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 6.06 | 6.48 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 86.88 | 89.55 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 2.35 | 4.69 | 100% | 9977.00 | +9557.00 | pass |
| [Ty](latest-results/ty-20260921T060722Z.json) | yes | 3.62 | 3.78 | 100% | 1555.00 | +1135.00 | pass |
| [Pyright](latest-results/pyright-20260921T060722Z.json) | yes | 36.23 | 40.49 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260921T060722Z.json) | yes | 230.57 | 232.76 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 467.00, 487.80).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 32.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | no | 225.07 | 0.42 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 1.81 | 4.30 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.20 | 0.21 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.23 | 0.25 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 0.24 | 0.25 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 6539.95 | 63.36 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 11.35 | 14.81 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 126.88 | 168.75 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260921T060722Z.json) | yes | 51.83 | 59.42 | 100% | 75.00 | 0.00 | pass |
