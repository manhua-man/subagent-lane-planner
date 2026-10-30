# Mode: /teamwork (Orthogonal Lane Decomposition & Single-Writer Invariant)

Activate this mode when the user explicitly includes `/teamwork` or requests multi-component, large-scale concurrent development.

This is an **auxiliary modifier** over the main-agent task loop. It activates parallel delegation lanes while maintaining central coordination.

## Invariants Under /teamwork

1. **Orthogonal Scope Decomposition**:
   - The main agent decomposes the large goal into mutually disjoint subtasks.
   - Map files to subtasks explicitly to guarantee zero overlap in write targets.

2. **Single-Writer Invariant (Zero Collisions)**:
   - No two parallel lanes may edit the same file concurrently.
   - Shared entry points (e.g. `index.ts`, central routers, root package configs) are retained strictly by the main agent and updated only in the final consolidation phase.

3. **Consolidation Phase**:
   - As parallel lanes finish their respective modules, the main agent integrates them into the shared entry point.
   - Run holistic integration checks across all modified modules.
   - Only declare completion once all lanes are integrated and global checks pass.
