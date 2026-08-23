# Releasing Rundesk Team Development

The manifest version labels the catalog Rundesk reports. Catalog content remains authoritative for
update detection, while the matching tag and GitHub Release provide an auditable published snapshot.

## Prepare

1. Put every intended catalog change in one pull request against `main`.
2. Before the first `v0.1.0` publication, keep unreleased iteration at `0.1.0`. After a version has
   been published, update `manifest.json` with semantic versioning: patch for compatible
   corrections, minor for a new skill or backward-compatible capability, and major for an
   incompatible catalog or package contract.
3. Run `python3 -m unittest discover -s tests -v` and wait for the `build` workflow on the exact head.
4. Review the complete package tree, README skill list, compatibility impact, sources, and licenses.

Do not tag unmerged content, reuse a published tag, or move a published tag.

## Publish

After the pull request is approved and merged, read the manifest version and tag that exact merge
commit:

```sh
version=$(python3 -c 'import json; print(json.load(open("manifest.json"))["version"])')
git tag "v$version" <merge-commit>
git push origin "v$version"
```

The release workflow refuses a mismatched tag, reruns the catalog suite, and creates the GitHub
Release. Verify the workflow and stored release:

```sh
gh run list --workflow release.yml --limit 1
gh release view "v$version"
```

Publishing, tagging, pushing, or creating a release always requires authority for that exact
repository, version, and commit.
