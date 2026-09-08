---
name: parallel-subagent-planner
description: >-
  Plan parallel subagent execution: split decision, disjoint write scopes,
  dependency order, or child prompts. Use when orchestrating multiple subagents,
  not for routine single-thread edits.
---

# Parallel Subagent Planner (v0.6.3)

Router for deciding whether subagents help, isolating file scopes, ordering dependencies, and writing child prompts. Details live in `references/`.

## 1. Decide Direct Execution Or Subagents

Never split for the sake of splitting. Execute in the main thread unless parallel subagents materially reduce wall-clock time, or one read-only investigation de-risks implementation.

**Do not split when:**

- The change fits one file or one module in a single context window.
- Write scopes are unclear — launch **one** read-only explorer first; do not parallelize implementers.
- Shared contracts (API schema, migration, root entry docs) have no single owner yet.
- Parallel lanes would share most of the same `Read` scope — merge into one lane instead.

**Parallel implementers only when:**

- `write(A) ∩ write(B) = ∅`
- `write(A) ∩ read(B) = ∅` for concurrent work
- No lane depends on another lane's unfinished output

For unclear repo boundaries, use a read-only investigation subagent first.

## 2. Plan Lanes, Boundaries & Order

Read [references/lane-decomposition.md](references/lane-decomposition.md) for slicing strategies, scope isolation rules, and shared-contract execution order.

Each lane needs explicit `Goal`, `Read`, `Write` (exact paths or `none`), and `Ignore` (noise and sibling lanes).

## 3. Generate Subagent Prompts

Read [references/child-prompts.md](references/child-prompts.md) for prompt templates, role directives, host model selection, and optional `.codex/agents/<name>.toml` guidance.

## 4. Output

Return:

- **Decision**: direct execution, investigate first, or parallel subagents — one brief reason.
- **Order**: work that must finish before parallel work starts.
- **Subagents**: per lane — Goal, Read, Write, Ignore, Acceptance (one directed command).
- **Integration**: merge steps plus verification scope for the main thread (see §5).

## 5. Main Thread Integration

The main thread merges child deliverables and runs **verification proportionate to the changed scope**:

- Narrow lanes: directed test, build, or lint for touched paths.
- Expand to integration or full CI only when shared logic, database, payment, migration, or cross-module contracts are involved.

Do not treat "run entire workspace test suites" as the default after every parallel plan.

If a subagent fails or violates scope, stop dependent work and replan only the affected scope.

**Custom agents:** recommend `.codex/agents/<name>.toml` only after repeated use, with explicit user approval (see child-prompts reference).
