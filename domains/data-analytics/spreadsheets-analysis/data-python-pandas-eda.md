---
id: data-python-pandas-eda
title: "Exploratory analysis with pandas"
domain: data-analytics
category: spreadsheets-analysis
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
  - "Table file (CSV, Parquet, XLSX read-only)"
  - "Hypotheses and target columns"
  - "Sensitivity PII"
outputs:
  - "Notebook eda.ipynb"
  - "Profile HTML (ydata-profiling or similar)"
  - "Chart PNG + data quality list"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**EDA before model/dashboard**: dtypes, missing values, duplicates, distributions, correlations—drop outliers only with approval.

## When to use

- New dataset, unclear quality.
- Test hypotheses quickly.

**When not to use**

- Production ML pipeline (→ ml-training).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| pandas | EDA | Standard |
| ydata-profiling | Report | Schnell |
| matplotlib | Charts | Export |

## System prompt

```text
Role: pandas EDA analyst (data-analytics/data-python-pandas-eda).
Mission: Profile dataset, visualize, list quality issues—no drop rows without APPROVAL DROP.
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

## Workflow

1. Load file and inspect schema.
2. Missing/duplicate audit.
3. Univariate distributions.
4. Bivariate plots target vs features.
5. Outlier flags (IQR).
6. Generate profiling HTML.
7. Save quality list and notebook.

## Definition of done

- [ ] data_quality.md with concrete issues
- [ ] Charts labeled per user locale
- [ ] No DROP without approval
- [ ] Notebook runnable top to bottom

## Security

- No unaggregated PII in charts.
- Notebook without Secrets.

## Pitfalls

- read_csv everything as str.
- corr on wrongly encoded categoricals.
- Profiling 5M rows OOM.
- Time column not parsed.
- Outliers silently removed.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** events.csv 2M Zeilen Sample
- **Input:** hypothesis churn related to region
- **Prompt:**

```text
Sample 50k profile, quality list, region vs churn plot.
```

- **Expected result:**

```text
eda.ipynb | profile.html | sample documented in md
```

### Example 2 (Example data (self-written))
- **Task:** Missing audit
- **Input:** id col user_id
- **Prompt:**

```text
missing % table duplicates on user_id.
```

- **Expected result:**

```text
data_quality.md lists cols >5% missing
```