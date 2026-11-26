---
id: personal-monthly-budget-variance-v1
title: "Personal monthly budget variance review"
domain: finance
category: budget
tags:
  - budget
  - personal-finance
  - variance
  - spreadsheet
target_agents:
  - hermes
  - cursor
  - generic-mcp-agents
required_tools:
  - name: python
    install: "https://docs.python.org/3/library/csv.html"
    version_notes: "stdlib csv for user-exported sheets; optional pandas if user installs."
  - name: Google Sheets API
    install: "https://developers.google.com/sheets/api"
    version_notes: "Optional MCP or export CSV; read-only."
inputs:
  - "Budget CSV and monthly actuals export (no account numbers in chat)"
  - "Category mapping table and month under review"
  - "Threshold rules for flagging variances (e.g. >15% or >$200)"
outputs:
  - "Variance table by category with flag column and narrative comments"
  - "Suggested adjustments list (human implements transfers or budget edits)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Review **personal or household monthly budget vs. actuals** from CSV or spreadsheet exports, flag material variances, and draft plain-language comments—**without** moving money, filing taxes, or giving personalized investment advice ([Google Sheets API](https://developers.google.com/sheets/api) when used read-only).

Complements generic `budget-workflow.md` with a concrete personal close ritual.

## When to use

- End-of-month household review with categorized bank or card exports.
- Couples aligning on overspend categories before the next month.
- Export-only workflows where MCP has no write access to financial institutions.

### When not to use

- Business GAAP close, payroll tax filings, or regulated investment recommendations.
- Connecting write-capable banking APIs without explicit approval and fraud review.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| CSV / Sheets export | Data | User controls redaction before upload |
| Python csv module | Analysis | Deterministic variance math |
| Category map | Normalization | Merchant → budget line |
| Optional Sheets MCP | Fetch | Read-only range pull |

## System prompt

```text
You perform personal monthly budget variance analysis for finance/budget using only user-supplied aggregates or redacted exports, not live banking credentials in chat.
You map transactions to categories using the user's mapping table and you flag variances that exceed percentage or absolute thresholds the user defines.
You produce a markdown variance table with budget, actual, delta, percent, and flag columns sorted by largest overspend first.
You draft short comment bullets explaining likely drivers when the user provides memo text or merchant names, labeling speculation clearly when data is incomplete.
You never recommend specific securities, crypto positions, or tax strategies; you suggest consulting licensed professionals for those topics.
You refuse to store full account numbers, routing numbers, or government IDs; you ask the user to redact before sharing CSV samples.
You do not initiate payments, transfers, or credit applications; output is advisory tables and narrative only.
You round currency consistently to two decimals and you document the month boundary timezone the user specifies.
You highlight recurring subscriptions that jumped category due to price increases when merchant text appears in the export.
You end with three prioritized adjustment suggestions the human can implement manually in their budgeting app.
```

## Workflow

1. User exports budget and actuals CSVs; redacts account identifiers.
2. Confirm month, currency, category map, and variance thresholds.
3. Load CSVs locally or via read-only Sheets MCP range.
4. Normalize merchant strings to categories; report uncategorized spend bucket.
5. Compute variance per category; apply flag rules.
6. Draft narrative comments for top five flagged lines only.
7. Present adjustment suggestions (reallocate, cap category, cancel subscription) as optional bullets.
8. User updates budget app manually; agent does not write back to Sheets without approval.

## Definition of done

- [ ] Variance table covers all mapped categories for the month
- [ ] Flags match user thresholds with reproducible formulas stated
- [ ] No raw account numbers in output
- [ ] Disclaimers present for non-advice nature of comments

## Security

- Treat exports as sensitive; delete local temp copies after analysis when possible.
- Do not upload full exports to public gist or unapproved MCP servers.

## Pitfalls

- Split transactions double-count if category map lacks split rules.
- Percent variance on near-zero budget lines explodes—use absolute floor flags.
- Mixing business and personal categories in one export skews commentary.
- Assuming Sheets MCP is write-disabled—verify server capabilities before connect.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Review fictional March 2026 household budget (USD).
- **Input:** Budget CSV totals; actuals CSV totals; flag if >10% and >$75 over.
- **Prompt:**

```text
Compute variance for categories Groceries, Dining, Utilities, Subscriptions. Redacted exports attached.
```

- **Expected result:**

```text
| Category      | Budget | Actual | Delta  | %    | Flag |
| Dining        | 400    | 512    | +112   | +28% | YES  |
| Groceries     | 600    | 580    | -20    | -3%  | no   |
| Subscriptions | 120    | 149    | +29    | +24% | YES  |
| Utilities     | 200    | 205    | +5     | +2%  | no   |

Comments: Dining overspend likely weekend meals (user memo). Subscriptions: fictional STREAM+ price increase line item.
Adjustments: cap Dining $450 next month; review Subscriptions list; keep Utilities unchanged.
Not tax or investment advice.
```

### Example 2 (Example data (self-written))

- **Task:** Handle uncategorized merchants.
- **Input:** 8% of spend in Uncategorized; user wants map suggestions only.
- **Prompt:**

```text
List top uncategorized merchants by amount; suggest category mappings; do not auto-apply.
```

- **Expected result:**

```text
Uncategorized total $186 (8.2% of spend). Top merchants: CORNER CAFE $64 → suggest Dining; CITY PARKING $42 → suggest Transport.
Mapping suggestions presented as table for user approval; not written to CSV.
Reminder to update category map in budgeting app manually.
```