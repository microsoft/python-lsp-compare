# Python LSP Benchmark Comparison

Generated from `results\bench-servers\summary-20260320T003622Z.json`

- Generated at: 20260320T003622Z
- Config: `C:\Users\rchiodo\source\repos\python-lsp-compare\configs\local\lsp_servers.json`
- Servers: pylance, ty, pyrefly
- Baseline server: Pylance (pylance)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Commit | Source |
| --- | --- | --- | --- |
| Pylance | af14f3725d68 | af14f3725d68 | C:\Users\rchiodo\source\repos\pyrx\packages\pylance-server\dist\server.js |
| Ty | af14f3725d68 | af14f3725d68 | C:\Users\rchiodo\source\repos\pyrx\packages\ruff\target\release\ty.exe |
| Pyrefly | 54df45a1c642 | 54df45a1c642 | C:\Users\rchiodo\source\repos\pyrefly\target\release\pyrefly.exe |


## Overview

| Server | Success | Benchmarks | Total ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Ty | yes | 6 | 7223.63 | 5.28 | 90 | 100% | 0 |
| Pyrefly | yes | 6 | 16727.97 | 8.23 | 90 | 100% | 0 |
| Pylance | yes | 6 | 42836.71 | 192.09 | 90 | 100% | 0 |

## Benchmark: data_science

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ty | yes | 395.75 | 1.00 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 1696.16 | 3.36 | 3 | 15 | 100% | 0 |
| Pylance | yes | 2306.77 | 21.66 | 3 | 15 | 100% | 0 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.71 | 0.84 | 100% | 252.00 | +49.00 | pass |
| Ty | yes | 2.37 | 2.87 | 100% | 226.00 | +23.00 | pass |
| Pylance | yes | 13.64 | 17.03 | 100% | 203.00 | 0.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.34 | 0.37 | 100% | 3908.00 | -210.00 | pass |
| Pyrefly | yes | 9.02 | 27.24 | 100% | 4417.00 | +299.00 | pass |
| Pylance | yes | 50.55 | 62.93 | 100% | 4118.00 | 0.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.28 | 0.30 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.36 | 0.40 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 0.80 | 0.87 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- dataframe completion: result differences detected (203.00, 226.00, 252.00).
- dataframe describe hover: result differences detected (3908.00, 4118.00, 4417.00).

## Benchmark: django

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ty | yes | 554.42 | 3.73 | 3 | 15 | 100% | 0 |
| Pylance | yes | 1453.39 | 18.82 | 3 | 15 | 100% | 0 |
| Pyrefly | yes | 1396.11 | 34.64 | 3 | 15 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 10.66 | 18.81 | 100% | 237.00 | +221.00 | pass |
| Pylance | yes | 54.49 | 93.85 | 100% | 16.00 | 0.00 | pass |
| Pyrefly | yes | 103.30 | 411.83 | 100% | 38.00 | +22.00 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.28 | 0.30 | 100% | 46.00 | -11.00 | pass |
| Pyrefly | yes | 0.33 | 0.41 | 100% | 324.00 | +267.00 | pass |
| Pylance | yes | 1.03 | 1.20 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.28 | 0.33 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 0.94 | 1.32 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- queryset completion: result differences detected (16.00, 237.00, 38.00).
- queryset filter hover: result differences detected (324.00, 46.00, 57.00).

## Benchmark: pandas

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 1987.75 | 4.18 | 3 | 15 | 100% | 0 |
| Ty | yes | 883.81 | 9.55 | 3 | 15 | 100% | 0 |
| Pylance | yes | 2764.21 | 67.26 | 3 | 15 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.46 | 0.51 | 100% | 39.00 | -120.00 | pass |
| Ty | yes | 28.11 | 38.35 | 100% | 1000.00 | +841.00 | pass |
| Pylance | yes | 199.05 | 459.11 | 100% | 159.00 | 0.00 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.31 | 0.35 | 100% | 308.00 | -7063.00 | pass |
| Pylance | yes | 1.94 | 2.64 | 100% | 7371.00 | 0.00 | pass |
| Pyrefly | yes | 11.67 | 37.12 | 100% | 3577.00 | -3794.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.23 | 0.25 | 100% | 1.00 | 0.00 | pass |
| Pyrefly | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 0.80 | 0.88 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 159.00, 39.00).
- dataframe groupby hover: result differences detected (308.00, 3577.00, 7371.00).

## Benchmark: sqlalchemy

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2247.76 | 2.00 | 3 | 15 | 100% | 0 |
| Ty | yes | 656.58 | 3.95 | 3 | 15 | 100% | 0 |
| Pylance | yes | 3857.87 | 82.24 | 3 | 15 | 100% | 0 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.52 | 0.55 | 100% | 38.00 | +37.00 | pass |
| Ty | yes | 11.08 | 21.95 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 244.10 | 297.55 | 100% | 1.00 | 0.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.48 | 0.53 | 100% | 10580.00 | +8.00 | pass |
| Pylance | yes | 1.80 | 1.96 | 100% | 10572.00 | 0.00 | pass |
| Pyrefly | yes | 5.04 | 16.75 | 100% | 13706.00 | +3134.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.29 | 0.31 | 100% | 2.00 | +1.00 | pass |
| Pyrefly | yes | 0.43 | 0.46 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 0.83 | 0.98 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10572.00, 10580.00, 13706.00).
- mapped class definition: result differences detected (1.00, 2.00).

## Benchmark: transformers

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 7250.86 | 0.33 | 3 | 15 | 100% | 0 |
| Ty | yes | 4121.39 | 7.84 | 3 | 15 | 100% | 0 |
| Pylance | yes | 31015.97 | 947.71 | 3 | 15 | 100% | 0 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.46 | 0.53 | 100% | 38.00 | -46.00 | pass |
| Ty | yes | 22.89 | 29.32 | 100% | 767.00 | +683.00 | pass |
| Pylance | yes | 2841.34 | 3352.29 | 100% | 84.00 | 0.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.27 | 0.30 | 100% | 48.00 | +14.00 | pass |
| Ty | yes | 0.27 | 0.30 | 100% | 7.00 | -27.00 | pass |
| Pylance | yes | 0.84 | 0.98 | 100% | 34.00 | 0.00 | pass |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.28 | 0.31 | 100% | 1.00 | 0.00 | pass |
| Ty | yes | 0.35 | 0.39 | 100% | 1.00 | 0.00 | pass |
| Pylance | yes | 0.95 | 1.34 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- classifier pipeline completion: result differences detected (38.00, 767.00, 84.00).
- pipeline hover: result differences detected (34.00, 48.00, 7.00).

## Benchmark: web

| Server | Success | Total ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Pyrefly | yes | 2149.33 | 4.85 | 3 | 15 | 100% | 0 |
| Ty | yes | 611.67 | 5.64 | 3 | 15 | 100% | 0 |
| Pylance | yes | 1438.49 | 14.82 | 3 | 15 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 6.15 | 6.53 | 100% | 357.00 | +345.00 | pass |
| Ty | yes | 16.09 | 21.61 | 100% | 439.00 | +427.00 | pass |
| Pylance | yes | 40.67 | 60.63 | 100% | 12.00 | 0.00 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Ty | yes | 0.25 | 0.30 | 100% | 7.00 | -19.00 | pass |
| Pylance | yes | 1.75 | 3.92 | 100% | 26.00 | 0.00 | pass |
| Pyrefly | yes | 7.88 | 19.80 | 100% | 340.00 | +314.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pylance | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Pyrefly | yes | 0.51 | 0.53 | 100% | 2.00 | 0.00 | pass |
| Ty | yes | 0.58 | 0.73 | 100% | 2.00 | 0.00 | pass |
| Pylance | yes | 2.03 | 3.89 | 100% | 2.00 | 0.00 | pass |

### Result Differences

- request args completion: result differences detected (12.00, 357.00, 439.00).
- client session hover: result differences detected (26.00, 340.00, 7.00).
