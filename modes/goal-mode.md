# Mode: /goal (Persistent Execution and Acceptance)

Use when the user requests `/goal` or sustained execution through verification. Apply the shared mode rules in [SKILL.md](../SKILL.md#auxiliary-command-modes).

## Verify the requested outcome

- Establish acceptance from the current user goal and project requirements. For implementation work, run relevant available tests, lint, or build commands and inspect the resulting behavior or artifacts. A successful exit code is necessary for a command that uses it to signal success, but does not by itself establish task completion.
- Choose checks that cover the changed behavior. Keep agreed contracts and acceptance criteria intact; do not weaken tests or suppress failures merely to obtain a green result.
- For analysis, documentation, or tasks without suitable automation, use concrete evidence such as source references, examples, rendered output, or artifact inspection. Do not invent a test requirement for an unrelated deliverable.
- If a required check cannot run, report what prevented it and which result remains unverified. Distinguish pre-existing failures from regressions with evidence; neither a missing check nor a baseline failure counts as a pass.

## Repair while useful action remains

- Diagnose routine implementation, syntax, type, and test failures and repair them within scope without asking for approval at each attempt. Re-run affected checks after a relevant change.
- Classify the failure before retrying. Continue independent useful work, but report a known missing authorization, necessary user decision, unavailable input, or external dependency when it prevents progress; do not wait for a retry count.
- Track progress by new evidence or a meaningful change in approach, not by whether the error text is identical. After three consecutive repair attempts without progress, reassess. Continue only with a materially different, evidence-supported next step; otherwise report the unresolved failure, attempted remedies, and what would enable progress. An unresolved implementation problem must not be relabeled an external blocker.

## Finish or report the actual stopping condition

- Declare completion only when the latest requested deliverable and its required acceptance checks are satisfied. Briefly report the result and actual verification.
- If required work or verification remains blocked, report it as incomplete, with the reason and resumption condition. Honor user redirection or cancellation immediately; safe stopping is distinct from successful completion.
