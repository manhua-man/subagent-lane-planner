# Mode: /goal (Autonomous Lifecycle & Machine Acceptance)

Activate this mode when the user explicitly includes `/goal` or requests unattended long-running execution until fully verified.

This is an **auxiliary modifier** over the main-agent task loop. It modifies termination behavior without altering baseline reasoning.

## Invariants Under /goal

1. **Deterministic Verification Gate**:
   - The main agent MUST NOT declare completion based on static review or intermediate edits alone.
   - Run relevant automated tests, linter, or build checks via the environment terminal.
   - Acceptance requires exit code 0 on all targeted verification commands.

2. **Autonomous Self-Healing Loop**:
   - If a test fails, syntax errors occur, or types break, the main agent continues immediately into a repair cycle.
   - Do not stop or prompt the user for routine compilation/test failures. Diagnose the error and fix it.
   - **Circuit Breaker**: If the exact same failure pattern repeats 3 consecutive times with zero progress, stop and report the precise external blocker or ambiguity to the user.

3. **Termination Signal**:
   - Only conclude when:
     1. All requested changes are applied.
     2. Automated checks pass with verified exit code 0.
     3. A brief summary of changed files and test outputs is presented.
