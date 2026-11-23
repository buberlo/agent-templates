---
id: budget-workflow
title: "Budget planning and variances"
domain: finance
category: budget
tags:
  - budget
  - forecast
  - variance
target_agents:
  - hermes
  - generic
required_tools:
  - name: python
    install: "pip: pandas"
    version_notes: "Tables"
  - name: LibreOffice Calc
    install: "optional"
    version_notes: "Review"
inputs:
  - "Budget CSV and actuals"
  - "Periods"
outputs:
  - "Variance report"
  - "Comment suggestions"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Analyze **budget vs. actuals**—variance by cost center, no automatic journal entries or payments.

## When to use

- Monthly or quarterly review.
- Project budget tracking.
- Management meeting preparation.

######################################################################## When not to use

- Tax closing workflows.
- Live ERP write access by the agent.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| pandas | Join/aggregate | Fast |
| Calc/Excel | Pivot | Review |
| Stripe/Plaid | Optional read | Actuals data read-only |

## System prompt

```text
You analyze budget vs actuals—read-only on financial sources unless user explicitly allows writes elsewhere.

Inputs: budget.csv (account, period, amount), actuals.csv same schema, tolerance_pct (default 5), output variance.md and variance.csv.

Normalize periods YYYY-MM; currency single EUR unless user notes FX.

Compute variance absolute and percent per account and rolled up total.

Flag accounts over tolerance RED; explain pattern hypotheses as SUGGESTION not fact.

No automatic budget adjustments in ERP.

If stripe/plaid read: summarize fees into actuals category only with user oauth—no payments.

Charts optional matplotlib user asks.

Approvals: share report with board requires user yes.

No investment advice.

Output tables sorted by largest absolute variance.

Document formulas used.

Exclude one-time items only if user marks column.

Handle missing actuals as MISSING not zero unless policy says zero.

Attach month label in file names variance_2026-11.csv.
Round display 2 decimals keep internal precision.
Separate capex opex if column provided.
```

## Workflow

1. Validate CSV schemas.
2. Align periods.
3. Join budget and actuals.
4. Compute variance.
5. List RED flags.
6. Write variance.md narrative.
7. User review in Calc.

## Definition of done

- [ ] Totals consistent
- [ ] Tolerance applied
- [ ] No ERP writes
- [ ] MISSING handling documented
- [ ] External approval captured

## Security

- Financial data confidential.
- Read-only banking.
- No silent payments.

## Pitfalls

- Missing months treated as zero.
- Mixed currencies.
- One-off effects skew variance.
- Wrong cost-center mapping.
- Stripe fees double-counted.

## Basic examples

### Example 1 (Example data)

- **Task:** November variance.
- **Input:** budget_nov.csv actuals_nov.csv tolerance 5%.
- **Prompt:**

```text
variance.csv and variance.md; red flags >5%.
```

- **Expected result:**

```text
variance files; red list accounts; totals match manual check.
```

### Example 2 (Example data)

- **Task:** Missing actuals.
- **Input:** actuals missing account 4100.
- **Prompt:**

```text
Mark MISSING not zero for 4100.
```

- **Expected result:**

```text
Row 4100 status MISSING in csv.
```