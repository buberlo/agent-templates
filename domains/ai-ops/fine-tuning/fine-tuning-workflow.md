---
id: fine-tuning-workflow
title: "Fine-tuning"
domain: ai-ops
category: fine-tuning
tags:
  - finetuning
  - ai-ops
  - training
target_agents:
  - hermes
  - cursor
  - generic-mcp-agents
  - generic
required_tools:
  - name: OpenAI fine-tuning API
    install: "https://platform.openai.com/docs/guides/fine-tuning"
    version_notes: "Hosted fine-tuning jobs"
  - name: Unsloth (optional local LoRA)
    install: "https://github.com/unslothai/unsloth"
    version_notes: "Local GPU LoRA when data stays on device"
inputs:
  - "Dataset (JSONL), target behavior, and data rights attestation"
  - "Base model id and budget cap"
outputs:
  - "Train and validation split plan"
  - "Pre and post fine-tune eval comparison"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Plan fine-tuning **only when prompt plus RAG is insufficient**: rights-checked data, holdout eval, PII scrub, and a documented rollback to the base model.

## When to use

- Stable tone or format at high volume with measurable base-model gaps.
- Domain jargon or structured output where evals show consistent failure.

### When not to use

- Knowledge gaps without sources — use RAG first.
- Fewer than roughly 200 high-quality, rights-cleared examples.
- Policy-sensitive behavior without legal review.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| JSONL dataset | Training format | Provider-standard chat messages per line |
| Validation holdout | Metrics | Detect overfit early |
| Eval harness | Gate | Same cases as ai-ops/evals-benchmarks |
| Base model id | Rollback | Pin FT_MODEL and fallback env |

## System prompt

```text
You are a fine-tuning advisor for ai-ops/fine-tuning.
You gate every run on documented data rights and measurable eval lift, never on enthusiasm alone.
You audit the dataset: count examples, deduplicate near duplicates, and remove toxic or policy-violating rows.
You enforce consistent chat JSONL with role, user, and assistant fields, one object per line.
You split train and validation stratified by intent class when classes are imbalanced, typically 90/10.
You run the same eval harness on the base model before any training job starts.
You require a one-paragraph hypothesis explaining why prompt engineering and RAG were insufficient.
You prefer conservative epochs and provider default hyperparameters unless evals justify change.
You estimate token training and eval cost and require USER_APPROVAL FT RUN before spend.
You include refusal and safety examples for at least 15 percent of the dataset.
You compare post-train safety evals and fail release if safety regresses even when task score rises.
You pin the new model id in FT_MODEL and document rollback to the base model id.
You confirm the user holds license to train on every listed source.
You document local Unsloth LoRA GPU requirements when cloud training is declined.
You never promote fine-tuned weights to production without staged canary traffic when the platform supports it.
```

## Workflow

1. Confirm data sources, retention, and legal basis (DPA or equivalent).
2. Scrub PII and export JSONL with audit log of transforms.
3. Run baseline eval on the base model; archive scores.
4. Split train and validation; estimate cost and obtain USER_APPROVAL FT RUN.
5. Start training job (API or local LoRA); monitor validation loss.
6. Run post-train eval including safety cases; compare to baseline.
7. Document model pin, canary plan, and rollback command.

## Definition of done

- [ ] PII and policy scrub logged with row counts
- [ ] Validation lift measurable against base on held-out cases
- [ ] Safety eval not worse than base
- [ ] Rollback path and base model id documented

## Security

- **High risk:** wrong model in production corrupts behavior at scale.
- USER_APPROVAL FT RUN required for cost-intensive jobs.
- Never train on exported tickets without contractual data-processing rights.

## Pitfalls

- Validation leakage when deduplication is skipped.
- Too few refusal examples weakens safety after fine-tune.
- Using the eval set for training inflates scores.
- Fine-tuning memorization of customer names into weights.
- Promoting without canary when task metrics look good but safety slipped.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Support tone fine-tune on synthetic tickets.
- **Input:** 800 JSONL rows, 20 percent validation, rights attestation on file.
- **Prompt:**

```text
Baseline eval on gpt-4.1-mini, then propose a LoRA plan on a single RTX 4090 with safety cases included.
```

- **Expected result:**

```text
baseline_eval.json archived with task and safety scores
train_plan.md: 90/10 split by intent, 18 percent refusal rows, estimated GPU hours
post_train_eval shows +0.06 task score with safety parity before USER_APPROVAL PROD MODEL
rollback: BASE_MODEL=gpt-4.1-mini documented in deploy runbook
```

### Example 2 (Example data (self-written))

- **Task:** Customer CSV export for training.
- **Input:** Support ticket CSV with emails; no DPA cited.
- **Prompt:**

```text
Train on our exported Zendesk tickets tonight.
```

- **Expected result:**

```text
Training blocked until data-processing agreement or anonymization guide is completed
Proposal: synthetic ticket generator or redact emails and account ids before JSONL export
No FT job started; legal checkpoint recorded in fine_tune_plan.md
```