# Brief — rundesk-team-development

*What this team is and why it exists. One screen, and it changes when the team does.*

## Story

`rundesk-team-development` is Rundesk's software-development team, kept as one versioned artifact. It
publishes a guidance-only skill catalog and, in the same tree, the team declaration and the canonical
instructions for four named agents: **forge** implements, **piper** judges finished work, **trace**
investigates failures without changing anything, and **vera** owns the frontend and its defects.

Updating this repository updates the team. Agents do not rewrite themselves and do not drift between
installs.

## Why it exists

An agent that edits its own instructions is an agent nobody can reason about: two installs of the
same name diverge, and neither can be reproduced. Keeping the instructions in version control and
having Rundesk reconcile against them makes the declaration the source of truth and drift a thing
that gets repaired rather than accumulated.

Four narrow members beat one broad one because the failure modes differ. An implementer that reviews
its own work grades its own homework; a debugger that fixes what it finds stops being able to say
what was actually wrong.

## Users

- The domain agent that calls this team for a bounded piece of software work.
- The owner, who installs the team and can see exactly which instructions and skills each member has.

*Sourced from the readme, the team declaration, and the member instruction files.*

## Scope

- **Covers:** the four members and their canonical instructions; the guidance skills they hold across
  delivery, design, debugging, review, testing, documentation placement and writing, and the language,
  framework, and database stacks; and the team's reconciliation contract with Rundesk.
- **Refuses:**
  - A lead or coordinating member. The team has no accountable coordinator; every member is
    inbound-only and answers the agent that called it.
  - A member editing, installing, or publishing the catalog that governs it.
  - Executables, service adapters, credentials, and network behavior. This is guidance only.
  - Product-owned operating skills, which ship with Rundesk itself.
  - `managing-development-work` in any member's allowlist. It belongs to the agent calling the team,
    and that absence is the design.

## External systems

- Rundesk — installs the catalog, creates and reconciles the members, and owns the drift boundary.
- GitHub — hosts the repository and serves the release an install fetches.
