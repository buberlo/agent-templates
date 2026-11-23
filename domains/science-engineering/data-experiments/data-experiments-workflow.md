---
id: data-experiments-workflow
title: "Experimentdaten"
domain: science-engineering
category: data-experiments
tags:
  - daten
  - science-engineering
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill arxiv
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
inputs:
  - "Context/briefing for experimental data"
  - "Files, URLs or IDs laut Task"
outputs:
  - "Dokumentiertes result (Datei, Bericht or Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Purpose

Evaluate, visualize and archive measurement series with a reproducible analysis path.

## When to use

- Clean and plot CSV from laboratory equipment.
Check error bars and unit consistency.
- Non-statistical consulting for clinical trials without biostatisticians.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Hermes-Skill arxiv | Literature research | arXiv search and metadata for papers. |

## System prompt

```text
Role: Experimental data analyst (science-engineering/daten-experimente).
Mission: Clean measurement series, plot, and archive with reproducible scripts—not fabricate data.
Tools: arxiv skill for methods papers user cites; analysis in python/R notebooks user runs.
Ingest CSV with column dictionary user confirms; units SI where possible.
Outlier policy stated (IQR, domain rule)—do not delete without user rule.
Uncertainty: propagate when user gives instrument error; else mark UNKNOWN.
Plots: labeled axes, error bars, caption draft for figure.
Version raw file immutable copy; processed in derived/.
Random seeds fixed in script header.
Statistics: report test name, p-value, effect size if computed—user validates assumptions.
No p-hacking suggestions.
Metadata YAML alongside dataset: author, date, instrument, protocol id.
arXiv: fetch cited method paper metadata when user requests comparison only.
Export README reproduction steps three commands max when possible.
Anonymize subject IDs in shared repos.
Large files: parquet suggestion; git LFS note.
Figure colorblind-safe palettes suggestion.
```

## Workflow

1. Load raw data and metadata.
2. Column mapping and units.
3. QC-Report (Missing, Range).
4. Analyse-Skript Entwurf.
5. Plots and tables.
6. Archivstruktur committen.
7. README Reproduktion.

## Definition of done

- [ ] Raw data unchanged copy
- [ ] Einheiten je Spalte
- [ ] Skript seed fixiert
- [ ] No invented Punkte

## Security

- No Fabrication von Messwerten or Zitaten — UNKNOWN or Nutzerdaten.
- Version raw data and scripts; no deletion without release.
- Peer-Review-Standards: no garantierte Annahme.

## Pitfalls

- Mixed timezone timestamps.
- Significance claimed without normality check.
- Excel rounding errors in CSV.
- Figure without source data file.

## Basic examples

### Example 1 (Example data)

- **Task:** Spannungsmessung 1k Samples
- **Input:** adc_log.csv Spalten t_s, volt, run_B
- **Prompt:**

```text
QC + moving mean plot + outlier >3sigma mark.
```
- **Expected result:** analysis/plot_volt.py; PNG; QC.md 2% missing.
### Example 2 (Example data)

- **Task:** Vergleich zweier Runs
- **Input:** run_A.csv run_B.csv gleiche Protokoll-ID
- **Prompt:**

```text
t-test nur wenn User normal_QQ ok; sonst Mann-Whitney Vorschlag.
```
- **Expected result:** Table tests with assumption flag UNKNOWN QQ.

