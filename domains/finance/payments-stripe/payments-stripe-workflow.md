---
id: payments-stripe-workflow
title: "Stripe reporting read-only"
domain: finance
category: payments-stripe
tags:
  - stripe
  - payments
  - read-only
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Stripe Agent Toolkit
    install: "https://github.com/Stripe/agent-toolkit"
    version_notes: "Official; Hermes optional-mcp stripe"
inputs:
  - "Berichtszeitraum"
  - "Metriken (MRR, refunds)"
outputs:
  - "stripe_report.md"
  - "CSV-Exporte"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Stripe-data lesen**—Charges, Refunds, Subscriptions—Reports and CSV, **no Refunds, no neuen Charges** without approval.

## When to use

- Monatsumsatz, Churn, Dispute-overview.
- agent with Stripe MCP Toolkit read scope.
- Vorbereitung Finance-Review.

######################################################################## When not to use

- Zahlungen auslosen or Preise change.
- Kunden-Payment-Methods exponieren in Logs.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Stripe Agent Toolkit | API read | Official |
| pandas | Aggregate | Reports |
| Hermes stripe MCP | Optional | Catalog |

## System prompt

```text
You read Stripe data via official toolkit/MCP—write operations forbidden unless user types explicit WRITE APPROVED with operation list.

Inputs: start_date end_date, metrics (revenue, refunds, disputes, subscriptions active count), output stripe_report.md, optional charges_sample.csv masked.

Read paths only: list charges, balance transactions, refunds, subs count—paginate and respect rate limits.

Mask customer email to first char***@domain in outputs.

Never log secret api keys; assume env STRIPE_SECRET_KEY set locally.

Disputes: status counts only no card numbers.

MRR estimate: document method simple sum active price intervals—label ESTIMATE not accounting truth.

Approvals: export csv to external email requires user yes.

No refunds create, no payment intent create, no price update.

Output summary tables and caveats on currency mix.

If test mode vs live mismatch stop and ask.

Document API calls count.

Handle inclusive tax per stripe object fields when present.
Separate test mode rows if mixed key error.
Round EUR 2 decimals display.
Include created_at timezone UTC in report header.
Flag large refunds > threshold user sets default 1000 eur.
```

## Workflow

1. test vs live key bestatigen.
2. Zeitraum UTC festlegen.
3. Paginierte Reads.
4. Aggregate in pandas.
5. stripe_report.md.
6. Maskierte CSV optional.
7. No Write-APIs.

## Definition of done

- [ ] Nur read calls geloggt
- [ ] PII maskiert
- [ ] test/live klar
- [ ] ESTIMATE labels
- [ ] Release before external CSV

## Security

- Secret key not in Chat.
- No silent Refunds.
- PCI: no Vollkartennummern.

## Pitfalls

- Testdaten in Live-Report.
- Pagination unvollstandig.
- MRR naive Summe.
- Fee net vs gross.
- Timezone UTC vs local.

## Basic examples

### Example 1 (Example data)

- **Task:** Oktober Revenue Report.
- **Input:** 2026-10-01..31 live mode.
- **Prompt:**

```text
stripe_report.md revenue refunds disputes; read only; mask emails.
```

- **Expected result:**

```text
report with totals; log only read endpoints; masked samples.
```

### Example 2 (Example data)

- **Task:** Refund write ablehnen.
- **Input:** User asks refund customer X.
- **Prompt:**

```text
Deny write without WRITE APPROVED; suggest manual dashboard steps only.
```

- **Expected result:**

```text
No refund API call; denial message with manual steps.
```