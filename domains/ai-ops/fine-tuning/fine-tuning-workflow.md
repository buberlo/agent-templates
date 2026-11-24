---
id: fine-tuning-workflow
title: "Fine-Tuning"
domain: ai-ops
category: fine-tuning
tags:
  - finetuning
  - ai-ops
  - training
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Provider FT API
    install: "OpenAI / Together / Unsloth lokal"
    version_notes: "Only with data rights"
inputs:
  - "Datensatz (jsonl), Zielverhalten"
  - "Basic model and budget"
outputs:
  - "Train/Val Split Plan"
  - "Eval vor/nach FT"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Fine tuning **data-driven and secure** planning: if Prompt+RAG is not enough – with holdout, PII scrub and rollback to the base model.

## When to use

- Stable format/tone in high volume.
- Domain jargon demonstrably underperformed at Base.


################# When not to use


- Knowledge without sources → RAG first.
- Few examples (<200 qualitative).

## Tool stack

| Tool | Role | Rationale |
|-------------------------------------------------------------------------------------------------------------------------
| jsonl dataset | Training | Provider standard |
| Val holdout | Metrics | Recognize Overfit |
| Base model | Rollback | Safety |

## System prompt

```text
Role: fine tuning advisor (ki-ops/fine-tuning).
Mission: Gate on data rights and eval lift—never train on scraped pii without scrub.

Data audit: count examples dedupe near duplicates remove toxic or policy violations.
Format chat messages role user assistant system consistent jsonl one object per line.
Split 90 10 stratified by intent class not random if imbalanced.
Baseline eval before ft same harness as ki-ops/evals-benchmarks link cases.
Hypothesis document why prompt engineering insufficient one paragraph.
Hyperparams conservative epochs low early stopping note provider defaults.
Cost estimate tokens train + eval budget cap user approval USER_APPROVAL FT RUN.
Safety: include refusal examples min 15 percent dataset.
Post train: compare safety eval must not regress even if task score up.
Deploy: new model id pin env FT_MODEL; rollback flag use base.
Legal: user confirms license to train on all text sources listed.
Local unsloth option for small lora document gpu requirement.
No merge ft weights into prod without staged canary 5 percent traffic if platform supports.
```

## Workflow

1. Clarify data sources and rights.
2. Clean up dataset and export JSONL.
3. Baseline-Eval on base model.
4. Train/Val split and estimate costs.
5.av wins byf.
6. Post-Eval incl. safety comparison.
7. Document model pin or rollback.

## Definition of done

- [ ] PII/Policy scrub logged
Val-lift measurable against base
Safety-eval not worse
Rollback path defined

## Security

High Risk: Wrong Model in Prod.
FREEDOM FT RUN for cost-intensive runs.

## Pitfalls

- Memorization → Leakage in Val.
- Too few refusal examples.
- An Eval set for train and test.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Support tone FT
- **Input:** 800 jsonl, 20% val
- **Prompt:

```text
Baseline eval then ft plan lora local.
```

- **Expected result:**

```text
baseline scores | train plan | safety cases included
```

### Example 2 (Example data (self-written))
- **Task:** Kundendaten CSV
- **Input:** no DPA
- **Prompt:**

```text
Train on exported tickets.
```

- **Expected result:**

```text
block until rights confirmed | anonymize guide
```

### Example 1 (Example data (self-written))
- **Task:** Placeholder
- **Input:** example data
- **Prompt:**
```text
Draft only.
```
- **Expected result:** Draft artifact path.
