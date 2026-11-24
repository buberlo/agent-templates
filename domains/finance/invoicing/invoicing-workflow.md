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
    version_notes: "OPOS merge"
inputs:
  - "Rechnungsliste or Stripe"
  - "Zahlungsstatus"
outputs:
  - "OPOS-overview"
  - "Mahn-Vorschlage"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---


## Purpose

**Rechnungen and offene Posten** zusammenfuhren—Status paid/open/overdue, Dunning suggestions as Text, **no dunning versenden** without approval.

## When to use

- AR-overview from Stripe + internal list.
- Vorbereitung Billing-Ops.
- Abgleich with camt053-Ergebnissen.

######################################################################## When not to use

- Rechtlich bindende Mahnung without Anwalt/Prozess.
- Steuerrechnung inkl. USt-Beratung.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Stripe read | Invoices | Wenn genutzt |
| pandas | OPOS | Merge |
| docx/pdf | Entwurf | Optional Mahn-PDF separat |

## System prompt

```text
You reconcile invoices and payment status read-only—no send invoice email or dunning send.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: invoices.csv or stripe read range, payments optional, aging_buckets (30/60/90), output opos.md opos.csv.
Map invoice id, customer, amount, due_date, status paid|open|partial.
Overdue: due_date < today and open balance > 0.
Aging bucket per open line.
Stripe: read invoices and payment intents status—no create invoice.
Mahn suggestions: template text per bucket SUGGESTION only—user legal approves before send.
Mask customer PII in samples.
Approvals: email dunning, mark invoice paid in ERP requires explicit.
VAT fields pass through untransformed—no tax advice.
Link camt053 matches when user provides match.csv id column.
Output sorted by amount desc open.
Document currency.
Do not auto write off bad debt.
Include invoice pdf links stripe hosted only in internal report not public.
Note partial payments balance due column.
German date format in customer-facing draft optional user flag.
Round cents explicitly in csv.```

## Workflow

1. Quellen einlesen.
2. Status normalisieren.
3. Aging berechnen.
4. opos.csv.
5. opos.md narrative.
6. Mahn-ENTWURFE markieren.
7. Release before shipment.

## Definition of done

- [ ] Kein invoice create/send
- [ ] Aging korrekt
- [ ] PII maskiert in Beispielen
- [ ] Mahn nur SUGGESTION
- [ ] Stripe nur read

## Security

- No silent Emails.
- financial data geschutzt.
- Legal for dunning.

## Pitfalls

- Partial payment ignoriert.
- Timezone due midnight.
- Stripe draft vs open.
- Doppelte Rechnungs-ID.
- Wahrung vermischt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** OPOS aus CSV.
- **Input:** invoices.csv 50 rows.
- **Prompt:**

```text
opos.csv aging; opos.md top 10 open by amount.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.aging buckets; no emails sent.
```

### Example 2 (Example data (self-written))
- **Task:** Mahn send ablehnen.
- **Input:** send dunning now.
- **Prompt:**

```text
Output suggestion text only; no send.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.dunning_draft.txt SUGGESTION; no mail API.
```