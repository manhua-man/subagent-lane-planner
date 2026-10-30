---
description: Specialized execution with mandatory adversarial quality audit. Invokes boost-mode.
---

# /boost

Activate the `/boost` auxiliary mode of `subagent-lane-planner`.

Follow the rules in `modes/boost-mode.md`:
- Distinguish investigation (root cause first) from coding (production quality, zero mocks/TODOs).
- Run mandatory adversarial self-audit on boundary values, nulls, concurrency, and error handling.
- Treat detected edge-case gaps as internal rejections and fix them before completion.
