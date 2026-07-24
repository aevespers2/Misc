#!/usr/bin/env python3
"""Validate the Misc/XYZ documentation candidate without publishing or mutating state."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

FROZEN_SOURCE_COMMIT = "68703e138ffa1df26924dd4e018078a246531ace"
MANIFEST_STATUS = "FILE_DISPOSITION_MANIFEST_COMPLETE_FOR_FROZEN_SOURCE_DECISION_UNAPPROVED"
MANIFEST_PATH = "phantomblock/docs/file-disposition-manifest-v1.json"
EXPECTED_FROZEN_SOURCE_PATHS = {
    ".github/workflows/documentation-candidate.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/phantomblock-ci.yml",
    "README.md",
    "changelog.md",
    "phantomblock/README.md",
    "phantomblock/compliance/README.md",
    "phantomblock/compliance/control-mapping.yml",
    "phantomblock/config/known_good.example.yml",
    "phantomblock/docs/architecture.md",
    "phantomblock/docs/compliance.md",
    "phantomblock/docs/component-overlap-inventory-v1.json",
    "phantomblock/docs/component-overlap-inventory.md",
    "phantomblock/docs/deployment.md",
    "phantomblock/docs/developer-guide.md",
    "phantomblock/docs/extensions.md",
    "phantomblock/docs/incubation-exit-and-migration.md",
    "phantomblock/docs/incubation-status.md",
    "phantomblock/docs/index.md",
    "phantomblock/docs/onboarding.md",
    "phantomblock/docs/purpose.md",
    "phantomblock/docs/threat-model.md",
    "phantomblock/docs/validation.md",
    "phantomblock/image/build.sh",
    "phantomblock/image/mkosi.conf",
    "phantomblock/mkdocs.yml",
    "phantomblock/packaging/build-binary.sh",
    "phantomblock/packaging/phantomblock.spec",
    "phantomblock/pyproject.toml",
    "phantomblock/src/phantomblock/__init__.py",
    "phantomblock/src/phantomblock/cli.py",
    "phantomblock/src/phantomblock/core.py",
    "phantomblock/src/phantomblock/dashboard.py",
    "phantomblock/src/phantomblock/extensions.py",
    "phantomblock/src/phantomblock/isolation.py",
    "phantomblock/src/phantomblock/policy.py",
    "phantomblock/tests/test_core.py",
    "punchlist.md",
    "release.md",
    "scripts/check_documentation_candidate.py",
    "taskchain.md",
    "tests/test_documentation_candidate.py",
}

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
    "phantomblock/docs/file-disposition-manifest.md",
    MANIFEST_PATH,
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
    "phantomblock/docs/file-disposition-manifest.md",
    MANIFEST_PATH,
    "punchlist.md",
    "taskchain.md",
    "release.md",
    "changelog.md",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MERMAID_RE = re.compile(r"```mermaid\s+.*?```", re.DOTALL)
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
COMPONENT_RE = re.compile(r"^C(?:0[1-9]|1[0-8])$")


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


def reject_constant(value: str) -> None:
    fail(f"non-finite JSON constant is prohibited: {value}")


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(root: Path, rel: str) -> dict[str, object]:
    raw = text(root, rel)
    value = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
    if not isinstance(value, dict):
        fail(f"JSON root must be an object: {rel}")
    return value


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
        fail("Documentation workflow must disable persisted checkout credentials")
    exact_group = "${{ github.workflow }}-${{ github.event.pull_request.head.sha || github.sha }}"
    if exact_group not in body:
        fail("Documentation workflow concurrency must be bound to the immutable submitted SHA")
    if re.search(r"cancel-in-progress:\s*true", body):
        fail("Documentation workflow must not cancel evidence collection for prior exact heads")
    if "cancel-in-progress: false" not in body:
        fail("Documentation workflow must explicitly preserve every exact-head generation")


def validate_file_manifest(root: Path) -> dict[str, object]:
    manifest = strict_json(root, MANIFEST_PATH)
    if manifest.get("schema") != "misc.file-disposition-manifest.v1":
        fail("file manifest schema is unsupported")
    if manifest.get("status") != MANIFEST_STATUS:
        fail("file manifest status does not preserve the unapproved decision boundary")
    if manifest.get("authority_effect") != "NONE":
        fail("file manifest must have no authority effect")

    source = manifest.get("source")
    if not isinstance(source, dict):
        fail("file manifest source must be an object")
    if source.get("repository") != "aevespers2/Misc" or source.get("commit") != FROZEN_SOURCE_COMMIT:
        fail("file manifest is not bound to the approved frozen source")
    if source.get("digest") != "git_blob_sha1" or source.get("historical_after_source_change") is not True:
        fail("file manifest source semantics are incomplete")

    completeness = manifest.get("completeness")
    if not isinstance(completeness, dict):
        fail("file manifest completeness must be an object")
    for field in ("expected", "recorded", "unique"):
        if completeness.get(field) != len(EXPECTED_FROZEN_SOURCE_PATHS):
            fail(f"file manifest completeness mismatch: {field}")
    if completeness.get("unclassified") != [] or completeness.get("successor_rebind_required") is not True:
        fail("file manifest must have no unclassified paths and require successor rebinding")
    expected_excluded = {
        "phantomblock/docs/file-disposition-manifest.md",
        MANIFEST_PATH,
    }
    excluded = completeness.get("excluded_generated")
    if not isinstance(excluded, list) or set(excluded) != expected_excluded:
        fail("file manifest generated-artifact exclusion is incomplete")

    field_order = manifest.get("record_field_order")
    expected_fields = ["path", "git_blob_sha1", "component_ids", "evidence_class", "sensitivity_class", "limitation_refs"]
    if field_order != expected_fields:
        fail("file manifest record field order is unsupported")

    defaults = manifest.get("record_defaults")
    if not isinstance(defaults, dict):
        fail("file manifest defaults must be an object")
    expected_defaults = {
        "current_disposition": "REMAIN_IN_INCUBATION_PENDING_ARCHITECT",
        "proposed_target_or_archive_path": None,
        "semantic_owner": "VACANT",
        "interface_owner": "VACANT",
        "correction_route": "SUPERSEDE_BY_REVIEWED_PULL_REQUEST_BOUND_TO_EXACT_SOURCE_AND_RECORD_IN_CHANGELOG",
        "rollback_treatment": "RESTORE_RECORDED_BLOB_FROM_FROZEN_SOURCE_PRESERVE_HISTORY_AND_DO_NOT_REVIVE_REVOKED_WITHDRAWN_OR_SUPERSEDED_AUTHORITY",
    }
    if defaults != expected_defaults:
        fail("file manifest defaults widen or obscure the fail-closed disposition")

    denials = manifest.get("authority_denials")
    if not isinstance(denials, dict) or not denials or any(value is not True for value in denials.values()):
        fail("every file-manifest authority denial must remain true")

    limitations = manifest.get("limitations")
    if not isinstance(limitations, dict) or set(limitations) != {f"L{i:02d}" for i in range(1, 12)}:
        fail("file manifest limitation catalog is incomplete")

    records = manifest.get("records")
    if not isinstance(records, list) or len(records) != len(EXPECTED_FROZEN_SOURCE_PATHS):
        fail("file manifest record count is incomplete")
    seen: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, list) or len(record) != len(expected_fields):
            fail(f"file manifest record {index} has an invalid shape")
        path, blob, components, evidence, sensitivity, limitation_refs = record
        if not isinstance(path, str) or not path or path in seen:
            fail(f"file manifest record {index} has a missing or duplicate path")
        seen.add(path)
        if not isinstance(blob, str) or not SHA1_RE.fullmatch(blob):
            fail(f"file manifest record {path} has an invalid Git blob SHA-1")
        if not isinstance(components, list) or not components or any(not isinstance(c, str) or not COMPONENT_RE.fullmatch(c) for c in components):
            fail(f"file manifest record {path} has invalid component IDs")
        if not isinstance(evidence, str) or not evidence or not isinstance(sensitivity, str) or not sensitivity:
            fail(f"file manifest record {path} lacks evidence or sensitivity classification")
        if not isinstance(limitation_refs, list) or not limitation_refs or any(ref not in limitations for ref in limitation_refs):
            fail(f"file manifest record {path} has invalid limitation references")
    if seen != EXPECTED_FROZEN_SOURCE_PATHS:
        missing = sorted(EXPECTED_FROZEN_SOURCE_PATHS - seen)
        extra = sorted(seen - EXPECTED_FROZEN_SOURCE_PATHS)
        fail(f"file manifest path set mismatch; missing={missing}, extra={extra}")

    fysa = manifest.get("fysa_120")
    if not isinstance(fysa, dict) or "017-F" not in str(fysa.get("proposed_refinement", "")):
        fail("file manifest lacks the proposed exact-generation provenance capability")
    return {"records": len(records), "source_commit": FROZEN_SOURCE_COMMIT}


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
        MANIFEST_STATUS,
        FROZEN_SOURCE_COMMIT,
        "017-F",
    ):
        if phrase not in combined:
            fail(f"controlled planning documents lack required concept: {phrase}")

    readme = text(root, "README.md")
    for route in REQUIRED_ROUTES:
        if route not in readme:
            fail(f"README front door is missing route: {route}")

    nav = text(root, "phantomblock/mkdocs.yml")
    for page in (
        "incubation-status.md",
        "onboarding.md",
        "developer-guide.md",
        "architecture.md",
        "file-disposition-manifest.md",
        "file-disposition-manifest-v1.json",
    ):
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
    manifest = validate_file_manifest(root)
    validate_planning_alignment(root)
    validate_authority_boundary(root)
    return {
        "disposition": "DOCUMENTATION_CANDIDATE_STRUCTURALLY_VALID",
        "required_files": len(REQUIRED_FILES),
        "markdown_files": len(markdown_files(root)),
        "internal_links_checked": links,
        "mermaid_diagrams_checked": diagrams,
        "frozen_source_records": manifest["records"],
        "frozen_source_commit": manifest["source_commit"],
        "successor_rebind_required": True,
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
