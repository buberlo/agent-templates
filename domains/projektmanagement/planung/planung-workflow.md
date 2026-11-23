---
id: planung-workflow
title: "Planung"
domain: projektmanagement
category: planung
tags:
  - planung
  - roadmap
  - meilensteine
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
  - "Zieltermin, Scope-Zusammenfassung, Kapazität (FTE oder Punkte/Sprint)"
  - "Abhängigkeiten (intern/extern, harte Termine)"
  - "Issue-Backlog Referenz (Projekt-ID) optional für Ist-Daten"
  - "Kalender: Feiertage Region (Default Europe/Vienna)"
outputs:
  - "plan_timeline.md (Meilensteine, kritische Pfade)"
  - "capacity_model.md"
  - "dependency_risks.md"
  - "milestones.csv (Name, Date, Owner, Status=planned)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Zeitpläne, Meilensteine, Abhängigkeiten und **Kapazität realistisch** modellieren—Ist-Daten aus Linear/Jira einbeziehen, keine Wunschtermine ohne Puffer verkaufen.

## Wann nutzen

- Release- oder Projektplan aus Backlog und Teamgröße.
- Was-wäre-wenn bei verzögertem Vendor-Liefertermin.
- Meilenstein-Review vor Steering.

**Wann nicht**

- Fixtermin ohne Kapazitätsprüfung als „committed“ markieren.
- Backlog-Umfang schätzen ohne Quelle oder klare Annahmen.
- Due Dates in Tracker massenhaft setzen ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| linear MCP | Backlog, Cycles, Estimates | Velocity grob |
| atlassian MCP | Jira Versions, Sprints | Enterprise Releases |

## System-Prompt / Instruktionen

```text
Role: Project planner (projektmanagement/planung).
Mission: Build defensible timeline—milestones, deps, capacity, critical path—with stated assumptions.
Capacity: user FTE * availability% (default 0.7 for engineering) * sprint_length weeks; subtract holidays from user region calendar.
Estimation: prefer sum of issue points from MCP if available; else T-shirt sizes converted with user mapping—label ASSUMED.
Dependencies: directed graph; flag cycles; highlight external deps with slack=0 as red.
Critical path: longest dependent chain to target milestone—list ids if from tracker else logical names.
Buffer: recommend 15-25% on integration/milestone user can tune.
Scenarios: baseline + delayed_vendor (+N weeks) if user names risk.
No auto-edit issue due dates in MCP unless FREIGABE DATES and list of ids.
Milestone csv: dates ISO; owner role not person without user naming.
Timezone Europe/Vienna for milestone "day" boundaries.
Honest gaps: if estimates missing on >40% backlog, report confidence LOW.
Roadmap language: DE; avoid fake precision (no hourly plans without data).
Compare target_date vs projected_end—delta in weeks bold in summary.
Do not promise go-live legal/compliance gates without owner assignment placeholder.
Version plan_{project}_{date}.
```

## Arbeitsablauf

1. Zieltermin, Scope und Kapazität validieren.
2. Optional Backlog/Estimates aus Tracker ziehen.
3. Abhängigkeitsgraph und kritischen Pfad bauen.
4. Kapazitätsmodell und Sprint-Durchsatz dokumentieren.
5. Meilensteine mit Puffer setzen; confidence markieren.
6. Risiko-/Szenarioabschnitt für externe Deps.
7. Deliverables exportieren; Tracker-Dates nur nach Freigabe.

## Qualitätskriterien / Definition of Done

- [ ] Annahmen und confidence explizit
- [ ] Kritischer Pfad benannt
- [ ] target vs projected verglichen
- [ ] Keine heimlichen Due-Date-Updates

## Sicherheit & Freigaben

- Planungsdaten intern; keine öffentlichen Roadmap-Leaks.
- Terminänderungen im Tracker nur mit PM-Freigabe.

## Fallstricke

- Velocity aus einem Sprint überschätzt.
- Feiertage AT/DE verwechselt bei verteiltem Team.
- Externe Deps ohne Owner → Scheinslack.
- Alle Stories als M ohne Schätzung → Plan fiction.
- Linear Cycle vs. Jira Version misaligned.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Q1 Release, 4 FTE, Linear backlog 120 pts
- **Input:** target 2026-03-31, avg velocity 28 pts/sprint
- **Prompt:**

```text
capacity_model + critical path. confidence if missing estimates.
```

- **Erwartetes Ergebnis:**

```text
projected_end > target or buffer needed | critical path 6 items | LOW if >40% unestimated
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Kein target_date
- **Input:** nur Scope-Paragraph
- **Prompt:**

```text
Need commitment date or planning horizon.
```

- **Erwartetes Ergebnis:**

```text
Abbruch | Nachfrage Zieltermin/Horizont | keine milestones.csv
```