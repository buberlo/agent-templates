---
id: git-github-workflow
title: "Git and GitHub"
domain: software-development
category: git-github
tags:
  - git
  - github
  - gh
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gh
    install: "https://cli.github.com"
    version_notes: "gh auth login"
  - name: git
    install: "System"
    version_notes: "2.40+"
inputs:
  - "Repo, Branch, Issue/PR-Nummer"
  - "Scope read vs write"
outputs:
  - "PR/Issue-Update or Diff-Zusammenfassung"
  - "Gh-Befehlsprotokoll"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

GitHub workflows with **gh** and **git**: branches, PRs, reviews, issues — writes only after approval.

## When to use

- PR erstellen, Review-Kommentare, Issue triagieren.
- Check CI status before merge.

**When not:** GitLab/Bitbucket (other templates).

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| gh | GitHub API | PR, issue, run |
| git | Lokal | commit, diff |
| GitHub MCP | optional | Read-only parallel |

## System prompt

```text
Git/GitHub workflow (software-development/git-github).

Verify auth: gh auth status; repo: gh repo view --json nameWithOwner.
Read: gh pr view, gh issue view, gh pr diff, gh pr checks.
Branch: git fetch origin; git checkout -b feature/x from updated main.
Commit only files user scoped; no drive-by formatting.
PR create: gh pr create --title --body --draft unless user wants ready.
Never gh pr merge without explicit MERGE_APPROVE.
Never push --force to shared branches without user naming branch.
Review: gh pr review --comment only with approval for approve/request-changes.
Link issues: closing keyword in PR body only if user wants Fixes #n.
Secrets: never gh secret set without approval.
Rebase/merge policy: ask if unclear; default merge commit if org unknown.
Document every gh command in order.
```

## Workflow

1. `gh auth status` and `git status`.
2. `git fetch origin && git switch -c fix/123-issue main`.
3. Changes commit: `git add <files> && git commit -m "fix: ..."`.
4. `git push -u origin fix/123-issue`.
5. `gh pr create --fill` or with body template.
6. `gh pr checks` warten.
7. Nach MERGE_APPROVE: `gh pr merge 42 --squash`.

## Definition of done

- [ ] Checks green or documented exception
- [ ] PR description with test plan
- [ ] Kein Force-Push auf main

## Security

- PAT not in chat; Fine-grained where possible.
- Merge and secret writes with release.

## Pitfalls

- gh check for false repo (submodule) — cwd.
- PR gegen veraltete main — erst rebase/fetch.
- --fill committet geheime Files — git diff vor push.
- gh pr merge without required checks — Branch protection.
- Co-authored-by without Zustimmung.

## Basic examples

### Example 1 (Example data)

- **Task:** PR for Fix #77.
- **Input:** Branch `fix/77-readme`.
- **Prompt:**

```text
Push branch, draft PR, list checks; no merge.
```

- **Expected result:**

```bash
git push -u origin fix/77-readme
gh pr create --draft --title "fix: readme typo" --body "Fixes #77"
gh pr checks
```

### Example 2 (Example data)

- **Task:** Review-Kommentar only.
- **Input:** PR 88.
- **Prompt:**

```text
gh pr diff 88 summary; post review comment draft, do not submit approve.
```

- **Expected result:**

```bash
gh pr diff 88
gh pr review 88 --comment --body "Consider extracting helper..."
# draft only unless user confirms
```