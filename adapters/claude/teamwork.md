---
description: Useful parallel work with owned writes and stable dependencies. Use when the user requests /teamwork mode.
---

# /teamwork

When the user requests `/teamwork` or its equivalent behavior:

Use the already selected `subagent-lane-planner` installation. If none is selected, look for the complete bundle in the current project's `.agents/skills/subagent-lane-planner/`, then in `$HOME/.agents/skills/subagent-lane-planner/` (`$HOME` means the user's home directory). The bundle root contains the canonical `SKILL.md`, `modes/`, and `references/`.

Resolve all paths below from that bundle root, not from this adapter or the working directory. If required files are missing, report the missing location; do not claim the mode is loaded.

Read `SKILL.md`, then `modes/teamwork-mode.md`. Apply their shared and mode-specific rules. The canonical files define acceptance, scope, authorization, and stopping behavior; this adapter only locates them.
