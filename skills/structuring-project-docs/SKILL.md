---
name: structuring-project-docs
description: Use when creating, auditing, or converting a repository's documentation home — deciding where the brief, the codemap, the surface reference, requirements, research, and comparison material live, and what each of those files must contain. It supplies one repository documentation layout, a template for every home, and the rules that keep an index level with the tree it describes. Do not use for writing or revising the prose of one page, for product requirement content, or for a repository that already publishes its own documentation template.
---

# Structure a repository's documentation

A repository accumulates documents faster than it accumulates places to put them. Once the same fact
has two homes, both are believed and one is wrong. This skill decides the homes.

It owns **where a document lives and what shape it takes**, and nothing about the prose inside one.
Load the documentation-writing skill alongside it for how a page is written and how its claims are
traced, and the product-requirements skill for how to reason about what the product must do.
Where a repository already publishes its own documentation template, that template wins over this
one; convert to it rather than over it.

## Audit before you create anything

List every documentation-bearing path before proposing a layout: `docs/`, `.ai/`, `.knowledge/`,
`wiki/`, a generated site, loose `PLAN-*.md` and `NOTES.md` at the root, and the agent instruction
files. For each, record what it holds, whether it is committed, and whether anything still reads it.

Then classify each file into exactly one of the homes below. A file that classifies into two is two
files. A file that classifies into none is the interesting case — it is usually one of:

- a plan for work that has not happened, which belongs with the work, not in `docs/`;
- a status report, which ages into a lie and belongs in the tracker or the pull request;
- somebody's private notes, which are not documentation and are not yours to move.

**Never stand up a second documentation home beside a working one.** Convert the existing one, or
leave it alone. Two homes is the failure this skill exists to prevent, and creating one while
migrating away from another produces exactly that state for however long the migration takes.

## Place every document in one home

```text
docs/
  README.md            the index — every page and home, with the question it answers
  BRIEF.md             what this is, who it serves, what it refuses
  CODEMAP.md           where each layer lives, with counts
  api/                 the surface this repository publishes
    README.md
  requirements/        what must be true, and whether anything proves it
    README.md
  research/            dated findings about the world outside this repository
    README.md
  references/          material from elsewhere that this repository is measured against
    README.md
  assets/<topic>/      images the pages embed
  <topic>.md           one page per subsystem, the source of truth for that subsystem
```

`api/` and `references/` sit next to each other and are constantly confused. The distinction is one
line: **`api/` is the surface you publish; `references/` is material from outside that you compare
yourself against.** A screenshot of a competitor's settings page is a reference. Your own command
list is api.

**Required:** `README.md`, `BRIEF.md`, `CODEMAP.md`, `requirements/`, and `research/`. Add `api/` for
any repository that publishes a surface somebody else calls — a CLI, an HTTP API, a library, a
plugin contract.

**On demand:** `references/` and `assets/` exist once there is a set or an image to put in them.
Never create an empty home. A directory holding only a placeholder teaches the next reader that the
layout is decoration.

Topic pages carry the subsystems. One page per subsystem, named for the thing a reader is looking
for, and it is the source of truth for that subsystem — not a summary of a source of truth kept
elsewhere. Read [references/layout.md](references/layout.md) for what belongs in each home, what to
do with material that fits none of them, and the order to convert an existing tree in.

## Date anything that came from outside

Three kinds of page get filed as each other, and the cost is that a stale one is trusted. Separate
them by what would make each wrong:

- A **topic page** describes this software as it is. It is wrong the moment the product changes.
- A **research note** describes the world outside this repository — a platform's real behavior, how
  somebody else solved a problem, what a previous build learned. It is wrong only when the world
  changes, and it carries the date it was established and what it was true of.
- A **reference** is material from elsewhere this project is measured against, kept in a set with a
  note saying where it came from and what to take from it.

Research is input, never truth. It informs a requirement; it is never the source of record for this
project's own behavior, and a topic page should not cite one for a guarantee.

Read [references/research.md](references/research.md) for both templates, the two rules that make a
research note usable a year later, and why a note is never rewritten when the world moves on.

## Write the orientation pair before the topic pages

`BRIEF.md` and `CODEMAP.md` are read first and read most, by people and by agents. They are the two
files worth writing before anything else, because every later decision about where something goes is
easier once they exist.

Most of a brief is not in the code. Scope and external systems are; who it is for and what it
deliberately refuses are not. **Never infer an audience from a schema** — a plausible invented one is
worse than a blank section, because it is loaded on every future task and nobody re-checks it. Draft
what the repository can prove, mark the rest, and get it confirmed.

A codemap is an inventory, not a tutorial. One section per layer, each listing what exists, with a
count in the heading. **Count artifacts, not lines** — "18 services" survives a refactor and makes
drift obvious; "client.py — 1,205 lines" is stale on the next commit and tells a reader nothing.

Read [references/orientation.md](references/orientation.md) for both templates, where the answers
come from, and the quality bar each has to clear.

## Keep requirements a closed schema

A requirements document asserts what must be true and whether anything proves it. It never explains
how something is built, and it never argues for it. Four headings, that order, nothing else:

```md
---
id: NS
name: <what this contract owns>
last_verified: YYYY-MM-DD
---

## What this is
## Why it exists
## Requirements

|    | ID | Requirement | Evidence |
|:--:|---|---|---|
| ✅ | R-NS-1 | <one assertion, in the language of the product> | `test_case_name` |
| ❌ | R-NS-2 | <built, but nothing proves it> | src/thing.ext:88 — no test |
| ❌ | R-NS-3 | <nothing exists yet> | — |

## Open questions
```

The glyph is the first column and its header stays empty. A ✅ means a named check was observed to
pass; a source path is not evidence, and neither is a test that exists but was never run. Requirement
IDs are `R-<NS>-<n>`, one namespace per file. **An ID is never reused and never renumbered.**

Withdraw a requirement by deleting its row and leaving the number missing. A gap is information — it
says something was withdrawn — and it costs a reader one question. Closing the gap costs them a
confident wrong answer: renumbering repoints every citation of every ID at or after it, in the other
contracts, in code comments, and in tests that name their requirement, and nothing fails when it
happens. Grep the namespace across the whole repository before withdrawing anything, and if a
citation sits somewhere you cannot change in the same commit, stop and ask.

Read [references/requirements.md](references/requirements.md) for how to word a requirement, where to
put the urge to explain, and how a document that is not a current promise is marked as one.

## Keep each index level with its tree

Every home has a `README.md` that lists what is in it, one row per document, each row saying what
that document answers. `docs/README.md` does the same for the whole set.

An index behind its directory is worse than no index, because a reader who finds nine of your twelve
research notes stops looking for the other three. This is the single most common drift in this
layout: files land, the index does not move, and nothing complains.

- Add the row in the same change that adds the file. Not afterwards.
- Record what a row **is**, never how many of them are green. A count in a summary is stale the day
  after it is written, and unlike a stale row, nobody re-reads a summary to catch it.
- When a page is deleted, delete its row and say so.

## Verify the layout

Nothing here is enforced by a machine unless the repository chooses to enforce it, so the check is
deliberate:

1. List the tree and the indexes side by side. Every file appears in exactly one index; every row
   resolves to a file that exists.
2. Follow every relative link in every changed page.
3. Confirm no home was created empty, and no fact acquired a second home.
4. For each namespace, confirm no ID is duplicated and every ✅ names a check that exists. A
   missing number is a withdrawal, not a defect.
5. Read `BRIEF.md` as somebody who has never seen the repository. If a section reads as invented
   rather than sourced, mark it rather than leaving it level with the rest.
6. Say which of these you did not do.

Read [references/sources.md](references/sources.md) before changing a rule in this package.
