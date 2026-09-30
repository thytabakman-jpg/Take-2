#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
OWNER="thytabakman-jpg"
DEST="$ROOT/dump/full-system-sources"
TMP="$RUNNER_TEMP/full-system-consolidation"

rm -rf "$TMP"
mkdir -p "$TMP" "$DEST"

: > "$DEST/SOURCE_HEADS.tsv"

for name in Take-3 Take-4 Take-5; do
  src="$TMP/$name"
  git clone --depth=1 "https://github.com/$OWNER/$name.git" "$src"
  head="$(git -C "$src" rev-parse HEAD)"
  rm -rf "$DEST/$name"
  mkdir -p "$DEST/$name"
  rsync -a --exclude='.git' "$src/" "$DEST/$name/"
  printf "%s\t%s\n" "$name" "$head" >> "$DEST/SOURCE_HEADS.tsv"
done

python tools/build_full_system_manifest.py
python tools/check_full_system_authority.py
