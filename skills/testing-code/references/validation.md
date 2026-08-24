# Testing Code Validation

This is the current validation record for `testing-code`; the repository-wide method is in
[Validating Skills](../../../docs/validation.md).

## Boundary under test

The skill should activate for designing, adding, repairing, or assessing automated tests, choosing a
test boundary, reproducing a defect as a failing case, or diagnosing flaky, brittle, or falsely green
results. It should not activate for a framework's test syntax alone, for reviewing a completed
change, or for diagnosing a failure whose cause is unknown.

Testing asks **what proves this behavior**. Debugging asks why a failure happens; review asks whether
a change is good.

## Trigger and exclusion cases

| ID | Request shape | Expected behavior |
|---|---|---|
| TST-T01 | Add tests for this payment calculation | Load |
| TST-T02 | "This test passes locally and fails in CI about a third of the time" | Load |
| TST-T03 | "Nobody knows why the export is empty" | Do not load; `debugging-code` owns it |
| TST-T04 | Review this pull request | Do not load; `reviewing-code` owns it |
| TST-T05 | What is the syntax for a parameterized case in this runner? | Do not load; syntax alone is not the boundary |
| TST-T06 | Turn a reported defect into a failing case before fixing it | Load |
| TST-T07 | Laravel feature tests using factories and fakes | Compose with `using-laravel`; that package supplies the framework mechanics, this one the method |
| TST-T08 | Python unittest isolation and cleanup | Compose with `using-python` |

## Workflow and authority cases

| ID | Request shape | Expected behavior |
|---|---|---|
| TST-W01 | A test asserting a private collaborator was called | Assert the observable contract instead, unless the interaction is itself required behavior |
| TST-W02 | An end-to-end test proposed for a pure calculation | Choose the narrowest boundary containing the risk |
| TST-W03 | A mocked serializer described as an integration test | Reject the label; name which dependencies were real |
| TST-W04 | A flaky test wrapped in a retry | Treat the flake as a defect; preserve seed, order, timing, and artifacts and fix the cause |
| TST-W05 | A `sleep` before an async assertion | Wait on the condition with a diagnostic timeout |
| TST-W06 | "Tests pass, so the fix works" | Require the test to be observed failing for the reported reason before the correction, or state the limitation explicitly |
| TST-W07 | A green run reported with no counts | Read exit status, discovered and executed counts, skips, and retries; zero discovered is not a pass |
| TST-W08 | A coverage target proposed as the goal | Coverage locates unexercised code; it does not prove assertions or justify an invented target |
| TST-W09 | An assertion weakened until the suite is green | Reject it; update expectations from the requirement, not from current output |
| TST-W10 | A unit case proposed for a transformation whose result is stored and drives an action elsewhere | Prove the transformation in a unit and the consequence where it lands; the narrowest boundary containing the risk reaches the consumer |
| TST-W11 | A case written for edge-case behavior nobody specified | Refuse to record a guess as a requirement; the behavior is returned as a question, not asserted |
| TST-W12 | A fixture-driven check that passes having discovered no fixtures | Report the discovered count and treat zero as unrun, whatever the check returned |
| TST-W13 | Cases built from the single input the assignment illustrated | Derive the partitions from what real producers emit and existing consumers accept, including alternate representations and missing or malformed values |

## Provider evidence

Last verification: not yet run against a live provider matrix.

- Claude Code: pending. This package was added after the sampled run performed for the ten
  technology packages.
- Codex: not run.

No case below is marked passed.

## Limits

TST-W06 is this package's central claim and the hardest to verify from a transcript alone, because a
model can describe observing a failure it did not observe. Grade it on whether the run and its
result are reported, not on the narration. TST-T03 and TST-T04 are the exclusion cases most likely
to misfire.
