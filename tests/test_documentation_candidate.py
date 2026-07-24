from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "check_documentation_candidate.py"
spec = importlib.util.spec_from_file_location("documentation_candidate", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(validator)


class DocumentationCandidateTests(unittest.TestCase):
    def sandbox(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name) / "repo"
        shutil.copytree(
            Path(__file__).parents[1],
            root,
            ignore=shutil.ignore_patterns(".git", "site", "__pycache__", "*.pyc"),
        )
        self.addCleanup(tmp.cleanup)
        return root

    def test_current_candidate_passes(self):
        report = validator.validate(Path(__file__).parents[1])
        self.assertEqual(report["release_state"], "BLOCKED")
        self.assertEqual(report["authority_effect"], "none")

    def test_missing_punchlist_fails(self):
        root = self.sandbox()
        (root / "punchlist.md").unlink()
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_broken_internal_link_fails(self):
        root = self.sandbox()
        readme = root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[Broken](missing.md)\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_mermaid_without_prose_fails(self):
        root = self.sandbox()
        page = root / "phantomblock/docs/architecture.md"
        page.write_text(page.read_text(encoding="utf-8").replace("Equivalent prose", "Visual explanation"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_release_ready_promotion_fails(self):
        root = self.sandbox()
        release = root / "release.md"
        release.write_text(release.read_text(encoding="utf-8").replace("Status: `BLOCKED", "Status: `READY"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_pages_push_trigger_fails(self):
        root = self.sandbox()
        workflow = root / ".github/workflows/pages.yml"
        workflow.write_text(workflow.read_text(encoding="utf-8").replace("  workflow_dispatch:", "  push:\n    branches: [main]\n  workflow_dispatch:"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_documentation_workflow_write_permission_fails(self):
        root = self.sandbox()
        workflow = root / ".github/workflows/documentation-candidate.yml"
        workflow.write_text(workflow.read_text(encoding="utf-8").replace("contents: read", "contents: write"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_mutable_pr_concurrency_fails(self):
        root = self.sandbox()
        workflow = root / ".github/workflows/documentation-candidate.yml"
        workflow.write_text(
            workflow.read_text(encoding="utf-8").replace(
                "${{ github.workflow }}-${{ github.event.pull_request.head.sha || github.sha }}",
                "${{ github.event.pull_request.number || github.ref }}",
            ),
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_cross_generation_cancellation_fails(self):
        root = self.sandbox()
        workflow = root / ".github/workflows/documentation-candidate.yml"
        workflow.write_text(
            workflow.read_text(encoding="utf-8").replace("cancel-in-progress: false", "cancel-in-progress: true"),
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_missing_front_door_route_fails(self):
        root = self.sandbox()
        readme = root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace("phantomblock/docs/onboarding.md", "phantomblock/docs/index.md"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)

    def test_missing_skill_gap_fails(self):
        root = self.sandbox()
        for name in validator.CONTROLLED_PLANNING:
            path = root / name
            path.write_text(path.read_text(encoding="utf-8").replace("040-H", "040-X"), encoding="utf-8")
        with self.assertRaises(ValueError):
            validator.validate(root)


if __name__ == "__main__":
    unittest.main()
