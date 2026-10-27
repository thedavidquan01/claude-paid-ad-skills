#!/usr/bin/env bash
# Install the paid ads skills for Claude Code (and optionally Cursor).
#
# Usage:
#   ./install.sh                  copy skills into ~/.claude/skills
#   ./install.sh --cursor         also copy into ~/.cursor/skills
#   ./install.sh --project DIR    copy into DIR/.claude/skills instead of your home folder
#   ./install.sh --dry-run        show what would happen, change nothing
#
# Safe to run again. Skills that are already up to date are skipped.
# A skill folder that differs is moved to a skills-backup folder before it is replaced.
# Nothing outside the target skills folders is touched.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SCRIPT_DIR/skills"
CURSOR=0
DRY=0
BASE="$HOME"

while [ $# -gt 0 ]; do
  case "$1" in
    --cursor) CURSOR=1 ;;
    --dry-run) DRY=1 ;;
    --project)
      shift
      [ $# -gt 0 ] || { echo "Error: --project needs a folder." >&2; exit 1; }
      [ -d "$1" ] || { echo "Error: folder not found: $1" >&2; exit 1; }
      BASE="$(cd "$1" && pwd)"
      ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "Error: unknown option: $1" >&2; exit 1 ;;
  esac
  shift
done

[ -d "$SRC" ] || { echo "Error: skills folder not found next to install.sh." >&2; exit 1; }

run() {
  if [ "$DRY" -eq 1 ]; then echo "  (dry run) $*"; else "$@"; fi
}

install_to() {
  local dest="$1"
  echo "Installing into $dest"
  run mkdir -p "$dest"
  local stamp
  stamp="$(date +%Y%m%d-%H%M%S)"
  for skill in "$SRC"/*/; do
    skill="${skill%/}"
    local name
    name="$(basename "$skill")"
    [ -f "$skill/SKILL.md" ] || continue
    local target="$dest/$name"
    if [ -d "$target" ]; then
      if diff -rq "$skill" "$target" >/dev/null 2>&1; then
        echo "  $name: up to date, skipped"
        continue
      fi
      local backup="$dest-backup/$name-$stamp"
      echo "  $name: changed, backing up your version to $backup"
      run mkdir -p "$dest-backup"
      run mv "$target" "$backup"
    else
      echo "  $name: new"
    fi
    run cp -R "$skill" "$target"
  done
}

install_to "$BASE/.claude/skills"
if [ "$CURSOR" -eq 1 ]; then
  install_to "$BASE/.cursor/skills"
fi

echo "Done. Restart Claude Code or Cursor, then type /skills (Claude Code) or / (Cursor) to check they loaded."
