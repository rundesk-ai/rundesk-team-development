# Codemap — rundesk-team-development

Where each part lives. Counts are of artifacts, so they survive a rename and go wrong visibly when
the tree moves on without this page.

Two things share one tree: a guidance-only skill catalog, and the declaration of the four agents
Rundesk creates from it. Every package is a directory under `skills/`; every member is a single
instruction file under `agents/`.

## Packages (skills/ — 21, 214 reference files)

Each holds `SKILL.md` for routing and core procedure, and `references/` for detail loaded on demand.
`references/sources.md` is required in every touched package.

| Package | References | Command |
|---|---|---|
| `debugging-code` | 8 | — |
| `designing-apis` | 10 | — |
| `designing-databases` | 6 | — |
| `designing-landing-pages` | 5 | — |
| `designing-ui-ux` | 8 | — |
| `managing-development-work` | 2 | — |
| `reviewing-code` | 6 | — |
| `structuring-project-docs` | 8 | — |
| `testing-code` | 7 | — |
| `using-axmol` | 9 | — |
| `using-cpp` | 9 | — |
| `using-inertia` | 6 | — |
| `using-laravel` | 24 | — |
| `using-mysql` | 20 | — |
| `using-postgres` | 34 | — |
| `using-python` | 10 | — |
| `using-reactjs` | 10 | — |
| `using-sqlite` | 8 | — |
| `using-tailwindcss` | 7 | — |
| `using-vuejs` | 10 | — |
| `writing-technical-docs` | 7 | — |

Every package is guidance only: no script, executable, credential, or network call.

## Team (agents/ — 4 members)

Each member's `agents/<name>/AGENTS.md` is its whole operating contract, and `team.json` declares
which skills it holds and who it may delegate to.

| Member | Owns |
|---|---|
| `forge` | bounded implementation, and the tests and documentation that prove it |
| `piper` | independent judgment of finished work; implements nothing it reviews |
| `trace` | read-only investigation; returns a reproduction and the located cause |
| `vera` | frontend and product judgment; writes no production code |

## Identity (root)

| File | What it is |
|---|---|
| `manifest.json` | schema, name, version (`0.9.3`), and description |
| `README.md` | the consumer contract: the team, its skills, and how to install both |
| `team.json` | the declaration Rundesk reconciles against: members, grants, delegation, upkeep |
| `agents/<member>/AGENTS.md` | one member`s whole operating contract, four sections and at most fifty lines |
| `AGENTS.md`, `CLAUDE.md` | the repository guide, byte-identical by contract |
| `RELEASING.md` | the publication contract |

## Tests (tests/ — 1 suite)

The repository contract: the manifest and the tree agree, every package is complete and correctly
named, the README lists exactly what ships, and the guide pair stays byte-identical.

## Automation (.github/)

Issue templates, the pull-request template, and the workflow that runs the suite.

## Documentation (docs/)

`README.md`, `BRIEF.md`, and `CODEMAP.md` at the root, plus `guides/`.
