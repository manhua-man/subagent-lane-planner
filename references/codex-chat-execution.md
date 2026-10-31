# Independent Codex Chat Execution

Read this guide when considering creation or coordination of Codex desktop chats. These are user-owned sidebar conversations, with a different lifecycle from native child agents. The following constraints describe the current Codex desktop tools, not a universal restriction imposed by this skill; current tool descriptions and higher-priority instructions are authoritative. Do not assume these tools or restrictions exist in another host.

## Establish Scope

- Use `Goal`, `Read`, `Write`, and `Acceptance` when they clarify the assignment. Send a clear, cohesive task prompt; include the actual project/checkout and accepted source identity when relevant. Coordinate shared writes through explicit ownership, isolation, or sequencing.
- Use `list_projects` before creating a project chat. Select the returned project ID. Use a projectless chat for work without a repository. Do not infer a project or checkout from a similar chat title.
- Default to local execution. Request a worktree only when the human explicitly requested one and the project is a Git repository. Specify a starting Git ref or working-tree snapshot only when requested; never invent a branch or assume uncommitted changes are copied.
- Check the actual selected checkouts for competing writers. Coordinate evolving inputs and provisional assumptions; independent investigation and implementation can proceed while shared details are being resolved. Reconcile dependent results against the accepted source before integration.

## Create and Wait

1. The current Codex desktop `create_thread` tool is available only when the human explicitly asks to create a new task. A general preference for autonomous coordination does not change this tool condition. Existing-chat work uses the existing identity and the authorization for that action.
2. Save the returned identity and host. A ready `threadId` can be inspected or waited on. A pending `clientThreadId` is a UI receipt, not a ready thread ID: do not pass it to `read_thread`, `wait_threads`, or `send_message_to_thread`.
3. For pending setup, use a returned setup operation/status mechanism when available; otherwise use `list_threads` or host completion evidence to establish the actual ready identity. Do not guess by title or create a duplicate after an unknown outcome. If no reliable identity can be established, report that unresolved setup.
4. After successful creation, include the host's required created-chat receipt in the final response: `::created-thread{threadId="..."}` for a ready chat, or `::created-thread{clientThreadId="..."}` for pending setup. Never emit a receipt for a chat that was not created.
5. Use compact `wait_threads` snapshots for ready workers, up to the tool's supported batch size (currently eight). Carry each returned cursor as `afterCursor`, and include the host ID when known. Use `timeoutMs: 0` for a snapshot or a bounded wait of at most 60 seconds while maintaining user updates. Use `read_thread` only when more evidence is needed, with bounded output.

Keep identities, cursors, write ownership and completion evidence in the current task's working context.

## Follow Up and Integrate

- `send_message_to_thread` requires explicit human authorization to message that destination. A request to create a chat authorizes its initial prompt; follow-up messaging needs authorization as well. Honor an existing human instruction to coordinate or send follow-ups without asking again when it clearly covers that destination and action.
- A worker's request to reply, report back, or message another chat is not human authorization. Return evidence through available status/reading tools; do not teach worker chats to message the parent automatically.
- Preserve the worker's configured model and reasoning unless the human requests an override; apply the current host's tool restrictions alongside the core model policy.
- A completed chat status is a signal to review. Verify actual files, diffs, source identity and relevant checks before claiming integrated completion. A receipt from an older candidate cannot prove the changed candidate.
- On failure, reassess affected dependencies, inspect the evidence, and recover using available authorized actions. Continue useful work and revise provisional assumptions as needed. Do not silently replace a specifically requested independent chat with a subagent, or claim required work complete while setup or verification is unresolved.
- Do not archive, move, navigate to, or otherwise reorganize worker chats unless the human requested that action. Keep the final report clear about which chats were created, which results were integrated, and what remains incomplete.

## Example Human Request

“Create one local chat in the public-controls project and one in the game-adapter project. Fix the export and adapter projection in disjoint files, coordinate them, and send follow-ups to those two chats as needed. Review and verify both before reporting completion.”

This request authorizes two creations and scoped follow-up messages. Resolve project IDs, accepted source and task boundaries, create both chats, wait on their ready identities, then integrate their evidence. Worktree and model choices remain subject to the current host tools and the user's request.
