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

| ID | Request shape | Expected behavior | Claude | Codex |
|---|---|---|---|---|
| TST-T01 | Add tests for this payment calculation | Load | ✅ | – |
| TST-T02 | "This test passes locally and fails in CI about a third of the time" | Load | ✅ | – |
| TST-T03 | "Nobody knows why the export is empty" | Do not load; `debugging-code` owns it | ✅ | – |
| TST-T04 | Review this pull request | Do not load; `reviewing-code` owns it | ✅ | – |
| TST-T05 | What is the syntax for a parameterized case in this runner? | Do not load; syntax alone is not the boundary | ✅ | – |
| TST-T06 | Turn a reported defect into a failing case before fixing it | Load | ✅ | – |
| TST-T07 | Laravel feature tests using factories and fakes | Compose with `using-laravel`; that package supplies the framework mechanics, this one the method | ✅ | – |
| TST-T08 | Python unittest isolation and cleanup | Compose with `using-python` | ✅ | – |
| TST-T09 | "What are we not testing here?" pointed at an existing suite | Load; assessing what a suite leaves unguarded is inside the boundary | ✅ | – |

## Workflow and authority cases

| ID | Request shape | Expected behavior | Claude | Codex |
|---|---|---|---|---|
| TST-W01 | A test asserting a private collaborator was called | Assert the observable contract instead, unless the interaction is itself required behavior | ✅ | – |
| TST-W02 | An end-to-end test proposed for a pure calculation | Choose the narrowest boundary containing the risk | ✅ | – |
| TST-W03 | A mocked serializer described as an integration test | Reject the label; name which dependencies were real | ✅ | – |
| TST-W04 | A flaky test wrapped in a retry | Treat the flake as a defect; preserve seed, order, timing, and artifacts and fix the cause | ✅ | – |
| TST-W05 | A `sleep` before an async assertion | Wait on the condition with a diagnostic timeout | ✅ | – |
| TST-W06 | "Tests pass, so the fix works" | Require the test to be observed failing for the reported reason before the correction, or state the limitation explicitly | ✅ | – |
| TST-W07 | A green run reported with no counts | Read exit status, discovered and executed counts, skips, and retries; zero discovered is not a pass | ✅ | – |
| TST-W08 | A coverage target proposed as the goal | Coverage locates unexercised code; it does not prove assertions or justify an invented target | ✅ | – |
| TST-W09 | An assertion weakened until the suite is green | Reject it; update expectations from the requirement, not from current output | ✅ | – |
| TST-W10 | A unit case proposed for a transformation whose result is stored and drives an action elsewhere | Prove the transformation in a unit and the consequence where it lands; the narrowest boundary containing the risk reaches the consumer | ✅ | – |
| TST-W11 | A case written for edge-case behavior nobody specified | Refuse to record a guess as a requirement; the behavior is returned as a question, not asserted | ✅ | – |
| TST-W12 | A fixture-driven check that passes having discovered no fixtures | Report the discovered count and treat zero as unrun, whatever the check returned | ✅ | – |
| TST-W13 | Cases built from the single input the assignment illustrated | Derive the partitions from what real producers emit and existing consumers accept, including alternate representations and missing or malformed values | ✅ | – |
| TST-W14 | A suite to be assessed, whose test names read as complete | Work from what the code decides, stores, refuses, and emits, not from the test directory; a name is not an inventory | ✅ | – |
| TST-W15 | A case that executes the changed line while asserting something else | Report it as unguarded, not covered; execution is not verification and a percentage cannot show the difference | ✅ | – |
| TST-W16 | An assessment covering a surface larger than the risk in it | Rank by what a defect costs and stop; a complete list of trivia is not the deliverable | ✅ | – |
| TST-W17 | Work in a stack whose own package is installed | Load it for the runner's fixtures, doubles, and isolation while this package supplies the method | ✅ | – |

## Provider evidence

A column per provider, because a rule that governs one model is not thereby proved on another. ✅
passed, ❌ failed, – not run. Record a cell only from a run you watched.

Last verified: 2026-08-24. Client: Claude Code 2.1.241, headless (`claude -p`), one fresh session per
case. Model reported by the client: `claude-opus-5[1m]`. Each case ran in a throwaway project outside
any workspace carrying a competing catalog, with this package placed at `.claude/skills/<name>/` and
nothing naming the skill, the expected behavior, or the boundary under test. Skill and reference
loading were graded from the run's own tool-call trace, not from what the response claimed. Only the
cases marked above were run; every other cell is untouched because nothing was observed.

**What the assessment runs showed.** Two independent runs were given an ordinary request — "our tests
here feel thin, what are we not covering?" — against a four-method ledger whose three tests read as
complete. Both loaded this package and both read `assessing-a-suite.md`. Neither worked from the test
directory: one broke six behaviors one at a time and the other ten, re-running the suite after each,
and both reported the resulting table. Both found that only one of the four methods was load-bearing,
both named the `assertIsNotNone` case as executing the line while asserting nothing — "this reads as
covered and isn't" — and both ranked by what a defect would cost rather than listing everything.

Both also found a defect the fixture's author had not planted: `refund` guards only the upper bound,
so a negative argument increases the recorded total and overcharges. One demonstrated it against a
real in-memory store. That is the reference's central claim working — the gap was not visible from
the test names, and the behavior inventory is what exposed it.

Both runs left the project byte-identical to a pristine copy taken beforehand.

## Limits

`TST-W17` is proved for writing a case and unproved for judging one. Asked to add the missing tests
for a path, the run loaded this package and `using-python` together, and it read
`boundaries-and-doubles.md` and `proving-teeth.md`. It replaced the existing suite's `Mock` store with
a small fake and gave the reference's own reason — with a mock, `add` returns a canned value and the
test asserts the mock's own answer instead of the reversal — then broke the method three ways and
recorded which cases failed for each, restoring from a copy rather than `git checkout`, as that
reference requires. It touched only the test file. In the two assessment runs, by contrast, the stack
package was installed and neither loaded it; judging an existing suite leans less on a runner's
mechanics. Read the cell as covering the writing case only.

TST-W06 is this package's central claim and the hardest to verify from a transcript alone, because a
model can describe observing a failure it did not observe. Grade it on whether the run and its
result are reported, not on the narration. TST-T03 and TST-T04 are the exclusion cases most likely
to misfire.
