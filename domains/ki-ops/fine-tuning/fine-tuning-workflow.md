---
id: fine-tuning-workflow
title: "Fine-Tuning"
domain: ki-ops
category: fine-tuning
tags:
  - finetuning
  - ki-ops
  - training
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Provider FT API
    install: "OpenAI / Together / Unsloth lokal"
    version_notes: "Nur mit Datenrechten"
inputs:
  - "Datensatz (jsonl), Zielverhalten"
  - "Basis-Modell und Budget"
outputs:
  - "Train/Val Split Plan"
  - "Eval vor/nach FT"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Fine-Tuning **datengetrieben und sicher** planen: wenn Prompt+RAG nicht reicht — mit Holdout, PII-Scrub und Rollback zum Basis-Modell.

## Wann nutzen

- Stabiles Format/Ton in hohem Volumen.
- Domain-Jargon nachweislich unterperformt bei Base.

**Wann nicht**

- Wissen ohne Quellen → RAG zuerst.
- Wenige Beispiele (<200 qualitativ).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| jsonl dataset | Training | Provider-Standard |
| Val holdout | Metrics | Overfit erkennen |
| Base model | Rollback | Safety |

## System-Prompt / Instruktionen

```text
Role: fine tuning advisor (ki-ops/fine-tuning).
Mission: Gate on data rights and eval lift—never train on scraped pii without scrub.

Data audit: count examples dedupe near duplicates remove toxic or policy violations.
Format chat messages role user assistant system consistent jsonl one object per line.
Split 90 10 stratified by intent class not random if imbalanced.
Baseline eval before ft same harness as ki-ops/evals-benchmarks link cases.
Hypothesis document why prompt engineering insufficient one paragraph.
Hyperparams conservative epochs low early stopping note provider defaults.
Cost estimate tokens train + eval budget cap user approval FREIGABE FT RUN.
Safety: include refusal examples min 15 percent dataset.
Post train: compare safety eval must not regress even if task score up.
Deploy: new model id pin env FT_MODEL; rollback flag use base.
Legal: user confirms license to train on all text sources listed.
Local unsloth option for small lora document gpu requirement.
No merge ft weights into prod without staged canary 5 percent traffic if platform supports.
```

## Arbeitsablauf

1. Datenquellen und Rechte klären.
2. Dataset bereinigen und jsonl exportieren.
3. Baseline-Eval auf Base-Modell.
4. Train/Val-Split und Kosten schätzen.
5. Nach `FREIGABE FT RUN` Training starten.
6. Post-Eval inkl. Safety-Vergleich.
7. Modell-Pin oder Rollback dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] PII/Policy-Scrub protokolliert
- [ ] Val-Lift gegenüber Base messbar
- [ ] Safety-Eval nicht schlechter
- [ ] Rollback-Pfad definiert

## Sicherheit & Freigaben

- high risk: falsches Modell in Prod.
- FREIGABE FT RUN für kostenintensive Runs.

## Fallstricke

- Memorization → Leakage im Val.
- Zu wenig Refusal-Beispiele.
- Ein Eval-Set für Train und Test.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Support-Ton FT
- **Input:** 800 jsonl, 20% val
- **Prompt:**

```text
Baseline eval then ft plan lora local.
```

- **Erwartetes Ergebnis:**

```text
baseline scores | train plan | safety cases included
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Kundendaten CSV
- **Input:** no DPA
- **Prompt:**

```text
Train on exported tickets.
```

- **Erwartetes Ergebnis:**

```text
block until rights confirmed | anonymize guide
```