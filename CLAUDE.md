# AGENTS

## Purpose

This repository prepares Rundesk's software-development team as one versioned artifact. It publishes
a current-format, guidance-only skill catalog and carries the proposed `team/` contract for a future
team mode. Current Rundesk installs the manifest and `skills/`; it does not yet read `team/team.json`
or role documents. Keep that distinction explicit in code, tests, documentation, and release claims.

`README.md` is the consumer contract, `manifest.json` is the installable catalog identity,
`team/team.json` is the proposed team definition, each `team/roles/*.md` file defines one role, and
each `skills/<name>/` package owns its reusable workflow guidance. `RELEASING.md` defines publication.
This repository is the complete source of truth for its catalog and proposed team contracts; do not
depend on instructions, packages, or files from another repository.

## Before you work

1. Read this file, `README.md`, `team/team.json`, every affected role document, and every complete
   file you may change. For skill work, also read that package's `SKILL.md` and
   `references/sources.md`.
2. Search the repository before adding a role, skill, term, field, workflow, or rule. Extend the
   existing owner instead of creating a second source of truth.
3. Load the smallest complete skill set for the task. Use current skill-authoring guidance for skill
   changes, naming guidance when a recurring concept crosses files, and guarded GitHub guidance for
   authorized issues, pull requests, or releases.
4. Inspect the branch, remotes, and worktree before editing. Preserve unrelated work and coordinate
   overlapping changes.
5. Verify catalog behavior against the current Rundesk CLI. Treat the team schema as a proposal
   enforced only by this repository until Rundesk implements and documents team mode.
6. Define the requested outcome and observable proof before acting. Investigate an owner's concern
   with evidence before contradicting it.

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/
├── skills/<name>/
│   ├── SKILL.md
│   └── references/sources.md
├── team/
│   ├── team.json
│   └── roles/
│       ├── forge.md
│       ├── piper.md
│       ├── trace.md
│       └── vera.md
├── tests/test_repository.py
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── RELEASING.md
├── LICENSE
└── manifest.json
```

Do not add empty optional directories, package-level READMEs, provider metadata, generated filler,
or a second catalog or team definition.

## Package and artifact contract

- `manifest.json` contains exactly `schema`, `name`, `version`, and `description`. Rundesk discovers
  packages under `skills/`; do not add a manually maintained skill index.
- Every package is entirely under `skills/<name>/`, contains `SKILL.md` and
  `references/sources.md`, and remains useful without another repository checkout.
- Skill frontmatter contains only `name` and `description`. The directory and name match, use
  lowercase hyphenated identifiers, and remain at most 64 characters.
- This is guidance-only content. No script, executable, `rundesk.json`, credential, service adapter,
  network caller, or provider-specific `agents/` metadata belongs in a skill package.
- `team/team.json` is the proposed team-mode contract. It contains exactly `schema`, `name`,
  `description`, `entry_role`, and `roles`. Each role contains exactly `name`, `path`, `purpose`, and
  `delegates_to`; names are unique lowercase identifiers, paths resolve inside `team/roles/`, and
  delegation targets name another declared role.
- `entry_role` is `piper`. Piper may hand bounded work to Forge, Trace, or Vera. Specialists do not
  delegate onward. A role document may narrow its behavior but may not contradict this graph.
- Keep `AGENTS.md` and `CLAUDE.md` byte-identical.

## Safety and approval gates

Get explicit approval before adding executable, service, credential, dependency, provider, or
network behavior; changing the proposed team schema or role graph; deleting or renaming a role or
skill; changing a public compatibility boundary or version; committing, pushing, tagging,
publishing, deploying, or modifying repository settings; or changing these guides outside an
authorized guide task.

Never publish credentials, tokens, private URLs, customer or personal identifiers, private-project
language, owner-specific paths, raw private conversations, unredacted logs, unsupported claims, or
dropped attribution. Preserve unrelated work. Never reset, discard, force-push, or rewrite another
person's work. A proposed team artifact must never be described as supported Rundesk runtime behavior
until the implementing CLI contract and tests exist.

## Delegation

Piper is the accountable entry role. Piper owns scope, architecture decisions, integration,
completion proof, requester communication, and any authorized GitHub write. Piper delegates only a
bounded task whose independent value exceeds coordination cost.

Forge owns bounded implementation. Trace owns read-only investigation and independent evidence.
Vera owns product and interface design decisions and artifacts. Each specialist returns artifacts,
evidence, risks, and unresolved decisions to Piper and does not delegate or publish externally.

Repository contributors may use subagents only when current instructions authorize delegation and
the work has non-overlapping ownership. The parent remains responsible for reading returns,
integrating artifacts, resolving findings, and rerunning proof.

## Architecture and conventions

Separate reusable workflow from team identity:

- Skills teach decisions any capable agent can apply. They do not name a required team role or
  assume team mode exists.
- Role documents define responsibility, authority, composition, and handoff. They link to skill
  names as optional capabilities without copying the skill's technical method.
- `managing-development-work` owns local delivery orchestration: outcome, scope, engagement mode,
  risk response, coordination, integration, and completion proof.
- `managing-github` owns GitHub-hosted artifacts and mutations: issues, pull requests, releases,
  deployment-branch reconciliation, target selection, authorization, and stored-object readback.
  It does not own local implementation or generic Git work.

Give every future skill a distinct trigger, decisions, workflow, and proof. Framework, language,
database, design, planning, documentation, debugging, review, and testing skills own their domain
method; the development-work skill may route to them but must not reproduce their manuals.

## Documentation duties

Research before drafting technical claims. Every touched `references/sources.md` cites the specific
page, specification, source, release, discussion, test, or study and states what it establishes.
Separate source facts from catalog conclusions, label local heuristics, preserve material limits,
and verify every relied-on link.

Adding, removing, or renaming a skill updates `README.md`, package tests, and compatibility notes.
Changing the team schema, role list, entry role, path, purpose, or delegation graph updates
`team/team.json`, every affected role document, README claims, and focused tests together.

## Build, test, and run

The complete offline validation is:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Run the full suite after every change and record its discovered test count and result. Also verify
every changed local link, open every changed external source link, inspect the complete diff for
privacy and package-boundary failures, and forward-test materially changed guidance with a realistic
raw task. Validate current Rundesk compatibility using a disposable root and local catalog preview;
never touch the live Rundesk install.

## Pull requests and releases

Use `.github/pull_request_template.md` for every pull request. Preserve its headings and checklists,
fill it with exact-head evidence, and mark a check complete only when observed. Required CI must pass
for that exact head.

Follow `RELEASING.md`. Skill content changes use the documented semantic-version policy. Changes to
the proposed team contract also require a version bump because they change distributed content, even
though current Rundesk does not execute it. Never tag unmerged content, reuse a published tag, or
claim team-mode availability from publication alone.

## Definition of done

Work is complete only when the requested scope is implemented without unrelated changes; manifest,
skill tree, README, team schema, role files, attribution, and guide parity agree; the full suite
passes with a non-zero count; applicable source, link, forward-test, and disposable catalog checks
pass; `git diff --check` and the privacy review are clean; no placeholder, debug artifact, unexplained
skip, or temporary file remains; and every unsupported future-runtime claim is labeled as proposed.

For publication work, the pull request must report exact-head evidence and required CI must be green.
Report every unrun check, unavailable source, failed gate, owner decision, or remaining blocker.
