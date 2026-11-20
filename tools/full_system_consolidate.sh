#!/usr/bin/env bash
set -euo pipefail

# Default mode: verify native Take-5 authority without creating any duplicate.
# Full mirror restoration is an explicit historical recovery operation only.
if [[ "${1:-}" != "--restore-full-mirror" ]]; then
  if [[ $# -gt 0 ]]; then
    echo "Usage: tools/full_system_consolidate.sh [--restore-full-mirror]" >&2
    exit 2
  fi
  exec python tools/check_full_system_authority.py
fi
shift
if [[ $# -ne 0 ]]; then
  echo "Unexpected restoration arguments" >&2
  exit 2
fi

ROOT="$(pwd)"
OWNER="thytabakman-jpg"
DEST="$ROOT/dump/full-system-sources"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$DEST"
: > "$DEST/SOURCE_HEADS.tsv"

for name in Take-3 Take-4 Take-5; do
  src="$TMP/$name"
  # Take-3 and Take-4 have finished as standalone experiments. Restore their
  # exact final experiment trees even after the default branches are retired.
  case "$name" in
    Take-3) snapshot="d85bef9ae256c3b59b88ae4aff3d2eeb41fcc3a7" ;;
    Take-4) snapshot="a93f3801555b75c88b180ec08bc136041662c785" ;;
    *) snapshot="" ;;
  esac
  if [[ -n "$snapshot" ]]; then
    git init --quiet "$src"
    git -C "$src" fetch --quiet --depth=1 "https://github.com/$OWNER/$name.git" "$snapshot"
    git -C "$src" checkout --quiet --detach FETCH_HEAD
    [[ "$(git -C "$src" rev-parse HEAD)" == "$snapshot" ]]
  else
    git clone --depth=1 "https://github.com/$OWNER/$name.git" "$src"
  fi
  head="$(git -C "$src" rev-parse HEAD)"
  rm -rf "$DEST/$name"
  mkdir -p "$DEST/$name"
  rsync -a --exclude='.git' "$src/" "$DEST/$name/"
  printf '%s\t%s\n' "$name" "$head" >> "$DEST/SOURCE_HEADS.tsv"
done

python tools/build_full_system_manifest.py
TAKE2_AUTHORITY_MODE=snapshot python tools/check_full_system_authority.py
echo "Historical mirror restored explicitly; native authority verification remains the default."
