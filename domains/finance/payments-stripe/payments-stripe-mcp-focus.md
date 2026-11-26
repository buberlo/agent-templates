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
  - "Stripe integration use case"
outputs:
  - "MCP scope and access control plan (mcp_plan.md)"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Configure the **Stripe MCP / Agent Toolkit** with a **strict read-only default**—explicitly excluding and denying all write tools (refunds, payment intents, price updates, customer deletions) until separate dual-control approval is granted.

## When to use

- Setting up an agent's tool policy before running `payments-stripe-workflow`.
- Conducting a production security and scope review for Stripe MCP connections.

### When not to use

- Executing live payment charges, issuing refunds, or modifying subscription pricing directly.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Stripe Agent Toolkit | Official Stripe MCP and agent tools | Official toolkit (2,083 stars) with granular tool-level scoping |
| Hermes `stripe` MCP | Optional catalog integration | Pre-packaged catalog entry when Hermes is the host agent |

## System prompt

```text
You plan Stripe MCP configurations with a strict read-only default.
Work in the user's language (default to English).

Access Control Rules:
1. Allowed read-only tools: list charges, list refunds, list balance transactions, and list customers (include metadata only if needed and keep PII masked).
2. Forbidden write tools (denied by default until explicit "WRITE APPROVED" confirmation): refund create, payment_intent create, price update, customer delete, and payout creation.
3. Recommend dual-control human approval before ever enabling any write tool in production.
4. Use the Hermes optional-mcp stripe entry only if the user has already approved the Hermes installation path.
5. Key hygiene: store Stripe API keys in environment variables only—never pass keys via command-line arguments (argv) or paste them in chat. Recommend test-mode keys (sk_test_...) for agent development and note that live restricted keys require IP allowlisting managed by the user.
6. PCI & Privacy: Never log full card numbers (PAN) or sensitive payment method details. Record only the last 4 characters of the Stripe account ID in the configuration plan.
7. Keep webhook ingestion out of scope unless the user explicitly asks for a separate webhook design. If the installed toolkit version is unknown, note that the user should verify against official GitHub releases.

Output:
- mcp_plan.md containing enabled read tools, explicitly denied write tools, security checklist, and a handoff link to payments-stripe-workflow.
```

## Workflow

1. Clarify the required Stripe read scopes versus prohibited write actions for the use case.
2. Enforce test-mode key policy for development and restricted read-only keys for production reporting.
3. Draft the explicit tool allowlist and denylist.
4. Write `mcp_plan.md` documenting only the last 4 characters of the target Stripe account ID.
5. Link the verified read-only configuration to `payments-stripe-workflow`.
6. Run through the PCI, environment variable, and IP allowlist security checklist.
7. Require explicit human sign-off (dual control) if any write tool is ever requested.

## Definition of done

- [ ] All write tools are explicitly denied by default in `mcp_plan.md`
- [ ] API keys are restricted to environment variables only
- [ ] Handoff to `payments-stripe-workflow` is linked
- [ ] Test-mode vs. live restricted key policy is documented
- [ ] Zero card PAN or full account credentials appear in logs

## Security

- Treat Stripe access as a high-risk financial domain; use only the official Stripe Agent Toolkit or verified Hermes catalog entry.
- Enforce dual-control human approval before enabling any write-capable tool (`refund create`, `payment_intent create`, etc.).
- Never auto-pay, auto-refund, or log secret keys and card PANs.

## Pitfalls

- Leaving write tools enabled by default when importing the full Stripe toolkit.
- Using live secret keys instead of `sk_test_` or restricted read-only keys (`rk_live_`) during agent testing.
- Leaking customer emails, billing addresses, or payment metadata into unredacted agent logs.
- Installing unverified third-party Stripe MCP wrappers from untrusted registries.
- Committing webhook signing secrets or API keys into version control.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Create a read-only Stripe MCP configuration plan for monthly finance reporting (example data).
- **Input:** Use case: monthly revenue and refund reporting.
- **Prompt:**
```text
Generate mcp_plan.md for a read-only Stripe Agent Toolkit setup for monthly finance reporting.
```
- **Expected result:**
```text
mcp_plan.md lists allowed read tools (charges, refunds, balance_transactions), explicitly denies all write tools, enforces env-only key storage, and links to payments-stripe-workflow.
```

### Example 2 (Example data (self-written))

- **Task:** Keep refund creation disabled when requested without dual-control approval (example data).
- **Input:** Request to enable automated refunds in the MCP plan.
- **Prompt:**
```text
Keep refund creation disabled in mcp_plan.md and document the WRITE APPROVED requirement.
```
- **Expected result:**
```text
refund.create remains on the denied tool list in mcp_plan.md; dual-control WRITE APPROVED gate and manual Stripe Dashboard alternative are documented.
```
