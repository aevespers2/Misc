#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v mkosi >/dev/null || { echo "mkosi is required" >&2; exit 1; }
mkosi build
printf '%s\n' "Image built. Verify signatures, hashes, and boot policy before deployment."
