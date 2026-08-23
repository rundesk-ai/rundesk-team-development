# AGENTS

## Purpose

This repository is Rundesk's software-development team, kept as one versioned artifact. It publishes
a guidance-only skill catalog and, in the same tree, the team declaration and canonical agent
instructions that Rundesk installs and reconciles. Updating this catalog updates the team's
instructions and allowed skills; agents do not rewrite themselves and do not drift between installs.

`README.md` is the consumer contract, `manifest.json` is the installable catalog identity,
`team.json` declares the team's members, each `agents/<member>/AGENTS.md` is that member's canonical
always-on instructions, and each `skills/<name>/` package owns one reusable workflow. `RELEASING.md`
defines publication. This repository is the complete source of truth for its catalog and its team;
do not depend on instructions, packages, or files from another repository.

Rundesk CLI owns the installing contract. Keep operational state in maintainer records and pull
requests. `README.md` describes the product contract; never put pull-request heads, merge state,
release readiness, validation evidence, or internal task memory in consumer copy.

## Before you work

1. Read this file, `README.md`, `team.json`, every affected `agents/<member>/AGENTS.md`, and every
   complete file you may change. For skill work, also read that package's `SKILL.md` and
   `references/sources.md`.
2. Search the repository before adding a member, skill, term, field, workflow, or rule. Extend the
   existing owner instead of creating a second source of truth.
3. Load the smallest complete skill set for the task. Use current skill-authoring guidance for skill
   changes, naming guidance when a recurring concept crosses files, and guarded GitHub guidance for
   authorized issues, pull requests, or releases.
4. Inspect the branch, remotes, and worktree before editing. Preserve unrelated work and coordinate
   overlapping changes.
5. Verify catalog and team behavior against the CLI contract named above, using a disposable root
   and an injected supervisor. Never touch the live Rundesk install, the real command, or a real
   agent.
6. Define the requested outcome and observable proof before acting. Investigate an owner's concern
   with evidence before contradicting it.

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/
├── agents/<member>/AGENTS.md
├── assets/readme/
├── docs/
├── skills/<name>/
│   ├── SKILL.md
│   └── references/
├── tests/test_repository.py
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── RELEASING.md
├── LICENSE
├── manifest.json
└── team.json
```

Do not add empty optional directories, package-level READMEs, provider metadata, generated filler,
or a second catalog or team declaration.

## Package and artifact contract

- `manifest.json` contains exactly `schema`, `name`, `version`, and `description`. Rundesk discovers
  packages under `skills/`; do not add a manually maintained skill index.
- Every package is entirely under `skills/<name>/`, contains `SKILL.md`, `references/sources.md`,
  and `references/validation.md`, and remains useful without another repository checkout.
- Skill frontmatter contains only `name` and `description`. The directory and name match, use
  lowercase hyphenated identifiers, and remain at most 64 characters.
- This is guidance-only content. No script, executable, `rundesk.json`, credential, service adapter,
  network caller, or `agents/` directory belongs inside a skill package.
- `team.json` contains exactly `schema`, `name`, and `members`, and its `name` equals the manifest's
  name. Each member contains exactly `name`, `description`, `instructions`, `skills`,
  `delegates_to`, and `self_improve`.
- A member's `description` is one sentence of at most 200 characters, because it is charged to every
  other agent's prompt. `instructions` is `agents/<member>/AGENTS.md` and that file is never empty.
- `skills` is the exact positive allowlist that member receives, may be empty, and may name only
  packages this catalog ships. It may never name a Rundesk product-owned skill. There is no exclude
  list: a grant outside the allowlist is revoked on reconciliation, whichever catalog gave it.
- `delegates_to` may name only other declared members. An empty list makes a member inbound-only,
  which is this team's default. `self_improve` is a literal `true` or `false` and controls Rundesk's
  protected weekly upkeep for that member.
- The team has no lead and no coordinating member. Domain agents talk directly to the specialist
  they need.
- `rundesk skills install` installs only the skill catalog: it creates no agent, starts no gateway,
  and writes no team-ownership marker. `rundesk teams install` applies the complete guarded member
  lifecycle and leaves every gateway stopped. A later team install promotes an existing skills-only
  catalog in place, preserving its installed skills while adding team ownership and members.
- Keep `AGENTS.md` and `CLAUDE.md` byte-identical. Each `agents/<member>/AGENTS.md` is its own file
  and is not mirrored here.

## Safety and approval gates

Get explicit approval before adding executable, service, credential, dependency, provider, or
network behavior; adding or removing a member, or changing the team schema or delegation graph;
deleting or renaming a member or skill; changing a public compatibility boundary or version;
committing, pushing, tagging, publishing, deploying, or modifying repository settings; or changing
these guides outside an authorized guide task.

Never publish credentials, tokens, private URLs, customer or personal identifiers, private-project
language, owner-specific paths, raw private conversations, unredacted logs, unsupported claims, or
dropped attribution. Preserve unrelated work. Never reset, discard, force-push, or rewrite another
person's work. Never describe a capability as merged, released, or published without having observed
it. Never install or update either catalog mode against the live Rundesk install.

## Delegation

This team has no accountable coordinator. Each member owns one outcome and answers the agent that
called it. Forge owns bounded implementation. Piper owns independent quality judgment and does not
implement what it reviews. Trace owns read-only investigation. Vera owns product and interface
judgment and does not write production code.

Every member is inbound-only. A member does not hand work to another member, does not deliver
outside the local machine, and does not accept another agent's summary as proof of its own work.
When work needs a second specialist, the member names what is needed and returns; the requester
decides.

A member may propose an improvement to its own instructions in what it returns. No member edits,
installs, updates, or publishes the catalog that governs it. Rundesk's reconciliation is the drift
boundary, and a confirmed team install or update is refused from inside an agent turn.

Repository contributors may use subagents only when current instructions authorize delegation and
the work has non-overlapping ownership. The parent remains responsible for reading returns,
integrating artifacts, resolving findings, and rerunning proof.

## Architecture and conventions

Separate always-on responsibility from optional capability:

- An `agents/<member>/AGENTS.md` file is that member's durable contract: mission, ownership,
  routing, sizing, authority, stop conditions, return format, and boundaries. It is operative
  instruction, not a role summary, and it never copies a skill's technical method or names a skill,
  which may not be installed.
- Skills teach decisions any capable agent can apply. They are triggered when relevant, never
  permanently active merely because they exist, and they do not assume this team's topology.
- `managing-development-work` owns local delivery orchestration: outcome, scope, engagement mode,
  risk response, coordination, integration, and completion proof.
Give every future skill a distinct trigger, decisions, workflow, and proof. Framework, language,
database, design, planning, documentation, debugging, review, and testing skills own their domain
method; the development-work skill may route to them but must not reproduce their manuals.

## Documentation duties

Research before drafting technical claims. Every touched `references/sources.md` cites the specific
page, specification, source, release, discussion, test, or study and states what it establishes.
Separate source facts from catalog conclusions, label local heuristics, preserve material limits,
and verify every relied-on link.

Adding, removing, or renaming a skill updates `README.md`, package tests, and compatibility notes.
Changing the team schema, member list, description, instructions, allowed skills, delegation, or
weekly upkeep updates `team.json`, every affected member instruction file, README claims, and
focused tests together.

Keep reusable validation method under `docs/`. Keep a skill's cases and current provider evidence in
its own `references/validation.md`, and the team's member cases and evidence in
[Validating the team](docs/team-validation.md). Validation records are maintainer artifacts, not
operational references; do not route agents to them from a `SKILL.md` or a member instruction file.
Do not create dated run logs. Stable case IDs preserve comparability; add or supersede a materially
different case instead of silently changing its meaning.

## Build, test, and run

The complete offline validation is:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Run the full suite after every change and record its discovered test count and result. Also verify
every changed local link, open every changed external source link, inspect the complete diff for
privacy and package-boundary failures, and forward-test materially changed guidance with a realistic
raw task.

Prove both modes against the CLI contract named in `## Purpose`, using its exact head and a
disposable `RUNDESK_HOME`. A skills-only install must create no agent, gateway, or team marker and
must update and remove through the ordinary skill lifecycle. Prove that a later team install promotes
that catalog in place, reconciles every declared member, and leaves every gateway stopped. Also prove
a direct team install from a clean root. Preview each mode first and prove it changed nothing. Never
use the live install, the installed command, or a real agent or gateway.

## Pull requests and releases

Use `.github/pull_request_template.md` for every pull request. Preserve its headings and checklists,
fill it with exact-head evidence, and mark a check complete only when observed. Required CI must pass
for that exact head.

Follow `RELEASING.md`. Before the first `v0.1.0` publication, iterative catalog changes may remain at
`0.1.0`. After a version is published, later content changes use the documented semantic-version
policy. Changes to the team declaration or a member's instructions also require the applicable
version bump because they change distributed content that Rundesk applies to real agents. Never tag
unmerged content, reuse a published tag, or claim availability from publication alone.

## Definition of done

Work is complete only when the requested scope is implemented without unrelated changes; manifest,
skill tree, README, team declaration, member instructions, attribution, and guide parity agree; the
full suite passes with a non-zero count; applicable source, link, forward-test, and disposable
skills-only and team install checks pass; `git diff --check` and the privacy review are clean; no
placeholder, debug artifact, unexplained skip, or temporary file remains; and every claim about what
is supported, merged, released, or published is labeled exactly as observed.

For publication work, the pull request must report exact-head evidence and required CI must be green.
Report every unrun check, unavailable source, failed gate, owner decision, or remaining blocker.
