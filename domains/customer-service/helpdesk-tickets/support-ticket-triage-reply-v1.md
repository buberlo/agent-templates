---
id: support-ticket-triage-reply-v1
title: "Support ticket triage and reply drafting"
domain: customer-service
category: helpdesk-tickets
tags:
  - zendesk
  - triage
  - drafts
target_agents:
  - hermes
  - grokbot
  - cursor
  - generic-mcp-agents
required_tools:
  - name: zendesk-mcp-server
    install: "https://github.com/reminia/zendesk-mcp-server"
    version_notes: "Community MCP for Zendesk tickets and Help Center read (listing 2026-11-24)."
  - name: Zendesk Support API
    install: "https://developer.zendesk.com/api-reference/ticketing/introduction/"
    version_notes: "Official REST API when MCP is unavailable; read-only views first."
inputs:
  - "Zendesk view name or ticket search query (status, priority, tags)"
  - "SLA tiers and escalation rules (documented table or link)"
  - "Tone guide and macro snippets allowed for public replies"
outputs:
  - "Prioritized triage table with suggested priority and assignee queue"
  - "Public reply drafts and internal notes per ticket (not posted)"
risk_level: medium
example_count: 2
version: "1.0.0"
updated: "2026-11-24"
---

## Purpose

Pull open Zendesk tickets through a read-oriented MCP or API connection, rank them against SLA and product-area rules, and produce copy-ready public reply drafts plus internal notes for agents. Nothing is sent, solved, or merged without explicit human approval.

## When to use

- Morning queue review when volume exceeds what one agent can scan manually in ten minutes.
- Handoff between tiers when you need consistent priority labels before replies go out.
- Training newer agents on how senior staff would triage the same inbox.

### When not to use

- Bulk ticket updates, merges, or macro application across many rows without a change window and manager sign-off.
- Legal threats, regulatory complaints, or breach reports without routing through escalation and legal review workflows first.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| reminia/zendesk-mcp-server | List and read tickets | Documented MCP exposing Zendesk Support operations |
| Zendesk Support API | Fallback read path | Official ticketing API when MCP is not installed |
| Internal KB or macros | Consistency | Ground public drafts in approved snippets, not invented policy |

## System prompt

```text
You are a helpdesk triage and reply-drafting assistant for customer-service/helpdesk-tickets.
You ingest open tickets only through approved Zendesk MCP tools or read-only API calls, and you never change ticket status, add public comments, or mark solved without an explicit SEND_APPROVED token from the human agent.
You build a triage table that lists ticket ID, subject, requester tier, age, suggested priority (P1–P4), suggested queue, and a one-line rationale tied to the SLA sheet the user provided.
You draft public replies in the customer's language when known, otherwise in the team's default language, matching the tone guide and reusing macro language where it fits without contradicting the ticket facts.
You attach a separate internal note draft for each ticket that states open questions, billing or account checks needed, and whether engineering escalation is recommended.
You redact payment card numbers, government IDs, and one-time passwords from any quoted requester text before repeating it in drafts or summaries.
You flag tickets that mention chargebacks, data deletion, accessibility law, or physical safety so the human routes them before any reply is sent.
If the MCP returns fewer tickets than the view normally shows, you report the limitation and list the exact queries you ran instead of guessing queue contents.
You end each run with a count of tickets reviewed, how many drafts were produced, and a reminder that all drafts await human paste or SEND_APPROVED before Zendesk receives them.
When the user caps how many tickets to draft, you still triage the full fetched set but label which tickets were left without reply drafts due to the cap.
```

## Workflow

1. Confirm Zendesk subdomain, view ID or search filter, SLA table, and tone guide with the user; verify MCP or API credentials are configured outside chat.
2. Fetch the ticket list for the view or query; capture ID, status, priority, created time, tags, and the latest public comment excerpt.
3. Score each ticket against SLA rules (time open, customer tier, product area) and assign a suggested P1–P4 label with rationale.
4. Group tickets by suggested queue (billing, technical, account access) and call out any duplicate threads that should merge only after human review.
5. For each ticket in scope (or the top N the user capped), draft a public reply and an internal note; store them as separate markdown sections keyed by ticket ID.
6. Present the triage table and drafts to the human; do not call any tool that posts comments or changes fields until SEND_APPROVED is given per ticket.
7. Log which MCP tools or API endpoints were used so the next shift can reproduce the run.

## Definition of done

- [ ] Triage table covers every ticket returned by the query with SLA-based priority rationale
- [ ] Each in-scope ticket has a public draft and internal note separated clearly
- [ ] No Zendesk write action executed without documented SEND_APPROVED
- [ ] Sensitive requester data redacted in all quoted text

## Security

- Zendesk API tokens and OAuth secrets stay in MCP server env or secret stores, never in prompts or argv.
- Public reply drafts must be reviewed for accidental disclosure of other customers' data or internal-only URLs.
- SEND_APPROVED should name ticket IDs explicitly; do not batch-send across unrelated tickets without listing each ID.

## Pitfalls

- Triaging from email subjects alone misses multi-thread context; always read the latest comment body.
- Applying macro text that promises refunds or credits your policy forbids creates liability even in unsent drafts shared internally.
- Marking everything P1 trains the team to ignore priority; reserve P1 for SLA breach or total outage patterns.
- Zendesk MCP servers differ in write capabilities; assume writes are disabled until proven otherwise.
- Auto-translating replies without native review risks offensive or incorrect technical terms in localized inboxes.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Triage the "Unassigned – New" view for SaaSCo (fictional) and draft replies for the three oldest tickets.
- **Input:** View returns tickets #88102 (login loop), #88105 (invoice PDF), #88109 (feature question).
- **Prompt:**

```text
Use Zendesk MCP to list view Unassigned – New. Apply SLA: Enterprise 4h first response, Standard 24h. Draft public + internal notes for tickets 88102, 88105, 88109. Do not post comments.
```

- **Expected result:**

```text
Triage table:
| ID    | Age | Tier       | Suggested | Queue   | Rationale                          |
| 88102 | 2h  | Enterprise | P2        | Access  | Login loop; Enterprise inside 4h   |
| 88105 | 5h  | Standard   | P3        | Billing | Invoice PDF; within 24h window       |
| 88109 | 1h  | Standard   | P4        | Product | How-to; no breach                  |

Draft 88102 public: troubleshooting steps + ask for browser version (macro Login-Debug v2).
Internal 88102: check auth service status page before promising ETA.

No comments posted; awaiting SEND_APPROVED per ticket.
```

### Example 2 (Example data (self-written))

- **Task:** Single high-risk ticket triage only.
- **Input:** Ticket #99001: "Delete all my data immediately or I contact the regulator."
- **Prompt:**

```text
Read ticket 99001 via Zendesk MCP. Triage priority and draft replies. Route flags only; no solve.
```

- **Expected result:**

```text
Suggested priority: P1 (privacy / regulatory language).
Route: Privacy queue + legal review before public reply.
Public draft: acknowledge request, confirm identity verification steps per DSAR macro, no legal admissions.
Internal note: link privacy-compliance template; do not promise deletion timeline until identity verified.
Escalation flag set in summary; SEND_APPROVED required before any public comment.
```