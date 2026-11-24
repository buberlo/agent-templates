---
id: helpdesk-tickets-workflow
title: "Helpdesk and tickets"
domain: customer-service
category: helpdesk-tickets
tags:
  - helpdesk
  - customer-service
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: intercom MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
  - name: awesome-mcp Support-Sektion
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "catalog."
inputs:
  - "Ticket ID or search filter"
  - "Macro policy and tonality"
  - "release for public response"
outputs:
  - "Priorisierte Ticketliste"
  - "Public answer draft and internal elite note"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

And I-I--B I I'm a----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## When to use

- Intercom (or similar helpdesk MCP) connected.
- SLA or priority rules known.
- Agent supports First Response, Human sends or gives OK.

**When not to use**

- Rechtliche Beschwerden without Legal-Review-Workflow.
mass state changes without change windows.
- Zendesk or similar without matching MCP (catalogue search only).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| intercom MCP | Ticket CRUD, Notizen | Hermes approved |
| awesome-mcp catalog | Alternative ITSM | Eval vor Install |
| Internal KB | Macro source | Consistent answers |

## System prompt

```text
You process helpdesk tickets for customer-service/helpdesk-tickets via Intercom MCP.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: view (open|snoozed|search query), sla_hours, tone (empathic DE), allowed_actions (draft_reply | internal_note | tag | resolve), macro_ids[].
Workflow:
1) List tickets matching view; sort by waiting_customer since longest.
2) For each ticket (max N per run): fetch thread, classify intent (billing|technical|howto|angry).
3) Draft public reply using approved macros when match; personalize with ticket facts only—no invented policies.
4) Add internal_note with next steps if escalation needed.
5) tag ticket only if user approved tags.
6) resolve or close ONLY if allowed_actions includes resolve AND user confirmed.
Redact card numbers, passwords from summaries.
If PII must appear in reply, keep minimal.
Output: ticket-run.md with ticket_id, actions taken, draft ids, nothing sent without send_approved flag.```

## Workflow

1. `hermes mcp install intercom` and credentials.
2. Load ticket view: sort open tickets by waiting time.
3. Top-5: Kontext lesen, Intent klassifizieren.
4. Build public response design from macro + facts.
5. Internal note for escalation risk.
6. User reviews; OK: Send public note (if allowed).
7. Run log `output/helpdesk-run.md` without unnecessary PII.

## Definition of done

No invented refund/policy promise
- [ ] Resolve only with explicit policy/release
- [ ] Antwort referenziert Ticket-Fakten
- [ ] Logs pseudonymised where possible

## Security

- Customer data not in public agent threads.
- OAuth tokens do not log.
- GDPR deletion questions to Human escalate.

## Pitfalls

- Stilles Resolve → CSAT-Kollateralschaden.
- Macro does not fit → called wrong product version.
- Internal note accidentally public.
- Suche zu breit → falsches Ticket bearbeitet.
- Halluzinierte Ticket-ID.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Billing-Ticket First Response.
- **Input:** Ticket `#8821`, Kunde fragt Rechnungsduplikat.
- **Prompt:**

```text
Draft public reply in German, attach internal note if refund policy unclear, do not resolve.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Public draft: "We will send you the invoice #445... again..."
Internal note: verify payment gateway status before promise
Resolve: not executed
```

### Example 2 (Example data (self-written))
- **Task:** Resolve without release.
- **Input:** User says only draft.
- **Prompt:**

```text
Close ticket 8821 as solved.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Abbruch: resolve not in allowed_actions.
Draft remains unsent; ticket state unchanged.
```