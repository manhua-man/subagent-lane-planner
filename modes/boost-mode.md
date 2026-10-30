# Mode: /boost (Specialized Execution & Adversarial Audit)

Activate this mode when the user explicitly includes `/boost` or demands deep verification, root-cause investigation, and zero-compromise engineering.

This is an **auxiliary modifier** over the main-agent task loop. It introduces a mandatory pre-completion audit hook.

## Invariants Under /boost

1. **Focused Specialization**:
   - **Investigation Work**: Dedicated strictly to tracing execution paths, reproducing defects, and verifying hypotheses before any code edit.
   - **Implementation Work**: No placeholders, no TODOs, no superficial mocks for critical paths. Deliver production-ready code.

2. **Adversarial Self-Audit (Mandatory Rejection Loop)**:
   - Before handing the work to the user, run an adversarial audit on the changes:
     - **Boundary Conditions**: Null/undefined, zero, empty arrays/strings, overflow, off-by-one.
     - **State & Concurrency**: Shared mutable state, race conditions, re-entrancy risks.
     - **Error Handling & Resources**: Graceful failures, explicit error propagation, open stream/file handle cleanup.
   - If ANY unhandled edge case or sloppy workaround is detected, treat it as an internal rejection. Self-correct and refactor before completing.

3. **High-Watermark Verification**:
   - Ensure tests cover both happy paths and negative edge cases identified during the adversarial audit.
