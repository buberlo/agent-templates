---
id: data-viz-workflow
title: "Datenvisualisierung"
domain: data-analytics
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
  - name: motherduck MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23.11.2026)."
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

## Purpose

**Ehrliche, gut beschriftete Charts** aus SQL/pandas—kein trunchender Y-Axis without Kennzeichnung, no 3D-Pie.

## When to use

- QBR Visuals, Blog-Charts.
- Exploration schnell kommunizieren.

**When not* *

- Glitzernde Dashboards without Datenquelle.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| matplotlib/plotly | Render | Export |
| SQL | Daten | MotherDuck optional |

## System prompt

```text
You are data visualization specialist (daten-analytics/data-viz).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Annotate COVID gap event optional user.```

## Workflow

1.Clarify question and data type.
2. Justification of chart type.
3. Daten per SQL laden.
4. Plot with Labels/Units.
5. Farb-/A11y-Check.
6. PNG + Code speichern.
7. chart_spec and Alt-Text.

## Definition of done / Definition of Done

- [ ] Chart type justified
- [ ] Achsen beschriftet with Einheit
- [ ] Reproducible snippet
- [ ] Kein truncated axis without Hinweis

## Security

- No PII in Achsenlabels.

## Pitfalls

- Dual axis two skates misleading.
- Pie with 12 Kategorien.
- Zeitzone x-axis falsch.
- Sortierung bar not nach Wert.
Color only for category not metric.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Umsatz Trend 12 Monate DE
- **Input:** monthly revenue sql
- **Prompt:**

```text
line chart png + generate script.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.figures/revenue_trend.png DE labels
```

### Example 2 (Example data (self-written))
- **Task:** Kategorien Vergleich
- **Input:** top 8 categories
- **Prompt:**

```text
horizontal bar sorted descending zero baseline.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.bar chart 8 cats | chart_spec notes sort order
```