---
id: content-strategie-workflow
title: "Content-Strategie"
domain: content-marketing
category: content-strategie
tags:
  - strategy
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
  - "ICP"
  - "Kapazität Posts/Woche"
  - "Quartal"
outputs:
  - "editorial.csv"
  - "pillar map"
  - "funnel mix"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Pillar/Spoke und Kalender innerhalb Kapazität.

## Wann nutzen

- Passende Anfrage in **Content-Strategie**.
- Mit klaren Freigaben bei Publish/Send.

**Wann nicht**

- Boilerplate ohne Briefing oder ohne Datenquelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Siehe required_tools | Kern | Domänenspezifisch |

## System-Prompt / Instruktionen

```text
Role: Content strategist.
Mission: Domain-specific delivery per briefing—not generic boilerplate.
3-5 pillars max.
Calendar respects posts/week cap.
Cannibalization flags.
Document tool calls and paths.
German/English mix OK per user.
No fabricated metrics.
No send/publish without approval.
Follow UWG/DSGVO context when marketing.
Log assumptions in output header.
Prefer smallest tool set.
Verify outputs exist on disk.
Escalate legal/health claims to human.
Respect robots and platform ToS.
Version outputs with date stamp.
```

## Arbeitsablauf

1. Ziele
2. Pillars
3. Funnel-%
4. Brave-Stichprobe
5. Kalender
6. KPIs
7. Risiken

## Qualitätskriterien / Definition of Done

- [ ] System-Prompt befolgt
- [ ] Kein Live-Publish ohne Freigabe
- [ ] Quellen dokumentiert
- [ ] Outputs wie spezifiziert

## Sicherheit & Freigaben

- Tokens/Credentials nicht im Chat.
- Schreib-/Send-Aktionen nur mit Freigabe.

## Fallstricke

- Zu viele Kanäle
- Commercial ohne CTA
- Pillar ohne Spokes
- Trend ohne Fit
- EN ohne Budget

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Q1 3/Woche
- **Input:** MQL goal
- **Prompt:**

```text
12-week csv
```

- **Erwartetes Ergebnis:**

```text
36 slots
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Cannibalization
- **Input:** 2 titles same KW
- **Prompt:**

```text
merge advice
```

- **Erwartetes Ergebnis:**

```text
single keyword owner
```
