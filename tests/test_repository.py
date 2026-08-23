"""The development team package is internally complete and safely bounded."""

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
ROLE_NAMES = {"forge", "piper", "trace", "vera"}
ALLOWED_PACKAGE_ROOTS = {"SKILL.md", "references"}
FORBIDDEN_PACKAGE_FILES = {"README.md", "CHANGELOG.md", "rundesk.json"}


class RepositoryContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        cls.team = json.loads((ROOT / "team" / "team.json").read_text(encoding="utf-8"))

    def skill_names(self):
        return {
            path.name
            for path in (ROOT / "skills").iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }

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
        listed = set(re.findall(r"(?m)^- `([a-z0-9-]+)`", readme))
        self.assertEqual(self.skill_names(), listed)
        self.assertEqual(
            README_HEADINGS,
            tuple(re.findall(r"^## .+$", readme, re.MULTILINE)),
        )
        self.assertIn("does not yet read `team/team.json`", readme)

    def test_every_skill_is_complete_and_guidance_only(self):
        for name in self.skill_names():
            with self.subTest(skill=name):
                self.assertRegex(name, NAME)
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
                for artifact in package.rglob("*"):
                    if artifact.is_file():
                        self.assertEqual(0, artifact.stat().st_mode & 0o111)

    def test_team_contract_and_role_graph_are_closed(self):
        self.assertEqual(
            {"schema", "name", "description", "entry_role", "roles"},
            set(self.team),
        )
        self.assertEqual(1, self.team["schema"])
        self.assertEqual("development", self.team["name"])
        self.assertEqual("piper", self.team["entry_role"])
        roles = self.team["roles"]
        names = [role["name"] for role in roles]
        self.assertEqual(ROLE_NAMES, set(names))
        self.assertEqual(len(names), len(set(names)))
        by_name = {role["name"]: role for role in roles}
        self.assertEqual(["forge", "trace", "vera"], by_name["piper"]["delegates_to"])
        for name, role in by_name.items():
            with self.subTest(role=name):
                self.assertEqual(
                    {"name", "path", "purpose", "delegates_to"},
                    set(role),
                )
                self.assertRegex(name, NAME)
                self.assertEqual(f"roles/{name}.md", role["path"])
                self.assertTrue(role["purpose"].strip())
                self.assertLessEqual(set(role["delegates_to"]), ROLE_NAMES - {name})
                role_file = ROOT / "team" / role["path"]
                self.assertTrue(role_file.is_file())
                self.assertIn(f"# {name.title()}", role_file.read_text(encoding="utf-8"))
                if name != "piper":
                    self.assertEqual([], role["delegates_to"])

    def test_skill_packages_do_not_depend_on_the_team_contract(self):
        for name in self.skill_names():
            skill = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=name):
                self.assertNotIn("team/team.json", skill)
                self.assertNotIn("team/roles/", skill)
                self.assertNotIn("entry_role", skill)

    def test_repository_guides_are_identical_and_ordered(self):
        agents = (ROOT / "AGENTS.md").read_bytes()
        self.assertEqual(agents, (ROOT / "CLAUDE.md").read_bytes())
        self.assertEqual(
            AGENT_HEADINGS,
            tuple(re.findall(r"^#{1,2} .+$", agents.decode("utf-8"), re.MULTILINE)),
        )

    def test_markdown_local_links_resolve(self):
        markdown_files = list(ROOT.rglob("*.md"))
        for page in markdown_files:
            text = page.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_text = target.split("#", 1)[0]
                with self.subTest(page=page.relative_to(ROOT), target=target):
                    self.assertTrue((page.parent / path_text).resolve().exists())

    def test_repository_is_self_contained(self):
        forbidden = (
            "/".join(("rundesk-ai", "rundesk-skills")),
            "/".join(("rundesk-ai", "rundesk-cli")),
            "/".join(("feat", "managing-development-work")),
            "_".join(("THIRD", "PARTY", "NOTICES.md")),
        )
        for artifact in ROOT.rglob("*"):
            if (
                not artifact.is_file()
                or ".git" in artifact.parts
                or "__pycache__" in artifact.parts
            ):
                continue
            text = artifact.read_text(encoding="utf-8", errors="ignore")
            for phrase in forbidden:
                with self.subTest(artifact=artifact.relative_to(ROOT), phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_text_files_have_clean_whitespace(self):
        for artifact in ROOT.rglob("*"):
            if (
                not artifact.is_file()
                or ".git" in artifact.parts
                or "__pycache__" in artifact.parts
            ):
                continue
            text = artifact.read_text(encoding="utf-8")
            with self.subTest(artifact=artifact.relative_to(ROOT)):
                self.assertTrue(text.endswith("\n"))
                self.assertFalse(re.search(r"[ \t]+$", text, re.MULTILINE))

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
