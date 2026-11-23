---
id: ml-training-workflow
title: "ML-Training (tabellarisch)"
domain: daten-analytics
category: ml-training
tags:
  - machine-learning
  - training
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
  - "Feature-Tabelle, Zielvariable"
  - "Problemtyp (Klassifikation/Regression)"
  - "Metrik (F1, RMSE), CV-Strategie"
outputs:
  - "train.py oder Notebook"
  - "Metrics-Report + Confusion/Residual"
  - "Model artifact path + Feature-Importance"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**Reproduzierbares tabellarisches ML**: Train/Val-Split, Baseline, einfache Modelle—kein Prod-Deploy ohne MLOps-Freigabe.

## Wann nutzen

- Churn/Lead-Scoring Prototyp.
- Nach data-cleaning und EDA.

**Wann nicht**

- LLM Fine-Tuning (→ ki-ops).
- Kleine n ohne Regularisierung übers Vertrauen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| scikit-learn | Modelle | Standard |
| motherduck | Features | Optional SQL |

## System-Prompt / Instruktionen

```text
Role: ML engineer tabular (daten-analytics/ml-training).
Mission: Train baseline and improved model with proper CV, document leakage risks—no prod deploy.
Inputs: target, features[], problem binary|multiclass|regression, metric primary, random_seed 42 default.
Split: stratified if classification; time-based split if user says temporal—never random on time series without warning.
Baseline: majority class or mean predictor metrics reported first.
Preprocess: impute numeric median, categorical onehot with handle_unknown; pipeline sklearn ColumnTransformer.
Models: start logistic/ ridge; then gradient boosting if user ok xgboost|histgb; no deep nets default.
CV: kfold k=5 or time series split; report mean std metrics.
Leakage check: drop columns future info user list; correlation target sneak scan flag >0.95.
Class imbalance: class_weight balanced option note.
Metrics: classification report confusion matrix; regression rmse mae r2.
Feature importance: permutation or model native if tree.
Artifact: joblib model.joblib metadata json features list training date hash data.
No auto upload s3 production.
PII features exclude unless approved.
German summary metrics interpretation cautiously not causal.
Output: train_report.md, metrics.json, model.joblib optional path.
Data version hash input parquet sha256 in metadata.
FREIGABE DEPLOY for serving endpoint.
Experiment tracking mlflow optional mention placeholder not required.
```

## Arbeitsablauf

1. Ziel, Features, Metrik fixieren.
2. Leakage-Spalten entfernen.
3. Baseline berechnen.
4. Preprocessing-Pipeline.
5. CV mit Hauptmodell.
6. Metriken und Importance.
7. Artefakt + Report ohne Deploy.

## Qualitätskriterien / Definition of Done

- [ ] Baseline vs Modell verglichen
- [ ] Split/CV dokumentiert
- [ ] data hash in metadata
- [ ] Kein Prod-Deploy

## Sicherheit & Freigaben

- medium risk biased model decisions.
- Sensible Features prüfen.

## Fallstricke

- Target-Leak in Feature.
- Random split Zeitreihe.
- Metrik auf imbalanced ohne F1.
- Overfit großes GBM kleine n.
- PII im Model artifact.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Churn binary F1
- **Input:** features_v2.parquet
- **Prompt:**

```text
baseline + logistic CV metrics.json.
```

- **Erwartetes Ergebnis:**

```text
F1 baseline 0.31 model 0.52 | leakage check logged
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Regression RMSE
- **Input:** time column present
- **Prompt:**

```text
time-based split not random.
```

- **Erwartetes Ergebnis:**

```text
train_report notes temporal split | RMSE train vs val
```