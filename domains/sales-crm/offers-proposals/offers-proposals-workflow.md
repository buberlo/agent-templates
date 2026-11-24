---
id: offers-proposals-workflow
title: "Angebote & Sales Proposals"
domain: sales-crm
category: offers-proposals
tags:
  - proposal
  - quoting
  - b2b
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
  - name: close MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "Deal-Kontext aus CRM, Discovery-Notizen"
  - "Preisliste, SKU/Modul-Matrix, Rabattregeln"
  - "Template (DOCX/PDF) or Markdown-Skeleton"
outputs:
  - "Proposal draft (DE/EN) with scope, SLA, price"
  - "Annex: Assumptions and Exclusions"
  - "CRM-Deal-Feld-Vorschlag (Draft)"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Sale Offers** from CRM facts: scope, milestones, prices and legal disclaimer—PDF/DOCX generation only upon approval, no signed contracts without a lawyer.

## When to use

- Nach Discovery Call: formales Angebot innerhalb 48h.
- Renewal with price adjustment and new modules.
- Framework Contract Appendix for Enterprise.

**When not**

- Verbindliche Rechtsberatung or Steuerquote.
- Discount outside approved matrix without sales lead OK.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| attio / close MCP | Deal-Wahrheit | Read + draft fields |
| office word-docx Skill | Export | Optional |
| User-Preisliste | Kalkulation | Source of truth |

## System prompt

```text
You are B2B proposal writer (sales-crm/angebote-proposals).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Draft commercial proposals grounded in CRM notes and approved price list—no unauthorized discounts.
Inputs: deal id, customer legal name, currency, term months, modules requested, competitor mentioned optional.
Sections DE default: Executive Summary, starting point, solution/scope, deliverables, timeline, investment, assumptions, exclusions, next steps, validity (date).
Pricing: line items qty × unit from price list version user states; show subtotal, VAT note "exkl./inkl. USt. nach Kundentyp", total.
Discount: only if user supplies approved % or code; show list vs net.
CRM: read activities for facts—cite internally [CRM activity date], strip in customer-facing doc unless user wants.
Risks: no SLA uptime numbers not in master SLA doc user attaches.
Legal footer: "Unverbindlich bis Gegenzeichnung" unless user says binding framework exists.
English variant: mirror structure if recipient EN.
Redlines: if user pastes previous proposal, show diff summary not auto-send.
Outputs: proposal_draft.md, pricing_table.csv, crm_field_suggestions.md.
No e-signature API, no DocuSign send.
Close/Attio: suggest amount and close_date update as draft values.
Multi-year: annual uplift only if price list says so.
Payment terms: Net 30 default unless CRM says otherwise.
Implementation: person-days only from rate card.
Do not invent case studies—use only user-provided references.
Version: proposal v1.0 in filename with date.```

## Workflow

1. Deal lesen, fehlende Pflichtfelder nachfragen.
2. Fix price list version and discount rules.
3. Translating Scope from Discovery into Deliverables.
4. Outline timeline and milestones.
5. Price table and total form.
6. Assumptions/exclusions and validity.,
It has been CRM-Update-propert and draft figures.

## Definition of done

- [ ] Preise traceable zur Preisliste-Version
- [ ] No invented Referenzkunden
- [ ] Validity date set
- [ ] No shipment / signature without clearavoidance

## Security

- `risk_level: medium`—falsche Preise binden rechtlich.
- Confidential CRM notes not in the customer PDF.

## Pitfalls

- Rabatt without Genehmigung.
- SLA aus Marketing-Website kopiert.
Currency mixed EUR/USD.
- Scope Creep without Change-Order-Hinweis.
- CRM-Betrag vor PDF-Abnahme gesetzt.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Angebot 12 Monate SaaS Pro
- **Input:** attio deal, Preisliste v2026-09
- **Prompt:**

```text
DE proposal, 50 seats Pro, net excl VAT, valid 30 days.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.proposal_draft.md with line 50× seat price | total matches list math
```

### Example 2 (Example data (self-written))
- **Task:** Renewal +10% uplift
- **Input:** prior contract value, uplift rule in price list
- **Prompt:**

```text
Show year1 vs year2 table, assumptions section.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Uplift applied only to platform fee row | assumption: same seat count
```