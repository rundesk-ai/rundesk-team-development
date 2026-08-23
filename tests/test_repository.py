"""The development team catalog is internally complete and safely bounded."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
AGENT_HEADINGS = (
    "# AGENTS",
    "## Purpose",
    "## Before you work",
    "## Repository layout",
    "## Package and artifact contract",
    "## Safety and approval gates",
    "## Delegation",
    "## Architecture and conventions",
    "## Documentation duties",
    "## Build, test, and run",
    "## Pull requests and releases",
    "## Definition of done",
)
README_HEADINGS = (
    "## Team",
    "## Skills",
    "## Install",
    "## Requirements",
    "## Repository layout",
    "## Development",
    "## Creating a skill catalog",
    "## Contributing",
    "## Releases",
    "## License",
)
MEMBER_HEADINGS = (
    "## Mission",
    "## What routes to you",
    "## What does not route to you",
    "## How to size the work",
    "## Authority and stop conditions",
    "## Working with the agent that called you",
    "## What to return",
    "## Boundaries",
)
MEMBER_NAMES = {"forge", "piper", "trace", "vera"}
ALLOWED_PACKAGE_ROOTS = {"SKILL.md", "references"}
FORBIDDEN_PACKAGE_FILES = {"README.md", "CHANGELOG.md", "rundesk.json"}

#: Upstream licenses this catalog has adapted material under. An attribution that
#: names none of them is not a complete citation.
LICENCES = ("MIT License", "Unlicense", "Apache License")

#: Rundesk owns these two skill names and refuses a team that allowlists either.
PRODUCT_OWNED = {"managing-rundesk", "delegating-work"}

#: What an agent is for travels in every other agent's prompt, so Rundesk caps it.
DESCRIBES_AT_MOST = 200


def texts():
    """Every tracked text file in the repository, with its path."""
    for artifact in sorted(ROOT.rglob("*")):
        if (
            not artifact.is_file()
            or ".git" in artifact.parts
            or "__pycache__" in artifact.parts
        ):
            continue
        yield artifact, artifact.read_text(encoding="utf-8", errors="ignore")


def prose(text):
    """Markdown with code samples neutralized.

    Code contains link-shaped text that is not a link -- Python's
    ``def f[T](...)`` is the case that first broke the link check. Inline code
    becomes an inert placeholder rather than being deleted, because link text
    is frequently code: ``[`references/core.md`](references/core.md)``.
    """
    text = re.sub(r"(?ms)^```.*?^```", "", text)
    return re.sub(r"`[^`\n]*`", "code", text)


def targets(page):
    """The file names a markdown page links to, ignoring anchors and code."""
    text = prose(page.read_text(encoding="utf-8"))
    found = set()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        found.add(target.split("#", 1)[0].rsplit("/", 1)[-1])
    return found


class RepositoryContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        cls.team = json.loads((ROOT / "team.json").read_text(encoding="utf-8"))

    def skill_names(self):
        return {
            path.name
            for path in (ROOT / "skills").iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }

    def members(self):
        return {member["name"]: member for member in self.team["members"]}

    def test_manifest_is_a_current_standalone_catalog(self):
        self.assertEqual(
            {"schema", "name", "version", "description"},
            set(self.manifest),
        )
        self.assertEqual(1, self.manifest["schema"])
        self.assertEqual("rundesk-team-development", self.manifest["name"])
        self.assertRegex(self.manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertTrue(self.manifest["description"].strip())
        self.assertGreaterEqual(len(self.skill_names()), 1)
        self.assertEqual(
            ".DS_Store\n__pycache__/\n*.py[cod]\n",
            (ROOT / ".gitignore").read_text(encoding="utf-8"),
        )

    def test_readme_lists_exactly_the_discovered_skills(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        listed = set(re.findall(r"(?m)^- `([a-z0-9-]+)` —", readme))
        self.assertEqual(self.skill_names(), listed)
        self.assertEqual(
            README_HEADINGS,
            tuple(re.findall(r"^## .+$", readme, re.MULTILINE)),
        )

    def test_readme_states_what_is_supported_without_claiming_a_release(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("pull request #451", readme)
        self.assertIn("dd2778d5", readme)
        self.assertIn("has not been merged", readme)
        self.assertIn("no published release", readme)

    def test_every_skill_is_complete_and_guidance_only(self):
        for name in self.skill_names():
            with self.subTest(skill=name):
                self.assertRegex(name, NAME)
                self.assertNotIn(name, PRODUCT_OWNED)
                package = ROOT / "skills" / name
                self.assertLessEqual(
                    {path.name for path in package.iterdir()},
                    ALLOWED_PACKAGE_ROOTS,
                )
                page = (package / "SKILL.md").read_text(encoding="utf-8")
                sections = page.split("---", 2)
                self.assertEqual(3, len(sections))
                frontmatter = [
                    line for line in sections[1].strip().splitlines() if line.strip()
                ]
                self.assertEqual(["name", "description"], [
                    line.partition(":")[0] for line in frontmatter
                ])
                self.assertEqual(f"name: {name}", frontmatter[0])
                description = frontmatter[1].partition(":")[2].strip()
                self.assertTrue(description)
                if re.search(r":\s", description):
                    self.assertTrue(
                        description.startswith(('"', "'"))
                        and description.endswith(('"', "'")),
                        "a description containing ': ' must be YAML-quoted",
                    )
                self.assertLessEqual(len(frontmatter[1]), 1024)
                self.assertLessEqual(len(page.splitlines()), 500)
                self.assertTrue((package / "references" / "sources.md").is_file())
                self.assertTrue((package / "references" / "validation.md").is_file())
                for forbidden in FORBIDDEN_PACKAGE_FILES:
                    self.assertFalse((package / forbidden).exists())
                self.assertFalse((package / "scripts").exists())
                self.assertFalse((package / "agents").exists())

    def test_every_reference_is_reachable_and_one_level_deep(self):
        """A package routes to all of its own depth, and never deeper than one hop.

        An unreachable reference is dead weight the agent never loads; a
        reference reachable only through a third file is the nesting the
        package contract rules out.
        """
        for name in self.skill_names():
            package = ROOT / "skills" / name
            references = {
                path.name
                for path in (package / "references").iterdir()
                if path.suffix == ".md"
            } - {"validation.md"}
            direct = references & targets(package / "SKILL.md")
            reachable = set(direct)
            for ref in direct:
                reachable |= references & targets(package / "references" / ref)
            with self.subTest(skill=name):
                self.assertEqual(references, reachable)

    def test_no_skill_routes_an_agent_to_a_validation_record(self):
        """Validation records are maintainer artifacts, not operational references."""
        for name in self.skill_names():
            package = ROOT / "skills" / name
            pages = [package / "SKILL.md"] + [
                path
                for path in (package / "references").iterdir()
                if path.suffix == ".md" and path.name != "validation.md"
            ]
            for page in pages:
                with self.subTest(page=page.relative_to(ROOT)):
                    self.assertNotIn("validation.md", targets(page))

    def test_team_declaration_matches_the_installing_contract(self):
        self.assertEqual({"schema", "name", "members"}, set(self.team))
        self.assertEqual(1, self.team["schema"])
        self.assertEqual(self.manifest["name"], self.team["name"])
        members = self.team["members"]
        names = [member["name"] for member in members]
        self.assertEqual(MEMBER_NAMES, set(names))
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(sorted(names), names)
        skills = self.skill_names()
        for member in members:
            with self.subTest(member=member["name"]):
                self.assertEqual(
                    {
                        "name",
                        "description",
                        "instructions",
                        "skills",
                        "delegates_to",
                        "self_improve",
                    },
                    set(member),
                )
                name = member["name"]
                self.assertRegex(name, NAME)
                description = member["description"]
                self.assertTrue(description.strip())
                self.assertEqual(description, description.strip())
                self.assertLessEqual(len(description), DESCRIBES_AT_MOST)
                self.assertEqual(f"agents/{name}/AGENTS.md", member["instructions"])
                page = ROOT / member["instructions"]
                self.assertTrue(page.is_file())
                self.assertTrue(page.read_text(encoding="utf-8").strip())
                allowed = member["skills"]
                self.assertEqual(len(allowed), len(set(allowed)))
                self.assertLessEqual(set(allowed), skills)
                self.assertEqual(set(), set(allowed) & PRODUCT_OWNED)
                delegates = member["delegates_to"]
                self.assertEqual(len(delegates), len(set(delegates)))
                self.assertLessEqual(set(delegates), MEMBER_NAMES - {name})
                self.assertIsInstance(member["self_improve"], bool)

    def test_no_member_leads_the_team_or_keeps_weekly_upkeep(self):
        for name, member in self.members().items():
            with self.subTest(member=name):
                self.assertEqual([], member["delegates_to"])
                self.assertIs(False, member["self_improve"])

    def test_every_member_has_executable_always_on_instructions(self):
        declared = {member["instructions"] for member in self.team["members"]}
        found = {
            str(page.relative_to(ROOT))
            for page in (ROOT / "agents").rglob("AGENTS.md")
        }
        self.assertEqual(declared, found)
        self.assertEqual(
            MEMBER_NAMES,
            {path.name for path in (ROOT / "agents").iterdir() if path.is_dir()},
        )
        for name in MEMBER_NAMES:
            with self.subTest(member=name):
                home = ROOT / "agents" / name
                self.assertEqual({"AGENTS.md"}, {p.name for p in home.iterdir()})
                page = home / "AGENTS.md"
                text = page.read_text(encoding="utf-8")
                self.assertEqual(0, page.stat().st_mode & 0o111)
                headings = tuple(re.findall(r"^#{1,2} .+$", text, re.MULTILINE))
                self.assertEqual((f"# {name.title()}",) + MEMBER_HEADINGS, headings)
                self.assertLessEqual(len(text.splitlines()), 200)
                for skill in self.skill_names():
                    self.assertNotIn(skill, text)

    def test_member_instructions_forbid_self_governance_and_onward_handoff(self):
        required = (
            "you do not delegate",
            "never edit, install, update, or publish",
        )
        for name in MEMBER_NAMES:
            page = (ROOT / "agents" / name / "AGENTS.md").read_text(encoding="utf-8")
            for phrase in required:
                with self.subTest(member=name, phrase=phrase):
                    self.assertIn(phrase, page.lower())

    def test_the_superseded_role_model_is_gone(self):
        stale = (
            "_".join(("entry", "role")),
            " ".join(("entry", "role")),
            "/".join(("team", "roles")),
            " ".join(("team", "lead")),
            "/".join(("team", "team.json")),
        )
        for artifact, text in texts():
            for phrase in stale:
                with self.subTest(artifact=artifact.relative_to(ROOT), phrase=phrase):
                    self.assertNotIn(phrase, text.lower())

    def test_skill_packages_do_not_depend_on_the_team_contract(self):
        for name in self.skill_names():
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=name):
                self.assertNotIn("team.json", skill)
                self.assertNotIn("agents/", skill)

    def test_repository_guides_are_identical_and_ordered(self):
        agents = (ROOT / "AGENTS.md").read_bytes()
        self.assertEqual(agents, (ROOT / "CLAUDE.md").read_bytes())
        self.assertEqual(
            AGENT_HEADINGS,
            tuple(re.findall(r"^#{1,2} .+$", agents.decode("utf-8"), re.MULTILINE)),
        )

    def test_markdown_local_links_resolve(self):
        for page in ROOT.rglob("*.md"):
            if ".git" in page.parts:
                continue
            text = prose(page.read_text(encoding="utf-8"))
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_text = target.split("#", 1)[0]
                with self.subTest(page=page.relative_to(ROOT), target=target):
                    self.assertTrue((page.parent / path_text).resolve().exists())

    def test_repository_is_self_contained(self):
        forbidden = (
            "/".join(("rundesk-ai", "rundesk-cli")),
            "/".join(("feat", "managing-development-work")),
            "_".join(("THIRD", "PARTY", "NOTICES.md")),
        )
        for artifact, text in texts():
            for phrase in forbidden:
                with self.subTest(artifact=artifact.relative_to(ROOT), phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_an_upstream_catalog_is_cited_but_never_depended_on(self):
        """Adapted packages must credit their upstream without importing it.

        MIT requires the notice to travel with adapted material, so a package's own
        ``references/sources.md`` may name the catalog it came from. Nothing else may:
        a sibling checkout is not part of this repository's contract.
        """
        upstream = "/".join(("rundesk-ai", "rundesk-skills"))
        for artifact, text in texts():
            provenance = (
                artifact.parent.name == "references"
                and artifact.name == "sources.md"
                and artifact.parent.parent.parent.name == "skills"
            )
            with self.subTest(artifact=artifact.relative_to(ROOT)):
                if provenance:
                    continue
                self.assertNotIn(upstream, text)

    def test_every_adapted_package_records_complete_provenance(self):
        """A citation is only honest when it names commit, path, and license."""
        upstream = "/".join(("rundesk-ai", "rundesk-skills"))
        for name in self.skill_names():
            sources = ROOT / "skills" / name / "references" / "sources.md"
            text = sources.read_text(encoding="utf-8")
            if upstream not in text:
                continue
            with self.subTest(skill=name):
                self.assertIn("## Attribution", text)
                self.assertRegex(text, r"`[0-9a-f]{40}`")
                self.assertTrue(
                    any(licence in text for licence in LICENCES),
                    f"{name} cites an upstream without naming its license",
                )

    def test_text_files_are_clean_and_never_executable(self):
        for artifact, _ in texts():
            with self.subTest(artifact=artifact.relative_to(ROOT)):
                text = artifact.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"))
                self.assertFalse(re.search(r"[ \t]+$", text, re.MULTILINE))
                self.assertEqual(0, artifact.stat().st_mode & 0o111)

    def test_release_workflow_ties_tag_to_manifest(self):
        workflow = (ROOT / ".github" / "workflows" / "release.yml").read_text(
            encoding="utf-8"
        )
        release = (ROOT / "RELEASING.md").read_text(encoding="utf-8")
        self.assertIn("does not match manifest", workflow)
        self.assertIn("git merge-base --is-ancestor", workflow)
        self.assertIn("refs/remotes/origin/main", workflow)
        self.assertIn("git diff --check", workflow)
        self.assertIn("gh release create", workflow)
        self.assertIn("manifest.json", release)

    def test_workflows_pin_actions_and_run_the_complete_gate(self):
        for name in ("build.yml", "release.yml"):
            workflow = (ROOT / ".github" / "workflows" / name).read_text(
                encoding="utf-8"
            )
            with self.subTest(workflow=name):
                self.assertRegex(workflow, r"actions/checkout@[0-9a-f]{40}")
                self.assertRegex(workflow, r"actions/setup-python@[0-9a-f]{40}")
                self.assertIn("git diff --check", workflow)
                self.assertIn("python -m unittest discover -s tests -v", workflow)


if __name__ == "__main__":
    unittest.main()
