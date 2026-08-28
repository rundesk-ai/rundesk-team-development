# Designing UI and UX Validation

This is the current validation record for `designing-ui-ux`; the repository-wide method is in
[Validating Skills](../../../docs/guides/validation.md).

## Boundary under test

The skill should activate for user-facing design — task flow, hierarchy, affordances and interaction
states, forms and feedback, responsive and mobile behavior, accessibility, interface text and the
naming of controls, and error recovery. It should not activate for backend behavior with no
interface, for marketing or brand copy, or for standalone image and asset production.

## Trigger and exclusion cases

| ID | Request shape | Expected behavior |
|---|---|---|
| UIX-T01 | Design the settings page for an admin application | Load |
| UIX-T02 | "Users keep losing what they typed when the form fails" | Load |
| UIX-T03 | Add a queue job with retry rules and no interface change | Do not load |
| UIX-T04 | Write the landing-page headline and marketing copy | Do not load; a different discipline |
| UIX-T05 | Produce a logo or an icon family as standalone assets | Do not load |
| UIX-T06 | Make a data table usable on a narrow screen | Load |
| UIX-T07 | A Vue component whose visual design and reactivity both need work | Compose with `using-vuejs`; that package owns component behavior, this one the experience |
| UIX-T08 | Interface labels that must agree with the schema and the API field names | Compose with `designing-databases` and `designing-apis`; one canonical term across the layers |

## Workflow and authority cases

| ID | Request shape | Expected behavior |
|---|---|---|
| UIX-W01 | A brief with no stated user or task | Establish the evidence-backed user context, trigger, starting point, goal, and success condition first; if any is material and unavailable, return the question rather than inventing a persona or verdict |
| UIX-W02 | Only the success path designed | Inventory loading, empty, partial, error, disabled, and permission-limited states, plus long content, zoom, keyboard, and touch |
| UIX-W03 | A list screen with one empty state | Require both: never-had-data and filtered-to-zero, and name showing the wrong one as a defect |
| UIX-W04 | Buttons labelled `Submit`, `Confirm`, `Yes` | Rename to verb plus object and keep the same words through control, confirmation, loading, and result |
| UIX-W05 | Primary action disabled to hide incomplete validation | Reject it; explain what enables the action, preserve entered values, and put messages beside fields |
| UIX-W06 | "The design is done and it looks good" | Reject fluent assurance; require the rendered result inspected, states exercised, keyboard traversal, and contrast checked — source code is not evidence |
| UIX-W07 | The current interface, design system, or tokens cannot be inspected | Read the interface and its tokens, or stop and name the unknown; do not invent content, capabilities, metrics, or states |
| UIX-W08 | Automated accessibility checks pass | Keep the limit: automated checks find defects but cannot prove a task is understandable or operable; record what was actually tested |
| UIX-W09 | A raw stored value such as `PENDING_REVIEW` shown to a user | Map it to a display term, and keep the machine value out of the interface |
| UIX-W10 | A review brief gives one screen and a happy-path click sequence | Distinguish the end-to-end journey from the UI flow, then add the trigger, prior state, handoffs, continuation, and named scenarios for permissions, data, device, interruption, failure, and recovery |
| UIX-W11 | A persona contains unsupported age, motivation, proficiency, and device claims | Keep only evidence-backed characteristics that affect the task; label the rest as assumptions and do not use them to determine the verdict |
| UIX-W12 | An invoice screen and `Approve` control are the only clues to the user | Do not infer an authorized invoice reviewer, their knowledge, goal, or success condition from interface nouns; return the material questions before judging acceptance |
| UIX-W13 | A supplied approval journey does not mention rejection | Keep rejection as an unscored adjacent observation unless the brief or product evidence places it in the accepted journey or scenarios |

## Provider evidence

Last focused verification: 27 August 2026.

- Codex CLI 0.148.0, `gpt-5.6-sol`, natural-task suite: `UIX-W01`, `UIX-W12`, and `UIX-W13` passed in
  an isolated temporary workspace containing only `designing-ui-ux` and
  `managing-development-work`, with a read-only sandbox and no rendered interface. Given only an
  invoice-review URL and `Open invoice → Approve → Done`, it returned the material user and journey
  questions, did not infer an authorized invoice reviewer, and did not add rejection to the
  acceptance scope.
- The first draft failed by inferring that reviewer and adding rejection despite labeling the
  context unspecified. The no-inference and unscored-adjacent-path rules produced the passing rerun.
- Instrumented Codex and all Claude cases remain unrun. No complete provider compatibility is
  claimed.

## Limits

This package's own workflow requires rendering the result and inspecting it. No case in this record
does that, so every case here grades the decision and the evidence demanded rather than an observed
interface. Visual judgment remains an owner verification.

UIX-T04 and UIX-T05 are the exclusion cases most likely to misfire, because both sit close to the
package's vocabulary without being inside its boundary.
