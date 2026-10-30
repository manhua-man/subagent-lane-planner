---
description: Run autonomously with mandatory machine verification. Invokes goal-mode.
---

# /goal

Activate the `/goal` auxiliary mode of `subagent-lane-planner`.

Follow the rules in `modes/goal-mode.md`:
- Do not stop until all code is implemented and verified via actual test/build commands.
- Require exit code 0 on verification.
- Auto-repair compilation and test failures.
- Stop only if the exact same failure recurs 3 times with zero progress.
