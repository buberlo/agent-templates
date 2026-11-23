---
id: coding-github-actions-ci-pipeline
domain: devops-cloud
title: "CI-Pipeline mit GitHub Actions"
category: cicd
tags:
  - github-actions
  - ci
  - pytest
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: github-actions
    install: ".github/workflows"
    version_notes: "ubuntu-latest runners"
  - name: act
    install: "brew/apt: nektos/act"
    version_notes: "Lokaler Dry-Run"
inputs:
  - "Repo URL"
  - "Stack (Python/Node)"
  - "Test-Befehl"
outputs:
  - "Workflow YAML"
  - "Status-Badge"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Automatisierte Tests und Lint bei jedem Push/PR einführen oder reparieren.

## Wann nutzen

- Neues Repo ohne CI, flaky Pipeline.
- Nicht für komplette GitLab-Migration in einem Schritt.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| GitHub Actions | CI | Native Integration |
| act | lokal testen | Schnelles Feedback |
| codecov | optional Coverage | Trend sichtbar |

## System-Prompt / Instruktionen

```text
Add or fix GitHub Actions workflow for lint and test.
Cache dependencies; pin action SHAs for supply chain.
Separate jobs: lint, test, build artifact if applicable.
Document required secrets; never print them in logs.
```

## Arbeitsablauf

1. Bestehende Workflows inventarisieren.
2. Matrix für OS/Version nur wenn nötig.
3. `act pull_request` lokal.
4. PR mit Workflow; grüner Lauf.
5. Branch protection empfehlen.

## Qualitätskriterien / Definition of Done

- [ ] PR und main getrennte Trigger
- [ ] Mittlere Laufzeit unter 10 min
- [ ] Keine hardcodierten Tokens

## Sicherheit & Freigaben

- GITHUB_TOKEN least scope.
- Fork-PRs ohne Secrets ausführen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Python-Repo, `pytest -q`
**Erwartetes Ergebnis:** `.github/workflows/ci.yml` grün
