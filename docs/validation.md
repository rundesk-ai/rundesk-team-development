# Validating Skills

Use this repository method to prove that a skill is discovered for the right requests and makes the
right workflow decisions after discovery. Keep reusable test method here. Keep a skill's cases and
current provider evidence in `skills/<name>/references/validation.md`; do not create dated run logs.
These are maintainer records, not operational skill references: do not link them from `SKILL.md` or
ask an agent to load them while performing the skill's normal workflow.

## Define the validation contract

Separate four questions that can fail independently:

1. **Trigger:** Does the provider load the skill for direct and indirect requests that reach its
   boundary?
2. **Exclusion:** Does it stay unloaded for local-only work, neighboring skills, and near-miss terms?
3. **Workflow:** Once loaded, does it choose the correct target, template, operation, safety gate,
   and completion proof?
4. **Authority:** Does it distinguish inspection, preparation, authorized mutation, a missing
   prerequisite, and an explicitly excluded effect?

A fluent response is not a pass when the provider loaded the wrong skill, skipped a required
reference, inferred a target, broadened authority, or reported completion without the skill's proof.

## Organize cases by behavior

Use stable IDs inside the skill's validation reference:

- `<PREFIX>-T##` for trigger and exclusion cases;
- `<PREFIX>-W##` for workflow and authority cases.

Cover direct, indirect, negative, adjacent-domain, ambiguous-target, unauthorized, partially
authorized, unsafe, blocked, failed-command, stored-result, and recovery partitions that materially
change the skill's decisions. Keep one observable decision per case. Add a case when a real failure
or distinct risk appears; do not enumerate wording variations with the same expected behavior.

## Run two provider suites

### Instrumented routing suite

Use a fresh session per case in a temporary workspace containing only the project-local skill. Ask
the provider to return selected project-local skills, its trigger reason, next step, and mutation
classification. This makes false positives and false negatives easy to count, but the prompt itself
draws attention to skill selection.

### Natural-task suite

Run the same behavioral partitions as ordinary user requests. Do not name the skill, ask which skill
applies, or disclose the expected result. Prevent real external effects with a natural dry-run
constraint or an isolated environment. Use provider traces to observe whether the skill loaded, then
grade the final workflow response separately.

For Codex, a project skill is placed under `.agents/skills/<name>/`. For Claude Code, place the same
package under `.claude/skills/<name>/`. Do not add repository instructions that name the expected
skill. Ignore user configuration where the provider supports it; otherwise record unrelated global
skills and grade only whether the skill under test loaded.

## Record current evidence

Update `references/validation.md` in place with:

- the last verification date, client versions, and model identifiers the clients expose;
- isolation and tool constraints;
- the stable trigger and workflow cases;
- pass or fail for each provider and suite;
- the exact observed failure that caused any skill change; and
- limits, including operations that were prepared but not executed against a live service.

Provider behavior changes over time. A current validation reference is a maintained compatibility
snapshot, not an immutable historical log and not proof for untested future models.
