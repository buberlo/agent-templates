---
id: invoicing-workflow
title: "Invoices and payment status"
domain: finance
category: invoicing
tags:
  - invoices
  - stripe
  - ar
target_agents:
  - hermes
  - generic
required_tools:
  - name: Stripe Agent Toolkit
    install: "https://github.com/Stripe/agent-toolkit"
    version_notes: "Read invoices"
  - name: python
    install: "pip: pandas"
    version_notes: "Open-items merge"
inputs:
  - "Invoice export CSV or Stripe read scope"
  - "Payment status records"
outputs:
  - "Open-items aging overview (CSV and Markdown)"
  - "Dunning draft suggestions"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Consolidate **invoices and open accounts receivable (AR) items**—tracking `paid`, `open`, `partial`, and `overdue` statuses, calculating aging buckets, and generating dunning text strictly as **draft suggestions without automatically sending dunning emails or creating invoices**.

## When to use

- Building an accounts receivable (AR) overview from Stripe read data and internal invoice lists.
- Preparing billing operations and collections review meetings.
- Cross-referencing open invoices with bank reconciliation outputs (`camt053` `match.csv`).

### When not to use

- Issuing legally binding collection notices or formal legal dunning without legal/process review.
- Performing tax accounting or VAT advisory tasks.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Stripe Agent Toolkit (read-only) | Read invoices and payment intents | Fetches live invoice statuses without creating or mutating charges |
| `pandas` | Open-items merge and aging | Computes overdue days, partial balances, and 30/60/90-day buckets |
| `docx` / `pdf` tools | Optional draft formatting | Formats dunning letter drafts locally after text review |

## System prompt

```text
You reconcile invoices and payment statuses in read-only mode. Never create invoices, mark invoices paid in an ERP, write off bad debt, or send invoice/dunning emails automatically.
Work in the user's language (default to English).

Inputs:
- invoices.csv or Stripe read date range
- optional payments list or camt053 match.csv
- aging_buckets (default: 30 / 60 / 90 days)
Outputs:
- opos.csv (open-items table) and opos.md (narrative summary)

Rules:
1. Map invoice_id, customer, amount, balance_due, due_date, currency, and normalized status (paid | open | partial).
2. Flag an invoice as overdue when due_date < today and open balance_due > 0. Assign each open line to its aging bucket.
3. When reading from Stripe, inspect invoices and payment_intents in read-only mode only—never call invoice creation or collection endpoints. Include Stripe-hosted invoice PDF links only in internal reports, never in public outputs.
4. When a camt053 match.csv is provided, link matched bank payments by invoice ID and update the remaining open balance_due column for partial payments.
5. Sort open items by open balance descending, explicitly document currency, and round amounts to exact cents (2 decimal places) in CSV exports.
6. Pass VAT/tax columns through untransformed without providing tax advice.
7. Generate dunning notice templates per aging bucket strictly marked as SUGGESTION. Use locale-specific date formats in customer-facing drafts if requested by the user. Require explicit user and legal approval before any dunning message is sent.
8. Mask customer PII in sample logs and previews.
```

## Workflow

1. Ingest the invoice CSV export, optional Stripe read feed, and any bank reconciliation match file.
2. Normalize invoice statuses (`paid`, `open`, `partial`) and verify currency consistency.
3. Calculate overdue days, remaining `balance_due`, and 30/60/90-day aging buckets.
4. Export the sorted open-items dataset to `opos.csv` rounded to 2 decimal places.
5. Generate the `opos.md` summary highlighting top overdue accounts and aging totals.
6. Produce dunning text drafts clearly labeled as `SUGGESTION` for each aging tier.
7. Obtain explicit human sign-off before sending any dunning communication or updating ERP records.

## Definition of done

- [ ] No invoices are created, modified, or emailed automatically
- [ ] Aging buckets (30/60/90 days) and partial payment balances are accurately calculated
- [ ] Customer PII is masked in sample outputs and logs
- [ ] Dunning drafts are explicitly marked as `SUGGESTION`
- [ ] Stripe integration operates strictly in read-only mode

## Security

- Never send silent reminder or dunning emails to customers; require explicit human approval for all external communications.
- Protect invoice data, hosted PDF links, and customer billing details as confidential financial records.
- Require legal or finance team sign-off on dunning templates before external use.

## Pitfalls

- Ignoring partial payments and dunning a customer for the original full invoice amount.
- Miscalculating due dates across timezones around midnight.
- Confusing Stripe `draft` invoices with finalized `open` invoices.
- Failing to deduplicate invoice IDs when merging Stripe data with an internal CSV.
- Summing open receivables across mixed currencies without separating totals by currency code.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Generate an aged open-items overview from an invoice CSV (example data).
- **Input:** `invoices.csv` containing 50 rows (example data).
- **Prompt:**
```text
Compute 30/60/90-day aging from invoices.csv, export opos.csv, and list the top 10 open invoices by balance due in opos.md. Do not send any emails.
```
- **Expected result:**
```text
opos.csv and opos.md generated with 30/60/90-day aging buckets and top 10 open items sorted by amount descending; zero emails sent.
```

### Example 2 (Example data (self-written))

- **Task:** Refuse an automated dunning send request and output a draft suggestion instead (example data).
- **Input:** Overdue invoice list; user prompt asks to send dunning emails immediately.
- **Prompt:**
```text
Output the dunning notice as suggestion text only; do not send any emails.
```
- **Expected result:**
```text
Saved dunning_draft.txt clearly labeled as SUGGESTION; no email or Stripe collection API called.
```
