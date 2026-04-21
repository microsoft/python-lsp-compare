# TSP Benchmark Plan

## Goal

Add a new benchmark path that exercises Pyrefly's Type Server Protocol (TSP) support against a curated set of Python source files, then records both latency and semantic evidence that real analysis occurred.

The benchmark should cover:

1. Trivial builtins and standard-library types.
2. User-defined types.
3. Flow-sensitive inference.
4. Generic specialization.
5. Context-sensitive expected types.
6. A small number of edit or virtual-file cases once the basic path is stable.

## Relevant Protocol Surface

The base TSP requests live in `pyrx/packages/type-server/src/protocol/typeServerProtocol.ts`.

The initial benchmark should use these requests:

1. `typeServer/getSupportedProtocolVersion`
2. `typeServer/getSnapshot`
3. `typeServer/getComputedType`
4. `typeServer/getDeclaredType`
5. `typeServer/getExpectedType`

Each of the type requests accepts `{ arg, snapshot }`, where `arg` can be a `Node` or `Declaration`.

For the first implementation, prefer `Node` arguments only. A `Node` is simpler to author in static benchmark fixtures because it is just:

```json
{
  "uri": "file:///...",
  "range": {
    "start": { "line": 0, "character": 0 },
    "end": { "line": 0, "character": 0 }
  }
}
```

Pyright-specific supplemental notifications live in `pyrx/packages/type-server/src/protocol/tspSupplemental.ts`:

1. `pyright/setVirtualFileRedirect`
2. `pyright/removeVirtualFileRedirect`

Those should be treated as phase-2 support, not part of the minimum viable benchmark.

## Current Harness Constraints

The current benchmark system in this repo is LSP-centric:

1. `benchmark_suites.py` maps config keys to a fixed set of LSP methods.
2. `runner.py` dispatches only `textDocument/hover`, `textDocument/completion`, `textDocument/documentSymbol`, `textDocument/definition`, and `textDocument/references`.
3. Validation and result summaries assume LSP result shapes.
4. `bench-servers` runs every selected suite against every selected server.

That means a TSP benchmark cannot be added cleanly as just another existing suite config key. The harness needs either a protocol-aware extension point or a dedicated TSP benchmark path.

## Recommendation

Implement TSP as a separate protocol family that reuses the existing environment preparation, process launch, JSON-RPC transport, metrics, and report plumbing.

Do not try to force TSP into the existing fixed LSP method map.

The recommended approach is:

1. Keep the existing LSP suite behavior unchanged.
2. Add a TSP-specific benchmark suite shape.
3. Add a dedicated runner path for TSP benchmark points.
4. Initially run TSP benchmarks only for Pyrefly-capable servers.

This avoids destabilizing the current LSP benchmark flow and keeps the data model honest about protocol differences.

## Proposed Architecture

### 1. Add a TSP benchmark model

Extend `benchmark_suites.py` with TSP-specific dataclasses rather than overloading `BenchmarkPoint`.

Suggested model:

```python
@dataclass(slots=True)
class TspBenchmarkValidation:
    require_non_empty: bool | None = None
    expected_type_kinds: list[str] = field(default_factory=list)
    min_union_member_count: int | None = None
    min_parameter_count: int | None = None
    min_type_argument_count: int | None = None
    require_literal: bool | None = None
    require_decl_node: bool | None = None
    min_size_chars: int | None = None


@dataclass(slots=True)
class TspBenchmarkPoint:
    label: str
    file_path: Path
    request: str
    start_line: int
    start_character: int
    end_line: int
    end_character: int
    validation: TspBenchmarkValidation = field(default_factory=TspBenchmarkValidation)
```

The `request` field should be one of:

1. `typeServer/getComputedType`
2. `typeServer/getDeclaredType`
3. `typeServer/getExpectedType`

Use explicit start and end positions rather than single cursor positions. TSP works on a `Node` range, and the benchmark config should reflect that directly.

### 2. Add a protocol discriminator to suites

Add an optional `protocol` field to suite config, defaulting to `lsp`.

Example:

```json
{
  "name": "tsp_core",
  "protocol": "tsp",
  "workspace_dir": "src",
  "requirements_file": null,
  "iterations": 5,
  "warmup_iterations": 1,
  "tsp_points": []
}
```

This keeps discovery uniform while allowing the runner to branch intentionally.

### 3. Add server capability filtering

Add a server capability field such as `protocols: ["lsp", "tsp"]` to `ConfiguredServer` and config files.

Initial behavior:

1. Existing servers default to `protocols=["lsp"]` if the field is missing.
2. Pyrefly can be marked as `protocols=["lsp", "tsp"]` in local configs and built-in defaults.
3. `bench-servers` should skip incompatible suites rather than fail every non-TSP server on unknown methods.

If that is too much surface area for the first pass, add a separate `bench-tsp-servers` command instead. Between the two options, capability filtering is the cleaner long-term design.

### 4. Add TSP request helpers to the client

`LspClient` already exposes generic `request()` and `notify()` methods, so only thin helpers are needed.

Suggested helpers:

```python
def tsp_get_supported_protocol_version(self) -> str | None: ...
def tsp_get_snapshot(self) -> int: ...
def tsp_get_computed_type(self, node: dict[str, Any], snapshot: int, context: dict[str, Any] | None = None) -> Any: ...
def tsp_get_declared_type(self, node: dict[str, Any], snapshot: int, context: dict[str, Any] | None = None) -> Any: ...
def tsp_get_expected_type(self, node: dict[str, Any], snapshot: int, context: dict[str, Any] | None = None) -> Any: ...
def tsp_set_virtual_file_redirect(self, real_uri: str, virtual_uri: str, context: dict[str, Any] | None = None) -> None: ...
def tsp_remove_virtual_file_redirect(self, real_uri: str, context: dict[str, Any] | None = None) -> None: ...
```

These methods keep runner code readable while still relying on the existing transport and metric capture.

### 5. Add a TSP benchmark execution path

In `runner.py`, add a dedicated `_run_tsp_benchmark_suite(...)` path. The flow should be:

1. Prepare environment exactly like existing benchmark suites.
2. Start the server and run normal LSP `initialize` and `initialized`.
3. Send `workspace/didChangeConfiguration` as usual.
4. Open all benchmark documents with `didOpen`.
5. Request `typeServer/getSupportedProtocolVersion` once and log it.
6. Request `typeServer/getSnapshot` before the first benchmark point.
7. For each measured point, send the configured TSP request with a `Node` argument and current snapshot.
8. If a `typeServer/snapshotChanged` notification is observed, refresh the snapshot before the next request.
9. Shut down normally.

Important detail: if any benchmark point performs an edit or uses virtual-file redirects later, always reacquire the snapshot after the change and before the next type request.

### 6. Record TSP-specific summaries

The current `metrics.py` result summaries are LSP-shaped. Add TSP-aware summaries when `method` is one of the TSP requests.

Useful summary fields:

1. `type_kind`
2. `type_name`
3. `decl_name`
4. `decl_category`
5. `type_flags`
6. `union_member_count`
7. `parameter_count`
8. `type_argument_count`
9. `has_literal`
10. `has_declaration_node`
11. `size_chars`

Do not aim for a full semantic normalizer at first. The benchmark only needs enough structured summary to prove the response differs across trivial and non-trivial code regions.

### 7. Add TSP-specific validation

The benchmark should not only assert that a result exists. It should assert that analysis produced the expected shape.

Examples:

1. A narrowed variable inside an `if isinstance(x, int)` branch should produce a computed type with kind consistent with `int`, not a union.
2. A generic helper called with `str` should return a specialized type whose return type is `str`.
3. A parameter position should produce a useful expected type for `getExpectedType`.
4. A declared type request against an annotated symbol should return a declared type even when the computed type is more specific.

Suggested validation style:

1. Prefer shape-based checks over exact whole-payload snapshots.
2. Allow optional exact-match assertions on a small stable field like `type_name` where Pyrefly returns a stable string.
3. Keep the validation rules per point so failures explain which analysis scenario regressed.

## Benchmark Corpus

Create a new suite, tentatively `benchmarks/tsp_core/`, with no third-party dependencies in the first pass.

Suggested files and scenarios:

### 1. `src/builtins_basic.py`

Purpose: verify trivial types and declared-vs-computed differences.

Suggested points:

1. Literal `1` assigned to `x` and query computed type of `x`.
2. Annotated variable `name: str = "a"` and compare declared vs computed type.
3. `items: list[int] = [1, 2, 3]` and query declared type of `items`.
4. `result = len(items)` and query computed type of `result`.

### 2. `src/stdlib_types.py`

Purpose: verify stdlib and imported symbol handling.

Suggested points:

1. `from pathlib import Path` then `path = Path(".")` and query computed type of `path`.
2. `from collections import defaultdict` then infer the type of a populated `defaultdict`.
3. `from typing import Iterable` and query a declared type on an annotated function parameter.

### 3. `src/flow_narrowing.py`

Purpose: prove flow-sensitive analysis.

Suggested points:

1. `value: int | str` before narrowing and query computed type.
2. Same symbol inside `if isinstance(value, int):` and query computed type.
3. Same symbol inside the `else:` branch and query computed type.
4. Optional narrowing with `if maybe is not None:`.

These points are the strongest signal that Pyrefly is doing real analysis rather than returning declarations.

### 4. `src/generics.py`

Purpose: verify specialization.

Suggested points:

1. Generic identity function called with `str`.
2. Generic container helper returning `list[T]` specialized with `int`.
3. Generic class instance method returning a type parameter.

### 5. `src/expected_types.py`

Purpose: exercise `typeServer/getExpectedType`.

Suggested points:

1. Function call argument position for `takes_number( /* point */ )`.
2. List append argument position for a `list[str]`.
3. Return expression position in a function annotated `-> bool`.

### 6. `src/classes_protocols.py`

Purpose: user-defined types and structural typing.

Suggested points:

1. Dataclass field access computed type.
2. Method return computed type.
3. `Protocol`-typed variable computed type after assignment.
4. `TypedDict` key access computed type.

## Config Shape Example

Use a suite config that looks roughly like this:

```json
{
  "name": "tsp_core",
  "description": "Benchmark Pyrefly TSP type queries across simple and analysis-heavy Python code.",
  "protocol": "tsp",
  "workspace_dir": "src",
  "iterations": 5,
  "warmup_iterations": 1,
  "tsp_points": [
    {
      "label": "narrowed int branch",
      "request": "typeServer/getComputedType",
      "file": "src/flow_narrowing.py",
      "start_line": 7,
      "start_character": 8,
      "end_line": 7,
      "end_character": 13,
      "validation": {
        "requireNonEmpty": true,
        "expectedTypeKinds": ["Class", "BuiltIn"],
        "minSizeChars": 20
      }
    }
  ]
}
```

Line and character values should stay zero-based to match LSP and TSP conventions.

## Reporting Strategy

Keep TSP benchmark results in the same top-level report structure if possible so existing report generation still works.

That said, markdown and CSV rendering will likely need a small extension so TSP points surface a sensible preferred metric. Suggested preference order for TSP rows:

1. `type_kind`
2. `type_name`
3. `union_member_count`
4. `parameter_count`
5. `size_chars`

If the existing renderers are too LSP-specific, it is acceptable for the first pass to store TSP summaries in JSON only and defer markdown/CSV polish.

## Testing Plan

Add tests in layers.

### 1. Suite loading tests

Extend `tests/test_benchmarks.py` to verify:

1. A `protocol: "tsp"` suite loads correctly.
2. `tsp_points` parse into the new point model.
3. Existing LSP suites still load unchanged.

### 2. Runner tests with a fake server

Add a fake TSP-capable server fixture that:

1. Responds to normal LSP initialization.
2. Returns a fixed snapshot number.
3. Returns different TSP type payloads based on the requested file/range.

Use it to verify:

1. Requests are sent in the expected order.
2. Snapshots are passed through.
3. TSP metrics are summarized.
4. Validation failures are surfaced per point.

### 3. Optional integration test against local Pyrefly

Do not make this a required CI test initially. Use it as an opt-in developer validation step once the feature exists.

## Phased Delivery

### Phase 1: Minimum viable benchmark

1. Add TSP suite model and config parsing.
2. Add TSP client helpers.
3. Add a TSP runner path.
4. Add `benchmarks/tsp_core/` with no third-party dependencies.
5. Add JSON summaries and tests.

### Phase 2: Better semantic validation

1. Add more structured TSP result normalization.
2. Tighten validation rules for narrowing and specialization cases.
3. Improve markdown and CSV rendering.

### Phase 3: Virtual overlays and edit benchmarks

1. Add support for `pyright/setVirtualFileRedirect` and `pyright/removeVirtualFileRedirect`.
2. Add edit-driven TSP points using virtual files.
3. Reacquire snapshots after each redirect or edit.

## Open Questions To Resolve During Implementation

1. Which parts of the Pyrefly TSP type payload are stable enough for exact assertions versus shape-only assertions?
2. Does Pyrefly emit `typeServer/snapshotChanged` notifications eagerly enough that the runner needs explicit notification tracking from day one?
3. Should TSP be integrated into `bench-servers` with capability filtering, or should it begin as a separate `run-tsp-benchmark` and `bench-tsp-servers` command pair?
4. Are `Node` ranges alone sufficient for all desired type queries, or will some points require `Declaration` arguments later?
5. Should the first benchmark corpus remain stdlib-only, or is it worth adding one small `typing_extensions` case if Pyrefly exposes richer behavior there?

## Recommended First Implementation Slice

If a future session wants the smallest end-to-end slice that proves the design, implement this sequence:

1. Add a single `tsp_core` suite with `builtins_basic.py` and `flow_narrowing.py`.
2. Add `typeServer/getSnapshot` and `typeServer/getComputedType` only.
3. Use `Node` ranges only.
4. Add one validation that proves a narrowed branch differs from the unnarrowed branch.
5. Store the result in JSON reports even if markdown and CSV rendering remain generic.

That slice will prove the benchmark can drive Pyrefly over TSP and distinguish trivial type lookup from actual analysis.