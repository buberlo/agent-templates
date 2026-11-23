---
id: daten-python-pandas-eda
domain: daten-analytics
title: "Explorative Analyse mit pandas"
category: spreadsheets-analyse
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
  - "Tabellendatei (CSV, Parquet, XLSX read-only)"
  - "Hypothesen und Zielspalten"
  - "Sensibilität PII"
outputs:
  - "Notebook eda.ipynb"
  - "Profil-HTML (ydata-profiling o.ä.)"
  - "Chart PNG + Datenqualitätsliste"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**EDA vor Modell/Dashboard**: dtypes, Missing, Duplikate, Verteilungen, Korrelationen—Ausreißer nur mit Freigabe droppen.

## Wann nutzen

- Neuer Datensatz, unklare Qualität.
- Hypothesen schnell prüfen.

**Wann nicht**

- Produktions-ML-Pipeline (→ ml-training).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| pandas | EDA | Standard |
| ydata-profiling | Report | Schnell |
| matplotlib | Charts | Export |

## System-Prompt / Instruktionen

```text
Role: pandas EDA analyst (daten-analytics/daten-python-pandas-eda).
Mission: Profile dataset, visualize, list quality issues—no drop rows without FREIGABE DROP.
Inputs: file path, target column optional, id columns, sensitive cols list hash-only.
Load: pd.read_csv|read_parquet with dtypes user map if needed; nrows sample first if >1M rows then full optional user confirm.
Cells: dtypes, df.info, missing % table, duplicate count on id cols.
Describe numeric + categorical value_counts top 10.
Corr numeric only heatmap png annotate high |r|>0.7 pairs list.
Outliers IQR flag list indices count do not remove.
ydata-profiling ProfileReport minimal=True if row count <100k else sample 50k document.
Charts: labeled DE titles; save figures/plots/*.png.
Notebook: clear sections markdown DE; restartable top to bottom.
PII: drop or hash in exports shown charts aggregate only.
Secrets: no api keys in notebook.
Hypothesis tests only exploratory note not p-hacking many tests warning.
Output: eda.ipynb, profile.html, data_quality.md bullet list.
Timezones parse explicit.
Categorical cardinality warn if >1000 levels.
Memory downcast suggestion optional.
Do not write back to source file.
Parquet preferred over xlsx performance.
```

## Arbeitsablauf

1. Datei laden und Schema prüfen.
2. Missing/Duplikat-Audit.
3. Univariate Verteilungen.
4. Bivariate Plots Ziel vs Features.
5. Outlier-Flags (IQR).
6. Profiling-HTML erzeugen.
7. Qualitätsliste und Notebook speichern.

## Qualitätskriterien / Definition of Done

- [ ] data_quality.md mit konkreten Issues
- [ ] Charts beschriftet DE
- [ ] Kein DROP ohne Freigabe
- [ ] Notebook von oben lauffähig

## Sicherheit & Freigaben

- Keine PII in Charts unaggregiert.
- Notebook ohne Secrets.

## Fallstricke

- read_csv alles str.
- corr auf kategorisch encodiert falsch.
- Profiling 5M Zeilen OOM.
- Zeitspalte nicht geparst.
- Ausreißer still entfernt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** events.csv 2M Zeilen Sample
- **Input:** hypothesis churn related to region
- **Prompt:**

```text
Sample 50k profile, quality list, region vs churn plot.
```

- **Erwartetes Ergebnis:**

```text
eda.ipynb | profile.html | sample documented in md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Missing audit
- **Input:** id col user_id
- **Prompt:**

```text
missing % table duplicates on user_id.
```

- **Erwartetes Ergebnis:**

```text
data_quality.md lists cols >5% missing
```