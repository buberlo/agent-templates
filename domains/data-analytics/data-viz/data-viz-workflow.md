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
    version_notes: "Nous-approved optional-mcps-catalog entry (Listing 23 Nov 2026)."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "197975 GitHub Stars"
inputs:
  - "Data source, chart goal (comparison, trend)"
  - "Target medium (slides, report, web)"
  - "DE Beschriftungen ja/nein"
outputs:
  - "PNG/SVG Charts"
  - "chart_spec.md (axes, colors)"
  - "SQL/Pandas reproducible snippet"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Honest, well-labeled charts** from SQL/pandas—no truncated Y-axis without labeling, no 3D pie.

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
Role: data visualization specialist (data-analytics/data-viz).
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

## Workflow

1.Clarify question and data type.
2. Justification of chart type.
3. Daten per SQL laden.
4. Plot with Labels/Units.
5. Farb-/A11y-Check.
6. Save PNG + code.
7. chart_spec and Alt-Text.

## Definition of done

- [ ] Chart type justified
- [ ] Axes labeled with unit
- [ ] Reproducible snippet
- [ ] No truncated axis without notice

## Security

- No PII in axis labels.

## Pitfalls

- Dual axis two skates misleading.
- Pie with 12 Kategorien.
- Zeitzone x-axis falsch.
- Bar sorting not by value.
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
figures/revenue_trend.png DE labels
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
bar chart 8 cats | chart_spec notes sort order
```