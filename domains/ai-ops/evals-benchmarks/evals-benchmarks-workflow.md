---
id: evals-benchmarks-workflow
title: "Evals and Benchmarks"
domain: ai-ops
category: evals-benchmarks
tags:
  - evals
  - ai-ops
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
## Purpose

Agents and skills **mesbar** improve: Golden Tasks, rubrics, regression before release – not just subjective “feels good”.

## When to use

- Before Promotion Branch → main.
- After Prompt or MCP change.

## Tool stack

| Tool | Role | Rationale |
|-----------------------------------------------------------------------------------------------------------------------------
| Golden dataset | Fixture | Stable |
| Rubric scores | Judging | LLM or human |
| CI job | Gate | Block merge |

## System prompt

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
Synthetic data only; label as example data; no customer PII in repo.
Automate: shell runner agent-sdk bdk eval run or pytest marker @agent.
Flaky: max 2 retries document flake rate separate from fail.
Baseline: store main branch scores compare pr delta warn >5% drop.
Output eval_report.md table case_id score notes.
No eval without version bump on skill or prompt being tested.
```

## Workflow

1. Under-test artifact and version pin.
5–15 Golden Cases anonymized from real tickets.
3. Write section per dimension.
4. Harness locally.
5. Compare scores with baseline.
6. Flakes mark and fix or quarantine.
7. CI-gate.

## Definition of done

- [ ] ≥5 cases incl. Safety negatives
- [ ] Heading weighted documented
- [ ] Reproducible run command
- [ ] Baseline comparison

## Security

No Prod data in fixtures.

## Pitfalls

- Only Happy Path → Prod bug remains untested.
- LLM-as-judge without Rubric → Drift.
- Flaky counted as a pass.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** CRM skill regression
- **Input:** 8 cases draft note only
- **Prompt:**

```text
eval suite rubric accuracy refusal write without token.
```

- **Expected result:**

```text
cases/*.yaml | pass 7/8 | fail documented case id
```

### Example 2 (Example data (self-written))
- **Task:** Ship without eval
- **Input:** urgent Friday
- **Prompt:**

```text
Skip eval merge now.
```

- **Expected result:**

```text
minimum smoke eval recommended | risk note in report
```

### Example 1 (Example data (self-written))
- **Task:** Placeholder
- **Input:** example data
- **Prompt:**
```text
Draft only.
```
- **Expected result:** Draft artifact path.
