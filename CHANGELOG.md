# Changelog

All notable changes to the `subagent-lane-planner` skill will be documented in this file.

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
