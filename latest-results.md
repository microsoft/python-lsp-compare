# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20261117T060341Z.json`

- Generated at: 20261117T060341Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web, tsp_core, tsp_semantic

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.414 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.414/package/dist/pyright-langserver.js |
| Ty | 0.0.104 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.104/ty-x86_64-unknown-linux-gnu/ty |
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
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 6 | 3358.16 | 3.80 | 150 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | no | 8 | 6210.68 | 5.83 | 205 | 97% | 2 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 6 | 35818.33 | 68.85 | 150 | 97% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 6 | 180484.03 | 272.92 | 150 | 80% | 5 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — but excludes one-time environment creation and dependency installation.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 447.05 | 3.65 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 645.64 | 5.29 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 4570.32 | 76.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 6706.65 | 95.08 | 5 | 25 | 80% | 1 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 1.92 | 2.36 | 100% | 223.00 | +22.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2.15 | 4.86 | 100% | 250.00 | +49.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 6.95 | 12.31 | 100% | 201.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 158.84 | 324.22 | 100% | 188.00 | -13.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.28 | 0.32 | 100% | 4232.00 | +213.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 1.26 | 1.68 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 4.74 | 7.57 | 100% | 3182.00 | -837.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 160.38 | 160.95 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.16 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.39 | 0.47 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 0.96 | 1.17 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.13 | 4.47 | 100% | 1.00 | 0.00 | pass |

### edit array then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 3.47 | 3.68 | 0% | 0.00 | -168.00 | fail (10) |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 11.42 | 12.79 | 100% | 168.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 15.33 | 20.20 | 100% | 168.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 340.59 | 524.15 | 100% | 168.00 | 0.00 | pass |

### edit array then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 1.11 | 3.22 | 100% | 2546.00 | +2268.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 4.44 | 4.47 | 100% | 267.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 30.83 | 34.15 | 100% | 278.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 151.74 | 154.50 | 100% | 5662.00 | +5384.00 | pass |

### Result Differences

- dataframe completion: result differences detected (188.00, 201.00, 223.00, 250.00).
- dataframe describe hover: result differences detected (3182.00, 4019.00, 4134.00, 4232.00).
- edit array then complete (edit+completion): result differences detected (0.00, 168.00).
- edit array then hover (edit+hover): result differences detected (2546.00, 267.00, 278.00, 5662.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 246.68 | 1.93 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 233.04 | 2.19 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 1328.24 | 13.25 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 6425.05 | 142.22 | 5 | 25 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 4.60 | 7.12 | 100% | 10.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 4.78 | 6.64 | 100% | 15.00 | +5.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 4.95 | 7.56 | 100% | 262.00 | +252.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 153.99 | 440.77 | 100% | 2.00 | -8.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.18 | 0.20 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.50 | 0.58 | 100% | 57.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.74 | 2.29 | 100% | 298.00 | +241.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 140.12 | 142.42 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.15 | 0.16 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.15 | 0.17 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.39 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 1.10 | 1.30 | 100% | 1.00 | 0.00 | pass |

### edit queryset then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2.00 | 3.98 | 100% | 104.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 3.68 | 4.37 | 100% | 104.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 24.01 | 26.07 | 100% | 104.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 202.43 | 234.16 | 100% | 143.00 | +39.00 | pass |

### edit queryset then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 1.96 | 4.00 | 100% | 858.00 | +775.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 1.97 | 2.08 | 100% | 100.00 | +17.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 36.73 | 44.29 | 100% | 83.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 213.48 | 219.35 | 100% | 71.00 | -12.00 | pass |

### Result Differences

- queryset completion: result differences detected (10.00, 15.00, 2.00, 262.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).
- edit queryset then complete (edit+completion): result differences detected (104.00, 143.00).
- edit queryset then hover (edit+hover): result differences detected (100.00, 71.00, 83.00, 858.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 620.40 | 7.06 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 741.35 | 7.24 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 6644.18 | 123.11 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 10437.35 | 165.97 | 5 | 25 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.33 | 7.51 | 100% | 16.00 | -255.20 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 17.73 | 21.77 | 100% | 1000.00 | +728.80 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 69.19 | 232.01 | 100% | 271.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 87.60 | 221.65 | 100% | 6.00 | -265.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.21 | 0.25 | 100% | 329.00 | -21.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.81 | 0.98 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.46 | 5.00 | 100% | 2759.00 | +2409.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 167.98 | 170.59 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.13 | 0.15 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.18 | 0.19 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.31 | 0.38 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 1.00 | 1.07 | 100% | 1.00 | 0.00 | pass |

### edit dataframe then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 14.26 | 15.40 | 100% | 448.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 25.16 | 33.72 | 100% | 274.00 | -166.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 196.59 | 205.18 | 100% | 441.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 748.12 | 1161.64 | 100% | 440.00 | 0.00 | pass |

### edit dataframe then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.14 | 10.88 | 100% | 943.00 | -3349.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 3.84 | 3.91 | 100% | 4441.00 | +149.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 11.41 | 13.18 | 100% | 4292.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 162.38 | 165.51 | 100% | 232.00 | -4060.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 16.00, 271.20, 6.00).
- dataframe groupby hover: result differences detected (2759.00, 301.00, 329.00, 350.00).
- edit dataframe then complete (edit+completion): result differences detected (274.00, 440.00, 441.00, 448.00).
- edit dataframe then hover (edit+hover): result differences detected (232.00, 4292.00, 4441.00, 943.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 534.96 | 2.23 | 5 | 25 | 100% | 0 |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 358.48 | 2.60 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 3541.91 | 49.62 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 6084.78 | 86.25 | 5 | 25 | 60% | 2 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.55 | 7.50 | 100% | 15.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 3.57 | 8.38 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 18.48 | 21.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 99.88 | 217.70 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.36 | 0.39 | 100% | 10621.00 | +42.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2.00 | 3.49 | 100% | 15239.00 | +4660.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 2.11 | 2.68 | 100% | 10579.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 271.57 | 273.85 | 100% | 10498.00 | -81.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.18 | 0.19 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.36 | 0.44 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 1.03 | 1.44 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 1.21 | 2.53 | 100% | 1.00 | 0.00 | pass |

### edit query then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 3.91 | 4.64 | 100% | 40.00 | +2.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 4.72 | 5.09 | 100% | 23.00 | -15.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 29.49 | 29.94 | 0% | 0.00 | -38.00 | fail (10) |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 131.22 | 167.07 | 100% | 38.00 | 0.00 | pass |

### edit session then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.49 | 0.54 | 100% | 2242.00 | +1349.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 4.16 | 4.21 | 100% | 951.00 | +58.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 29.30 | 29.48 | 0% | 0.00 | -893.00 | fail (10) |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 95.94 | 105.70 | 100% | 893.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 15.00).
- sessionmaker hover: result differences detected (10498.00, 10579.00, 10621.00, 15239.00).
- mapped class definition: result differences detected (1.00, 2.00).
- edit query then complete (edit+completion): result differences detected (0.00, 23.00, 38.00, 40.00).
- edit session then hover (edit+hover): result differences detected (0.00, 2242.00, 893.00, 951.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 1391.11 | 2.80 | 5 | 25 | 80% | 0 |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 1220.43 | 3.83 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 14518.47 | 99.24 | 5 | 25 | 80% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 150649.51 | 1114.09 | 5 | 25 | 40% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 6.08 | 23.54 | 100% | 15.00 | -108.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 11.31 | 13.51 | 100% | 789.00 | +666.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 48.21 | 78.74 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 116.72 | 120.89 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.16 | 0.17 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.20 | 0.23 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.54 | 0.61 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 2092.27 | 2153.05 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.16 | 0.18 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.18 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.50 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 1500.95 | 1553.64 | 100% | 1.00 | 0.00 | pass |

### edit prediction then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 1.65 | 3.87 | 0% | 0.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 2.38 | 2.55 | 0% | 0.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 4.15 | 5.85 | 100% | 23.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 5.75 | 6.47 | 0% | 0.00 | 0.00 | pass |

### edit tokenizer then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 3.29 | 3.33 | 100% | 7.00 | -23.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 5.94 | 15.51 | 100% | 33.00 | +3.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 441.21 | 474.68 | 100% | 30.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | no | 1858.11 | 1886.00 | 0% | 0.00 | -30.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 15.00, 2.00, 789.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- edit prediction then complete (edit+completion): result differences detected (0.00, 23.00).
- edit tokenizer then hover (edit+hover): result differences detected (0.00, 30.00, 33.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 357.81 | 3.31 | 5 | 25 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 550.10 | 4.92 | 5 | 25 | 100% | 0 |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 1422.05 | 9.01 | 5 | 25 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 3973.86 | 76.79 | 5 | 25 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 5.80 | 10.65 | 100% | 14.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 6.20 | 9.48 | 100% | 496.00 | +482.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 15.55 | 23.56 | 100% | 254.40 | +240.40 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 53.07 | 80.98 | 100% | 1.00 | -13.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 0.15 | 0.16 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.49 | 0.55 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2.30 | 8.77 | 100% | 167.00 | +141.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 39.30 | 58.11 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.29 | 0.33 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 0.85 | 1.22 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 1.39 | 1.45 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 17.02 | 31.42 | 100% | 2.00 | 0.00 | pass |

### edit response then complete (edit+completion)

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2.00 | 4.00 | 100% | 54.00 | -151.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 4.59 | 6.50 | 100% | 205.00 | 0.00 | pass |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 5.55 | 6.45 | 100% | 225.00 | +20.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 72.13 | 74.86 | 100% | 57.00 | -148.00 | pass |

### edit response then hover (edit+hover)

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20261117T060341Z.json) | yes | 3.26 | 3.78 | 100% | 1555.00 | +1135.00 | pass |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 4.44 | 4.56 | 100% | 9977.00 | +9557.00 | pass |
| [Pyright](latest-results/pyright-20261117T060341Z.json) | yes | 33.32 | 35.70 | 100% | 420.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20261117T060341Z.json) | yes | 202.40 | 203.63 | 100% | 880.00 | +460.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 14.00, 254.40, 496.00).
- client session hover: result differences detected (167.00, 26.00, 359.00, 7.00).
- edit response then complete (edit+completion): result differences detected (205.00, 225.00, 54.00, 57.00).
- edit response then hover (edit+hover): result differences detected (1555.00, 420.00, 880.00, 9977.00).

## Benchmark: tsp_core

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | no | 205.73 | 0.29 | 8 | 40 | 100% | 2 |

### builtins semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.92 | 1.06 | 100% | 30.00 | 0.00 | pass |

### builtin int computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.16 | 0.17 | 100% | 7.00 | 0.00 | pass |

### list declared type

Method: `typeServer/getDeclaredType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.22 | 0.23 | 100% | 7.00 | 0.00 | pass |

### generic specialization computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.21 | 0.22 | 100% | 7.00 | 0.00 | pass |

### stdlib path computed type

Method: `typeServer/getComputedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.25 | 0.38 | 100% | 7.00 | 0.00 | pass |

### function argument expected type

Method: `typeServer/getExpectedType`

| Server | Success | Mean ms | P95 ms | Non-empty % | Results found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | 0.00 | pass |

## Benchmark: tsp_semantic

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 2016.06 | 38.52 | 3 | 15 | 100% | 0 |

### django semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 23.33 | 34.70 | 100% | 126.00 | 0.00 | pass |

### transformers semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 86.25 | 111.66 | 100% | 74.00 | 0.00 | pass |

### stdlib semantic tokens

Method: semantic token impl using typeServer/getComputedType

| Server | Success | Mean ms | P95 ms | Non-empty % | Semantic tokens found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20261117T060341Z.json) | yes | 5.99 | 6.07 | 100% | 75.00 | 0.00 | pass |
