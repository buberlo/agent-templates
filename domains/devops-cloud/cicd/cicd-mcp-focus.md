---
id: cicd-mcp-focus
title: "CI/CD: MCP/Skill-Fokus"
domain: devops-cloud
category: cicd
tags:
  - cicd
  - mcp
  - github-actions
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: GitHub Official MCP
    install: "https://github.com/github/github-mcp-server"
    version_notes: "Actions, PRs, Workflow-Runs"
  - name: gh
    install: "https://cli.github.com"
    version_notes: "Ergänzung wenn MCP read-only reicht"
inputs:
  - "Repo und fehlgeschlagene Workflow-Run-ID"
  - "Skill-Schritte für Lint/Test/Deploy"
outputs:
  - "Skill↔MCP-Matrix für CI"
  - "Root-Cause-Notiz mit Log-Auszug"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

CI/CD-Aufgaben über **GitHub MCP** und **gh** orchestrieren: Failed Runs lesen, Logs analysieren, Fixes als PR — Writes nur nach Freigabe.

## Wann nutzen

- Agent soll Actions-Logs und PR-Kontext ohne manuelles UI.
- Team dokumentiert, welcher Skill-Schritt welches MCP-Tool nutzt.

**Wann nicht:** Wenn nur lokaler `act`-Test nötig ist ohne Remote — dann `coding-github-actions-ci-pipeline`.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub Official MCP | Runs, PRs | Strukturierte API |
| gh CLI | Logs/Fallback | `gh run view --log-failed` |
| Skill-CI | Ablauf | Repro, Fix, Verify |

## System-Prompt / Instruktionen

```text
MCP/Skill focus for CI/CD (devops-cloud/cicd).

Map each skill step: discover workflows | fetch failed run | reproduce locally | propose yaml fix | open PR.
Use GitHub MCP for read: workflows, runs, check suites, PR files.
Use gh for large logs when MCP truncates: gh run view <id> --log-failed.

Never merge or approve PRs without user approval.
Never paste secrets from workflow logs; redact tokens and URLs with credentials.
Prefer read-only MCP tools; restrict write tools in Hermes/Cursor policy.

Skill verify: after yaml change, reference act or pending Actions run as DoD.
CircleCI/Buildkite MCP only if listed in required_tools for that session.
Document which tool answered each question (MCP vs gh).
One MCP for GitHub; do not duplicate with third-party GitHub mirrors.
```

## Arbeitsablauf

1. Skill-Matrix: Schritt → MCP-Tool / gh-Kommando.
2. MCP: Workflow-Liste und letzte Runs auf `main` und PR-Branch.
3. Fehl-Run-ID notieren; parallel `gh run view <id> --json conclusion,jobs`.
4. Log-Auszug (Fehlerblock) ins Ticket; Secrets redigieren.
5. Lokalen Repro-Befehl aus Workflow extrahieren.
6. Fix-Entwurf als Diff; MCP/Skill Write nur nach Freigabe.
7. Nach Push: Run beobachten; Matrix aktualisieren.

## Qualitätskriterien / Definition of Done

- [ ] Failed Run mit Job+Step identifiziert
- [ ] Skill↔MCP-Matrix für den Task vollständig
- [ ] Keine Secrets in Chat oder PR-Beschreibung

## Sicherheit & Freigaben

- Pipeline-Secrets nie in den Chat spiegeln.
- Write-Tools (PR merge, workflow_dispatch) nur mit Freigabe.
- Fine-grained PAT auf nötige Repos beschränken.

## Fallstricke

- MCP-Log-Größe truncated — gh CLI als Fallback.
- Zwei GitHub-MCPs parallel — doppelte Tool-Schemas, langsamer Agent.
- `workflow_dispatch` aus Agent ohne Policy — versehentlicher Prod-Deploy.
- Fork-PR-Kontext: MCP sieht andere Permissions als Maintainer-Branch.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Letzten roten CI-Run auf PR #88 analysieren.
- **Input:** Repo `acme/api`, Run `20112233`.
- **Prompt:**

```text
Use GitHub MCP read tools for run 20112233; supplement with gh log-failed; no writes.
```

- **Erwartetes Ergebnis:**

```text
Matrix: step2=search_workflow_runs, step3=gh run view --log-failed
Root cause: pytest collection error in tests/integration/
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Skill definieren für „grün vor Merge“.
- **Input:** Branch protection verlangt `ci / test`.
- **Prompt:**

```text
Write 5-step skill mapping MCP reads and local verify; approval before gh pr merge.
```

- **Erwartetes Ergebnis:**

```text
Skill steps 1-4 read-only; step5 merge blocked until user types APPROVE
Check name documented: ci / test
```