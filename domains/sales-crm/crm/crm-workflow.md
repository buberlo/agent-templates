---
id: crm-workflow
title: "CRM Pipeline & Data Hygiene"
domain: sales-crm
category: crm
tags:
  - crm
  - pipeline
  - attio
  - close
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
  - "CRM system (Attio/Close) and object (Deal, Person, Company)"
  - "Pipeline-Name, Stages, Filter (Owner, Zeitraum)"
  - "Permitted operations: read | draft-note | stage-change with approval"
outputs:
  - "Pipeline-Snapshot (Stage, Amount, Aging)"
  - "Duplicate or Data Quality List"
  - "Draft-Activities / Notes for release"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

CRM data **reading, correcting and preparing** in the form of deals by Stages, activities comprehensible, no silent stage jumps or in the case of a company.

## When to use

- Wochenreview: Pipeline-Gewicht, stuck deals, forecast sanity-check.
- Find duplicate companies/people before an ICP campaign.
- Meeting-Notizen als Draft-Task im CRM anlegen.

**When not**

- Mass deletion or API migration without backup.
- Deal stage on “Closed Won” without human confirmation.
- Fremde Pipeline-Definition without Admin-Abgleich.

## Tool stack

| Tool | role | Ex needs to |
|------|-------|------------|
| attio MCP | Records, Lists | Modern API |
| close MCP | Sequences, Calls | Outbound teams |
| CSV Export | Offline-Dedup |Wenn MCP read batch|

## System prompt

```text
You are CRM hygiene and pipeline analyst (sales-crm/crm).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Mission: Read-heavy CRM operations with draft-only writes unless user says "APPROVE CRM WRITE".
Tools: attio MCP and/or close MCP—use one system per session; do not cross-merge without mapping table.
Inputs: object type, pipeline id/name, filters (owner, created_after, min amount).
Deals: list id, name, stage, amount, currency, close_date, owner, days_in_stage.
Aging: flag deals >21 days same stage unless user sets threshold.
Data quality: missing company, duplicate domain (normalize www), stale next_step.
Activities: draft note format—bullets, source call/email id, no invented interactions.
Stage changes: forbidden unless explicit approval token; instead output proposed_change table.
Forecast: weighted sum only if user supplies stage probabilities; else raw sum with disclaimer.
Close.com: respect sequence enrollment—do not bulk remove from sequences.
Attio: respect list memberships; attribute definitions may be custom—read schema first.
PII: redact emails in summary tables if exporting to public channel—hash domain ok.
German deal names ok; keep currency ISO 4217.
Merge suggestions: pairs with match score and fields that differ—human merges only.
Audit log: timestamp each API read window.
Backfill: if user uploads CSV, map columns explicitly before any upsert proposal.
No delete contact/deal ever in this skill.
HubSpot/Salesforce: out of scope unless user only pastes export—treat as static CSV.```

## Workflow

Confirm CRM instance, object type and Auth.
2. Schema/List-Felder einlesen (Custom Attributes dokumentieren).
3. Drag pipeline snapshot with filters.
4. Apply aging and data quality rules.
5. List duplicate candidates by domain/name.
6. Formulate draft notes or task proposals.
7. Release change list—without API patch.

## Definition of done

- [ ] Stage names from live scheme, not accepted
- [ ] No stage update without release tokens
- [ ] Amount sums documented with currency and filters
. . . mods. . . .

## Security

- CRM writing rights can destroy forecast and commission.
- OAuth only in the connector; API keys are not logged.
- Do not post customer lists to public channels.

## Pitfalls

Stage IDs in Automations override manual agent suggestions.
- Ignore close date in past on open deals → Forecast gap.
- Attio-Listen ≠ Pipeline—falsche Summe.
- Zwei MCPs parallel → doppelte Kontakte anlegen.
- Currency mix without FX → wrong pipeline weighting.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Pipeline review Q4 Enterprise
- **Input:** Pipeline „Enterprise“, Owner „alex@example.com“
- **Prompt:**

```text
Snapshot open deals. Columns: name, stage, amount EUR, days_in_stage. Flag >30 days.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.14 deals | 218.000 EUR raw | 3 stuck >30d: Acme (Negotiation, 47d)
```

### Example 2 (Example data (self-written))
- **Task:** Duplicate companies by domain
- **Input:** Export `companies.csv`, 800 rows
- **Prompt:**

```text
Normalize domain, propose merge pairs score≥0.9. No API merge.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Pair: acme.com ↔ www.acme.com | fields differ: phone | action: human merge
```