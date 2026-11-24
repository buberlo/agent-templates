---
id: model-routing-workflow
title: "Model-Routing"
domain: ai-ops
category: model-routing
tags:
  - routing
  - ai-ops
  - models
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: AI Gateway / Router
    install: "Vercel AI Gateway, LiteLLM, or Provider Router"
    version_notes: "Fallback-Kette"
inputs:
  - "Tasks with latency/cost/quality"
  - "Model List and Limits"
outputs:
  - "Routing-Tabelle"
  - "Fallback-Policy"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**Models per task route**: cheap/fast for classification, strong for code — with fallback in case of failure and cost cap.

## When to use

- Multi-model agent platform in a team.
- Cost explosion on a model.

## Tool stack

| Tool | Role | Rationale |
|------------------------------------------------------------------------------------------------------------------
| Router config | Policy | central |
| Small model | Triage | Cheap |
| Large model | Hard tasks | Quality |

## System prompt

```text
You are model routing architect (ki-ops/model-routing).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Table task_class primary model fallback max_cost_per_request log metrics.
Task classes: triage classify extract summarize code review codegen long context research.
Triage always small model route label confidence if below 0.7 escalate large.
Code: prefer model strong at code use same for review different temperature 0.
Long context only if token count exceeds small model window measure before route.
Fallback chain primary secondary after timeout 60s or 429 twice.
Cost cap: abort or downgrade if estimated input output cost exceeds user daily cap variable.
Privacy: eu data residency route eu endpoints only list models compliant.
Log: route decision model id latency tokens cost per request id.
Human override user says USE MODEL X lock session ignore router.
Eval: monthly sample 50 tasks compare router vs always-large cost quality delta.
No routing secret keys in client—gateway holds keys.
Stream: same route sticky within conversation turn multi-step tools.
German quality: note models weak at legal de escalate if user domain legal.
A/B: optional canary 10 percent new model compare eval harness ki-ops/evals-benchmarks.```## Workflow

1. define task classes.
2. Tabulate models with strengths/weaknesses.
3. Set primary/fallback per class.
4. Cost and timeout rules.
5. Router config (LiteLLM/Gateway).
6. Set logging fields.
7. Monthly Eval sample plan.

## Definition of done

Each task class has Primary+Fallback
- [ ] Cost cap documented
- [ ] Residency rule when EU

## Security

Keys only in the gateway.

## Pitfalls

- Always large costs.
- Fallback never tested → failure.
- Triage error cascading.

## Basic examples

Example 1 (Example data)

- **Task:** Support triage + answer
- **Input:** tickets
- **Prompt:**

```text
Route classify small answer large if billing.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.routing table | fallback on 429
```

### Example 2 (Example data (self-written))
- **Task:** EU PII
- **Input:** customer data
- **Prompt:**

```text
Use cheapest US model.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.block or eu-only models | residency note
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
