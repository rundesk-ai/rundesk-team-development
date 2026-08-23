# Rundesk Team Development

Rundesk's development-team package. It combines a current-format, guidance-only skill catalog with
the proposed team definition that will prepare a future Rundesk team mode. Current Rundesk can
install and grant the skills; it does not yet read `team/team.json` or create the four roles.

## Skills

- `managing-development-work` — Scope and coordinate a software change from request through verified local completion.
- `managing-github` — Route and verify GitHub-hosted issue, pull-request, release, and repository-delivery workflows, whether reached directly or from development work.

## Install

Preview the catalog before changing an install, then confirm it and grant only the skills an agent
needs:

```sh
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development
rundesk skills install https://github.com/rundesk-ai/rundesk-team-development --confirm
rundesk skills grant ava rundesk-team-development/managing-development-work
```

Installation grants no skills automatically. The catalog name owns updates; each skill name owns
grants:

```sh
rundesk skills update rundesk-team-development
rundesk skills update rundesk-team-development --confirm
rundesk skills grant ava rundesk-team-development/managing-github
```

## Requirements

- The catalog is public and installs from its GitHub repository with the current Rundesk CLI.
- Packages are guidance-only. They ship no executable, credential, dependency, service adapter, or
  network integration.
- Skills may describe local development tools and GitHub CLI operations. The active task and target
  repository rules still control whether any mutation is authorized.
- Each package works without another catalog checkout. Related skills may compose when installed,
  but no package makes another skill a runtime dependency.

`managing-development-work` owns the local delivery contract: scope, mode, risk response,
coordination, and proof. `managing-github` owns GitHub-hosted delivery: issues, pull requests,
releases, and the stored-object readback after an authorized mutation. The first may hand a verified
local result to the second; neither duplicates the other's workflow.

The proposed team starts with Piper as its accountable entry role. Piper may hand bounded work to
Forge for implementation, Trace for read-only investigation and review, or Vera for product and
interface design. The role files define responsibility and handoff; the skills remain reusable and
do not depend on those role names.

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

## Development

Read [AGENTS.md](AGENTS.md) before changing the repository. The complete offline gate is:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

Skill changes also require verification of every relied-on source link and a realistic forward test
when guidance materially changes.

## Creating a skill catalog

This repository is the complete catalog contract: `manifest.json` identifies the installable
catalog, `skills/<name>/SKILL.md` supplies provider-compatible `name` and `description` frontmatter,
and the offline suite validates discovery, package boundaries, role structure, and documentation
parity. No sibling checkout or external catalog guide is required to develop or install it.

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
notes together. Never publish credentials, customer data, private-project language, personal
identifiers, or owner-specific paths.

## Releases

Published skill behavior follows [RELEASING.md](RELEASING.md). Content changes update the manifest
version in the same pull request; repository-process-only corrections do not require a version bump.

## License

This catalog is available under the [MIT License](LICENSE).
