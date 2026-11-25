---
id: model-routing-workflow
title: "Model routing"
domain: ai-ops
category: model-routing
tags:
  - routing
  - ai-ops
  - models
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
  - generic
required_tools:
  - name: LiteLLM
    install: "https://docs.litellm.ai/docs/"
    version_notes: "Proxy router with fallbacks"
  - name: Vercel AI Gateway
    install: "https://vercel.com/docs/ai-gateway"
    version_notes: "Optional hosted routing and budgets"
inputs:
  - "Task classes with latency, cost, and quality targets"
  - "Model list, limits, and residency rules"
outputs:
  - "Routing table per task class"
  - "Fallback policy and logging fields"
risk_level: low
example_count: 2
version: "1.2.0"
updated: "2026-11-25"
---

## Purpose

**Route models by task class**: cheap models for triage, stronger models for code and long context — with tested fallbacks, cost caps, and residency rules.

## When to use

- Multi-model agent platforms where cost or latency spiked on a single model.
- Teams standardizing router config across Hermes, Cursor, and Grok Bot.

### When not to use

- Single-model deployments with flat pricing and no SLO variance.
- Ad hoc per-chat model picking without logging.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| LiteLLM proxy | Policy | Central model_list and fallbacks — https://docs.litellm.ai/docs/ |
| Small model | Triage | Classification and extraction |
| Large model | Hard tasks | Code review and long context |
| Vercel AI Gateway | Optional | Team budgets — https://vercel.com/docs/ai-gateway |

## System prompt

```text
You are a model routing architect for ai-ops/model-routing.
You maintain a routing table linking task_class to primary model, fallback chain, and max_cost_per_request.
You define task classes such as triage, classify, extract, summarize, code_review, codegen, long_context, and research.
You route triage and classify tasks to the smallest adequate model and escalate when confidence is below 0.7.
You prefer one strong code model for review at temperature 0 and a separate codegen profile when evals justify it.
You measure token count before routing long_context and only then select models with sufficient windows.
You configure fallback chains to secondary models after 60 second timeouts or two consecutive HTTP 429 responses.
You abort or downgrade when estimated cost exceeds the user’s daily cap variable documented in config.
You honor EU data residency by routing only to endpoints and models the user lists as compliant.
You log route decision, model id, latency, tokens, and cost per request id for monthly review.
You honor session overrides when the user sends USE MODEL <id> and document the override in logs.
You sample 50 tasks monthly comparing router decisions to always-large baseline on cost and quality.
You keep API keys only in the gateway or proxy, never in client repositories.
You keep streaming routes sticky within a multi-step tool turn when the host supports it.
You link eval suites from ai-ops/evals-benchmarks when proposing A/B canaries on new models.
```

## Workflow

1. Enumerate task classes from real traffic samples.
2. Tabulate models with strengths, weaknesses, and price per million tokens.
3. Assign primary and fallback per class with timeout rules.
4. Document cost caps and residency constraints.
5. Implement router config in LiteLLM or AI Gateway YAML.
6. Define structured log fields for observability.
7. Schedule monthly eval sampling and cost review.

## Definition of done

- [ ] Every task class has primary and fallback documented
- [ ] Cost cap and downgrade behavior defined
- [ ] Residency rule recorded when EU PII is in scope
- [ ] Fallback path tested with simulated 429

## Security

- Keys live only in the gateway or proxy vault.
- Do not route customer PII to non-approved regions.
- Override keywords should not bypass safety classifiers.

## Pitfalls

- Always routing to the largest model raises cost without measured quality gain.
- Fallback chains never tested fail during provider outages.
- Triage mislabels cascade into wrong downstream tools.
- Confidence thresholds copied from blogs without domain evals.
- Sticky streaming routes stick on the wrong model after escalation.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Support triage then detailed answer.
- **Input:** 500 synthetic tickets per day; billing intents need strong model.
- **Prompt:**

```text
Route classify to a small model; escalate to large only when intent is billing or confidence low.
```

- **Expected result:**

```text
routing_table.yaml: triage→gpt-4.1-nano, billing→gpt-4.1, fallback chain on 429 documented
LiteLLM config includes 60s timeout and two-retry fallback to secondary
Log fields: task_class, model_id, confidence, tokens, cost_usd
Simulated 429 test shows fallback invocation in logs
```

### Example 2 (Example data (self-written))

- **Task:** EU customer PII in prompts.
- **Input:** “Use the cheapest US-hosted model for everything.”
- **Prompt:**

```text
Minimize cost; US endpoints are fine.
```

- **Expected result:**

```text
Proposal blocked or revised: eu_only model list with residency note in routing_table.md
Non-EU models flagged as disallowed for customer_data class
Human review ticket required before exceptions
```