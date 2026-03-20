# Python LSP Benchmark Comparison

Generated from `results\bench-servers\summary-20260320T210745Z.json`

- Generated at: 20260320T210745Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Commit | Source |
| --- | --- | --- | --- |
| Pyright | 4334f0d7c8df | 4334f0d7c8df | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\pyright\1.1.408\package\dist\pyright-langserver.js |
| Ty | 4334f0d7c8df | 4334f0d7c8df | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\ty\0.0.24\ty.exe |
| Pyrefly | 4334f0d7c8df | 4334f0d7c8df | C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\servers\pyrefly\0.57.1\pyrefly.exe |


## Overview

| Server | Success | Benchmarks | Total ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 6 | 32927.90 | 3.37 | 90 | 100% | 0 |
| Ty | yes | 6 | 10113.40 | 6.20 | 90 | 100% | 0 |
| Pyright | yes | 6 | 24823.26 | 9.94 | 90 | 100% | 0 |

## Benchmark: data_science

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ty | yes | 682.91 | 1.11 | 3 | 15 | 100% | 0 |
| Pyright | yes | 2143.74 | 2.97 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 7673.18 | 8.20 | 3 | 15 | 100% | 0 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 1.43 | 2.64 | 100% | 252.00 | +49.00 | pass |
| Ty | yes | 2.66 | 3.30 | 100% | 226.00 | +23.00 | pass |
| Pyright | yes | 6.59 | 9.94 | 100% | 203.00 | 0.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.39 | 0.45 | 100% | 3908.00 | -111.00 | pass |
| Pyright | yes | 1.41 | 1.98 | 100% | 4019.00 | 0.00 | pass |
| Pyrefly | yes | 22.76 | 75.68 | 100% | 9154.00 | +5135.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.28 | 0.28 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.40 | 0.54 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.91 | 1.38 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- dataframe completion: result differences detected (203.00, 226.00, 252.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 9154.00).

## Benchmark: django

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 1044.71 | 0.35 | 3 | 15 | 100% | 0 |
| Pyright | yes | 1720.15 | 3.17 | 3 | 15 | 100% | 0 |
| Ty | yes | 1026.11 | 4.66 | 3 | 15 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.45 | 0.47 | 100% | 38.00 | +18.20 | pass |
| Pyright | yes | 7.87 | 16.81 | 100% | 19.80 | 0.00 | pass |
| Ty | yes | 13.19 | 19.20 | 100% | 237.00 | +217.20 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.33 | 0.41 | 100% | 324.00 | +267.00 | pass |
| Ty | yes | 0.50 | 0.59 | 100% | 46.00 | -11.00 | pass |
| Pyright | yes | 0.97 | 1.23 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.28 | 0.33 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 0.30 | 0.32 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.66 | 0.81 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- queryset completion: result differences detected (19.80, 237.00, 38.00).
- queryset filter hover: result differences detected (324.00, 46.00, 57.00).

## Benchmark: pandas

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2079.53 | 3.93 | 3 | 15 | 100% | 0 |
| Ty | yes | 1320.16 | 10.48 | 3 | 15 | 100% | 0 |
| Pyright | yes | 4008.84 | 27.64 | 3 | 15 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.57 | 0.77 | 100% | 39.00 | -238.80 | pass |
| Ty | yes | 30.56 | 46.48 | 100% | 1000.00 | +722.20 | pass |
| Pyright | yes | 81.41 | 262.49 | 100% | 277.80 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.56 | 0.85 | 100% | 308.00 | -42.00 | pass |
| Pyright | yes | 0.95 | 1.15 | 100% | 350.00 | 0.00 | pass |
| Pyrefly | yes | 10.87 | 31.08 | 100% | 3577.00 | +3227.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.33 | 0.36 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.36 | 0.38 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.56 | 0.71 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 277.80, 39.00).
- dataframe groupby hover: result differences detected (308.00, 350.00, 3577.00).

## Benchmark: sqlalchemy

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2467.64 | 1.11 | 3 | 15 | 100% | 0 |
| Pyright | yes | 2065.74 | 2.82 | 3 | 15 | 100% | 0 |
| Ty | yes | 820.90 | 4.67 | 3 | 15 | 100% | 0 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 1.13 | 2.79 | 100% | 38.00 | +37.00 | pass |
| Pyright | yes | 6.41 | 9.78 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 13.26 | 21.97 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.51 | 0.55 | 100% | 10580.00 | +8.00 | pass |
| Pyrefly | yes | 0.90 | 1.01 | 100% | 13706.00 | +3134.00 | pass |
| Pyright | yes | 1.52 | 2.32 | 100% | 10572.00 | 0.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.26 | 0.27 | 100% | 2.00 | +1.00 | pass |
| Pyright | yes | 0.52 | 0.55 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 1.29 | 3.25 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10572.00, 10580.00, 13706.00).
- mapped class definition: result differences detected (1.00, 2.00).

## Benchmark: transformers

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 8592.19 | 0.64 | 3 | 15 | 100% | 0 |
| Ty | yes | 5533.63 | 10.14 | 3 | 15 | 100% | 0 |
| Pyright | yes | 13658.50 | 20.39 | 3 | 15 | 100% | 0 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 1.03 | 2.53 | 100% | 38.00 | -85.00 | pass |
| Ty | yes | 29.78 | 37.34 | 100% | 767.00 | +644.00 | pass |
| Pyright | yes | 59.65 | 95.72 | 100% | 123.00 | 0.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.28 | 0.31 | 100% | 7.00 | -27.00 | pass |
| Pyrefly | yes | 0.63 | 1.23 | 100% | 48.00 | +14.00 | pass |
| Pyright | yes | 0.91 | 1.08 | 100% | 34.00 | 0.00 | pass |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.27 | 0.30 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 0.36 | 0.41 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.60 | 0.81 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 38.00, 767.00).
- pipeline hover: result differences detected (34.00, 48.00, 7.00).

## Benchmark: web

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyright | yes | 1226.29 | 2.63 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 11070.64 | 5.99 | 3 | 15 | 100% | 0 |
| Ty | yes | 729.70 | 6.13 | 3 | 15 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyright | yes | 6.35 | 9.50 | 100% | 16.00 | 0.00 | pass |
| Pyrefly | yes | 6.75 | 7.58 | 100% | 357.00 | +341.00 | pass |
| Ty | yes | 17.52 | 21.29 | 100% | 439.00 | +423.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.30 | 0.33 | 100% | 7.00 | -19.00 | pass |
| Pyright | yes | 0.68 | 0.76 | 100% | 26.00 | 0.00 | pass |
| Pyrefly | yes | 10.65 | 30.79 | 100% | 340.00 | +314.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.57 | 0.59 | 100% | 2.00 | 0.00 | pass |
| Ty | yes | 0.58 | 0.68 | 100% | 2.00 | 0.00 | pass |
| Pyright | yes | 0.85 | 0.91 | 100% | 2.00 | 0.00 | pass |

### Result Differences

- request args completion: result differences detected (16.00, 357.00, 439.00).
- client session hover: result differences detected (26.00, 340.00, 7.00).
