---
id: payments-stripe-mcp-focus
title: "Stripe: MCP-Fokus"
domain: finanzen
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
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Stripe MCP/Toolkit** mit **read-only default** konfigurieren—Write-Tools explizit ausgeschlossen bis Freigabe.

## Wann nutzen

- Agent-Setup vor payments-stripe-workflow.
- Scope-Review für Produktion.

**Wann nicht**

- Zahlung ausführen.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Stripe Agent Toolkit | MCP | Official 2083 stars |
| Hermes stripe MCP | Optional | Catalog |

## System-Prompt / Instruktionen

```text
You plan Stripe MCP configuration with read-only default.

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

Document stripe account id last4 only in plan.
```

## Arbeitsablauf

1. Read vs write scope.
2. test key policy.
3. Tool allow/deny list.
4. mcp_plan.md.
5. Workflow handoff.
6. Security checklist.
7. Nutzer sign-off write tools.

## Qualitätskriterien / Definition of Done

- [ ] Write tools denied by default
- [ ] Keys env-only
- [ ] Workflow linked
- [ ] test mode note
- [ ] No PAN logging

## Sicherheit & Freigaben

- High risk domain.
- Dual control for writes.
- Official toolkit only.

## Fallstricke

- Write tools default on.
- Live key in dev.
- Customer PII in logs.
- Unofficial MCP.
- Webhook secrets in repo.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Finance read agent.
- **Input:** monthly reporting.
- **Prompt:**

```text
mcp_plan.md read-only stripe toolkit.
```

- **Erwartetes Ergebnis:**

```text
plan denies write tools; links payments-stripe-workflow.
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Write request.
- **Input:** enable refunds.
- **Prompt:**

```text
Keep refunds disabled; document WRITE APPROVED requirement.
```

- **Erwartetes Ergebnis:**

```text
refund create in denied list; approval phrase documented.
```