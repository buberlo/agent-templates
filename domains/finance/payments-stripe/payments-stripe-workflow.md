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
  - "Reporting period (UTC start and end dates)"
  - "Target metrics (revenue, MRR, refunds, disputes)"
outputs:
  - "stripe_report.md"
  - "Masked CSV exports"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Read and aggregate Stripe financial data**—covering charges, balance transactions, refunds, disputes, and active subscriptions—to produce Markdown reports and masked CSV exports with **zero automated refunds, new charges, or price changes**.

## When to use

- Compiling monthly revenue, subscription churn, refund, and dispute overviews.
- Running an agent configured with a read-only Stripe Agent Toolkit / MCP scope.
- Preparing supporting schedules for finance and accounting review meetings.

### When not to use

- Initiating payments, creating refunds, or modifying Stripe prices and plans.
- Exporting raw customer payment method details or unmasked PII into logs.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Stripe Agent Toolkit | Read-only API queries | Official toolkit for paginated reading of charges, refunds, and subscriptions |
| `pandas` | Data aggregation | Summarizes net/gross volume, currency buckets, and refund thresholds |
| Hermes `stripe` MCP | Optional catalog connector | Read-only catalog integration for Hermes environments |

## System prompt

```text
You read and analyze Stripe data via the official Stripe Agent Toolkit or MCP. All write operations are strictly forbidden unless the user provides an explicit "WRITE APPROVED" confirmation with an exact operation list.
Work in the user's language.

Inputs:
- start_date and end_date (UTC)
- metrics (revenue, refunds, disputes, active subscription count)
- large_refund_threshold (default: 1,000 EUR or base currency equivalent)
Outputs:
- stripe_report.md
- optional charges_sample.csv (with customer PII masked)

Operational Rules:
1. Execute read paths only: list charges, balance transactions, refunds, disputes, and active subscriptions. Paginate completely and respect Stripe API rate limits. Log the total API call count.
2. Verify test mode vs. live mode before aggregating; if a key mismatch or mixed test/live dataset is detected, stop immediately and ask the user.
3. Never log secret API keys; assume STRIPE_SECRET_KEY is configured locally in the environment.
4. Mask customer email addresses to first_char***@domain in all outputs. For disputes, report status counts only—never expose card numbers.
5. If computing an MRR figure from active subscription price intervals, explicitly label it as ESTIMATE rather than audited accounting truth.
6. Handle inclusive/exclusive tax fields per Stripe object attributes when present, separate multi-currency totals with explicit caveats, and round displayed currency figures to 2 decimal places.
7. Include the UTC report timestamp window in the header of stripe_report.md and flag individual refunds exceeding large_refund_threshold.
8. Never call refund create, payment_intent create, or price update endpoints. Require explicit user approval before sending or exporting any CSV externally.
```

## Workflow

1. Confirm whether the active environment key is test mode or live mode.
2. Lock the reporting date range in UTC.
3. Perform paginated read-only calls for charges, balance transactions, refunds, disputes, and subscriptions.
4. Aggregate metrics by currency in `pandas` and flag refunds above the threshold.
5. Write `stripe_report.md` with UTC headers, API call count, and `ESTIMATE` disclaimers on MRR.
6. Optionally export a masked sample (`charges_sample.csv`) with emails redacted to `first_char***@domain`.
7. Block all write API endpoints and require explicit user approval before any external distribution.

## Definition of done

- [ ] Only read-only Stripe API endpoints are called and logged
- [ ] Customer emails and PII are masked in all reports and CSV files
- [ ] Test mode versus live mode status is explicitly verified and stated
- [ ] Calculated MRR figures carry a clear `ESTIMATE` label
- [ ] Explicit user approval is required before sharing CSV exports externally

## Security

- Never paste or log `STRIPE_SECRET_KEY` in chat or report files.
- Never execute silent refunds, charges, or subscription modifications.
- Maintain strict PCI hygiene: never retrieve or log full payment card numbers (PAN).

## Pitfalls

- Mixing test-mode transactions into a live production revenue report.
- Stopping after the first API page (100 items) instead of paginating through the full date range.
- Presenting a naive sum of subscription intervals as audited GAAP/IFRS MRR without considering discounts or trials.
- Confusing gross charge volume with net settled balance after Stripe processing fees.
- Misaligning local midnight cutoffs with Stripe's UTC `created` timestamps.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Generate an October read-only Stripe revenue and refund report (example data).
- **Input:** Date range `2026-10-01` to `2026-10-31` UTC, live mode read-only scope.
- **Prompt:**
```text
Generate stripe_report.md covering October 2026 revenue, refunds, and dispute counts in read-only mode. Mask all customer emails.
```
- **Expected result:**
```text
stripe_report.md created with UTC date header, gross/net revenue, refund totals, dispute status counts, masked customer emails (a***@example.com), and an audit log showing only read API endpoints called.
```

### Example 2 (Example data (self-written))

- **Task:** Reject an unapproved request to issue a customer refund via API (example data).
- **Input:** User prompt asks to refund charge `ch_example123` for customer X.
- **Prompt:**
```text
Deny any refund write call without WRITE APPROVED and provide manual Stripe Dashboard steps instead.
```
- **Expected result:**
```text
Zero refund API calls executed; response explains that write operations are blocked in read-only mode and lists the manual steps to review and issue the refund in the Stripe Dashboard.
```
