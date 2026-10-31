---
name: lane-modes
description: Load the goal, boost, or teamwork modifiers of subagent-lane-planner when the user requests those modes.
---

# Auxiliary Mode Adapter

Use the already selected `subagent-lane-planner` installation. If none is selected, look for the complete bundle in the current project's `.agents/skills/subagent-lane-planner/`, then in `$HOME/.agents/skills/subagent-lane-planner/` (`$HOME` means the user's home directory). The bundle root contains the canonical `SKILL.md`, `modes/`, and `references/`.

Resolve all paths below from that bundle root, not from this adapter or the working directory. If required files are missing, report the missing location; do not claim the mode is loaded.

Read `SKILL.md` and only the requested mode files:

- `/goal`: `modes/goal-mode.md`.
- `/boost`: `modes/boost-mode.md`.
- `/teamwork`: `modes/teamwork-mode.md`.

Apply the canonical shared and mode-specific rules. This adapter only locates them; it adds no separate execution policy.
