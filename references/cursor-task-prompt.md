# Cursor Host Guide

Read only for Cursor-specific adaptation. The active host's instructions and tool schema are authoritative; do not assume another host's tool names, model IDs, chat APIs, or continuation behavior.

- Keep the goal, task understanding, next action, and final acceptance in the main conversation. Use available skills/references and tools without creating an agent just to represent each specialty.
- Complete direct work in the main conversation when appropriate; independent tool calls can run in parallel without extra agents.
- If external work is justified and authorized, apply [delegation](delegation.md). If the host exposes a `Task` tool, map the four-field contract to supported prompt/description fields and use only available executor types.
- Apply the model policy in that reference; do not maintain a separate Cursor model catalog.
- Dispatch independent authorized work before waiting, using the concurrency mechanism the host actually supports. Dependent work waits for accepted inputs.
- Do not assume a `Task` tool also permits creating or messaging standalone chats. Check those capabilities and their authorization separately.
- Bring accepted results back into the main task and take the next action. If automatic resumption is unsupported, preserve pending work and disclose the required continuation step.

Use [context and capabilities](context-and-capabilities.md) for noisy context or resumption, and the optional [living task plan](plan-artifact-template.md) only when useful.
