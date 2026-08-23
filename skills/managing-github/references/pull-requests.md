# GitHub pull requests

## Discover the pull-request contract

Read applicable repository instructions, `CONTRIBUTING.md`, pull-request templates, and workflows
that define required checks. Inspect templates on the default branch and preserve the matching
template's headings, order, questions, checklists, and footer. Remove comments and placeholders;
support each checked claim with evidence from the exact head.

Map the target repository and branch destination to explicit remotes:

```sh
git remote get-url <base-remote>
git remote get-url <push-remote>
```

Resolve the base from repository rules or the default branch. Confirm the current branch is not the
base or an unrelated worktree. If the worktree is dirty, determine which changes belong to the
request before proceeding. Never hide, discard, or rewrite changes to make a branch appear ready.

Check for an existing pull request from the same branch and owner:

```sh
gh pr list --repo <owner/repo> --state all --head <branch> \
  --json number,state,url,title,headRepositoryOwner
```

`--head` takes the branch name in this listing. Inspect `headRepositoryOwner` before deciding whether
to update an existing pull request or open another.

## Inspect the review range

Fetch the selected base and inspect the merge-base range reviewers will receive:

```sh
git fetch <base-remote> <base>
git log --oneline <base-remote>/<base>..HEAD
git diff --stat <base-remote>/<base>...HEAD
git diff --check <base-remote>/<base>...HEAD
git diff <base-remote>/<base>...HEAD
```

Confirm one coherent outcome, no credentials or generated clutter, no unrelated edits, and no
unexplained change outside the accepted boundary. Run repository-required validation. Report only
checks observed for the current head and name each required check that remains unrun.

## Separate review judgment from hosted review state

Use the applicable technical review workflow to inspect the diff for defects, regressions, security,
and maintainability. This GitHub workflow owns the hosted pull-request context around that judgment:
the explicit repository and pull request, base and head, template compliance, requested reviewers,
existing reviews, check state, and any authorized review submission.

Inspect the current hosted state before calling a pull request ready or deciding what kind of review
is appropriate:

```sh
gh pr view <number> --repo <owner/repo> \
  --json url,title,body,baseRefName,headRefName,headRefOid,isDraft,reviewDecision,reviewRequests,reviews,statusCheckRollup
gh pr checks <number> --repo <owner/repo>
```

Do not infer code quality from a filled template, green checks, or an existing approval. Conversely,
do not submit a GitHub review merely because a technical reviewer returned findings: confirm the
review applies to the pull request's current head, sanitize the body, and require authority for the
exact `comment`, `approve`, or `request changes` effect.

Record the current `headRefOid`, submit a prepared review body from a file, and select exactly one
decision:

```sh
gh pr review <number> --repo <owner/repo> --comment --body-file <review.md>
gh pr review <number> --repo <owner/repo> --approve --body-file <review.md>
gh pr review <number> --repo <owner/repo> --request-changes --body-file <review.md>
```

After submission, read `reviews`, `latestReviews`, `reviewDecision`, and the current head OID back.
Verify the stored author, decision, and body, and confirm the head still equals the recorded OID. If
the head changed, report that the technical judgment may be stale; do not silently resubmit or
change the decision.
Requesting or removing reviewers, dismissing a review, resolving threads, merging, or enabling
auto-merge are separate mutations and require their own authority.

## Write the merge case

A pull-request body is a scan-friendly review map, not an implementation diary, design archive, or
test transcript. Use the repository template when one applies. Otherwise complete the
[fallback pull-request template](pull-request-template.md).

Keep the body proportionate:

- State the current problem and its impact in one or two lines.
- Explain three to six important solution decisions, their rationale, boundaries, and preserved
  behavior. Link deeper artifacts rather than pasting algorithms or chronology.
- Give concise before-and-after evidence when the diff alone cannot establish the result.
- Map acceptance criteria to observable outcomes proven by the exact head.
- Name material compatibility and risk; group exact validation commands with observed results.
- Give the shortest representative manual path, normally no more than five steps.
- Make blockers, unrun checks, and readiness visible.

Delete generic filler, repeated request text, changed-file inventories, and claims such as “works as
expected.” Preserve a repository's required identity block. With none, append:

```md
## Agent

🤖 by <Agent display name>
```

Do not add provider, model, tool, session, vendor link, generated-by footer, or provider-style
co-author attribution. Follow the repository title convention; use an imperative title only when no
convention exists.

Use one full closing reference per issue the pull request completes. GitHub applies closing keywords
automatically only when the pull request targets the repository's default branch. Use `Refs` or
`Related` for partial work or a staging base.

## Open, update, and verify

Recheck repository, base, head, review range, template, validation, and authority immediately before
mutation. Use a body file:

```sh
git push -u <push-remote> <branch>
gh pr create --repo <owner/repo> \
  --base <base> \
  --head <branch> \
  --title '<title>' \
  --body-file <pull-request-body.md> \
  [--draft]
```

For a user-owned fork, qualify the head as `<user>:<branch>`. GitHub CLI does not support an
organization name in that qualified form. Stop rather than opening from a different repository.

For an existing pull request, inspect it before `gh pr edit` and change only requested fields. Do not
add reviewers, assignees, projects, labels, merge queues, or merge settings without specific
authority.

Read the stored pull request and checks:

```sh
gh pr view <number> --repo <owner/repo> \
  --json url,title,body,baseRefName,headRefName,headRefOid,headRepository,headRepositoryOwner,isDraft,closingIssuesReferences,latestReviews,reviewDecision,reviews
gh pr checks <number> --repo <owner/repo>
```

Verify repository, base, head, owner, title, body, template, identity, privacy, draft state, closing
links, and URL. Report pending or failing checks; creation alone is not merge readiness.
