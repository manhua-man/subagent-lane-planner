---
name: subagent-lane-planner
description: >-
  Decide and execute safe Codex subagent delegation for coding, debugging,
  refactoring, testing, verification, documentation, and cleanup. Use when Codex
  must judge whether delegation provides clear parallel or investigative value,
  divide work into independent scopes, or integrate delegated results.
---

# Subagent Lane Planner

Use the current host's native subagent tools as a thin execution policy. Do not create a scheduling system, persistent agent configuration, or elaborate planner artifact. For Cursor-specific usage, read [the host guide](references/cursor-task-prompt.md); for a requested plan-only deliverable, use the optional [plan template](references/plan-artifact-template.md).

## Assess

- Execute in the main thread unless delegation clearly reduces wall-clock time, protects the main context from noisy work, or de-risks an unclear boundary.
- Start the minimum useful number of subagents. Do not delegate trivial work or a single dependent chain.
- Do not allow subagents to spawn or delegate to other agents.
- Prefer parallel delegation for independent read-heavy work. Parallelize writes only when write scopes are disjoint and no task needs another task's unfinished result.
- Stable read scopes may overlap. Assign exactly one owner to every shared contract or concurrently edited file.

## Choose Subagent Models

- Honor available explicit user model and reasoning choices independently. For unspecified fields, inherit the runtime defaults unless an allowed override has a clear task-specific benefit; this policy permits such overrides when supported by the active tool and higher-priority instructions.
- If a requested model or reasoning level is unavailable, automatically use a suitable supported alternative, preferring the runtime default when suitable, and continue without requesting confirmation. Briefly tell the user what was requested, what was used, and why. Preserve any supported requested field; do not substitute if the user explicitly forbids fallback. If no suitable alternative is available, report the blocker.
- Choose from models and reasoning levels actually available in the current environment. Use their declared capabilities or measured task results; do not infer price, speed, or quality from model names. If that evidence is missing, keep the default.
- For bounded routine work with objective acceptance checks, prefer a known faster or lower-cost model that meets the task's capability needs. For ambiguous root-cause analysis, architecture decisions, or high-risk review, prioritize demonstrated reasoning ability and required tools/context capacity. Do not bind roles to particular model names or default every task to maximum reasoning.
- Before escalating after failure, distinguish missing context, unclear scope, and environment/tool failures from a reasoning limitation. The main thread may choose a more capable available model when evidence supports it; subagents report blockers rather than changing their own model. Record the reason for an override briefly.

## Delegate

Give each subagent only:

- `Goal`: one narrow outcome.
- `Read`: the files or subtrees it may inspect.
- `Write`: exact files or directories it may edit, or `none`.
- `Acceptance`: an objective check or concrete evidence to return.

Add a role, working directory, model override, ignore list, or extra directives only when the task requires them. Keep unrelated edits out of scope.

- Return concise findings, relevant file or symbol references, verification results, and blockers; include raw logs only when needed to assess the evidence.
- If progress requires an architectural decision, a shared-contract change outside the assignment, or broader file ownership, report the blocker to the main thread before making that change.

## Integrate

- The main thread owns shared contracts, coordination decisions, result review, and verification proportionate to the change. Run targeted checks first; expand to integration or workspace-wide checks when shared behavior or cross-module contracts warrant them.
- Continue useful independent main-thread work while subagents run.
- If a subtask fails or violates scope, stop dependent work until its inputs are stable and accepted, and replan only the affected work. Do not automatically broaden scope or add agents.
- Before claiming completion, ensure all required subagents have finished or explicitly failed, resolve conflicting findings, and integrate and verify the required results. Recover unfinished required work or report it as incomplete.
- For implementation requests, perform useful delegation and integration instead of stopping after a plan. For plan-only requests, return the decision, dependency order, subtask contracts, and integration checks briefly.
