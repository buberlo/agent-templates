---
id: daten-python-pandas-eda
title: "Explorative Analyse mit pandas"
category: daten-analyse
tags:
  - pandas
  - eda
  - jupyter
target_agents:
  - hermes
  - generic
required_tools:
  - name: pandas
    install: "pip: pandas pyarrow"
    version_notes: "2.2+"
  - name: jupyter
    install: "pip: jupyterlab"
    version_notes: "Export nbconvert HTML"
inputs:
  - "Tabellendatei"
  - "Hypothesen"
  - "Zielspalten"
outputs:
  - "Notebook"
  - "Profil-HTML"
  - "Chart PNG"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Datenqualität und Verteilungen verstehen, bevor Modell oder Dashboard gebaut wird.

## Wann nutzen

- Neuer Datensatz, unklare Anomalien.
- Nicht für produktionsreife ML-Pipeline (separates Template).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | EDA | Standard |
| ydata-profiling | Report | Schnell |
| matplotlib | Charts | Einfach exportierbar |

## System-Prompt / Instruktionen

```text
Run pandas EDA: dtypes, missing %, describe, corr for numeric.
Flag outliers with IQR rule; do not drop without approval.
Export ydata-profiling HTML and save notebook with cleared outputs optional.
```

## Arbeitsablauf

1. Laden und Schema.
2. Missing/duplicate Audit.
3. Univariate + Bivariate Plots.
4. Hypothesen-Stichproben.
5. Notebook + HTML profilieren.

## Qualitätskriterien / Definition of Done

- [ ] Datenqualitätsprobleme liste
- [ ] Charts beschriftet (DE)
- [ ] Reproduzierbares Notebook

## Sicherheit & Freigaben

- Keine personenbezogenen Spalten in Charts ohne Aggregierung.
- Notebook nicht mit Secrets.

## Beispiele

**Eingabe:** `events.csv` 2M Zeilen
**Erwartetes Ergebnis:** `eda.ipynb`, `profile.html`
