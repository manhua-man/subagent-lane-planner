# Cursor Host Guide

Adapt the main task loop to Cursor's actual tools and current project instructions.

- Choose direct execution, parallel tool calls, or external work according to the task. Use [delegation](delegation.md) to describe assignments and coordinate writes.
- If the host exposes a `Task` tool, map the assignment to its supported fields and executor types. Select models through the shared delegation guidance and available choices.
- Run useful independent work concurrently, and manage provisional assumptions where interfaces are evolving. Reconcile affected work before relying on its integrated result.
- Retain pending results and use the host's supported continuation mechanism. Independent chats and native child agents may expose different creation, messaging, and waiting tools.

Use [context and capabilities](context-and-capabilities.md) for continuity, and the optional [living task plan](plan-artifact-template.md) when a saved record helps.
