---
id: context-token-management-workflow
title: "Kontext- und Token-Management"
domain: ki-ops
category: context-token-management
tags:
  - context
  - ki-ops
  - tokens
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: MCP tool filtering
    install: "Hermes include/exclude, OpenClaw tool policy"
    version_notes: "Vor Session starten"
inputs:
  - "Modell-Kontextlimit und aktive MCP-Liste"
  - "Aufgabenprofil (read/write/browser)"
outputs:
  - "Token-Budget-Plan"
  - "Empfohlene MCP-Deaktivierungen"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Kontextbudget planen**: MCP-Overhead messen, Tools deaktivieren, progressive disclosure — damit Aufgaben nicht an leerem Fenster scheitern.

## Wann nutzen

- Vor großen Sessions mit vielen MCPs.
- Nach „Kontext voll“-Fehlern.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| MCP include/exclude | Schneiden | Hermes |
| Skills lazy load | Text | OpenClaw |
| CLI statt MCP | Spart Tokens | Playwright/gh |

## System-Prompt / Instruktionen

```text
Role: context budget engineer (ki-ops/context-token-management).
Mission: Produce trim plan before task starts; prefer CLI over heavy snapshot MCP when equivalent.

Inventory: list each enabled MCP estimate schema overhead high medium low from docs or prior measure.
Browser trio playwright devtools firecrawl browserbase—pick at most one interact one read.
Measure anecdote cite 67k mcp overhead reddit claudeai when user has 15+ mcps enabled.
Progressive: start session read-only tools only add write mcp when user approves action class.
Summarize: rolling summary of long threads each N turns keep decisions table outside chat body file.
Artifacts: large outputs write files reference path not paste megabyte json inline.
Model limit: if 200k context reserve 30% for answer and tools rest user content.
Handoff long research to separate subagent return executive summary 1500 tokens max.
Skills: enable single skill per task domain not entire clawhub bundle.
Token heavy rejected for pure extraction: suggest firecrawl markdown or curl.
Re-evaluate after task phase change disable unused mcps mid session if client allows.
Document final enabled set and estimated overhead in session header note.
```

## Arbeitsablauf

1. Kontextlimit und Modell notieren.
2. Aktive MCPs auflisten und grob klassifizieren.
3. Aufgabe in Phasen (read/plan/write) teilen.
4. Pro Phase Minimalliste empfehlen.
5. Schwere MCPs ersetzen (CLI, Datei-Handoff).
6. Rolling Summary-Datei anlegen.
7. Nach Aufgabe: Lessons ins Runbook.

## Qualitätskriterien / Definition of Done

- [ ] ≤3 MCPs für erste Phase empfohlen
- [ ] Schwere Browser-Tools begründet oder abgelehnt
- [ ] Artefakte ausgelagert statt inline

## Sicherheit & Freigaben

- Keine API-Keys zum „Kontext sparen“ in Klartext-Dateien.

## Fallstricke

- Alle MCPs „für später“ an → kein Platz für Aufgabe.
- Riesige Tool-Outputs ungekürzt in Thread.
- Skill + MCP Duplikat für gleiches Tool.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 20 MCPs aktiv
- **Input:** SQL-Report schreiben
- **Prompt:**

```text
Trim for motherduck + filesystem only.
```

- **Erwartetes Ergebnis:**

```text
trim plan | browser mcps off | motherduck on
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Webseite Text
- **Input:** Playwright MCP default
- **Prompt:**

```text
Extract article text one url.
```

- **Erwartetes Ergebnis:**

```text
recommend search/scrape not playwright snapshots
```