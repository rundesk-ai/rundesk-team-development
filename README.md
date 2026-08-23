# Rundesk Team Development

Rundesk's development team, kept under version control. This repository is a skill catalog that also
declares a team: four named agents whose canonical instructions, allowed skills, delegation scope,
and weekly-upkeep setting are owned here rather than edited on each machine.

## Team

Four specialists, and no lead. A domain agent talks directly to the one it needs.

| Member | Owns |
|---|---|
| `forge` | Bounded implementation across languages and frameworks, and the checks that prove it. |
| `piper` | Independent review of code, tests, compatibility, security, maintainability, and release readiness. |
| `trace` | Read-only investigation of unproved causes, returning reproducible evidence. |
| `vera` | User-facing behavior, usability, accessibility, states, and recovery. |

Each member is inbound-only: it does not hand work to another member and does not deliver outside
the machine it runs on. Each is memoryless by contract — Rundesk replaces `AGENTS.md` and
`CLAUDE.md` from this catalog and removes `MEMORY.md` on every reconciliation, so a member cannot
quietly rewrite the instructions it is governed by. Weekly upkeep is off for all four, and every
member's allowed-skill list is currently empty; the skill catalog below is granted to ordinary
agents, not to team members.

**Availability.** The team lifecycle is implemented by Rundesk CLI pull request #451, exact head
`dd2778d5`. At the time of writing that pull request has not been merged into the CLI's main branch
and is not in any published CLI release, and this catalog has no published release of its own. The
skills below install today with the current CLI; the team declaration requires that pull request or
its released successor.

## Skills

- `managing-development-work` — Scope and coordinate a software change from request through verified local completion.
- `managing-github` — Route and verify GitHub-hosted issue, pull-request, release, and repository-delivery workflows, whether reached directly or from development work.
- `using-inertia` — Own the Inertia protocol seam: page responses and props, partial, deferred, once, and shared data, authorization exposure, history, assets, SSR, and adapter compatibility.
- `using-vuejs` — Own Vue 3 and Nuxt semantics: reactivity, components, composables, Pinia and Router, SSR and hydration, rendering performance, and Vue-focused tests.
- `using-laravel` — Own Laravel backend conventions and traps: request lifecycle, validation and authorization, Eloquent, migrations, queues, caching, events, mail, scheduling, testing integration, and deployment-sensitive behavior.
- `using-reactjs` — Own modern React semantics: rendering purity, state ownership, effects and their alternatives, refs, context, external stores, concurrency, server and client boundaries, performance, and React-focused tests.

## Install

Preview any operation before it changes an install, then confirm it.

As an ordinary skill catalog, with the current CLI:

```sh
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development --confirm
rundesk skills grant ava rundesk-team-development/managing-development-work
```

As a team, with a CLI that carries the team lifecycle:

```sh
rundesk teams install https://github.com/rundesk-ai/rundesk-team-development --provider <provider>
rundesk teams install https://github.com/rundesk-ai/rundesk-team-development --provider <provider> --confirm
rundesk teams update rundesk-team-development --confirm
```

Installing the team refuses any member name that already exists as an agent and names the removal
command required first. A confirmed team install or update is refused from inside an agent turn; an
owner applies it from a terminal.

## Requirements

- The catalog is public and installs from its GitHub repository.
- Packages are guidance-only. They ship no executable, credential, dependency, service adapter, or
  network integration, and the team declaration is data: Rundesk runs no repository hook.
- Skills may describe local development tools and GitHub CLI operations. The active task and target
  repository rules still control whether any mutation is authorized.
- Each package works without another catalog checkout. Related skills may compose when installed,
  but no package makes another skill a runtime dependency.

`managing-development-work` owns the local delivery contract: scope, mode, risk response,
coordination, and proof. `managing-github` owns GitHub-hosted delivery: issues, pull requests,
releases, and the stored-object readback after an authorized mutation. The first may hand a verified
local result to the second; neither duplicates the other's workflow.

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/
├── agents/<member>/AGENTS.md
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

## Development

Read [AGENTS.md](AGENTS.md) before changing the repository. The complete offline gate is:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Skill changes also require verification of every relied-on source link and a realistic forward test
when guidance materially changes. [Validating Skills](docs/validation.md) defines the shared method,
and each skill keeps its cases and provider evidence in `references/validation.md`. Member
instructions and the installed team lifecycle are covered by
[Validating the team](docs/team-validation.md).

## Creating a skill catalog

This repository is the complete catalog contract: `manifest.json` identifies the installable
catalog, `skills/<name>/SKILL.md` supplies provider-compatible `name` and `description` frontmatter,
`team.json` declares the members and their canonical instructions, and the offline suite validates
discovery, package boundaries, the team declaration, and documentation parity. No sibling checkout
or external catalog guide is required to develop or install it.

The catalog contains researched judgment rather than condensed manuals. Search existing packages
before adding one, make routing descriptions discriminate between neighboring skills, keep one
source of truth per rule, and record the evidence behind each material lesson in
`references/sources.md`.

## Contributing

Use the repository templates to keep work bounded and reviewable:

- [Report a reproducible bug](.github/ISSUE_TEMPLATE/bug-report.md)
- [Propose a change](.github/ISSUE_TEMPLATE/change-proposal.md)
- [Prepare a pull request](.github/pull_request_template.md)

Adding, removing, or renaming a skill updates this README, the package tree, tests, and compatibility
notes together, and the same applies to a member, its instructions, its allowed skills, its
delegation scope, or its weekly upkeep. Never publish credentials, customer data, private-project
language, personal identifiers, or owner-specific paths.

## Releases

Published catalog behavior follows [RELEASING.md](RELEASING.md). Iteration may remain at `0.1.0`
until that version is first published. After publication, content changes update the manifest
version in the same pull request; repository-process-only corrections do not require a version bump.

## License

This catalog is available under the [MIT License](LICENSE).
