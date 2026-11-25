---
id: stripe-refund-dispute-investigation-v1
title: "Stripe MCP refund and dispute investigation (read-only)"
domain: finance
category: payments-stripe
tags:
  - stripe
  - refunds
  - disputes
  - read-only
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Stripe Agent Toolkit
    install: "https://github.com/Stripe/agent-toolkit"
    version_notes: "MCP-capable toolkit; restrict tools to list/read before investigation."
inputs:
  - "Customer alias or charge id (ch_...) or payment intent id"
  - "Date window for related balance transactions"
  - "Question type: duplicate charge, missing refund, or open dispute"
outputs:
  - "stripe_investigation.md timeline with masked identifiers"
  - "Recommended human actions list (no API writes executed)"
risk_level: high
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Investigate refunds, disputes, and duplicate charges through Stripe's official Agent Toolkit or MCP integration in read-only mode, producing a finance-ready timeline. The agent does not create refunds, capture payments, or close disputes.

## When to use

- Support escalates a billing question that needs authoritative Stripe object history.
- Month-end reconciliation flags mismatched refund totals against the general ledger.
- You need structured evidence before a human issues `WRITE APPROVED` for a refund API call.

### When not to use

- PCI-heavy flows requiring full card numbers (never pull PAN into chat).
- Instant refund execution during the agent session.
- Tax filing or revenue recognition sign-off (finance officer required).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Stripe Agent Toolkit | List and retrieve objects | Official Stripe tooling with MCP path ([Stripe/agent-toolkit](https://github.com/Stripe/agent-toolkit)) |
| Spreadsheet or pandas | Summarize | Optional offline aggregation of exported rows |
| Internal ticket | Audit | Link investigation id for SOC-style traceability |

## System prompt

```text
You are a billing investigator for finance/payments-stripe using Stripe read APIs only via the Stripe Agent Toolkit or MCP.
You start from the user-supplied charge, payment intent, or customer id and expand to refunds, disputes, and balance transactions within the given date window without calling create, capture, cancel, or refund endpoints.
You paginate list results responsibly and stop when the question is answered to avoid excessive API usage.
You mask customer email as first-character plus stars and domain, and you never print full payment method fingerprints or card last-four unless the user explicitly needs last-four for a matched support ticket.
You label live mode versus test mode on every object id and halt if the user mixes modes in one investigation.
You produce a chronological timeline in UTC with object ids, amounts, currencies, and status fields copied from Stripe objects without inventing FX rates.
You recommend human next steps such as issue refund, respond to dispute, or contact acquiring bank, but you execute zero write operations unless the user types STRIPE WRITE APPROVED with the Stripe id and amount.
You document API object types you queried for audit, and you cite https://github.com/Stripe/agent-toolkit for integration scope.
You flag regulatory or chargeback deadlines using dispute evidence due dates when present in API fields, without legal advice language.
You refuse to export unmasked customer lists to external email addresses in chat.
```

## Workflow

1. Confirm mode (test/live) and investigation question type.
2. Retrieve anchor object (charge or PI) and verify status.
3. List related refunds and disputes; pull balance transaction links.
4. Build masked timeline table and note currency splits.
5. Compare totals to user-provided ledger figure; quantify delta only from cited rows.
6. Output recommended actions with owner role (support, finance, engineering).
7. Store investigation markdown locally; no Stripe writes.

## Definition of done

- [ ] Timeline uses only retrieved Stripe fields with masked PII
- [ ] No refund, capture, or dispute submit calls in session
- [ ] Live versus test mode explicit
- [ ] Delta to ledger explained or marked unknown

## Security

- API keys stay in environment variables; never echo `sk_live` prefixes from config files.
- Restrict MCP tool allowlist to read operations where the client supports it.
- Investigations containing EU customer data follow internal retention policy.

## Pitfalls

- Partial pagination hides older duplicate charges with the same amount.
- Refund failures leave charge succeeded while customer sees pending bank credit.
- Dispute status `needs_response` requires human calendar tracking, not auto replies.
- Subscription credits versus one-off refunds confuse support narratives.
- Toolkit write tools left enabled by misconfiguration cause accidental refunds.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Customer claims double charge on 2026-11-20 for EUR 49.00.
- **Input:** Customer id `cus_Example01`, live mode, window 2026-11-18 to 2026-11-22.
- **Prompt:**

```text
Read-only Stripe investigation: find duplicate EUR 49 charges for cus_Example01 in the date window.
Output stripe_investigation.md timeline.
No refunds.
```

- **Expected result:**

Timeline showing two charges with distinct ids, one succeeded and one failed with `card_declined`, or two succeeded with different descriptors, masked email `j***@example.com`, recommended action to refund only if duplicate succeeded charges confirmed, and explicit STRIPE WRITE APPROVED gate for any refund API call.

### Example 2 (Example data (self-written))

- **Task:** Open dispute on charge `ch_Example99` needs evidence summary.
- **Input:** Dispute reason `fraudulent`, evidence due date field present in API mock.
- **Prompt:**

```text
Summarize dispute status and evidence fields for ch_Example99.
Read-only.
```

- **Expected result:**

Summary listing dispute id, status, amount, reason code, due date copied from dispute object fields, checklist of evidence categories Stripe accepts described generically without filing evidence, and reminder that submitting evidence requires human login to Dashboard or WRITE APPROVED tooling.