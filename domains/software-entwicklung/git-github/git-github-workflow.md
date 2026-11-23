---
id: git-github-workflow
title: "Git und GitHub"
domain: software-entwicklung
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
  - "PR/Issue-Update oder Diff-Zusammenfassung"
  - "Gh-Befehlsprotokoll"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

GitHub-Workflows mit **gh** und **git**: Branches, PRs, Reviews, Issues — Writes nur nach Freigabe.

## Wann nutzen

- PR erstellen, Review-Kommentare, Issue triagieren.
- CI-Status vor Merge prüfen.

**Wann nicht:** GitLab/Bitbucket (andere Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| gh | GitHub API | PR, issue, run |
| git | Lokal | commit, diff |
| GitHub MCP | optional | Read-only parallel |

## System-Prompt / Instruktionen

```text
Git/GitHub workflow (software-entwicklung/git-github).

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

## Arbeitsablauf

1. `gh auth status` und `git status`.
2. `git fetch origin && git switch -c fix/123-issue main`.
3. Änderungen commit: `git add <files> && git commit -m "fix: ..."`.
4. `git push -u origin fix/123-issue`.
5. `gh pr create --fill` oder mit Body-Template.
6. `gh pr checks` warten.
7. Nach MERGE_APPROVE: `gh pr merge 42 --squash`.

## Qualitätskriterien / Definition of Done

- [ ] Checks grün oder Ausnahme dokumentiert
- [ ] PR-Beschreibung mit Testplan
- [ ] Kein Force-Push auf main

## Sicherheit & Freigaben

- PAT nicht im Chat; fine-grained wo möglich.
- Merge und secret writes mit Freigabe.

## Fallstricke

- gh auf falsches Repo (submodule) — cwd prüfen.
- PR gegen veraltete main — erst rebase/fetch.
- --fill committet geheime Dateien — git diff vor push.
- gh pr merge ohne required checks — Branch protection.
- Co-authored-by ohne Zustimmung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** PR für Fix #77.
- **Input:** Branch `fix/77-readme`.
- **Prompt:**

```text
Push branch, draft PR, list checks; no merge.
```

- **Erwartetes Ergebnis:**

```bash
git push -u origin fix/77-readme
gh pr create --draft --title "fix: readme typo" --body "Fixes #77"
gh pr checks
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Review-Kommentar only.
- **Input:** PR 88.
- **Prompt:**

```text
gh pr diff 88 summary; post review comment draft, do not submit approve.
```

- **Erwartetes Ergebnis:**

```bash
gh pr diff 88
gh pr review 88 --comment --body "Consider extracting helper..."
# draft only unless user confirms
```