# Writing Technical Docs Validation

This is the current validation record for `writing-technical-docs`; the repository-wide method is in
[Validating Skills](../../../docs/validation.md).

Four runs were observed on 2026-08-25 against a fixture whose documentation deliberately contradicts
its code, with the correct behavior established by execution before any run. Cases those runs
exercised carry a result; every other case remains unrun. The language cases were written after
those runs and are unrun, and the two corrections made to them came from a run rather than from
review.

## Boundary under test

The skill should activate for creating, revising, or auditing documentation of software that already
exists — developer or consumer guides, API and CLI reference, how-it-works explanations, architecture
notes, troubleshooting, extension guides, and maintainer documentation. It should not activate for
planning work that has not been built, for writing code comments alone, or for describing a design
that exists only as an intention.

Documentation asks **what does this software do now, and how would someone verify that**. A plan asks
what should be built; a requirements document asks what the product must do for a user. The dividing
question is what falsifies the page: for documentation it is the code, and for the other two it is
nothing yet.

## Trigger and exclusion cases

| ID | Request shape | Expected behavior | Claude | Codex |
|---|---|---|---|---|
| DOC-T01 | Document this API for the people who will call it | Load | ✅ | – |
| DOC-T02 | The README is out of date after the refactor | Load | – | – |
| DOC-T03 | Write the troubleshooting page for these failures | Load | – | – |
| DOC-T04 | Explain how this subsystem fits together, for maintainers | Load | – | – |
| DOC-T05 | Write the plan for the feature we are about to build | Do not load; work not yet built | – | – |
| DOC-T06 | Add comments to this function | Do not load; code comments alone | – | – |
| DOC-T07 | Write the requirements for the new tier | Do not load; product requirements, not current behavior | – | – |
| DOC-T08 | Document the endpoint we are going to add next sprint | Do not load; nothing exists to verify against | – | – |

## Evidence and accuracy cases

| ID | Request shape | Expected behavior | Claude | Codex |
|---|---|---|---|---|
| DOC-W01 | An existing page describes behavior the code no longer has | Correct it against the current contract and say what changed, rather than preserving the old claim | ✅ | – |
| DOC-W02 | A parameter's behavior is not obvious from its signature | Trace it to the implementation or a test before describing it; do not infer from the name | ✅ | – |
| DOC-W03 | An example is requested for a flow with no test covering it | Verify the example by running it, or mark it unverified; do not present an untested example as working | ✅ | – |
| DOC-W04 | The request asks for the happy path only | Include the failure paths and their causes; a reference that documents only success is incomplete | ✅ | – |
| DOC-W05 | Two sources disagree — a comment says one thing, the code another | Report the code as the contract and flag the stale comment; never average them into a hedge | ✅ | – |
| DOC-W06 | Asked to document a private or unstable internal as though it were public | Name the stability boundary rather than promoting an internal to a contract | – | – |
| DOC-W07 | The codebase is unfamiliar and spans several layers | Establish what it can reach and trace the path before writing, rather than describing structure from file names | – | – |
| DOC-W08 | Asked to document why a design decision was made, with no record of it | Return the missing rationale as unknown; do not invent a justification that reads as history | ✅ | – |

## Language and naming cases

| ID | Request shape | Expected behavior | Claude | Codex |
|---|---|---|---|---|
| DOC-L01 | A parameter is named `attempts` in the signature | Use `attempts` throughout; never drift to tries, retries, or count in adjacent prose | – | – |
| DOC-L02 | Errors both leave a function and pass through it unhandled | Hold one verb per meaning — raises and propagates — rather than mixing in throws, bubbles, or escapes | – | – |
| DOC-L03 | A table column records whether each exception is retried | Label it "Retried", not "Is it retried?"; the question form belongs in a heading, not a column label | – | – |
| DOC-L09 | A section answers a question the reader arrives with, such as why a timeout is not retried | Head it with that question where it is the most findable form; do not flatten it into a tidy noun phrase | – | – |
| DOC-L04 | A behavior changed in the version being documented | State current behavior in the present; put the version-bound fact in a compatibility field, not in "new in this release". A line dating the verification itself is provenance and stays | – | – |
| DOC-L05 | An exception is re-raised after the last attempt | Name the actor performing it rather than writing "the exception is re-raised" | – | – |
| DOC-L06 | The page is a reference and the repository's product copy uses contractions and a warm voice | Keep the reference dense and factual; do not import the product register | – | – |
| DOC-L07 | A claim could not be verified by execution | Mark it unverified rather than hedging it with "appears to" or "should generally" | – | – |
| DOC-L08 | An identifier in the code is badly named | Document the name that exists and record the mismatch; do not improve it in prose | – | – |

### What those runs observed

All four discrepancies planted between the code and its documentation were found: a default of five
attempts against a documented three, a documented `timeout` parameter that does not exist, a
docstring claiming any exception is retried where only `ConnectionError` is, and a fixed delay that
is exponential. The third is the one the fixture was built to catch, because repeating the docstring
is both plausible and the cause of the misuse.

Each run also produced findings the fixture did not plant, and every one reproduced when checked
independently: a positional argument in the documented parameter position becomes `backoff`, turning
"give up after 30 seconds" into a ninety-second schedule; `attempts=0` reaches `raise` with nothing
assigned and never calls `fn`; rebinding the module default after import has no effect because it is
bound at definition; an `async def` callable returns a coroutine that is never awaited or retried;
and the exhausted call re-raises only the last exception, with `__cause__` and `__context__` both
unset.

Both documenting runs declined to correct the stale README, on the ground that it does not merely
misdescribe the function but describes a different one — so whether the code or the documentation is
wrong is a product decision, not a documentation one. Each flagged the conflict on its own page
instead.

## Next validation

Run every case in fresh supported provider sessions, with and without the skill installed, using
ordinary requests that never name the boundary under test. Point each run at a real codebase and
establish the current contract independently first, so a claim traced to the code can be told apart
from one that merely reads plausibly. Record activation, whether each claim was traced to a contract,
test, or executed example, whether failure paths appear, and whether anything unverifiable was
returned as unverified rather than smoothed over.
