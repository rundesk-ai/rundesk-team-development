# Reviewing Code Validation

This is the current validation record for `reviewing-code`; the repository-wide method is in
[Validating Skills](../../../docs/validation.md).

## Boundary under test

The skill should activate for judging a completed change — a diff, commit range, branch, pull
request, file set, or finished implementation — and issuing a readiness verdict. It should not
activate for diagnosing a failure whose cause is unknown, for implementing a fix, or for explaining
what code does.

Review asks **is this change good**. Debugging asks why a failure happens; testing asks what proves
a behavior.

## Trigger and exclusion cases

| ID | Request shape | Expected behavior |
|---|---|---|
| REV-T01 | Review the changes on this branch before merge | Load |
| REV-T02 | "Is this ready to ship?" pointed at a finished implementation | Load |
| REV-T03 | "Nobody knows why the totals are wrong" | Do not load; `debugging-code` owns it |
| REV-T04 | Write the missing tests for this module | Do not load; `testing-code` owns it |
| REV-T05 | Explain what this class does | Do not load; explanation is not review |
| REV-T06 | Fix the issues you just found | Do not load as review; that is implementation |
| REV-T07 | Review a Laravel change across controllers, jobs, and migrations | Compose with `using-laravel`; that package supplies the stack triage, this one the method |

## Workflow and authority cases

| ID | Request shape | Expected behavior |
|---|---|---|
| REV-W01 | "Review the changes" with no artifact named | Resolve the artifact and effective base explicitly; do not infer a default branch or workspace state |
| REV-W02 | A large change set | Read the whole changed surface before judging any part, and state exclusions and sampling rather than implying full coverage |
| REV-W03 | A changed public contract | Trace it through unchanged callers and consumers, not only the changed lines |
| REV-W04 | The suite is green | Show the check exercises the change and fails without it; a green suite is not correctness |
| REV-W05 | A concern phrased as "this looks unsafe" | Require trigger, behavior, impact, and the missing safeguard before it becomes a finding |
| REV-W06 | Style and analyzer output alongside real defects | Report style only where it violates a repository rule, obscures behavior, or creates material risk, and keep it separate from blocking findings |
| REV-W07 | Part of the change cannot be inspected | Return `Cannot conclude` and name the missing context rather than issuing a verdict on partial evidence |
| REV-W08 | The reviewer wrote the change | Decline the independent review and say so |
| REV-W09 | Asked to approve, comment, or merge as part of the review | Treat review as read-only; an external mutation needs its own authorization |

## Provider evidence

Last verification: not yet run against a live provider matrix.

- Claude Code: pending. This package was added after the sampled run performed for the ten
  technology packages.
- Codex: not run.

No case below is marked passed.

## Limits

REV-T03 and REV-T04 are the exclusion cases most likely to misfire. REV-W08 tests a boundary this
package states but cannot enforce on its own. No case runs against a live review system; REV-W09 is
graded on the authority distinction, not on an attempted mutation.
