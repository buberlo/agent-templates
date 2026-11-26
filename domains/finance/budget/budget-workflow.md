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
  - "Budget CSV and actuals CSV"
  - "Target periods"
outputs:
  - "Variance report"
  - "Commentary suggestions"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Analyze **budget vs. actuals** by cost center or account to surface variances and commentary suggestions without automatic journal entries, ERP writes, or payments.

## When to use

- Monthly or quarterly budget vs. actuals reviews.
- Project budget tracking across cost centers.
- Preparing variance summaries for management meetings.

### When not to use

- Statutory or tax closing workflows.
- Automated live ERP write access by an agent.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| pandas | Join and aggregate tables | Fast and reproducible variance calculation |
| LibreOffice Calc / Excel | Pivot and manual review | Familiar spreadsheet inspection before sign-off |
| Stripe / Plaid | Optional read-only feed | Pull actuals or fee totals in read-only mode |

## System prompt

```text
You analyze budget vs. actuals in read-only mode on financial sources. Never write to ERP systems, execute payments, or send reports externally without explicit user approval.
Work in the user's language (default to English).

Inputs:
- budget.csv (account, period, amount)
- actuals.csv (same schema)
- tolerance_pct (default: 5)
Outputs:
- variance.md and variance.csv (include period label in file names, e.g., variance_2026-11.csv)

Rules:
1. Normalize all periods to YYYY-MM. Use a single currency unless the user explicitly provides FX rates and rules.
2. Compute both absolute variance and percentage variance per account and for the rolled-up total.
3. Flag accounts exceeding tolerance_pct as RED. Frame pattern explanations strictly as SUGGESTION, never as confirmed fact.
4. Handle missing actuals as MISSING rather than zero, unless user policy explicitly specifies zero-fill.
5. Separate CapEx and OpEx if a classification column is provided. Exclude one-time items only if marked in a dedicated column.
6. If optional Stripe or Plaid read data is provided, summarize fees into the actuals category only with authorized read-only access—never initiate payments.
7. Output tables sorted by largest absolute variance. Keep full internal precision and round displayed values to 2 decimal places. Document all formulas used.
8. Generate optional matplotlib charts only when requested by the user.
9. Do not provide investment advice. Sharing reports with stakeholders or boards requires explicit user confirmation.
```

## Workflow

1. Validate the schemas of the budget and actuals CSV files.
2. Align and normalize period formats (`YYYY-MM`).
3. Join budget and actuals data by account and period.
4. Calculate absolute and percentage variances plus rolled-up totals.
5. Flag accounts exceeding the tolerance threshold as `RED` and mark absent actuals as `MISSING`.
6. Draft the `variance.md` narrative report with clearly labeled commentary suggestions.
7. Hand off the generated CSV and Markdown report for user review in Calc or Excel before any external distribution.

## Definition of done

- [ ] Rolled-up totals and account-level variances are mathematically consistent
- [ ] Tolerance threshold is applied and `RED` flags are listed
- [ ] Missing actuals handling (`MISSING` vs. zero) is explicitly documented
- [ ] No ERP writes or payment actions are triggered
- [ ] Explicit user approval is obtained before sharing the report externally

## Security

- Treat all financial CSVs and account structures as confidential.
- Restrict banking and payment integrations (e.g., Stripe, Plaid) strictly to read-only scopes.
- Never execute silent payments, budget reallocations, or external report transmissions without explicit user approval.

## Pitfalls

- Treating missing months or unbooked accounts as zero instead of `MISSING`.
- Mixing multiple currencies without explicit FX normalization.
- Allowing unmarked one-off effects to distort recurring variance trends.
- Misaligning cost center or account mappings between budget and actuals exports.
- Double-counting payment processor fees (such as Stripe fees) already netted in actuals.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** November budget variance analysis with a 5% tolerance threshold (example data).
- **Input:** `budget_nov.csv`, `actuals_nov.csv`, `tolerance_pct=5`.
- **Prompt:**
```text
Generate variance_2026-11.csv and variance_2026-11.md from budget_nov.csv and actuals_nov.csv, flagging all accounts with variance > 5% as RED.
```
- **Expected result:**
```text
Created variance_2026-11.csv and variance_2026-11.md; accounts exceeding 5% variance are listed under RED flags with SUGGESTION notes; rolled-up totals match manual verification.
```

### Example 2 (Example data (self-written))

- **Task:** Handle missing actuals for an unbooked account (example data).
- **Input:** `budget_nov.csv` and `actuals_nov.csv` where account `4100` has no entry in actuals.
- **Prompt:**
```text
Run the variance analysis and mark MISSING instead of zero for account 4100.
```
- **Expected result:**
```text
Row for account 4100 is marked with status MISSING in variance_2026-11.csv and highlighted in variance_2026-11.md without assuming 0.00 actual spend.
```
