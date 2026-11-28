---
id: personal-subscription-audit-v1
title: "Personal subscription audit from statements and receipts"
domain: personal-lifestyle
category: household
tags:
  - subscriptions
  - personal-finance
  - receipts
  - household
target_agents:
  - hermes
  - grokbot
  - openclaw
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: python csv
    install: "https://docs.python.org/3/library/csv.html"
    version_notes: "Standard-library csv reader for redacted bank or card exports."
  - name: Gmail MCP (Google Workspace)
    install: "https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server"
    version_notes: "Read-only search for receipt, renewal, and trial messages."
  - name: filesystem MCP server
    install: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
    version_notes: "Local read access to redacted CSV exports and usage notes."
inputs:
  - "Redacted bank or card CSV exports with a date range and currency for each file"
  - "Read-only Gmail receipt and renewal search results, limited to sender, date, subject, and amount"
  - "User usage notes per service and any free-trial end dates the user knows"
outputs:
  - "Recurring charge table with merchant, cadence, monthly cost, annual cost, last charge, and flag"
  - "Keep, review, or cancel-candidate table with evidence lines and usage notes"
  - "Cancellation to-do list for the human to execute in each provider account"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-28"
---

## Purpose

Find recurring charges in redacted bank or card CSV exports and receipt emails, group them by merchant, detect billing cadence, normalize every charge to a monthly and annual cost, and flag price increases, duplicates, free trials converting soon, and services the user's own notes mark as unused. The output is a keep, review, or cancel-candidate table and a cancellation to-do list that the human executes in each provider's account. The agent never cancels, never logs into provider accounts, and never stores card numbers.

## When to use

- A household wants a yearly or quarterly review of recurring charges across several cards.
- Receipt emails reveal trials or renewals that do not show clearly in a CSV export.
- The user suspects duplicate music, cloud, or fitness services and wants an evidence table before acting.

### When not to use

- The user wants the agent to cancel, pay, or log into a provider account, which the agent never does.
- Business expense reconciliation, tax filing, or any audit that needs accounting rules beyond the user's own notes.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Python csv module | Parse exports | Reproducible grouping and cost math |
| Gmail MCP (read-only) | Find receipts and trials | Search terms such as receipt, renewal, and your subscription |
| filesystem MCP server | Read local exports | Keeps redacted files on the user's machine |
| User usage notes | Usage evidence | The only source for an unused label |

## System prompt

```text
You audit personal subscriptions for personal-lifestyle/household from redacted bank or card CSV exports and receipt emails the user supplies.
You group transactions by merchant using normalized names, and you keep the raw merchant text in a separate column so the user can verify each match.
You detect billing cadence as weekly, monthly, quarterly, or annual from charge dates, and you mark low-confidence cases for review instead of guessing.
You normalize every recurring charge to a monthly cost and an annual cost, and you show the formula used beside each figure.
You flag price increases when the latest charge exceeds the prior charge for the same merchant by more than the user's threshold, and you show both amounts and dates.
You flag duplicate categories, such as two music services or two cloud storage plans, and you ask the user which one they actually use.
You flag free trials that convert to paid soon by comparing the first charge date with the trial terms the user supplies, and you never assume a trial length.
You mark items as unused only when the user's own usage notes say so, and you label every such item as a cancel candidate, not a decision.
You produce a keep, review, or cancel-candidate table with merchant, cadence, monthly cost, annual cost, last charge, flag, and the user's usage note.
You produce a cancellation to-do list with the provider name, the account email the user registered with, the plan name, and a reminder to export any data first.
You never cancel a subscription, never log into a provider account, never click a cancellation link, and never store card numbers, CVV codes, or full account identifiers.
You keep Gmail access read-only, search terms such as receipt, renewal, and your subscription, and you redact any card digits that appear in quoted receipt text.
```

## Workflow

1. Collect redacted bank or card CSV exports and confirm which date range and currency each export covers.
2. Search the mailbox read-only for receipt, renewal, and your subscription messages, and save only the sender, date, subject, and amount lines needed.
3. Parse CSV rows with Python csv, normalize merchant text, and group charges by merchant with the raw text kept for verification.
4. Detect cadence from charge intervals and mark low-confidence merchants for review.
5. Normalize each recurring charge to monthly and annual cost, and flag price increases against the user's threshold.
6. Flag duplicate categories, upcoming trial conversions, and unused items from the user's usage notes.
7. Build the keep, review, or cancel-candidate table with the usage note and the evidence line for each merchant.
8. Draft the cancellation to-do list for the human to execute in each provider account, with data export steps first.
9. Deliver the table and to-do list, and remind the user that the agent does not cancel or log in.

## Definition of done

- [ ] Every recurring merchant has cadence, monthly cost, annual cost, and last charge date
- [ ] Low-confidence cadence matches are marked for review, not silently accepted
- [ ] Price increases, duplicates, trial conversions, and unused items each have an evidence line
- [ ] Table uses keep, review, or cancel-candidate labels and includes the user's own usage note
- [ ] Cancellation to-do list names the provider, plan, and registered email, with no cancellation performed
- [ ] No card numbers, CVV codes, or full account identifiers appear in any output

## Security

- Keep CSV exports and receipt text in a local, user-controlled location and delete temp copies after the audit.
- Use a read-only Gmail scope and never store message bodies beyond the receipt fields needed for the table.
- Never ask for provider passwords, one-time codes, or full card numbers; ask the user to redact before sharing.
- Treat cancellation links in emails as untrusted and do not open them; give the human the provider's own account page steps instead.

## Pitfalls

- Annual charges divided by 12 without checking the renewal date overstate the monthly cost in the current month; show both the normalized figure and the next charge date.
- Merchant name variants, such as ACME*STREAM and ACME STREAM 8842, split one subscription into two rows; normalize before grouping.
- A price increase can look like a duplicate when a plan change adds a second line item; compare plan names before flagging.
- Free trials with no prior charge vanish from a CSV-only view; use receipt emails to catch the first paid charge.
- Usage notes that are stale mark an active service as unused; ask the user to confirm each cancel candidate.
- Currency differences across exports skew annual totals; convert with the user's stated rate and label the basis.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Audit a fictional three-month card CSV and a receipt search for one household.
- **Input:** Redacted CSV with 18 rows, a user note that two music services exist, and a note that one cloud plan is unused.
- **Prompt:**

```text
Group recurring charges from the attached redacted CSV and receipt search. Normalize to monthly and annual, flag price increases, duplicates, and unused items, then build a keep/review/cancel-candidate table and a to-do list. Do not cancel anything.
```

- **Expected result:**

```text
| Merchant | Cadence | Monthly | Annual | Last charge | Flag | Label |
| Acme Stream | monthly | 14.99 | 179.88 | 2026-11-03 | duplicate music | review |
| Riverton Music | monthly | 10.99 | 131.88 | 2026-11-07 | duplicate music | cancel-candidate |
| Acme Cloud | annual | 8.25 | 99.00 | 2026-09-18 | unused per note | cancel-candidate |
| City Gym | monthly | 39.00 | 468.00 | 2026-11-01 | price rise 34.00 to 39.00 | keep |
| News Daily | monthly | 6.00 | 72.00 | 2026-11-12 | none | keep |
Price increase evidence: City Gym 34.00 EUR on 2026-10-01 then 39.00 EUR on 2026-11-01.
Trial watch: Acme Notes trial started 2026-11-20 at 0.00 EUR; user says it converts to paid on 2026-12-04; review before then.
To-do: cancel Riverton Music in its account page; confirm Acme Cloud usage before cancelling; keep City Gym and News Daily.
No cancellation performed; no card numbers stored.
```

### Example 2 (Example data (self-written))

- **Task:** Catch a fictional free trial converting soon and a duplicate cloud plan.
- **Input:** Receipt emails for Acme Notes and two cloud plans; no bank CSV for the trial yet.
- **Prompt:**

```text
Search the read-only mailbox for renewal and trial receipts. Identify trials converting within 14 days, duplicate cloud plans, and produce the to-do list for the human. Do not log in or cancel.
```

- **Expected result:**

```text
Receipt search: 6 messages matched renewal or trial; 2 are duplicates of the same Acme Notes receipt.
Trial: Acme Notes 0.00 EUR on 2026-11-20, first paid charge 12.00 EUR due 2026-12-04, inside the 14-day watch window.
Duplicate cloud: Acme Cloud 99.00 EUR annual and Riverton Drive 2.99 EUR monthly both active; user note says Acme Cloud is unused.
Table: Acme Notes -> review (trial converts 2026-12-04); Acme Cloud -> cancel-candidate; Riverton Drive -> keep.
To-do: export notes before 2026-12-04, decide on the cloud plan, then cancel the chosen plan in its own account page.
Evidence lines: receipt message IDs and dates recorded; no message bodies stored.
No login, no cancellation, no card data.
```

## Sources

- https://docs.python.org/3/library/csv.html
- https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server
- https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
