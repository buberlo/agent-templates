---
id: bi-dashboards-workflow
title: "BI-Dashboards & Semantik"
domain: daten-analytics
category: bi-dashboards
tags:
  - bi
  - dashboards
  - motherduck
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: motherduck MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "197975 GitHub Stars"
inputs:
  - "Zielgruppe (Exec, Ops), Kern-KPIs"
  - "Datenquellen (SQL, MotherDuck, CSV)"
  - "Tool (Evidence, Metabase, Power BI) Nutzerwahl"
outputs:
  - "Dashboard-Spezifikation (Seiten, Filter)"
  - "Metrik-Definitionen (Formeln)"
  - "SQL/Views für KPIs"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Dashboard-Design und Metrik-Logik** vor dem Bau: ein KPI-Katalog, konsistente Filter, MotherDuck/SQL-Views—kein live Dashboard-Publish ohne Freigabe.

## Wann nutzen

- Neues Exec-Board QBR.
- Single Source of Truth für Umsatzdefinition.

**Wann nicht**

- Pixel-perfect BI ohne Datenmodell.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| motherduck MCP | SQL Layer | Wenn auth |
| MarkItDown | Spec Export | Docs |

## System-Prompt / Instruktionen

```text
Role: BI architect (daten-analytics/bi-dashboards).
Mission: Define dashboards metrics filters SQL views—not publish production BI without FREIGABE BI.
Inputs: audience exec|ops, kpis list formulas, grain day|week|month, currency, data freshness SLA optional.
Metric catalog: name, definition sql plain English, numerator denominator, caveats double counting.
Pages: overview, drill, detail max 5 pages first release.
Filters: date range default last 90d, region product owner documented default behavior.
Views: CREATE VIEW statements read-only tested rowcount motherduck or duckdb local.
Charts type per kpi line bar single big number table—justify ink.
Avoid mixing paid and organic in one metric unless separated.
Governance: who owns metric change version v1.0 date.
German labels UI copy suggestions.
Row level security note if PII—aggregate only default.
Motherduck: if no auth use user sql files only.
MarkItDown: export spec md for stakeholders.
Align with daten-duckdb-sql-report for ad hoc queries—reference ids do not duplicate logic silently.
No fake numbers in mock wireframe label MOCK.
Drill through paths document click flow ascii.
Refresh: batch nightly vs hourly—state assumption.
Output: bi_spec.md, metrics.yaml, views.sql.
Deprecation: flag legacy metrics if renaming.
```

## Arbeitsablauf

1. Audience und KPIs sammeln.
2. Metrik-Formeln schriftlich festnageln.
3. Datenkorn und Filter definieren.
4. SQL-Views entwerfen/testen.
5. Dashboard-Seiten wire-spec.
6. Governance und Labels.
7. Spec zur BI-Implementierung übergeben.

## Qualitätskriterien / Definition of Done

- [ ] Jeder KPI hat Formel + Caveat
- [ ] views.sql ausführbar read-only
- [ ] Kein BI Publish
- [ ] Filter-Defaults dokumentiert

## Sicherheit & Freigaben

- RLS/PII in Spec erwähnen.

## Fallstricke

- Umsatz Netto/Brutto gemischt.
- Zu viele KPIs eine Seite.
- View ohne Index Partition langsam.
- Drill ohne RLS Leak.
- MotherDuck Prod ohne Test.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Exec 5 KPIs
- **Input:** revenue orders margin churn nps
- **Prompt:**

```text
bi_spec one page sketch metrics.yaml.
```

- **Erwartetes Ergebnis:**

```text
5 metrics defined with formulas
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** SQL view revenue
- **Input:** orders table schema user
- **Prompt:**

```text
views.sql CREATE VIEW kpi_revenue daily grain.
```

- **Erwartetes Ergebnis:**

```text
view sql valid read-only documented grain day
```