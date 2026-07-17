from pathlib import Path

from phantomblock.core import sha256_file, verify_manifest
from phantomblock.isolation import DryRunSwitchAdapter


def test_sha256_and_manifest(tmp_path: Path) -> None:
    artifact = tmp_path / "firmware.bin"
    artifact.write_bytes(b"trusted")
    digest = sha256_file(artifact)
    manifest = tmp_path / "manifest.yml"
    manifest.write_text(f"artifacts:\n  - path: {artifact}\n    sha256: {digest}\n")
    findings = verify_manifest(manifest)
    assert findings[0].severity == "clean"


def test_manifest_mismatch_is_high(tmp_path: Path) -> None:
    artifact = tmp_path / "firmware.bin"
    artifact.write_bytes(b"changed")
    manifest = tmp_path / "manifest.yml"
    manifest.write_text(f"artifacts:\n  - path: {artifact}\n    sha256: {'0' * 64}\n")
    assert verify_manifest(manifest)[0].severity == "high"


def test_isolation_defaults_to_dry_run() -> None:
    result = DryRunSwitchAdapter().isolate("switch-1", "Gi1/0/7")
    assert result.applied is False
    assert result.action == "disable-port"
