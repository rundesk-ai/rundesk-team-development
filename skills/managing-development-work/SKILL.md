---
name: managing-development-work
description: Use when planning, coordinating, implementing, or completing a software change, including a feature, bug fix, refactor, configuration change, or repository documentation. It owns outcome definition, scope, workflow selection, risk response, integration, and verified local completion. Compose it with the applicable stack and task skills. Do not use it for a standalone GitHub issue, pull request, release, repository administration, or non-development work.
---

# Manage development work

Deliver the requested software outcome through the smallest workflow that can prove it. This skill
coordinates development; it does not replace the technical method owned by a framework, language,
database, design, planning, debugging, review, testing, or documentation skill.

## Keep the ownership boundary explicit

This skill owns:

- the completion contract, scope, constraints, and preserved behavior;
- the choice between direct work, bounded implementation, planned delivery, and discovery;
- risk-based coordination, integration, and completion evidence; and
- the decision that a verified local result is ready for any separately authorized delivery.

It does not own GitHub issues, pull requests, releases, hosted repository administration, or stored
GitHub verification. Use the [GitHub handoff](#separate-the-github-handoff) only after the local
development result is coherent. It also does not teach specialized implementation, debugging,
review, test, planning, or stack rules; load those skills when their actual triggers apply.

## Define completion before choosing a workflow

Turn the request into one concise contract:

- **Outcome:** the behavior or artifact the requester will receive.
- **Proof:** the observable automated checks and representative user or system path that distinguish
  complete from plausible.
- **Scope:** the components and contracts that may change, plus explicit exclusions.
- **Preservation:** behavior, compatibility, data, and interfaces that must remain unchanged.
- **Authority:** actions already requested and later mutations that still require approval.
- **Unknowns:** only facts that could materially change the solution, risk, cost, or reversibility.

Read repository instructions and inspect the current branch, worktree, relevant implementation,
tests, and documentation before proposing an architecture. Preserve existing owner changes. Ask for
an owner decision only when the answer cannot be discovered and choosing would change the accepted
outcome or authority.

Investigation, review, planning, and implementation are different authorizations. A request for one
does not silently grant the others.

## Choose the smallest engagement mode

Classify from observed boundaries, not from the apparent sophistication of a solution.

**Direct work.** Use for a localized documentation, copy, metadata, configuration, or contained code
change with a confirmed cause, no architectural choice, and focused proof. Keep a short working
checklist in the current turn. Do not create a standalone plan or delegate for ceremony.

**Bounded implementation.** Use for one coherent code outcome inside a known design boundary. One
implementer owns the change and its focused proof. Pause before implementation when the likely work
crosses several production components, introduces a new service or architectural layer, changes a
public contract, or needs a refactor to make the outcome possible. Those are decision signals, not
size targets.

**Planned delivery.** Use an executable implementation plan when work has three or more dependent
steps, crosses meaningful component boundaries, requires staged compatibility or recovery, or will
be handed across contributors. Each plan task must leave a coherent state and include its own proof.

**Discovery before commitment.** Use bounded read-only discovery when one unknown in a sizable or
unfamiliar codebase materially changes the approach. State the exact question, inspection boundary,
evidence required, and decision it unlocks. Stop when that unknown is resolved; do not inventory the
whole system.

## Increase ceremony only for observed risk

Name the trigger and add the matching evidence:

| Risk trigger | Required response |
|---|---|
| Authentication, authorization, secrets, or privacy | Trace trust boundaries, redaction, and refusal paths. |
| Money, entitlement, or irreversible business state | Preserve invariants and define reconciliation. |
| Schema, migration, deletion, or persisted state | Define compatibility, recovery, and post-change checks. |
| Production, infrastructure, or deployment | Separate implementation authority from rollout and define rollback and health proof. |
| Public API, format, or integration | Identify actual consumers and prove compatibility. |
| Concurrency, performance, or broad blast radius | Characterize a representative baseline and the relevant limit. |

Independent review or additional testing responds to repository policy, requester direction, or a
named risk. Do not route every ordinary change through a fixed sequence of specialists.

## Hold the scope boundary

Before approving an approach, verify:

1. Every production change directly delivers the accepted outcome or necessary proof.
2. An existing boundary cannot solve it more simply.
3. Cleanup, modernization, deployment, and adjacent defects remain excluded unless requested or
   strictly necessary.
4. The work remains inside the accepted behavior, compatibility, risk, and authority boundary.

If a larger boundary is genuinely necessary, stop before changing it. Present the smallest viable
expansion, why the original boundary fails, affected contracts, risks, alternatives, and proof. Do
not let sunk effort or passing tests authorize new scope.

Never infer a refactor from a feature or bug request. For an explicit or proven refactor,
characterize preserved behavior first and split work into reversible increments.

## Coordinate without duplicating work

Keep decisions, dependency order, integration, and final communication with one responsible agent.
Use one implementer by default. Split work only into independent outcomes with non-overlapping edit
boundaries whose parallel value exceeds the coordination cost.

A handoff states:

- one testable outcome and why it is needed;
- files or component boundary, read/write permission, and prohibited changes;
- accepted size, compatibility, risk, and authority limits;
- applicable repository rules and technical skills;
- expected artifacts and exact proof; and
- stop conditions for completion, expansion, or a specific unavailable dependency.

A returned summary is not integration. Inspect the workspace, full diff, surrounding contracts,
changed-file and production-line scope, and reported evidence. Rerun the narrowest meaningful checks
on the integrated result, followed by the repository-required gate. Exercise a safe representative
path when behavior is observable.

Allow a focused correction for a contained miss. If correction reveals a different design or a
larger boundary, re-scope rather than layering patches.

## Prove completion

Trace every accepted requirement to the integrated artifact and observed evidence. Completion
requires all of these:

- the requested behavior or artifact exists;
- unrelated work and speculative abstraction are absent;
- focused checks and repository gates passed with observed non-zero discovery where applicable;
- the representative safe user or system path produced the expected result;
- named risks have their required failure, recovery, compatibility, or rollout evidence;
- temporary artifacts and processes are gone; and
- every unrun check, owner-only visual judgment, or external delivery step is reported accurately.

Do not report completion from a successful exit status, a started background process, an uninspected
return, pending CI, or a statement that something should work.

## Separate the GitHub handoff

An issue, branch push, pull request, tag, release, or deployment operation is not automatic
development ceremony. Prepare or perform it only when the requester asks, repository policy requires
it, or it is the separately authorized durable delivery artifact.

Before handing the verified local result to `managing-github`, record:

```text
Outcome: <delivered behavior>
Scope: <changed production surface and material compatibility impact>
Risk: <named triggers and safeguards, or none material>
Proof: <observed automated and representative-path results>
Excluded: <adjacent work intentionally not performed>
Unrun: <required checks or external state still pending>
```

That handoff supplies evidence; it does not grant a GitHub mutation. The responsible agent must
re-establish the account, repository, base, head, authority, and stored result under
`managing-github`.

Read [references/sources.md](references/sources.md) when auditing or changing the engagement modes,
risk triggers, scope gates, or ownership boundaries in this workflow.
