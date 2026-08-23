<h1 align="center">
  <img src="assets/readme/rundesk-team-development-banner.png" alt="Rundesk Development Team — Forge, Piper, Vera, and Trace." width="100%">
</h1>

<p align="center">
  <a href="https://github.com/rundesk-ai/rundesk-team-development/actions/workflows/build.yml?query=branch%3Amain"><img src="https://github.com/rundesk-ai/rundesk-team-development/actions/workflows/build.yml/badge.svg?branch=main" alt="Build and tests"></a>
  <a href="manifest.json"><img src="https://img.shields.io/badge/catalog-v0.1.0-blue?style=flat-square" alt="Catalog version 0.1.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/rundesk-ai/rundesk-team-development?style=flat-square" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#team"><strong>Team</strong></a>
  &nbsp;·&nbsp;
  <a href="#skills"><strong>Skills</strong></a>
  &nbsp;·&nbsp;
  <a href="#install"><strong>Install</strong></a>
  &nbsp;·&nbsp;
  <a href="#development"><strong>Development</strong></a>
</p>

A versioned Rundesk development team: four specialists, their canonical instructions, and the
skills they use. The repository is both an installable skill catalog and a team declaration.

## Team

| Member | Responsibility |
|---|---|
| `forge` | Implements bounded changes and the tests that prove them. |
| `piper` | Reviews completed work for correctness, safety, compatibility, and readiness. |
| `trace` | Investigates unknown failures and returns reproducible evidence without changing code. |
| `vera` | Defines and validates user-facing behavior, usability, accessibility, and recovery. |

There is no development lead. A domain agent calls the right specialist directly, keeps ownership
of the outcome, and integrates the result. Team members do not delegate or publish externally.

Rundesk reconciles each member from `team.json`: instructions, allowed skills, delegation, and
weekly upkeep. The catalog replaces `AGENTS.md` and `CLAUDE.md`, removes `MEMORY.md`, and revokes
skills outside the member's allowlist. Weekly upkeep is disabled for all four members.

**Availability:** Team installation depends on Rundesk CLI pull request #451 at tested head
`dd2778d5`. It has not been merged into CLI `main` and is in no published CLI release. This catalog
also has no published release. Its skills install today with the current CLI; its team declaration
requires that pull request or a released successor.

## Skills

### Workflow and design

- `managing-development-work` — Scope and coordinate a software change through verified local completion.
- `managing-github` — Handle authorized GitHub issues, pull requests, releases, and delivery verification.
- `designing-apis` — Design HTTP interfaces, resources, contracts, errors, evolution, and security boundaries.
- `designing-databases` — Design data models, constraints, relationships, history, concurrency, and growth.
- `designing-ui-ux` — Design task flows, states, responsive behavior, accessibility, interface text, and recovery.
- `debugging-code` — Reproduce a failure, isolate its cause, and prove the smallest safe correction.
- `reviewing-code` — Judge a completed change and return ranked findings with a readiness verdict.
- `testing-code` — Choose trustworthy test boundaries and prove that tests detect the behavior they cover.

### Technology

- `using-laravel` — Laravel requests, Eloquent, migrations, queues, caching, testing, and deployment behavior.
- `using-inertia` — Inertia page responses, props, data loading, history, SSR, and adapter compatibility.
- `using-vuejs` — Vue 3 and Nuxt reactivity, components, state, routing, SSR, performance, and tests.
- `using-reactjs` — React rendering, state, effects, refs, concurrency, server boundaries, performance, and tests.
- `using-tailwindcss` — CSS behavior, layout, themes, responsive states, and Tailwind v4 composition.
- `using-mysql` — MySQL and InnoDB types, indexes, plans, locks, DDL, replication, and operations.
- `using-postgres` — PostgreSQL types, indexes, plans, MVCC, vacuum, security, migrations, and operations.
- `using-sqlite` — SQLite types, transactions, WAL, migrations, integrity, backups, FTS, and file constraints.
- `using-python` — Python APIs, typing, errors, resources, concurrency, performance, security, and tests.
- `using-cpp` — Modern C++ ownership, lifetime, undefined behavior, CMake, warnings, and platform builds.
- `using-axmol` — Axmol lifetime, scenes, input, UI, rendering, migration, CMake, and platform builds.

## Install

Preview first, then confirm.

Install the skill catalog with the current CLI:

```sh
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development --confirm
rundesk skills grant ava rundesk-team-development/managing-development-work
```

Install the team with a CLI that carries the team lifecycle:

```sh
rundesk teams install https://github.com/rundesk-ai/rundesk-team-development --provider <provider>
rundesk teams install https://github.com/rundesk-ai/rundesk-team-development --provider <provider> --confirm
rundesk teams update rundesk-team-development --confirm
```

Team installation refuses an existing member name and any confirmed operation run from inside an
agent turn. Apply it from an owner-controlled terminal.

## Requirements

- A supported Rundesk CLI and provider.
- Public GitHub access to this repository.
- An unused local agent name for every team member.

Skills are guidance-only. They add no executable, credential, dependency, service adapter, network
integration, or repository hook. Each package works without another catalog checkout.

## Repository layout

```text
.
├── agents/<member>/AGENTS.md
├── assets/readme/
├── docs/
├── skills/<name>/
│   ├── SKILL.md
│   └── references/
├── tests/test_repository.py
├── AGENTS.md
├── README.md
├── RELEASING.md
├── manifest.json
└── team.json
```

## Development

Read [AGENTS.md](AGENTS.md), then run the complete offline gate:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Skill changes also require verified source links and realistic forward tests. See
[skill validation](docs/validation.md) and [team validation](docs/team-validation.md).

## Creating a skill catalog

`manifest.json` identifies the catalog, `skills/<name>/SKILL.md` defines each package, `team.json`
declares members and allowlists, and `agents/<member>/AGENTS.md` supplies canonical instructions.
Keep every package self-contained, guidance-only, and distinct from neighboring skills.

## Contributing

Use the repository templates:

- [Report a bug](.github/ISSUE_TEMPLATE/bug-report.md)
- [Propose a change](.github/ISSUE_TEMPLATE/change-proposal.md)
- [Prepare a pull request](.github/pull_request_template.md)

Keep the README, manifest, tests, team declaration, member instructions, and package tree in sync.
Never publish credentials, customer data, private-project language, personal identifiers, or
owner-specific paths.

## Releases

See [RELEASING.md](RELEASING.md). Unpublished work may remain at `0.1.0`; after the first release,
catalog changes follow semantic versioning. Publishing requires separate authorization.

## License

MIT, except material in `designing-ui-ux` adapted under Apache License 2.0. See that package's
[source basis](skills/designing-ui-ux/references/sources.md).
