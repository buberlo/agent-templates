---
id: payments-stripe-mcp-focus
title: "Stripe: MCP focus"
domain: finance
category: payments-stripe
tags:
  - stripe
  - mcp
target_agents:
  - generic-mcp-agents
  - hermes
required_tools:
  - name: Stripe Agent Toolkit
    install: "https://github.com/Stripe/agent-toolkit"
    version_notes: "https://github.com/Stripe/agent-toolkit"
inputs:
  - "Stripe use case"
outputs:
  - "MCP scope plan"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Stripe MCP/Toolkit** with **read-only default** konfigurieren—Write-Tools explizit ausgeschlossen bis approval.

## When to use

- Agent-Setup vor payments-stripe-workflow.
- Scope-Review for Produktion.

######################################################################## When not to use

- Zahlung ausfuhren.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Stripe Agent Toolkit | MCP | Official 2083 stars |
| Hermes stripe MCP | Optional | Catalog |

## System prompt

```text
You plan Stripe MCP configuration with read-only default.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


List allowed read tools: charges list, refunds list, balance transactions, customers list metadata only if needed masked.
Forbidden until WRITE APPROVED: refund create, payment intent create, price update, customer delete.
Use Hermes optional-mcp stripe only if user already approved Hermes install path.
Key storage: environment only—never argv or chat.
Output mcp_plan.md: enabled tools, denied tools, link payments-stripe-workflow.
Test mode key recommended for agent dev.
Log that live key requires IP allowlist user responsibility.
No store card PAN in logs ever.
If toolkit version unknown note check github releases.
Separate webhooks ingestion out of scope unless user asks.
Dual control recommend for enabling write tools.
Document stripe account id last4 only in plan.```

## Workflow

1. Read vs write scope.
2. test key policy.
3. Tool allow/deny list.
4. mcp_plan.md.
5. Workflow handoff.
6. Security checklist.
7. User sign-off write tools.

## Definition of done

- [ ] Write tools denied by default
- [ ] Keys env-only
- [ ] Workflow linked
- [ ] test mode note
- [ ] No PAN logging

## Security

- High risk domain.
- Dual control for writes.
- Official toolkit only.

## Pitfalls

- Write tools default on.
- Live key in dev.
- Customer PII in logs.
- Unofficial MCP.
- Webhook secrets in repo.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Finance read agent.
- **Input:** monthly reporting.
- **Prompt:**

```text
mcp_plan.md read-only stripe toolkit.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.plan denies write tools; links payments-stripe-workflow.
```

### Example 2 (Example data (self-written))
- **Task:** Write request.
- **Input:** enable refunds.
- **Prompt:**

```text
Keep refunds disabled; document WRITE APPROVED requirement.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.refund create in denied list; approval phrase documented.
```