# Python LSP Benchmark Comparison

Generated from `results\bench-servers\summary-20260320T220921Z.json`

- Generated at: 20260320T220921Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Commit | Source |
| --- | --- | --- | --- |
| Pyright | a11e5b5c58e6 | a11e5b5c58e6 | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\pyright\1.1.408\package\dist\pyright-langserver.js |
| Ty | a11e5b5c58e6 | a11e5b5c58e6 | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\ty\0.0.24\ty.exe |
| Pyrefly | a11e5b5c58e6 | a11e5b5c58e6 | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\pyrefly\0.57.1\pyrefly.exe |
| pylsp-mypy | a11e5b5c58e6 | a11e5b5c58e6 | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\pylsp-mypy\venv\Scripts\pylsp.exe |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Total ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 6 | 19806.19 | 2.50 | 90 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 6 | 10088.10 | 5.60 | 90 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 6 | 24270.62 | 10.61 | 90 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | no | 6 | 460621.83 | 3628.87 | 90 | 89% | 2 |

## Benchmark: data_science

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 2271.21 | 0.97 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 694.51 | 1.18 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 1977.04 | 2.68 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 9250.95 | 243.65 | 3 | 15 | 100% | 0 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 1.59 | 3.16 | 100% | 252.00 | +49.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 2.77 | 4.42 | 100% | 226.00 | +23.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 5.62 | 9.33 | 100% | 203.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 231.46 | 713.50 | 100% | 181.00 | -22.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.45 | 0.55 | 100% | 3908.00 | -111.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.92 | 0.99 | 100% | 9154.00 | +5135.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 1.84 | 3.17 | 100% | 4019.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 496.73 | 512.68 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.31 | 0.34 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.58 | 0.66 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 2.75 | 3.24 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 203.00, 226.00, 252.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4134.00, 9154.00).

## Benchmark: django

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 2017.13 | 0.75 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 1529.62 | 3.41 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 1048.65 | 4.50 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 6994.00 | 251.28 | 3 | 15 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 1.42 | 3.05 | 100% | 38.00 | +18.20 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 8.78 | 21.02 | 100% | 19.80 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 12.71 | 19.53 | 100% | 237.00 | +217.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 297.65 | 827.47 | 100% | 2.00 | -17.80 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.44 | 0.50 | 100% | 324.00 | +267.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.53 | 0.95 | 100% | 46.00 | -11.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.69 | 0.79 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 453.43 | 469.14 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.39 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.77 | 0.92 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 2.74 | 2.98 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- queryset completion: result differences detected (19.80, 2.00, 237.00, 38.00).
- queryset filter hover: result differences detected (324.00, 46.00, 57.00).

## Benchmark: pandas

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 2098.62 | 4.49 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 1310.91 | 10.37 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 4087.20 | 29.58 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 8870.12 | 209.84 | 3 | 15 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.48 | 0.51 | 100% | 39.00 | -238.80 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 30.29 | 36.25 | 100% | 1000.00 | +722.20 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 87.38 | 291.47 | 100% | 277.80 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 103.45 | 126.48 | 100% | 6.00 | -271.80 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.45 | 0.45 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.80 | 0.89 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 12.63 | 39.58 | 100% | 3577.00 | +3227.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 523.14 | 541.61 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.37 | 0.45 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.38 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.57 | 0.68 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 2.92 | 3.31 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 277.80, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 350.00, 3577.00).

## Benchmark: sqlalchemy

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 2458.71 | 0.66 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 2050.37 | 3.00 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 790.77 | 3.63 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 10175.55 | 311.02 | 3 | 15 | 100% | 0 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.71 | 0.78 | 100% | 38.00 | +37.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 6.55 | 9.46 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 9.90 | 20.92 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 268.37 | 784.53 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.69 | 0.89 | 100% | 10580.00 | +8.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.91 | 1.00 | 100% | 13706.00 | +3134.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 1.94 | 2.43 | 100% | 10572.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 661.87 | 671.49 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.31 | 0.33 | 100% | 2.00 | +1.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.52 | 0.57 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 2.82 | 3.24 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10580.00, 13706.00).
- mapped class definition: result differences detected (1.00, 2.00).

## Benchmark: transformers

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 8715.34 | 0.34 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 5515.08 | 8.74 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 13399.49 | 22.31 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | no | 422156.12 | 20670.04 | 3 | 15 | 33% | 2 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.44 | 0.48 | 100% | 38.00 | -85.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 25.32 | 30.28 | 100% | 767.00 | +644.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 65.76 | 97.54 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 259.41 | 329.40 | 100% | 2.00 | -121.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.25 | 0.28 | 100% | 48.00 | +14.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.29 | 0.31 | 100% | 7.00 | -27.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.61 | 0.67 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | no | 30499.46 | 49632.41 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.33 | 0.43 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.56 | 0.66 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.62 | 1.03 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | no | 31251.23 | 38850.30 | 0% | 0.00 | -1.00 | fail (10) |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 767.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).
- auto tokenizer definition: result differences detected (0.00, 1.00).

## Benchmark: web

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 1226.90 | 2.64 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 728.19 | 5.15 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 2245.19 | 7.78 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 3175.08 | 87.42 | 3 | 15 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 6.36 | 9.72 | 100% | 16.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 14.50 | 28.73 | 100% | 356.20 | +340.20 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 14.56 | 23.65 | 100% | 439.00 | +423.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 37.99 | 40.24 | 100% | 1.00 | -15.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.31 | 0.37 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.72 | 0.90 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 8.32 | 20.32 | 100% | 340.00 | +314.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 208.27 | 714.46 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T220921Z.json) | yes | 0.53 | 0.58 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T220921Z.json) | yes | 0.58 | 0.72 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T220921Z.json) | yes | 0.85 | 0.91 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T220921Z.json) | yes | 16.01 | 26.00 | 100% | 2.00 | 0.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 356.20, 439.00).
- client session hover: result differences detected (26.00, 340.00, 359.00, 7.00).
