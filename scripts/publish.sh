#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-claude-certified-associate-foundations}"
DESCRIPTION="Independent study guide for the Claude Certified Associate - Foundations certification"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required: https://cli.github.com/" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Authenticate first with: gh auth login" >&2
  exit 1
fi

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init -b main
fi

git add -A
if ! git diff --cached --quiet; then
  git commit -m "Build Claude Foundations study repository"
fi

OWNER="$(gh api user --jq .login)"
FULL_NAME="${OWNER}/${REPO_NAME}"

if gh repo view "${FULL_NAME}" >/dev/null 2>&1; then
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/${FULL_NAME}.git"
  fi
  git push -u origin "$(git branch --show-current)"
else
  gh repo create "${FULL_NAME}" \
    --public \
    --description "${DESCRIPTION}" \
    --source . \
    --remote origin \
    --push
fi

echo "Published: https://github.com/${FULL_NAME}"
echo "After the first documentation workflow succeeds, enable GitHub Pages with"
echo "Source: GitHub Actions, if it is not already enabled."
