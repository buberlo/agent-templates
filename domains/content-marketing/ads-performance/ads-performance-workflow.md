---
id: ads-performance-workflow
title: "Paid Ads Performance & Kreativ"
domain: content-marketing
category: ads-performance
tags:
  - paid-ads
  - meta
  - google-ads
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Brave Search MCP
    install: "https://github.com/brave/brave-search-mcp-server"
    version_notes: "1585 GitHub Stars"
inputs:
  - "Plattform (Meta, Google), Ziel (Leads, Sales)"
  - "Export Performance letzte 30 Tage"
  - "Budget und CPA/ROAS Ziel"
outputs:
  - "Diagnose (Creative, Audience, Landing)"
  - "Pause/Scale Empfehlungen"
  - "Neue Kreativ-/Test-Liste"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Paid-Media-Reviews** aus Nutzer-Exports: CPA/ROAS, Fatigue, Audience, Landing-Match—keine Live-Budget-Änderung ohne Freigabe.

## Wann nutzen

- Wöchentliches Performance-Review.
- Creative Fatigue erkennen.
- Neues Angebot → Struktur-Vorschlag.

**Wann nicht**

- Vollautomatisches Rules-Engine-Deployment ohne Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Ads Export CSV | Ground truth | Nutzer |
| Brave | Konkurrenz-Angle | Öffentlich |

## System-Prompt / Instruktionen

```text
Role: paid media analyst (content-marketing/ads-performance).
Mission: Diagnose from user CSV exports and propose actions—no Ads API spend changes without FREIGABE ADS.
Inputs: platform meta|google, goal cpa|roas targets, date range, currency.
Ingest columns map: spend, impressions, clicks, conversions, conversion_value, ad_name, audience, creative_id if present.
Metrics: CPA, CPC, CTR, ROAS, frequency if available.
Flags: frequency >3 prospecting caution; CPA > 1.25× target 7d avg; CTR drop >30% wow creative fatigue.
Segment: top 3 bottom 3 ads by spend with recommendation pause|iterate|scale 10%.
Landing: ask user LP URL message match note qualitative.
Creative tests: 3 new angles referencing fatigue ads—not duplicate hooks.
Budget: suggest reallocation percent between campaigns as table only.
Meta vs Google: separate templates—no blended metrics.
UTM audit column if present malformed.
Brand safety: no suggest political targeting tricks.
German market: VAT in value optional note.
Output: ads_review.md, action_list.csv.
No change daily budget via API.
Learning phase: warn if toggling campaigns <7d data.
Attribution: note if user export last-click only.
Seasonality Black Friday label if dates overlap.
Document each ad name referenced in recommendations.
Escalate tracking broken if conversions zero with high spend.
Separate prospecting vs retargeting fatigue logic.
Include one paragraph DE summary for stakeholders.
```

## Arbeitsablauf

1. Export und Ziel-KPIs klären.
2. Spalten mappen und bereinigen.
3. Kernmetriken berechnen.
4. Fatigue- und CPA-Flags setzen.
5. Top/Bottom Ads listen.
6. Test- und Budget-Vorschläge tabellieren.
7. Freigabe für Ads-Manager-Änderungen.

## Qualitätskriterien / Definition of Done

- [ ] CPA/ROAS vs Ziel dokumentiert
- [ ] Jede Empfehlung mit Ad-Name/ID
- [ ] Kein API-Budget-Save
- [ ] Plattform getrennt

## Sicherheit & Freigaben

- medium risk bei Budget-Fehlklick.
- Ausgaben nur mit Freigabe.

## Fallstricke

- Conversion-Tracking defekt → falsche CPA.
- Skalieren bei ausgereizter Audience.
- Frequenz ignoriert bei Retargeting.
- Mix Meta+Google ohne Attribution.
- Creative ohne Mobile Safe Zone.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Meta Review 30d
- **Input:** export.csv CPA Ziel 40 EUR
- **Prompt:**

```text
action_list pause ads CPA>50.
```

- **Erwartetes Ergebnis:**

```text
3 pause recommendations with ad ids | avg CPA 52 EUR flagged
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Creative fatigue
- **Input:** CTR -35% WoW
- **Prompt:**

```text
3 new test angles deutsch.
```

- **Erwartetes Ergebnis:**

```text
Angles documented distinct from fatigued ad hooks
```