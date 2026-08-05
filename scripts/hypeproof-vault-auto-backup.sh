#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${HYPEPROOF_REPO:-$(cd "$SCRIPT_DIR/.." && pwd)}"
LOG_DIR="${HYPEPROOF_LOG_DIR:-${XDG_STATE_HOME:-$HOME/.local/state}/hypeproof}"
LOG_FILE="$LOG_DIR/hypeproof-vault-auto-backup.log"
LOCK_DIR="/tmp/hypeproof-vault-auto-backup.lock"
BACKUP_BRANCH="${HYPEPROOF_BACKUP_BRANCH:-vault-backup}"

mkdir -p "$LOG_DIR"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$*" >> "$LOG_FILE"
}

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  log "Skipped: another backup is running"
  exit 0
fi
trap 'rmdir "$LOCK_DIR"' EXIT

cd "$REPO"

branch="$(git branch --show-current)"
if [ -z "$branch" ]; then
  log "Skipped: detached HEAD"
  exit 0
fi

if [ "$branch" != "$BACKUP_BRANCH" ]; then
  log "Skipped: current branch $branch is not backup branch $BACKUP_BRANCH"
  exit 0
fi

if [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ] || [ -f .git/MERGE_HEAD ]; then
  log "Skipped: git rebase/merge in progress"
  exit 0
fi

git pull --rebase --autostash origin "$branch" >> "$LOG_FILE" 2>&1 || {
  log "Failed: pull --rebase --autostash origin $branch"
  exit 1
}

git add -A kids_edu_vault

if git diff --cached --quiet -- kids_edu_vault; then
  log "No vault changes on $branch"
  exit 0
fi

git commit -m "vault: auto backup $(date '+%Y-%m-%d %H:%M %Z')" >> "$LOG_FILE" 2>&1
git push origin "$branch" >> "$LOG_FILE" 2>&1
log "Backed up vault changes on $branch"
