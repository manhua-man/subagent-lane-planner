---
description: Parallel decomposition with single-writer collision avoidance. Invokes teamwork-mode.
---

# /teamwork

Activate the `/teamwork` auxiliary mode of `subagent-lane-planner`.

Follow the rules in `modes/teamwork-mode.md`:
- Decompose large tasks into mutually disjoint scopes.
- Enforce the single-writer invariant: no two lanes may touch the same file.
- Keep shared entry points in the main coordinator and merge during the consolidation phase.
