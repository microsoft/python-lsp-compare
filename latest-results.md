# Python LSP Benchmark Comparison

Generated from `results/bench-servers/summary-20260320T232017Z.json`

- Generated at: 20260320T232017Z
- Config: `github-releases`
- Servers: pyright, ty, pyrefly, pylsp-mypy
- Baseline server: Pyright (pyright)
- Benchmarks: data_science, django, pandas, sqlalchemy, transformers, web

## Server Versions

| Server | Version | Source |
| --- | --- | --- |
| Pyright | 1.1.408 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyright/1.1.408/package/dist/pyright-langserver.js |
| Ty | 0.0.24 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/ty/0.0.24/ty-x86_64-unknown-linux-gnu/ty |
| Pyrefly | 0.57.1 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pyrefly/0.57.1/pyrefly |
| pylsp-mypy | 1.14.0 | /home/runner/work/python-lsp-compare/python-lsp-compare/.python-lsp-compare/servers/pylsp-mypy/venv/bin/pylsp |

## Server Notes

- **Pyright**: Requires Node.js to be installed.
- **pylsp-mypy**: Uses python-lsp-server (pylsp) with the pylsp-mypy plugin.
- **pylsp-mypy**: LSP features like hover and completion are provided by pylsp/jedi, not mypy.
- **pylsp-mypy**: mypy contributes diagnostics only.


## Overview

| Server | Success | Benchmarks | Wall clock ms | Avg measured ms | Measured requests | Non-empty % | Failed points |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 6 | 6227.91 | 2.66 | 90 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 6 | 73234.24 | 8.60 | 90 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 6 | 9741.68 | 33.47 | 90 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | no | 6 | 182422.86 | 358.53 | 90 | 94% | 1 |

*Wall clock ms includes server startup, warmup iterations, and shutdown — not just measured requests.*

## Benchmark: data_science

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 799.88 | 0.71 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 12393.00 | 3.27 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 1152.33 | 14.46 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 5871.24 | 80.20 | 3 | 15 | 100% | 0 |

### dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 1.63 | 1.82 | 100% | 225.00 | +24.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 5.72 | 13.13 | 100% | 201.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 40.07 | 158.30 | 100% | 250.00 | +49.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 50.93 | 56.17 | 100% | 181.00 | -20.00 | pass |

### dataframe describe hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.28 | 0.30 | 100% | 3908.00 | -111.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 2.22 | 3.57 | 100% | 4019.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 3.06 | 10.41 | 100% | 8341.00 | +4322.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 188.46 | 189.00 | 100% | 4134.00 | +115.00 | pass |

### summarize definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.23 | 0.24 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 1.21 | 1.46 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 1.89 | 4.18 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- dataframe completion: result differences detected (181.00, 201.00, 225.00, 250.00).
- dataframe describe hover: result differences detected (3908.00, 4019.00, 4134.00, 8341.00).

## Benchmark: django

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 708.99 | 1.71 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 6540.75 | 2.93 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 920.81 | 11.37 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 4029.46 | 140.10 | 3 | 15 | 100% | 0 |

### queryset completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 4.71 | 7.53 | 100% | 237.00 | +218.20 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 7.75 | 16.59 | 100% | 18.80 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 33.67 | 133.36 | 100% | 38.00 | +19.20 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 248.84 | 451.03 | 100% | 2.00 | -16.80 | pass |

### queryset filter hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.23 | 0.25 | 100% | 46.00 | -11.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.24 | 0.26 | 100% | 298.00 | +241.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.61 | 0.69 | 100% | 57.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 170.39 | 171.43 | 100% | 57.00 | 0.00 | pass |

### model definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.19 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.45 | 0.48 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 1.08 | 1.13 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- queryset completion: result differences detected (18.80, 2.00, 237.00, 38.00).
- queryset filter hover: result differences detected (298.00, 46.00, 57.00).

## Benchmark: pandas

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 1057.40 | 5.83 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 1084.83 | 16.39 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 14531.35 | 25.25 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 5236.97 | 105.89 | 3 | 15 | 100% | 0 |

### report dataframe completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 17.07 | 23.72 | 100% | 1000.00 | +725.80 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 47.18 | 187.41 | 100% | 39.00 | -235.20 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 74.55 | 249.16 | 100% | 274.20 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 115.86 | 314.62 | 100% | 6.00 | -268.20 | pass |

### dataframe groupby hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.23 | 0.25 | 100% | 308.00 | -42.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.76 | 0.84 | 100% | 350.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 1.78 | 1.84 | 100% | 3120.00 | +2770.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 200.74 | 201.24 | 100% | 301.00 | -49.00 | pass |

### build report definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.20 | 0.20 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.20 | 0.21 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.45 | 0.55 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 1.07 | 1.10 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- report dataframe completion: result differences detected (1000.00, 274.20, 39.00, 6.00).
- dataframe groupby hover: result differences detected (301.00, 308.00, 3120.00, 350.00).

## Benchmark: sqlalchemy

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 783.31 | 1.61 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 6630.77 | 2.62 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 1371.02 | 27.59 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 7013.06 | 132.37 | 3 | 15 | 100% | 0 |

### query completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 4.23 | 10.52 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 6.14 | 10.79 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 65.04 | 117.52 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 79.27 | 315.42 | 100% | 38.00 | +37.00 | pass |

### sessionmaker hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.38 | 0.39 | 100% | 10580.00 | +8.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 1.28 | 1.67 | 100% | 10572.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 3.29 | 6.72 | 100% | 13682.00 | +3110.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 331.02 | 351.39 | 100% | 10498.00 | -74.00 | pass |

### mapped class definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.21 | 0.23 | 100% | 1.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.21 | 0.22 | 100% | 2.00 | +1.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.43 | 0.49 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 1.06 | 1.14 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- query completion: result differences detected (1.00, 38.00).
- sessionmaker hover: result differences detected (10498.00, 10572.00, 10580.00, 13682.00).
- mapped class definition: result differences detected (1.00, 2.00).

## Benchmark: transformers

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 2090.02 | 3.87 | 3 | 15 | 100% | 0 |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 28017.78 | 15.45 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 3860.35 | 114.16 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | no | 158814.80 | 1670.03 | 3 | 15 | 67% | 1 |

### classifier pipeline completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 11.20 | 13.52 | 100% | 767.00 | +644.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 45.47 | 74.57 | 100% | 123.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 140.28 | 147.48 | 100% | 2.00 | -121.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 342.04 | 1322.72 | 100% | 38.00 | -85.00 | pass |

### pipeline hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.19 | 0.20 | 100% | 7.00 | -27.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.20 | 0.23 | 100% | 48.00 | +14.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.48 | 0.55 | 100% | 34.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | no | 2584.40 | 2611.02 | 0% | 0.00 | -34.00 | fail (10) |

### auto tokenizer definition

Method: `textDocument/definition`

| Server | Success | Mean ms | P95 ms | Non-empty % | Definitions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.22 | 0.25 | 100% | 1.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.25 | 0.27 | 100% | 1.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.41 | 0.46 | 100% | 1.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 2285.41 | 2362.94 | 100% | 1.00 | 0.00 | pass |

### Result Differences

- classifier pipeline completion: result differences detected (123.00, 2.00, 38.00, 767.00).
- pipeline hover: result differences detected (0.00, 34.00, 48.00, 7.00).

## Benchmark: web

| Server | Success | Wall clock ms | Avg measured ms | Points | Measured requests | Non-empty % | Failed points |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 5120.59 | 2.05 | 3 | 15 | 100% | 0 |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 788.32 | 2.20 | 3 | 15 | 100% | 0 |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 1352.35 | 16.84 | 3 | 15 | 100% | 0 |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 1457.34 | 22.62 | 3 | 15 | 100% | 0 |

### request args completion

Method: `textDocument/completion`

| Server | Success | Mean ms | P95 ms | Non-empty % | Completions found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 4.97 | 10.11 | 100% | 16.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 6.01 | 9.89 | 100% | 439.00 | +423.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 22.44 | 26.18 | 100% | 1.00 | -15.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 46.77 | 155.03 | 100% | 351.40 | +335.40 | pass |

### client session hover

Method: `textDocument/hover`

| Server | Success | Mean ms | P95 ms | Non-empty % | Hover length | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.21 | 0.23 | 100% | 7.00 | -19.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.50 | 0.57 | 100% | 26.00 | 0.00 | pass |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 3.37 | 10.82 | 100% | 314.00 | +288.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 22.52 | 41.56 | 100% | 359.00 | +333.00 | pass |

### client references

Method: `textDocument/references`

| Server | Success | Mean ms | P95 ms | Non-empty % | References found | Delta vs Pyright | Validation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| [Pyrefly](latest-results/pyrefly-20260320T232017Z.json) | yes | 0.37 | 0.38 | 100% | 2.00 | 0.00 | pass |
| [Ty](latest-results/ty-20260320T232017Z.json) | yes | 0.39 | 0.43 | 100% | 2.00 | 0.00 | pass |
| [Pyright](latest-results/pyright-20260320T232017Z.json) | yes | 0.68 | 0.74 | 100% | 2.00 | 0.00 | pass |
| [pylsp-mypy](latest-results/pylsp-mypy-20260320T232017Z.json) | yes | 22.90 | 39.25 | 100% | 2.00 | 0.00 | pass |

### Result Differences

- request args completion: result differences detected (1.00, 16.00, 351.40, 439.00).
- client session hover: result differences detected (26.00, 314.00, 359.00, 7.00).
