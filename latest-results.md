# Python LSP Benchmark Comparison

Generated from `results\bench-servers\summary-20260320T203859Z.json`

- Generated at: 20260320T203859Z
- Config: `C:\Users\rchiodo\source\repos\python-lsp-compare\.python-lsp-compare\lsp_servers.json`
- Servers: pyright, ty, pyrefly
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Commit | Source |
| --- | --- | --- | --- |
| Pyright | af14f3725d68 | af14f3725d68 | C:\Users\rchiodo\source\repos\pyrx\packages\pyright\packages\pyright\langserver.index.js |
| Ty | f9324a5bf669 | f9324a5bf669 | C:\Users\rchiodo\source\repos\ruff\target\release\ty.exe |
| Pyrefly | 54df45a1c642 | 54df45a1c642 | C:\Users\rchiodo\source\repos\pyrefly\target\release\pyrefly.exe |


## Overview

| Server | Success | Benchmarks | Total ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 6 | 18901.87 | 3.48 | 90 | 100% | 0 |
| Ty | yes | 6 | 7949.75 | 5.89 | 90 | 100% | 0 |
| Pyright | yes | 6 | 25740.46 | 10.13 | 90 | 100% | 0 |

## Benchmark: data_science

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ty | yes | 463.53 | 1.09 | 3 | 15 | 100% | 0 |
| Pyright | yes | 2115.68 | 3.08 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 2057.95 | 4.56 | 3 | 15 | 100% | 0 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.80 | 0.88 | 100% | 252.00 | +49.00 | pass |
| Ty | yes | 2.60 | 3.21 | 100% | 226.00 | +23.00 | pass |
| Pyright | yes | 7.38 | 13.14 | 100% | 203.00 | 0.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.36 | 0.39 | 100% | 3908.00 | -111.00 | pass |
| Pyright | yes | 1.23 | 1.58 | 100% | 4019.00 | 0.00 | pass |
| Pyrefly | yes | 12.52 | 41.22 | 100% | 4417.00 | +398.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.30 | 0.33 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.37 | 0.41 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.62 | 0.73 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- dataframe completion: result differences detected (203.00, 226.00, 252.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4417.00).

## Benchmark: django

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 1014.41 | 0.43 | 3 | 15 | 100% | 0 |
| Pyright | yes | 1510.37 | 3.26 | 3 | 15 | 100% | 0 |
| Ty | yes | 689.29 | 4.94 | 3 | 15 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.53 | 0.58 | 100% | 38.00 | +18.20 | pass |
| Pyright | yes | 8.30 | 14.95 | 100% | 19.80 | 0.00 | pass |
| Ty | yes | 14.20 | 20.68 | 100% | 237.00 | +217.20 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.35 | 0.37 | 100% | 46.00 | -11.00 | pass |
| Pyrefly | yes | 0.41 | 0.45 | 100% | 324.00 | +267.00 | pass |
| Pyright | yes | 0.68 | 0.76 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.27 | 0.28 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.37 | 0.46 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.79 | 1.09 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- queryset completion: result differences detected (19.80, 237.00, 38.00).
- queryset filter hover: result differences detected (324.00, 46.00, 57.00).

## Benchmark: pandas

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2374.63 | 4.26 | 3 | 15 | 100% | 0 |
| Ty | yes | 1094.43 | 11.04 | 3 | 15 | 100% | 0 |
| Pyright | yes | 4330.85 | 27.40 | 3 | 15 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.66 | 0.72 | 100% | 39.00 | -238.80 | pass |
| Ty | yes | 32.44 | 45.02 | 100% | 1000.00 | +722.20 | pass |
| Pyright | yes | 80.46 | 262.39 | 100% | 277.80 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.37 | 0.39 | 100% | 308.00 | -42.00 | pass |
| Pyright | yes | 0.87 | 1.21 | 100% | 350.00 | 0.00 | pass |
| Pyrefly | yes | 11.73 | 35.20 | 100% | 3577.00 | +3227.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.32 | 0.35 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.40 | 0.42 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.88 | 1.06 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 277.80, 39.00).
- dataframe groupby hover: result differences detected (308.00, 350.00, 3577.00).

## Benchmark: sqlalchemy

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2719.62 | 1.12 | 3 | 15 | 100% | 0 |
| Pyright | yes | 2045.55 | 3.42 | 3 | 15 | 100% | 0 |
| Ty | yes | 686.31 | 4.15 | 3 | 15 | 100% | 0 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.99 | 1.96 | 100% | 38.00 | +37.00 | pass |
| Pyright | yes | 8.37 | 11.57 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 11.66 | 19.02 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.49 | 0.51 | 100% | 10580.00 | +8.00 | pass |
| Pyright | yes | 1.28 | 1.58 | 100% | 10572.00 | 0.00 | pass |
| Pyrefly | yes | 1.87 | 2.54 | 100% | 13706.00 | +3134.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.30 | 0.32 | 100% | 2.00 | +1.00 | pass |
| Pyrefly | yes | 0.49 | 0.56 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.62 | 0.79 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10572.00, 10580.00, 13706.00).
- mapped class definition: result differences detected (1.00, 2.00).

## Benchmark: transformers

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 8470.63 | 0.57 | 3 | 15 | 100% | 0 |
| Ty | yes | 4330.24 | 9.35 | 3 | 15 | 100% | 0 |
| Pyright | yes | 14490.20 | 20.85 | 3 | 15 | 100% | 0 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.82 | 1.81 | 100% | 38.00 | -85.00 | pass |
| Ty | yes | 26.91 | 32.35 | 100% | 767.00 | +644.00 | pass |
| Pyright | yes | 61.27 | 95.68 | 100% | 123.00 | 0.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.35 | 0.37 | 100% | 7.00 | -27.00 | pass |
| Pyrefly | yes | 0.56 | 0.69 | 100% | 48.00 | +14.00 | pass |
| Pyright | yes | 0.69 | 0.88 | 100% | 34.00 | 0.00 | pass |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.32 | 0.39 | 100% | 1.00 | 0.00 | pass |
| Pyright | yes | 0.59 | 0.77 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 0.79 | 0.89 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 38.00, 767.00).
- pipeline hover: result differences detected (34.00, 48.00, 7.00).

## Benchmark: web

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyright | yes | 1247.80 | 2.78 | 3 | 15 | 100% | 0 |
| Ty | yes | 685.96 | 4.75 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 2264.62 | 9.94 | 3 | 15 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyright | yes | 6.22 | 10.22 | 100% | 16.00 | 0.00 | pass |
| Ty | yes | 13.37 | 17.48 | 100% | 439.00 | +423.00 | pass |
| Pyrefly | yes | 19.98 | 45.48 | 100% | 356.20 | +340.20 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.28 | 0.31 | 100% | 7.00 | -19.00 | pass |
| Pyright | yes | 0.70 | 0.99 | 100% | 26.00 | 0.00 | pass |
| Pyrefly | yes | 9.28 | 24.72 | 100% | 340.00 | +314.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.55 | 0.62 | 100% | 2.00 | 0.00 | pass |
| Ty | yes | 0.60 | 0.76 | 100% | 2.00 | 0.00 | pass |
| Pyright | yes | 1.41 | 2.61 | 100% | 2.00 | 0.00 | pass |

### Result Differences

- request args completion: result differences detected (16.00, 356.20, 439.00).
- client session hover: result differences detected (26.00, 340.00, 7.00).
