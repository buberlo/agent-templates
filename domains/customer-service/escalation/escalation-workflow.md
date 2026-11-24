---
id: escalation-workflow
title: "Eskalation"
domain: customer-service
category: escalation
tags:
  - escalation
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
inputs:
  - "Ticket or Conversation ID"
  - "Eskalationsstufen-Matrix"
  - "Notification channels (Slack/email draft)"
outputs:
  - "Eskalationspaket"
  - "--"-- "-- "-- "-- "-- "-- " - "----- Riviera "s"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Recognize serious support cases** (legal threat, default, VIP, media), **internally escalate** with structured package and **customer communication only as a draft**.

## When to use

- Keywords/SLA-Bruch triggern Eskalation (angry, legal, outage, exec).
- Intercom or similar connected; matrix defines stage → owner.
- No car send to customer or legal without OK.

**When not to use**

- Routine-Ticket without Schwellenwert → helpdesk-tickets.
- Threat by force → Human + if necessary. Authorities, no bot triage alone.
- Missing escalation matrix → first clarify policy.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| intercom MCP | Ticket + History | Full Context |
| Eskalations-Matrix MD | Routing | L2/Legal/Engineering |
| Slack/Email Draft | Internal externally separated | No leak of internal notes.

## System prompt

```text
You escalate customer cases for customer-service/escalation.

Inputs: ticket_id, escalation_matrix path, severity hints, customer_visible_update (draft only).

Steps:
1) Load full conversation; score severity 1-4 (4=legal/media/safety).
2) Map to matrix row: owner team, slack channel, due_hours.
3) Build escalation_package: summary, timeline, revenue_at_risk, quoted customer messages, attachments list, suggested_root_cause (hypothesis labeled).
4) Draft internal slack message with @owner; do not post without APPROVE_ESCALATE.
5) Draft customer-facing message: empathic, no liability admission, next_contact_time.
6) Tag ticket Escalated; assign if MCP allows and user approved.

Never promise refunds/compensation unless matrix authorizes wording.
Safety threats: stop automation, output HUMAN_REQUIRED safety banner.

Deliver: escalation_package.json, customer_draft.txt, slack_draft.txt.
```

## Workflow

1. Matrix `config/escalation-matrix.yaml` laden.
2. Ticket via Intercom MCP inkl. aller Teile lesen.
3. Determine Severity and Target Team.
4. `escalation package.json` with quotes and timeline.
5. Slack draft to #support-escalations (do not post).
6. Customer status draft without admission of guilt.
7. According to APPROVE ESCALATE: tag + assign. Send actions only if released.

## Definition of done

- [ ] Severity with justification and quotes
- [ ] Richtiger Owner laut Matrix
- [ ] Kundenentwurf without unautorisierte Zusagen
Safety: HUMAN REQUIRED when a threat

## Security

- Legal threads not in Slack without #legal-private.
- No internen RCA-Details in Kundenentwurf.
- Medienanfragen an Comms eskalieren.

## Pitfalls

- Escalation without complete history → wrong context.
- Kunde sieht interne Slack-Kopie.
Severity inflation Team alert fatigue.
- Auto-assign to wrong team except holiday.
- Versprechen zur Frist without Engineering-OK.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** VIP-Ausfall, Severity 3.
- **Input:** Ticket `#9902`, Matrix L2-Engineering.
- **Prompt:**

```text
Build escalation package, draft customer message with 2h update pledge only if matrix allows.
```

- **Expected result:**

```text
Owner: oncall-engineering | Due: 2h
Customer draft: "Wir priorisieren Ihren Fall… Update innerhalb 2 Stunden…"
Slack draft: @oncall — summary + timeline (not posted)
```

### Example 2 (Example data (self-written))
- **Task:** Gewaltandrohung.
**Input:** Customer text related to physicals threat.
- **Prompt:**

```text
Escalate and respond.
```

- **Expected result:**

```text
HUMAN_REQUIRED — safety_threat_detected
No customer auto-reply; ticket flagged for human + security playbook.
No slack post executed.
```