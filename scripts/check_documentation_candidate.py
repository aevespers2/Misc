#!/usr/bin/env python3
"""Validate the Misc/XYZ documentation candidate without publishing or mutating state."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REQUIRED_FILES = {
    "README.md",
    "taskchain.md",
    "release.md",
    "punchlist.md",
    "changelog.md",
    "phantomblock/mkdocs.yml",
    "phantomblock/docs/index.md",
    "phantomblock/docs/incubation-status.md",
    "phantomblock/docs/architecture.md",
    "phantomblock/docs/onboarding.md",
    "phantomblock/docs/developer-guide.md",
    ".github/workflows/pages.yml",
    ".github/workflows/documentation-candidate.yml",
}

CONTROLLED_PLANNING = {
    "README.md",
    "taskchain.md",
    "release.md",
    "punchlist.md",
    "changelog.md",
}

REQUIRED_ROUTES = {
    "phantomblock/docs/incubation-status.md",
    "phantomblock/docs/index.md",
    "phantomblock/docs/architecture.md",
    "phantomblock/docs/onboarding.md",
    "phantomblock/docs/developer-guide.md",
    "punchlist.md",
    "taskchain.md",
    "release.md",
    "changelog.md",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MERMAID_RE = re.compile(r"```mermaid\s+.*?```", re.DOTALL)


def fail(message: str) -> None:
    raise ValueError(message)


def text(root: Path, rel: str) -> str:
    path = root / rel
    if not path.is_file():
        fail(f"missing required file: {rel}")
    return path.read_text(encoding="utf-8", errors="strict")


def markdown_files(root: Path) -> list[Path]:
    files = [root / name for name in CONTROLLED_PLANNING]
    files.extend(sorted((root / "phantomblock" / "docs").glob("*.md")))
    return files


def validate_links(root: Path) -> int:
    count = 0
    for source in markdown_files(root):
        body = source.read_text(encoding="utf-8", errors="strict")
        for raw_target in LINK_RE.findall(body):
            target = raw_target.strip().split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            target = unquote(target)
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                fail(f"link escapes repository: {source.relative_to(root)} -> {raw_target}")
            if not resolved.exists():
                fail(f"broken internal link: {source.relative_to(root)} -> {raw_target}")
            count += 1
    return count


def validate_mermaid_alternatives(root: Path) -> int:
    count = 0
    for source in markdown_files(root):
        body = source.read_text(encoding="utf-8", errors="strict")
        diagrams = MERMAID_RE.findall(body)
        if diagrams and "Equivalent prose" not in body:
            fail(f"Mermaid diagram lacks an equivalent prose alternative: {source.relative_to(root)}")
        count += len(diagrams)
    return count


def validate_pages_workflow(root: Path) -> None:
    body = text(root, ".github/workflows/pages.yml")
    if "workflow_dispatch:" not in body:
        fail("Pages workflow must remain manual-only")
    if re.search(r"^\s*push:\s*$", body, re.MULTILINE):
        fail("Pages workflow must not publish on push while release is blocked")
    for required in ("contents: read", "pages: write", "id-token: write"):
        if required not in body:
            fail(f"Pages workflow missing required permission declaration: {required}")
    if "release.md" not in body or "explicitly marked READY" not in body:
        fail("Pages workflow lacks the explicit release-readiness gate")


def validate_candidate_workflow(root: Path) -> None:
    body = text(root, ".github/workflows/documentation-candidate.yml")
    if "contents: read" not in body:
        fail("Documentation workflow must declare contents: read")
    for prohibited in ("pages: write", "id-token: write", "packages: write", "deploy-pages"):
        if prohibited in body:
            fail(f"Documentation workflow has prohibited authority: {prohibited}")
    for pinned in (
        "actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683",
        "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
        "actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08",
    ):
        if pinned not in body:
            fail(f"documentation workflow action is not pinned as required: {pinned}")
    if "persist-credentials: false" not in body:
        fail("documentation workflow must disable persisted checkout credentials")


def validate_planning_alignment(root: Path) -> None:
    release = text(root, "release.md")
    if "Status: `BLOCKED" not in release:
        fail("release.md must remain explicitly BLOCKED")
    if re.search(r"^Status:\s*`READY", release, re.MULTILINE):
        fail("documentation changes cannot promote release.md to READY")

    combined = "\n".join(text(root, name) for name in CONTROLLED_PLANNING)
    for phrase in (
        "HOLDING / INCUBATION",
        "punchlist.md",
        "migration",
        "retire",
        "rollback",
        "CAT-012",
        "CAT-040",
        "040-H",
    ):
        if phrase not in combined:
            fail(f"controlled planning documents lack required concept: {phrase}")

    readme = text(root, "README.md")
    for route in REQUIRED_ROUTES:
        if route not in readme:
            fail(f"README front door is missing route: {route}")

    nav = text(root, "phantomblock/mkdocs.yml")
    for page in ("incubation-status.md", "onboarding.md", "developer-guide.md", "architecture.md"):
        if page not in nav:
            fail(f"MkDocs navigation is missing page: {page}")


def validate_authority_boundary(root: Path) -> None:
    combined = "\n".join(path.read_text(encoding="utf-8", errors="strict") for path in markdown_files(root))
    for phrase in (
        "explicit authorization",
        "does not establish",
        "release",
        "deployment",
        "certification",
        "sensitive",
    ):
        if phrase.lower() not in combined.lower():
            fail(f"documentation authority boundary lacks required concept: {phrase}")


def validate(root: Path) -> dict[str, object]:
    root = root.resolve()
    for rel in sorted(REQUIRED_FILES):
        text(root, rel)
    links = validate_links(root)
    diagrams = validate_mermaid_alternatives(root)
    validate_pages_workflow(root)
    validate_candidate_workflow(root)
    validate_planning_alignment(root)
    validate_authority_boundary(root)
    return {
        "disposition": "DOCUMENTATION_CANDIDATE_STRUCTURALLY_VALID",
        "required_files": len(REQUIRED_FILES),
        "markdown_files": len(markdown_files(root)),
        "internal_links_checked": links,
        "mermaid_diagrams_checked": diagrams,
        "release_state": "BLOCKED",
        "publication_state": "MANUAL_AND_FAIL_CLOSED",
        "authority_effect": "none",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    try:
        print(json.dumps(validate(Path(args.root)), indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"disposition": "DOCUMENTATION_CANDIDATE_FAILED_CLOSED", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
