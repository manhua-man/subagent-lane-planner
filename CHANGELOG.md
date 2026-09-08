# Changelog

All notable changes to the `parallel-subagent-planner` skill will be documented in this file.

## [v0.6.3] - 2026-09-08

- Router-style `SKILL.md` with details in `references/lane-decomposition.md` and `references/child-prompts.md`
- Split decision with do-not-split triggers; disjoint write/read scopes and single contract owner
- Proportionate main-thread verification (directed checks by default, not full-repo CI)
- Child prompts use one directed Acceptance command per lane
- Host-driven model/subagent selection; no frozen model catalog in the skill
