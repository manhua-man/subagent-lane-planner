# Cursor Host Guide

Use this reference only when executing in Cursor. The active host's tool schema is authoritative; do not assume tool names, agent types, or model IDs from another session are available.

- If the host exposes a `Task` tool, map the narrow task contract to its supported prompt and description fields. Select an investigation or implementation agent type only from those currently available.
- Give each child `Goal`, `Read`, `Write`, and `Acceptance`. Read-only work uses `Write: none` and must still return concrete evidence. Add working directory or role only when needed.
- Apply the [core model-selection policy](../SKILL.md#choose-subagent-models), including supported fallback with notification. Do not maintain a separate Cursor model catalog.
- Dispatch independent tasks before waiting for their results, using the concurrency mechanism the host supports. Dependent work waits for stable accepted inputs.
- Children must not delegate further. The main thread reviews evidence, resolves conflicts, and performs checks proportionate to the changed scope.

For a user-requested planning deliverable, use the optional [plan template](plan-artifact-template.md). An implementation request already authorizes useful delegation within scope; this template does not add an approval step.
