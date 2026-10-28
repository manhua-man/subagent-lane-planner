# Changelog

All notable changes to the `subagent-lane-planner` skill will be documented in this file.

## [Unreleased]

### Host-dependent chat selection

- Removed the skill's blanket explicit-request gate: the main loop can select independent chats autonomously where the host and user constraints allow it.
- Documented current Codex desktop creation and messaging requirements as host-specific, and added contrasting evaluation conditions without claiming real-host validation.

### Independent chat execution

- Added an optional Codex desktop chat lifecycle for explicitly requested independent conversations, while keeping native subagents as the default parallel path.
- Defined ready versus pending identities, cursor-based waits, human authorization for follow-up messages, source-aware integration and failure recovery.
- Added chat behavior replay cases without introducing a scheduler or persistent planner state.

### Main-agent task loop — 2026-10-26

- Repositioned the workflow around one main conversation that owns the goal, acts, absorbs evidence, revises its plan, and verifies completion; delegation is no longer the central required stage.
- Retained the skill identifier and installation paths; updated UI metadata, invocation examples, and both READMEs without adding another entry point.
- Added progressive references for context/capability loading and task continuity; moved the existing model, scope, and four-field delegation policy into a conditional reference.
- Distinguished native subagents from authorized independent chats without adding a scheduler, persistent role system, permission mechanism, or automatic continuation.
- Reworked the optional plan as a living task plan and aligned Cursor guidance with actual host capabilities and authorization.
- Added task-level replay observations, a runnable reference fixture with fixed failing-starter preparation, and a pilot record separating local validation from unmeasured agent performance and host integration.

### History integration

- Combined the formerly separate histories while retaining the `subagent-lane-planner` name and current repository/install paths.
- Retained the optional Cursor guide and plan template, aligned them with the four-field task contract, and kept model policy in the core skill.
- Preserved proportionate verification and stopping dependent work after failures; removed the stale tracked release archive.
- Added a reusable real-task review prompt and README entry points.

### Delegation evidence and evaluation

- Added automatic fallback with brief user notification for unavailable requested models or reasoning levels, preserving explicit no-fallback instructions and independently supported choices.
- Added model-neutral subagent selection based on user choices, available models, task needs, and capability/cost evidence, with failure classification before escalation.
- Added separate model-selection replay cases for multiple models, default preservation, and escalation decisions.
- Added concise evidence returns, reporting before out-of-scope decisions or changes, and an explicit integration completion check.
- Extended replay guidance with repeated controlled runs, per-thread/model token breakdowns, and separate model-configuration comparisons.
- Added replay cases for noisy evidence, shared-schema escalation, and incomplete or conflicting subagent results.

### Convergence release

- Reframed the project as a thin execution policy over Codex's native subagent tools.
- Reduced the core loop to assess, minimally delegate, and verify in the main thread.
- Replaced the eight-field prompt template with `Goal`, `Read`, `Write`, and `Acceptance`.
- Allowed overlapping reads of stable inputs while retaining disjoint concurrent writes and single ownership for shared contracts.
- Removed duplicated references, custom-agent persistence guidance, the nested anti-overengineering skill, and the tracked release archive.
- Added a small set of paired behavioral replay cases instead of a planner schema or scheduling framework.

## [v0.7.0] - 2026-09-08

### Rename — skill, repository, and install paths
- **Skill `name`**: `parallel-subagent-planner` → `subagent-lane-planner`
- **GitHub repository**: `codex-parallel-subagent-planner` → `subagent-lane-planner` (old URL redirects)
- **Install directory**: `~/.agents/skills/subagent-lane-planner/` or `<repo>/.agents/skills/subagent-lane-planner/`
- **Release zip**: `subagent-lane-planner-v0.7.0.zip`
- Display name and trigger phrases updated; skill behavior unchanged from v0.6.5

## [v0.6.5] - 2026-09-08

- **README trigger guides**: Three-line how-to for Cursor, Codex, and Claude Code after install.
- **`references/cursor-task-prompt.md`**: `subagent_type` selection, default `inherit` model, true parallelism via multiple `Task` calls in one message.
- **`references/plan-artifact-template.md`**: Optional markdown plan for user review before spawn.
- **`lane-decomposition.md` §4 Replan triggers**: Scope violation, shared-file conflict, lane failure — stop dependents, replan affected lanes only.
- **SKILL.md**: Links to plan artifact and Cursor reference; version bump.

## [v0.6.3] - 2026-09-08

- Router-style `SKILL.md` with details in `references/lane-decomposition.md` and `references/child-prompts.md`
- Split decision with do-not-split triggers; disjoint write/read scopes and single contract owner
- Proportionate main-thread verification (directed checks by default, not full-repo CI)
- Child prompts use one directed Acceptance command per lane
- Host-driven model/subagent selection; no frozen model catalog in the skill

## Legacy branch history

The entries below belong to the previously separate parallel-subagent-planner history; their version numbers are not newer releases of this repository.

## [v3.0.1] - 2026-08-05

### Patch Release — Pragmatic Refinements & Output Standardization
- **Decoupled Read-Only Investigation**: Separated read-only Explorer rules from parallel implementation write-isolation criteria.
- **Purged State Machine Residuals**: Replaced `blocked` and `frozen` terms with natural, step-by-step behavioral execution directives.
- **Flexible Contract Ownership**: Extended shared contract file ownership to support either the main thread or a subagent.
- **Minimal Output Specification**: Added standardized `## 5. Output` section (`Decision`, `Order`, `Subagents`, `Integration`).
- **Text & Metadata Consistency**:
  - Updated `agents/openai.yaml` short description and default prompt.
  - Updated Core Cycle in README docs to `Decide ➔ Split ➔ Isolate ➔ Order ➔ Prompt ➔ Integrate`.
  - Removed non-coding disclaimer from frontmatter.

## [v3.0.0] - 2026-08-05

### Major Release — Pure Pragmatic Planning Skill (Breaking Refactor)
- **Purged Pseudo-Engineering Bloat**:
  - Removed state machine systems (`ready`, `running`, `done`, `integrated`, `blocked`, `held`).
  - Removed anti-scope disclaimers ("Four Hard Boundaries", "No Physical Runtime").
  - Removed 12-field Ready Gate bureaucracy.
  - Removed simulated evolution engines (`promotion_check: silent/ask/off` policies & 4 Quality Filters).
- **Consolidated References (5 Assets -> 2 Assets)**:
  - `references/lane-decomposition.md`: Task slicing, scope isolation, and shared contract execution order.
  - `references/child-prompts.md`: Subagent prompt templates, directive examples, and custom agent `.toml` guidance.
- **Streamlined SKILL.md**: Reduced to ~50 lines of clean, pragmatic instructions focused 100% on real cognitive value.

## [v2.0.10] - 2026-08-05
- Refined role metadata table and read-only sandboxing wording.

## [v2.0.0] - 2026-08-04
- Refactored repository into Lean Agent Planning Harness Skill.
