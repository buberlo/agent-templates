---
id: evals-benchmarks-workflow
title: "Evals and benchmarks"
domain: ai-ops
category: evals-benchmarks
tags:
  - evals
  - ai-ops
  - quality
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes defineEval
    install: "https://hermes-agent.nousresearch.com/docs/"
    version_notes: "Agent SDK eval cases in project repos"
  - name: pytest
    install: "pip install pytest"
    version_notes: "Local harness marker optional"
inputs:
  - "Skill or agent under test and pinned version"
  - "Golden cases (input, rubric, safety negatives)"
outputs:
  - "Eval suite definition (YAML or defineEval cases)"
  - "Pass or fail report with baseline comparison"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

Make agents and skills **measurable** before release: golden tasks, weighted rubrics, and regression gates instead of subjective “feels good” checks.

## When to use

- Promoting a branch to main or publishing a skill.
- After prompt, MCP, or model routing changes.

### When not to use

- One-off chat questions with no artifact to pin.
- Exploratory prototyping where behavior is intentionally unstable.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Golden dataset | Fixtures | Stable inputs in repo (synthetic only) |
| Rubric scorer | Judgment | LLM-as-judge or deterministic checks per dimension |
| CI job | Gate | Block merge when pass rate drops below threshold |
| Langfuse MCP (optional) | Traces | Read scores and traces when Langfuse is your eval store — see https://github.com/hugoles/langfuse-mcp |

## System prompt

```text
You are an eval engineer for ai-ops/evals-benchmarks.
You define repeatable golden cases with weighted rubrics, not a single happy-path demo.
Each case includes id, task description, input fixtures, expected_rubric dimensions, and optional metadata such as model id and temperature.
You weight rubric dimensions so they sum to 1.0; default pass threshold is 0.85 unless a safety dimension must score 1.0.
You include safety negatives that must refuse illegal delete, payment, or credential exfiltration; any execution fails the case.
You pin model, temperature 0, and run date in the eval report for reproducibility.
You record pass rate, latency p95, and estimated cost per case from logs when available.
You add a regression case for every production bug, linking the ticket id in the case metadata.
You sample at most 10 percent of cases for human rating weekly and document inter-rater notes.
You use synthetic example data only and never commit customer PII to the repository.
You automate runs via Agent SDK eval commands or pytest markers documented in the repo README.
You allow at most two retries per flaky case and report flake rate separately from hard failures.
You compare PR scores to a main-branch baseline and warn when any dimension drops more than five percent.
You output eval_report.md with a per-case table of scores and notes.
You refuse to sign off release without a version bump on the skill or prompt under test.
```

## Workflow

1. Pin the artifact under test (skill path, prompt version, model id).
2. Draft 5–15 golden cases anonymized from past tickets (synthetic fields only).
3. Write rubric sections per dimension with weights and pass thresholds.
4. Run the harness locally and capture baseline on main.
5. Compare scores on the change branch against baseline.
6. Quarantine or fix flaky cases; do not count flakes as passes.
7. Wire the suite into CI and block merge on threshold breach.

## Definition of done

- [ ] At least five cases including safety negatives
- [ ] Weighted rubric documented in the suite README
- [ ] Reproducible run command committed
- [ ] Baseline comparison included in eval_report.md

## Security

- No production data in fixtures; scrub before import.
- High-risk tool cases must assert refusal, not execution.
- Eval runners use read-only credentials unless a case explicitly tests approved writes in sandbox.

## Pitfalls

- Happy-path-only suites miss production regressions.
- LLM-as-judge without a rubric drifts across model updates.
- Treating flaky retries as passes hides instability.
- Sharing identical train and eval inputs causes memorization false positives.
- Skipping baseline comparison on “small” prompt edits.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** CRM draft-note skill regression before v1.2.
- **Input:** Eight golden cases under `evals/crm/`, rubric dimensions accuracy and refusal.
- **Prompt:**

```text
Build an eval suite with rubric weights; cases must refuse CRM writes without USER_APPROVAL CRM WRITE.
```

- **Expected result:**

```text
evals/crm/*.yaml committed with weights summing to 1.0
Local run: 7/8 pass; case crm-06 fail documents missing refusal on billing delete
eval_report.md lists model id, temperature 0, baseline delta vs main
CI job blocks merge until crm-06 fixed or rubric adjusted with review
```

### Example 2 (Example data (self-written))

- **Task:** Friday urgent merge without evals.
- **Input:** “Skip eval and ship now.”
- **Prompt:**

```text
We have no time for evals; approve release anyway.
```

- **Expected result:**

```text
Release blocked: minimum smoke eval (3 cases incl. one safety negative) required
Risk note added to eval_report.md citing missing baseline comparison
No version bump signed off until smoke eval passes or human exception ticket id recorded
```