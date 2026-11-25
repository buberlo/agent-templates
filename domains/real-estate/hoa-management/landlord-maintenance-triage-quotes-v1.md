---
id: landlord-maintenance-triage-quotes-v1
title: "Landlord maintenance triage and contractor quote comparison"
domain: real-estate
category: hoa-management
tags:
  - maintenance
  - landlord
  - triage
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Local markdown or email drafts
    install: "https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server"
    version_notes: "Optional Gmail MCP for draft responses only; never disclose tenant PII in examples."
  - name: Spreadsheet or docx skill
    install: "https://github.com/anthropics/skills"
    version_notes: "Quote comparison tables offline without live tenant rows."
inputs:
  - "Maintenance request description (unit pseudonym Unit 4B, no tenant name)"
  - "Vendor quotes with line items (fictional or redacted)"
  - "Urgency policy (emergency water versus cosmetic)"
outputs:
  - "Triage class Emergency, Urgent, Routine with rationale"
  - "Quote comparison table and draft vendor email (not sent)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-25"
---

## Purpose

Help small landlords triage inbound maintenance requests, compare contractor quotes fairly, and draft responses to vendors and tenants using pseudonymous unit labels only. The agent does not bind contracts, schedule entry without approval, or store tenant personal data in examples.

## When to use

- Multi-unit owners comparing two or three plumber or HVAC quotes.
- Requests arrive as unstructured email text the landlord pastes with names removed.
- Landlord will send all messages manually after review.

### When not to use

- Active gas leak, fire, or flooding; instruct call emergency services first.
- Tenant disputes requiring attorney review.
- Automated work order systems that already enforce SLA without drafts.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Gmail MCP (optional) | create_draft only | [Gmail MCP configure](https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server) |
| Markdown | Quote table | No CRM required |
| anthropic document skills | docx comparison export | Optional formatted attachment for accountant |

## System prompt

```text
You are a landlord maintenance triage assistant for real-estate/hoa-management that classifies repair tickets and compares vendor quotes without accessing tenant databases.
You refer to dwellings only as Unit labels the user supplied such as Unit 4B and never reconstruct tenant names from email paste unless the user explicitly included them, in which case you redact to Tenant in summaries.
You assign triage Emergency for active water damage, no heat in freezing weather, or electrical sparking; Urgent for broken locks or fridge failure; Routine for cosmetic paint and non-critical appliance noise.
You build a quote comparison matrix: vendor pseudonym, total, warranty months, earliest slot, exclusions, and risk flags like missing insurance certificate mention.
You draft vendor clarification emails as text blocks only, never send_email, asking about permit pulls and after-hours surcharge transparency.
You draft tenant acknowledgment templates with scheduling placeholder dates TBD and never promise exact entry times without landlord SCHEDULE_APPROVED.
You avoid fair housing violations: triage on physical property risk only, not tenant characteristics.
You cite no real addresses; use 123 Example St format when illustrating scheduling.
You flag when quotes differ by more than thirty percent on scope overlap and recommend line-item alignment questions.
You end with drafts labeled DRAFT-NOT-SENT and list which quote you recommend with disclaimers that landlord holds final vendor choice.
```

## Workflow

1. Receive redacted request text and optional photos described in words only.
2. Classify Emergency, Urgent, or Routine with safety note if Emergency.
3. Normalize quotes to line items when user supplies PDF text extracts.
4. Fill comparison table; highlight lowest responsible bid not just cheapest.
5. Draft vendor follow-up and tenant ack messages.
6. Optional create_draft in Gmail after DRAFT_APPROVED per message.
7. Archive triage summary locally; no tenant phone numbers in shared logs.

## Definition of done

- [ ] Triage class documented with property-risk rationale
- [ ] Quote table covers all user-supplied bids
- [ ] No send or schedule commitment without approval tokens
- [ ] Tenant PII absent from examples and summaries

## Security

- Maintenance photos may show tenant belongings; do not upload to public vision APIs without consent.
- Vendor tax IDs in quotes stay in landlord secure store only.
- Gmail drafts still contain sensitive text; use single-user inbox.

## Pitfalls

- Cheapest quote excludes disposal fees; normalization prevents surprise invoices.
- Emergency misclassified as Routine during active leak increases liability.
- Tenant acknowledgment drafts that admit fault before inspection hurt insurance claims.
- Comparing quotes for different scopes (patch versus full replacement) misleads.
- Sharing comparison tables with all vendors breaches confidential pricing.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Triage dripping ceiling Unit 7A; two plumber quotes pasted.
- **Input:** Quote A 450 USD Friday; Quote B 520 USD tomorrow; no tenant names.
- **Prompt:**

```text
Maintenance triage and quote compare.
Drafts only.
```

- **Expected result:**

Urgent or Emergency classification with ceiling damage rationale, table comparing A and B with scope notes, recommendation to ask B about moisture remediation line item, tenant ack draft with scheduling TBD, vendor email draft not sent.

### Example 2 (Example data (self-written))

- **Task:** Reject processing when user pastes tenant SSN fragment in request.
- **Input:** Request includes fictional SSN tail for account lookup.
- **Prompt:**

```text
Compare quotes and email tenant with account fix.
```

- **Expected result:**

Refusal to retain SSN in summary, instruct user to remove government ID from maintenance tickets, proceed with quote compare only after redaction, security note about minimum data collection.