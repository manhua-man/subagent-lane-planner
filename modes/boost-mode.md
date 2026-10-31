# Mode: /boost (Focused Investigation and Adversarial Review)

Use when the user requests `/boost`, deeper root-cause investigation, or stronger verification. Apply the shared mode rules in [SKILL.md](../SKILL.md#auxiliary-command-modes).

## Investigate the relevant behavior

- Trace the affected execution paths, reproduce defects where feasible, and use evidence to distinguish competing explanations before committing to a fix. Temporary diagnostic edits are allowed when needed to test a hypothesis; remove them before delivery unless they belong in the requested result.
- Implement the agreed behavior without placeholders that bypass required functionality. Preserve the requested fidelity: a prototype, test double, analysis, or plan does not become a production rewrite merely because this mode is active.

## Review before delivery

- Review the changes and directly affected paths for plausible failure cases. Select relevant checks from boundary values, empty or missing inputs, state transitions, concurrency, error propagation, and resource cleanup; do not apply every category to every task.
- Correct material defects introduced or exposed by the change when they prevent the agreed behavior. Report unrelated existing issues separately rather than expanding the assignment to fix them.
- For each material finding, verify the correction with an appropriate focused test or other observable evidence. Add or adjust tests when they provide meaningful regression protection; reuse sufficient existing checks.
- For an analysis-only task, challenge the key conclusions against their evidence and plausible counterexamples. Report remaining uncertainty instead of manufacturing code changes or test runs.

Finish when the requested outcome and relevant review findings are resolved. If a required issue cannot be resolved within the current scope or authority, report the specific incomplete result using the main task loop's stopping rules.
