---
id: ml-training-workflow
title: "ML training (tabular)"
domain: data-analytics
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
  - name: motherduck MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
  - name: MarkItDown
    install: "https://github.com/microsoft/markitdown"
    version_notes: "197975 GitHub Stars"
inputs:
  - "Feature table, target variable"
  - "Problem type (classification/regression)"
  - "Metric (F1, RMSE), CV strategy"
outputs:
  - "train.py or notebook"
  - "Metrics report + confusion/residual"
  - "Model artifact path + feature importance"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Reproducible tabular ML**: train/validation split, baseline, simple models—no prod deploy without MLOps approval.

## When to use

- Churn/lead scoring prototype.
- After data cleaning and EDA.

**When not to use**

- LLM fine-tuning (→ ai-ops).
- Small n without regularization over confidence.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| scikit-learn | Models | Standard |
| motherduck | Features | Optional SQL |

## System prompt

```text
Role: ML engineer tabular (data-analytics/ml-training).
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
APPROVAL DEPLOY for serving endpoint.
Experiment tracking mlflow optional mention placeholder not required.
```

## Workflow

1. Fix target, features, and metric.
2. Remove leakage columns.
3. Compute baseline.
4. Preprocessing pipeline.
5. CV with main model.
6. Metrics and importance.
7. Artifact + report without deploy.

## Definition of done

- [ ] Baseline vs model compared
- [ ] Split/CV documented
- [ ] Data hash in metadata
- [ ] No prod deploy

## Security

- Medium risk biased model decisions.
- Review sensitive features.

## Pitfalls

- Target leak in features.
- Random split on time series.
- Metric on imbalanced data without F1.
- Overfit large GBM on small n.
- PII in model artifact.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Churn binary F1
- **Input:** features_v2.parquet
- **Prompt:**

```text
baseline + logistic CV metrics.json.
```

- **Expected result:**

```text
F1 baseline 0.31 model 0.52 | leakage check logged
```

### Example 2 (Example data (self-written))
- **Task:** Regression RMSE
- **Input:** time column present
- **Prompt:**

```text
time-based split not random.
```

- **Expected result:**

```text
train_report notes temporal split | RMSE train vs val
```