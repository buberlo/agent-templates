---
id: qos-csat-workflow
title: "Qualität und CSAT"
domain: kundenservice
category: qos-csat
tags:
  - qos
  - kundenservice
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Zeitraum und Team-Filter"
  - "CSAT/NPS Export oder API"
outputs:
  - "QoS-Report"
  - "Top Drivers negativer Bewertungen"
  - "Maßnahmen-Backlog (Entwurf)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**CSAT/NPS, Reaktionszeiten und Eskalationsmuster** auswerten, qualitative Ursachen aus Tickets ziehen und **Maßnahmenliste** für Support-Leadership vorbereiten.

## Wann nutzen

- Wöchentlicher/monatlicher Qualitätsreview.
- Intercom (oder Export CSV) mit Bewertungen und Metriken.
- Keine personenbezogene öffentliche Shaming-Listen.

**Wann nicht**

- Einzelnes schlechtes Ticket ohne Statistik → helpdesk.
- Rohdaten mit PII an unkontrollierte Drittanbieter-LLMs ohne Freigabe.
- Automatische Agentenbewertung ohne HR-Policy.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| intercom MCP | Tickets + ratings | Primärquelle |
| CSV/Sheets | Aggregation | Trends |
| Markdown-Report | Leadership | Lesbar, versionierbar |

## System-Prompt / Instruktionen

```text
You analyze support QoS for kundenservice/qos-csat.

Inputs: period (ISO start/end), team_filter, metrics (csat|nps|first_response_median|resolution_median), sample_size_low_csat.

Steps:
1) Pull aggregate metrics for period vs previous period delta.
2) Sample low CSAT tickets (max sample_size); anonymize customer names in report (Agent IDs ok if policy allows).
3) Tag themes: product_bug, policy, tone, wait_time, resolution_incomplete.
4) Correlate themes with product area if tags exist.
5) Propose action_backlog[] with owner suggestion (support|product|docs), priority, evidence ticket_ids redacted.

No individual performance ranking in customer-visible docs.
Quantify: "% tickets theme X among low CSAT sample".

Deliver: qos-report.md with tables, theme chart ascii optional, backlog.csv.
```

## Arbeitsablauf

1. Zeitraum und Metriken definieren.
2. Intercom MCP: CSAT-Verteilung und Median FRT laden.
3. Stichprobe negativer Tickets (n≤30) lesen.
4. Themen clustern mit Zählung.
5. Delta zur Vorperiode berechnen.
6. `qos-report.md` und `backlog.csv` schreiben.
7. Review mit Support-Lead; keine Auto-Maßnahmen in Produktion.

## Qualitätskriterien / Definition of Done

- [ ] Aggregat + Stichprobe klar getrennt
- [ ] Kundennamen in Report pseudonymisiert
- [ ] Jede Backlog-Zeile mit Evidenz-Anker
- [ ] Vorperiode-Vergleich wenn Daten da

## Sicherheit & Freigaben

- HR-sensible Agenten-Metriken nur intern nach Policy.
- Export nicht in öffentliche Repos.
- GDPR bei Zitaten minimal.

## Fallstricke

- Kleine Stichprobe überinterpretiert.
- CSAT bias nach Happy-Flow nur.
- Themen-Doppelzählung.
- Zeitzone verzerrt FRT.
- Maßnahmen ohne Product-OK versprechen Fixes.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Woche 47 Review.
- **Input:** 2026-11-17–23, CSAT + 20 low ratings sample.
- **Prompt:**

```text
Produce qos-report.md with theme counts and 5-item action backlog.
```

- **Erwartetes Ergebnis:**

```text
CSAT: 4.2 → 4.0 (Δ -0.2)
Top themes: wait_time 40%, product_bug 35%, tone 15%
Backlog: P1 reduce FRT staffing Fri peak; P2 KB article billing delay…
File: qos-report.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlender Zeitraum.
- **Input:** Kein start/end.
- **Prompt:**

```text
Analyze CSAT trends.
```

- **Erwartetes Ergebnis:**

```text
Abbruch: period_start and period_end required.
Suggested default: last 7 days — confirm?
No MCP queries executed.
```