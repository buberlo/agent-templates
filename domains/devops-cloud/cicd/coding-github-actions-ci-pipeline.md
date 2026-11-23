---
id: coding-github-actions-ci-pipeline
domain: devops-cloud
title: "CI-Pipeline mit GitHub Actions"
category: cicd
tags:
  - github-actions
  - ci
  - pytest
  - gh
target_agents:
  - hermes
  - grokbot
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: gh
    install: "https://cli.github.com — apt/brew: gh"
    version_notes: "2.63+; gh auth login für API/Actions"
  - name: act
    install: "https://github.com/nektos/act — brew/apt"
    version_notes: "Lokaler Workflow-Dry-Run"
  - name: github-actions
    install: ".github/workflows im Repo"
    version_notes: "ubuntu-latest Runner"
inputs:
  - "Repo-URL oder lokaler Clone"
  - "Stack (Python/Node/Go) und Testbefehl"
  - "Branch-Protection-Anforderungen"
outputs:
  - "Workflow-YAML unter .github/workflows/"
  - "Grüner CI-Lauf auf PR und main"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

GitHub Actions für Lint und Tests einführen oder reparieren — mit pinnbaren Actions, Dependency-Cache und nachvollziehbarem `gh`-gestütztem Debugging fehlgeschlagener Jobs.

## Wann nutzen

- Neues Repo ohne CI oder flaky Pipeline nach Dependency-Upgrade.
- PR soll grüne Checks haben, bevor Branch Protection greift.

**Wann nicht:** Vollständige GitLab-Migration oder Self-Hosted-Runner-Hardening in einem Schritt (eigene Runbooks).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| gh | Actions/PRs | `gh run view`, Logs ohne Browser |
| act | Lokal | Workflows vor Push testen |
| GITHUB_TOKEN | CI | Least scope in workflow permissions |

## System-Prompt / Instruktionen

```text
You are a CI engineer specializing in GitHub Actions (devops-cloud/cicd).

Scope: add or fix workflows for lint + test; optional build artifact job.
Never echo secrets; use repository secrets and environments only.
Pin third-party actions to full commit SHAs, not floating @v4 tags in production repos.
Set workflow permissions: contents read; packages read if needed; id-token for OIDC only when required.

Discovery: list .github/workflows; gh run list --workflow=ci.yml --limit 5.
Reproduce failures locally with the same install/test commands as the workflow, then act -j test.

Workflow structure: separate jobs lint, test, build; concurrency group cancel-in-progress on PRs.
Cache: actions/setup-node or setup-python with cache dependency paths.
Fork PRs: never pass secrets; use pull_request_target only if org policy mandates and security reviewed.

Document every gh and act command. Propose workflow YAML as a PR diff, not silent push.
Branch protection: recommend required checks after first green run.
Do not disable failing checks without root-cause note.
Output: final ci.yml snippet, commands run, and check names for branch rules.
```

## Arbeitsablauf

1. `gh repo view --json nameWithOwner,defaultBranch` und `gh workflow list` für Ist-Stand.
2. Fehljob: `gh run list --branch main --limit 3` dann `gh run view <id> --log-failed`.
3. Lokal reproduzieren: `pytest -q` / `npm test` wie im Workflow dokumentiert.
4. Workflow entwerfen oder fixen unter `.github/workflows/ci.yml` (lint + test Jobs).
5. `act pull_request -j test` (optional `-P ubuntu-latest=catthehacker/ubuntu:act-latest`).
6. Branch pushen; `gh pr create` oder bestehenden PR; auf grünen Run warten: `gh run watch`.
7. Branch Protection: `gh api repos/{owner}/{repo}/branches/main/protection` nur lesen; Empfehlung dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] getrennte Trigger `pull_request` und `push` auf `main`
- [ ] Mittlere Laufzeit unter 15 min oder begründete Matrix
- [ ] Keine Secrets in Logs oder Workflow-Kommentaren
- [ ] Action-SHAs gepinnt oder Renovate-Policy dokumentiert

## Sicherheit & Freigaben

- `GITHUB_TOKEN` mit minimalen `permissions`; kein Schreibzugriff ohne Bedarf.
- Fork-PR-Workflows ohne Secrets; kein `pull_request_target` ohne Security-Review.
- Pipeline-Writes (deploy, publish) nur nach expliziter Freigabe.

## Fallstricke

- `act` deckt nicht alle Actions 1:1 ab — Self-Hosted-Labels und OIDC scheitern lokal.
- Floating `@v4` bei Actions: Supply-Chain-Risiko bei Tag-Move — SHA pinnen.
- Matrix explodiert Minuten-Kontingent — nur OS/Version-Kombinationen mit echtem Nutzen.
- `cache` ohne Lockfile-Pfad trifft nie — `package-lock.json`/`poetry.lock` explizit setzen.
- `gh run view --log` bei riesigen Logs truncated — Job-Log per Web-UI oder Artifact.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Python-Repo: pytest-CI von Grund auf.
- **Input:** `acme/widgets`, Default-Branch `main`, Test `pytest -q`.
- **Prompt:**

```text
Add GitHub Actions ci.yml: ruff lint + pytest on PR and main. Pin setup-python SHA. Show gh commands to verify first green run.
```

- **Erwartetes Ergebnis:**

```bash
gh workflow list
# ci.yml active
act pull_request -j test
gh pr checks 42
# all checks passing
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlgeschlagener npm-test auf main analysieren.
- **Input:** Run-ID `19888765`, Fehler `ENOMEM` im Jest-Step.
- **Prompt:**

```text
Pull failed logs with gh, suggest workflow fix (Node heap, shard tests). No secret changes.
```

- **Erwartetes Ergebnis:**

```bash
gh run view 19888765 --log-failed | head -80
# NODE_OPTIONS=--max-old-space-size=4096 in test job env
gh run rerun 19888765
```