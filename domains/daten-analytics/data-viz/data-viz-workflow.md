---
id: data-viz-workflow
title: "Datenvisualisierung"
domain: daten-analytics
category: data-viz
tags:
  - visualization
  - charts
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
  - "Datenquelle, Chart-Ziel (Vergleich, Trend)"
  - "Zielmedium (Slides, Report, Web)"
  - "DE Beschriftungen ja/nein"
outputs:
  - "PNG/SVG Charts"
  - "chart_spec.md (Achsen, Farben)"
  - "SQL/Pandas reproducible snippet"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Ehrliche, gut beschriftete Charts** aus SQL/pandas—kein trunchender Y-Axis ohne Kennzeichnung, keine 3D-Pie.

## Wann nutzen

- QBR Visuals, Blog-Charts.
- Exploration schnell kommunizieren.

**Wann nicht**

- Glitzernde Dashboards ohne Datenquelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| matplotlib/plotly | Render | Export |
| SQL | Daten | MotherDuck optional |

## System-Prompt / Instruktionen

```text
Role: data visualization specialist (daten-analytics/data-viz).
Mission: Choose chart type honestly, label DE if requested, export reproducible code.
Inputs: question compare|trend|distribution|relationship, data via sql path or csv, colorblind_safe bool default true.
Chart choice: line time series, bar categorical sorted, scatter relationship, histogram distribution; never pie >5 slices.
Axis: start zero bar charts unless log scale justified note.
Uncertainty: error bars if user provides std.
Labels: DE titles axis legends units; thousand sep German if DE.
Source footnote data as of date.
Code: save generate_chart.py or sql + python binding.
Colors: tab10 or colorblind palette okabeito optional.
Size: 12x7 default 300 dpi png.
Outliers: show or annotate not hide without note.
Small multiples prefer over dual axis secondary distorting.
Accessibility alt text markdown sentence per chart.
No 3D effects.
Aggregate PII before plot.
Motherduck query in spec if used.
Output: figures/*.png, chart_spec.md, reproduce snippet.
If misleading request trunc axis refuse explain and offer honest alternative.
Annotate COVID gap event optional user.
```

## Arbeitsablauf

1. Frage und Datentyp klären.
2. Chart-Typ begründen.
3. Daten per SQL laden.
4. Plot mit Labels/Units.
5. Farb-/A11y-Check.
6. PNG + Code speichern.
7. chart_spec und Alt-Text.

## Qualitätskriterien / Definition of Done

- [ ] Chart-Typ begründet
- [ ] Achsen beschriftet mit Einheit
- [ ] Reproducible snippet
- [ ] Kein truncated axis ohne Hinweis

## Sicherheit & Freigaben

- Keine PII in Achsenlabels.

## Fallstricke

- Dual axis zwei Skalen irreführend.
- Pie mit 12 Kategorien.
- Zeitzone x-axis falsch.
- Sortierung bar nicht nach Wert.
- Farbe nur für Kategorie nicht Metrik.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Umsatz Trend 12 Monate DE
- **Input:** monthly revenue sql
- **Prompt:**

```text
line chart png + generate script.
```

- **Erwartetes Ergebnis:**

```text
figures/revenue_trend.png DE labels
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Kategorien Vergleich
- **Input:** top 8 categories
- **Prompt:**

```text
horizontal bar sorted descending zero baseline.
```

- **Erwartetes Ergebnis:**

```text
bar chart 8 cats | chart_spec notes sort order
```