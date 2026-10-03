#!/usr/bin/env bash
# Clean-clone reproducibility test (MASTER_PLAN §6). Usage: bash scripts/repro_clone.sh [ep-001] [/short/path]
# Clones this repo into a SHORT path (espeak-ng data-path buffer limit, see reports/pilot/reproducibility.md), reuses local models,
# builds the episode and compares it with the current build via scripts/repro_check.py. Takes ~10 min on 4 vCPU.
set -euo pipefail
EP="${1:-ep-001}"; R="${2:-/tmp/ytf-repro}"
SRC="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "$R"; mkdir -p "$R"
git clone -q "$SRC" "$R/c"
ln -s "$SRC/models" "$R/c/models"
cd "$R/c" && uv sync -q --frozen --extra dev
echo "== clean clone build $(date -u +%T) path=$R/c"
YTF_ROOT="$R/c" /usr/bin/time -v uv run ytf build "$EP" --workers 2 2>&1 | grep -E "^\[|Elapsed|Maximum resident"
echo "== repro check"
YTF_ROOT="$R/c" uv run python scripts/repro_check.py "$SRC/build/$EP/long" "$R/c/build/$EP/long" --frames 8
