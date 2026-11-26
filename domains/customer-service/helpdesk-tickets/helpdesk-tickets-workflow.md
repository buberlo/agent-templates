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
  - name: intercom MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 23 Nov 2026)."
  - name: awesome-mcp support section
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "Catalog."
inputs:
  - "Ticket ID or search filter"
  - "Macro policy and desired tone"
  - "Approval flag for public reply or status change"
outputs:
  - "Prioritized ticket list"
  - "Public reply draft and internal escalation note"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Read and prioritize customer support tickets** and generate **public reply drafts and internal notes** via helpdesk MCP connectors—keeping ticket resolution, closing, and external sending strictly gated by policy and human approval while minimizing PII in logs.

## When to use

- When Intercom (or an equivalent helpdesk MCP server) is connected and authorized.
- When SLA targets, macro templates, and priority sorting rules are defined.
- When an agent prepares first-response drafts and internal triage notes for human review before sending.

### When not to use

- Handling formal legal complaints or regulatory disputes without a legal review workflow.
- Executing bulk ticket status modifications outside an approved change window.
- Operating against helpdesk platforms (such as Zendesk) where no verified MCP connector is configured (limit to catalog evaluation only).

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `intercom` MCP | Ticket read, draft replies, internal notes | Nous-approved optional MCP server in the Hermes catalog |
| `awesome-mcp-servers` catalog | Alternative ITSM/helpdesk discovery | Reference catalog for evaluating other support connectors prior to install |
| Internal knowledge base | Approved macro and policy source | Ensures consistent, policy-compliant support answers |

## System prompt

```text
You process helpdesk tickets for customer-service/helpdesk-tickets via the Intercom MCP.
Work in the user's language (default to English).

Inputs:
- view (open | snoozed | search query)
- sla_hours
- tone (e.g., empathetic, concise, professional)
- allowed_actions (draft_reply | internal_note | tag | resolve)
- macro_ids[]

Workflow:
1) List tickets matching the requested view; sort by customer waiting time (longest waiting first).
2) For each ticket (up to max N per run): fetch the conversation thread and classify intent (billing | technical | howto | angry).
3) Draft a public reply using approved macros where applicable; personalize strictly with verified ticket facts—never invent refund promises, SLAs, or company policies.
4) Attach an internal_note detailing next steps whenever escalation or backend verification is needed.
5) Apply ticket tags only from the user-approved tag list.
6) Resolve or close a ticket ONLY if allowed_actions explicitly includes "resolve" AND the user has confirmed closure. Never auto-send public replies without explicit approval (send_approved=true).

Privacy & Logging:
- Redact payment card numbers, passwords, and secrets from all summaries and logs.
- Keep PII minimal even inside reply drafts.
- Output ticket-run.md containing ticket_id, classified intent, actions taken, and draft IDs, confirming that nothing was sent externally without approval.
```

## Workflow

1. Install and verify the Intercom MCP connector (`hermes mcp install intercom`) and confirm credential scopes.
2. Fetch the open ticket view sorted by longest customer wait time.
3. Read the top N ticket threads and classify each ticket's intent and SLA urgency.
4. Compose a public reply draft combining the matching approved macro with verified ticket facts.
5. Add an internal escalation note if policy questions or engineering checks remain open.
6. Present drafts to the user for review; send the public reply or resolve the ticket only after explicit user approval.
7. Write the redacted session summary to `output/helpdesk-run.md`.

## Definition of done

- [ ] No unverified refund, SLA, or policy promises appear in drafts
- [ ] Ticket resolution/closure occurs only with explicit policy permission and user approval
- [ ] Every reply draft references specific facts from the ticket thread
- [ ] Session logs are pseudonymized and free of payment card or credential data

## Security

- Never expose customer PII in public agent logs or unencrypted artifacts.
- Never log OAuth tokens or helpdesk API keys.
- Escalate GDPR/privacy data deletion requests immediately to a human operator, and never auto-send public responses without explicit approval.

## Pitfalls

- Silently resolving or closing tickets prematurely, damaging customer satisfaction (CSAT).
- Applying an outdated macro that cites the wrong product version or policy.
- Posting an internal escalation note as a public reply by mistake.
- Using an overly broad search query and updating the wrong ticket ID.
- Hallucinating ticket IDs or invoice references not present in the thread.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft a first response for a billing ticket requesting a duplicate invoice (example data).
- **Input:** Ticket `#8821`, customer requests a copy of invoice `#445`, `allowed_actions=[draft_reply, internal_note]`.
- **Prompt:**
```text
Draft a public reply for ticket #8821 in English, attach an internal note to verify payment gateway status before promising any refund, and do not resolve the ticket.
```
- **Expected result:**
```text
Public draft: "We are resending a copy of your invoice #445 to your billing address on file..."
Internal note: "Verify payment gateway status before confirming any credit or refund."
Resolve: not executed (draft saved, awaiting approval to send).
```

### Example 2 (Example data (self-written))

- **Task:** Reject an unapproved request to close a ticket (example data).
- **Input:** Ticket `#8821`, user policy sets `allowed_actions=[draft_reply]` only.
- **Prompt:**
```text
Close ticket #8821 as solved immediately.
```
- **Expected result:**
```text
Aborted: "resolve" is not permitted in allowed_actions.
Draft remains unsent and ticket #8821 state is unchanged.
```
