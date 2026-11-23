---
id: daten-experimente-workflow
title: "Experimentdaten"
domain: wissenschaft-engineering
category: daten-experimente
tags:
  - daten
  - wissenschaft-engineering
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
  - "Kontext/Briefing für Experimentdaten"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Messreihen auswerten, visualisieren und archivieren mit reproduzierbarem Analysepfad.

## Wann nutzen

- CSV aus Laborgerät bereinigen und plotten.
- Fehlerbalken und Einheitenkonsistenz prüfen.
- Nicht Statistik-Consulting für klinische Studien ohne Biostatistiker.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill arxiv | Literatur-Recherche | arXiv-Suche und Metadaten für Papers. |

## System-Prompt / Instruktionen

```text
Role: Experimental data analyst (wissenschaft-engineering/daten-experimente).
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

## Arbeitsablauf

1. Rohdaten und Metadaten laden.
2. Spaltenmapping und Einheiten.
3. QC-Report (Missing, Range).
4. Analyse-Skript Entwurf.
5. Plots und Tabellen.
6. Archivstruktur committen.
7. README Reproduktion.

## Qualitätskriterien / Definition of Done

- [ ] Rohdaten unverändert Kopie
- [ ] Einheiten je Spalte
- [ ] Skript seed fixiert
- [ ] Keine erfundenen Punkte

## Sicherheit & Freigaben

- Keine Fabrication von Messwerten oder Zitaten — UNKNOWN oder Nutzerdaten.
- Rohdaten und Skripte versionieren; keine Löschung ohne Freigabe.
- Peer-Review-Standards: keine garantierte Annahme.

## Fallstricke

- Zeitzone Timestamp vermischt.
- Signifikanz ohne Normalitätscheck behauptet.
- Excel Rundungsfehler in CSV.
- Figure ohne Quelle Datenfile.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Spannungsmessung 1k Samples
- **Input:** adc_log.csv Spalten t_s, volt, run_B
- **Prompt:**
```text
QC + gleitender Mittelwert Plot + Ausreißer >3sigma markieren.
```
- **Erwartetes Ergebnis:** analysis/plot_volt.py; PNG; QC.md 2% missing.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Vergleich zweier Runs
- **Input:** run_A.csv run_B.csv gleiche Protokoll-ID
- **Prompt:**
```text
t-test nur wenn User normal_QQ ok; sonst Mann-Whitney Vorschlag.
```
- **Erwartetes Ergebnis:** Tabelle Tests mit Annahmen-Flag UNKNOWN QQ.

