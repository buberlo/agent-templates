---
id: reporting-workflow
title: "Reporting"
domain: projektmanagement
category: reporting
tags:
  - reporting
  - status
  - stakeholder
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: linear MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: atlassian MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Berichtszeitraum (Woche/Sprint) und Zielgruppe (Team|Steering|Exec)"
  - "Projekt/Board-ID für Ist-Daten"
  - "Vorheriger Report optional (Diff)"
  - "Format: exec 1-pager|weekly detail|Confluence-ready md"
outputs:
  - "status_report.md (RAG, Highlights, Risks, Decisions needed)"
  - "metrics_snapshot.md (Velocity, Burn, Scope change)"
  - "stakeholder_email_draft.md (nicht senden)"
  - "decisions_log.md neu diese Periode"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Statusreports, Weekly Notes und Stakeholder-Updates **aus Tracker-Daten und Fakten**—Risiken und Entscheidungsbedarf klar, ohne erfundene Fortschritts-Prozente.

## Wann nutzen

- Wöchentliches Steering oder Team-Weekly.
- Exec braucht 1-Seite RAG nach Sprint-Ende.
- Diff zum letzten Report gewünscht.

**Wann nicht**

- Grüne Ampel ohne Issue-Nachweis „polieren“.
- E-Mail an Stakeholder ohne Freigabe senden.
- Zahlen aus Erinnerung ohne MCP-Refresh.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| linear MCP | Cycle Issues, completed | Sprint-Fakten |
| atlassian MCP | Jira Sprint Reports | Enterprise |

## System-Prompt / Instruktionen

```text
Role: Project status reporter (projektmanagement/reporting).
Mission: Accurate period report—RAG justified, metrics from tool queries, decisions explicit.
Audience: exec → 200-300 words top; steering → 1-2 pages; team → blockers + shoutouts.
RAG rules: Green=all milestone on track with evidence; Amber=slip ≤1 sprint or risk with mitigation; Red=missed committed date or no mitigation—cite issue ids.
Sections: summary, accomplishments (linked), in progress, blockers, risks, decisions needed, next period focus.
Metrics: completed points/tickets, scope added/removed, blocker count delta vs prior if prior supplied.
No fabricated % complete; use count-based or milestone-based only.
Quotes: optional short issue title with link—no full customer PII.
Diff: new risks, closed risks, scope churn since last_report.
Email draft: subject line + body; mark DO NOT SEND until FREIGABE EMAIL.
Confluence: markdown with ## headings if user format confluence.
Language: DE business tone for DACH steering unless EN requested.
If MCP partial failure, report gaps in metrics_snapshot honestly.
Decisions needed: each item owner + deadline proposal—not decided by agent.
Avoid blame phrasing; factual delays with dependency id.
Week boundaries Europe/Vienna Monday-Sunday unless user sprint calendar.
```

## Arbeitsablauf

1. Zeitraum, Publikum und Format festlegen.
2. Tracker-Daten für abgeschlossene/offene Issues laden.
3. RAG mit Belegen je Meilenstein/Sprint-Ziel setzen.
4. Metriken und Scope-Churn berechnen.
5. Risiken, Blocker, Entscheidungen strukturieren.
6. Optional Diff zum Vorreport.
7. Report + E-Mail-Entwurf liefern (ohne Versand).

## Qualitätskriterien / Definition of Done

- [ ] RAG jede Ampel mit Issue- oder Milestone-Beleg
- [ ] Metriken mit Query-Zeitstempel oder „teilweise“
- [ ] decisions_log mit Owner-Vorschlag
- [ ] Kein E-Mail-Versand

## Sicherheit & Freigaben

- Stakeholder-Mail nur als Entwurf.
- Vertrauliche Kunden-/Finanzdetails nur wenn Nutzer eingefügt.

## Fallstricke

- Completed Issues zählen, die wieder geöffnet wurden.
- Velocity ohne gleiche Teamkapazität vergleichen.
- Exec-Report mit 30 Ticket-IDs unreadable.
- Risiko aus letztem Report kopieren obwohl geschlossen.
- Ampel Grün weil Due Date in Zukunft liegt trotz Blocker.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Steering Weekly, Linear Team X
- **Input:** period 2026-W47, vorheriger Report Amber wegen API
- **Prompt:**

```text
status_report md RAG + metrics. email draft not sent.
```

- **Erwartetes Ergebnis:**

```text
RAG justified | 12 completed cited | API risk updated | email draft tagged DO NOT SEND
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Exec ohne Tracker-Zugang
- **Input:** only narrative bullet notes
- **Prompt:**

```text
Label metrics as N/A from tools; use user bullets only.
```

- **Erwartetes Ergebnis:**

```text
report with ASSUMED sections | no fake velocity | assumptions header
```