---
id: appsec-sast-workflow
title: "AppSec und SAST"
domain: security
category: appsec-sast
tags:
  - sast
  - appsec
  - semgrep
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: semgrep
    install: "pip install semgrep"
    version_notes: "Community rules"
  - name: npm audit / pip-audit
    install: "dependency scan"
    version_notes: "SCA"
  - name: gh
    install: "PR checks integration"
    version_notes: "optional"
inputs:
  - "Repo path und Sprachen"
  - "Policy (blocker vs warn)"
outputs:
  - "SAST report summary"
  - "Fix PR suggestions"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Static Analysis und Dependency-Scans in CI und lokal ausführen, Findings priorisieren und sichere Fixes vorschlagen.

## Wann nutzen

- Vor Release, nach Dependabot/Architektur-Wechsel.
- Security Champions Review.

**Wann nicht:** DAST/E2E-Pentest (pentest template).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| semgrep | SAST | custom rules |
| pip-audit/npm audit | SCA | CVEs |
| SARIF | CI | upload artifact |

## System-Prompt / Instruktionen

```text
AppSec SAST workflow (security/appsec-sast).

Run semgrep with org ruleset: semgrep scan --config auto or --config p/ci.
Dependency: pip-audit -r requirements.txt; npm audit --production.
Triage: OWASP category, reachability, exploitability; false positive reasoning required to dismiss.
Fix: prefer parameterized queries, encoder libraries, not regex HTML sanitize alone.
Never disable rules globally without ticket and expiry.
SARIF output for GitHub code scanning when user uses Actions.
No secret values in SARIF paths; redact filenames if sensitive.
Block merge on CRITICAL reachable only per user policy statement.
Document command exit codes and paths scanned.
Do not claim CVE not affected without version proof from lockfile.
```

## Arbeitsablauf

1. Sprachen/Monorepo-Pfade identifizieren.
2. `semgrep scan --config auto --json -o semgrep.json`.
3. `pip-audit` / `npm audit --json` parallel.
4. Findings dedupe und severity sortieren.
5. Fix-Vorschläge pro CRITICAL/HIGH.
6. Tests nach Fix laufen lassen.
7. Optional `gh pr create` mit SARIF summary.

## Qualitätskriterien / Definition of Done

- [ ] Scan-Befehle dokumentiert
- [ ] CRITICAL triagiert (fix oder Ausnahme-Ticket)
- [ ] Keine Rule-Disables ohne Begründung

## Sicherheit & Freigaben

- SARIF kann Pfade preisgeben — Scope beachten.
- Prod-Daten in repro fixtures vermeiden.

## Fallstricke

- semgrep auto-only für Enterprise langsam.
- npm audit devDeps noise.
- False positive SQLi in ORM.
- Fix bricht Tests — characterization fehlt.
- SARIF riesig in PR comment.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Python API semgrep.
- **Input:** `src/`.
- **Prompt:**

```text
semgrep scan; summarize HIGH; suggest fix for SQL concat if any.
```

- **Erwartetes Ergebnis:**

```bash
semgrep scan --config p/ci --json -o out.json
# 0 critical after parameterized query fix
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** npm audit production.
- **Input:** web app.
- **Prompt:**

```text
npm audit --production; list fixable via npm audit fix --dry-run.
```

- **Erwartetes Ergebnis:**

```bash
npm audit --production
npm audit fix --dry-run
```