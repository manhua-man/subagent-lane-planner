# Context and Capabilities

Read when the main agent needs specialized knowledge, context cleanup, a goal change, or task resumption. Keep task understanding in the main conversation; do not build a new memory service or capability registry.

## Load what the current action needs

- Start from the host's existing skill descriptions and tool discovery, if provided. Select for the current need, not a predefined professional role.
- Read the selected skill and mandatory project instructions as required by their own rules. Progressive disclosure means choosing relevant resources, not skipping parts of a selected mandatory instruction.
- Prefer an existing skill or reference for domain procedure and an actual tool for facts or actions. Do not spawn an agent just to load a procedure the main agent can use.
- Load supporting resources only when relevant. Reuse a known source while it remains applicable; do not repeatedly reload it or paste all references into the main prompt.
- If tools can run independently in one context, batch those calls. If the host lacks deferred search or a requested capability, work with the real tool surface or report the limitation.

## Retain decisions, not all intermediate output

Keep the latest goal and constraints, accepted facts with evidence locations, consequential decisions, unresolved work, and the next useful action. Long logs and repetitive exploration can stay in source artifacts; preserve the part needed to judge the next step.

For a long task or impending context handoff, update the existing task record or use a short checkpoint. A small task does not require a new plan, CONTEXT file, HANDOFF, or stage report.

A useful checkpoint answers:

- What is the current goal, scope, and acceptance result?
- What is established, where is its evidence, and which checks actually ran?
- What remains, what is the next action, and what is blocked?
- Is external work still active, what may it write, and which task/version does its result belong to?

This is a content guide, not a mandatory schema or a second source of truth.

## Change direction without losing control

When the user changes or cancels the goal, reconcile the old work before applying its results. Stop or redirect affected external work through supported, authorized controls; protect user edits and keep independent useful work only if it remains in scope.

On resumption, compare the checkpoint with the latest user request, relevant files, and active work. Recheck stale or conflicting facts narrowly. A past green test does not prove an artifact that changed afterward, and a chat title does not prove its current assignment.

When shared context is genuinely becoming noisy, use a narrower evidence read, a compact checkpoint, or a bounded external investigation as appropriate. Do not blindly keep everything in one prompt or create a fresh chat for every phase.

## Know the host boundary

Skill instructions do not add persistent memory, automatic compaction, permission enforcement, message delivery, or automatic continuation. Use supported mechanisms and state what was actually retained or verified. If a required result cannot return automatically, explain how the task will be resumed rather than promising invisible background progress.
