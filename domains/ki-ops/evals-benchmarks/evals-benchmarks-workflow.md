---
id: evals-benchmarks-workflow
title: "Evals und Benchmarks"
domain: ki-ops
category: evals-benchmarks
tags:
  - evals
  - ki-ops
  - quality
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes evals / defineEval
    install: "https://hermes-agent.nousresearch.com/docs/"
    version_notes: "Wenn Agent-SDK im Projekt"
  - name: pytest / harness
    install: "pip: deepeval optional"
    version_notes: "Lokal reproduzierbar"
inputs:
  - "Skill/Agent unter Test"
  - "Golden cases (input, expected rubric)"
outputs:
  - "Eval suite Definition"
  - "Pass/Fail Report"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Agenten und Skills **mesbar** verbessern: Golden Tasks, Rubriken, Regression vor Release — nicht nur subjektives „fühlt sich gut an“.

## Wann nutzen

- Vor Promotion Branch → main.
- Nach Prompt- oder MCP-Änderung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Golden dataset | Fixture | Stabil |
| Rubric scores | Judging | LLM oder human |
| CI job | Gate | Block merge |

## System-Prompt / Instruktionen

```text
Role: eval engineer (ki-ops/evals-benchmarks).
Mission: Define repeatable cases with rubrics—not single happy path demo.

Case format: id task input_files expected_rubric dimensions correctness safety tokens_used optional.
Rubric each dimension 0-1 weight sum 1; pass threshold 0.85 unless safety dimension must be 1.0.
Safety cases: must refuse illegal delete payment; score fail if executed.
Determinism: pin model temperature 0 for eval runs document model id date.
Metrics: pass rate latency p95 cost per case from logs.
Regression: new case for every production bug ticket id link.
Human eval: sample 10% weekly inter-rater note.
Synthetic data only label Beispieldaten; no customer pii in repo.
Automate: shell runner agent-sdk bdk eval run or pytest marker @agent.
Flaky: max 2 retries document flake rate separate from fail.
Baseline: store main branch scores compare pr delta warn >5% drop.
Output eval_report.md table case_id score notes.
No eval without version bump on skill or prompt being tested.
```

## Arbeitsablauf

1. Unter-Test-Artefakt und Version pinnen.
2. 5–15 Golden Cases aus realen Tickets anonymisiert.
3. Rubrik pro Dimension schreiben.
4. Harness lokal ausführen.
5. Scores mit Baseline vergleichen.
6. Flakes markieren und fixen oder quarantinen.
7. CI-Gate dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] ≥5 Cases inkl. Safety-Negative
- [ ] Rubrik gewichtet dokumentiert
- [ ] Reproduzierbarer Run-Befehl
- [ ] Baseline-Vergleich

## Sicherheit & Freigaben

- Keine Prod-Daten in Fixtures.

## Fallstricke

- Nur Happy-Path → Prod-Bug bleibt ungetestet.
- LLM-as-judge ohne Rubric → Drift.
- Flaky als Pass gezählt.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** CRM skill regression
- **Input:** 8 cases draft note only
- **Prompt:**

```text
eval suite rubric accuracy refusal write without token.
```

- **Erwartetes Ergebnis:**

```text
cases/*.yaml | pass 7/8 | fail documented case id
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Ship without eval
- **Input:** urgent Friday
- **Prompt:**

```text
Skip eval merge now.
```

- **Erwartetes Ergebnis:**

```text
minimum smoke eval recommended | risk note in report
```