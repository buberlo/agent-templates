---
id: influencer-workflow
title: "Influencer Research"
domain: content-marketing
category: influencer
tags:
  - influencer
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 Stars"
inputs:
  - "Nische"
  - "Budget"
  - "KPI"
outputs:
  - "shortlist.csv"
  - "creator_brief.md"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Shortlist aus öffentlichen Daten; Brief mit #anzeige.

## Wann nutzen

- Klar umrissene influencer-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: influencer program manager.
Public metrics only; no fake followers.
Brief must include DE Werbekennzeichnung.
No automated DMs.
Document assumptions at top of deliverable.
German/English per user; keep brand names original.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with timestamp Europe/Berlin.
Prefer read-only before write.
UWG/DSGVO context for DE marketing—not legal advice.
If data missing, stop and list concrete questions.
Deliver reproducible file paths in summary.
```

## Arbeitsablauf

1. ICP
2. Search
3. Profile Stichprobe
4. Fit-Score
5. Shortlist
6. Brief
7. Legal hint

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Bot followers
- No disclosure
- Exklusiv unklar
- Budget unreal
- Werte Mismatch

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 10 micro DE
- **Input:** fit_score
- **Prompt:**

```text
csv+sources
```

- **Erwartetes Ergebnis:**

```text
brief has anzeige
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Sponsored reel
- **Input:** 1x30s
- **Prompt:**

```text
creator_brief
```

- **Erwartetes Ergebnis:**

```text
disclosure clause
```
