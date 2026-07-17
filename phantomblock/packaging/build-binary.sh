#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONHASHSEED=0
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(git log -1 --pretty=%ct 2>/dev/null || date +%s)}"
python -m pip install --disable-pip-version-check -e '.[build]'
rm -rf build dist
pyinstaller --clean --noconfirm packaging/phantomblock.spec
sha256sum dist/phantomblock > dist/phantomblock.sha256
cyclonedx-py environment --output-format JSON --output-file dist/phantomblock.cdx.json
printf '%s\n' "Built dist/phantomblock with checksum and CycloneDX SBOM. Sign in the release pipeline."
