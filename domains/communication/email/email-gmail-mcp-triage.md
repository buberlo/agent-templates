---
id: email-gmail-mcp-triage
title: "Posteingang triagieren with Gmail MCP"
domain: communication
category: email
tags:
  - gmail
  - mcp
  - triage
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: gmail-mcp
    install: "MCP: Gmail"
    version_notes: "search_emails, drafts, labels"
  - name: google-calendar
    install: "MCP optional"
    version_notes: "Terminal proposals"
inputs:
  - "Label/Query"
  - "Priority rules"
  - "Signatur"
outputs:
  - "Label-Struktur"
  - "Draft answers"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Posteingang-Triage** with Gmail MCP: ungelesene Threads priorisieren, Labels konsistent setzen and **Antworten nur als Entwurf** vorbereiten—kein Auto-Send.

## When to use

- Leadership or support inbox with 20+ new mails per day and documented priority rules.
- Gmail MCP (or Grok Gmail plugin) is connected OAuth-enabled.
- User wants a short overview plus finished drafts, sending remains manual.

**When not* *

- Cold-Outreach or Newsletter-Kampagnen without Opt-in (Spam-/Compliance-Risiko).
Legally sensitive content (lawyer, HR discipline) without release for AI summaries externally.
- IMAP-only without MCP: dann Skill **email-inbox-triage** / Himalaya statt dieses Template.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| Gmail MCP | Reading, labels, drafts | OAuth, auditable API |
| YAML/MD Regelsatz | Priorisierung | Transparente Triage |
| Kalender MCP (optional) | Termin-Snippets | Meeting-Antworten |

## System prompt

```text
You triage a Gmail inbox via MCP (search_emails, read_email, create_draft, update labels). Default: drafts only; never send_email without explicit user confirmation.

Inputs: time window (hours), base query, rules file path (Action / Waiting / FYI), user tone, signature block, max drafts to produce.

Steps:
1) search_emails with query e.g. is:unread newer_than:2d -category:promotions
2) Classify each thread: Action (needs reply), Waiting (awaiting others), FYI (archive after skim), Newsletter (archive).
3) Apply labels from rules; do not delete without approval.
4) For top Action threads: read full thread, create_draft reply referencing ticket/case IDs when present.
5) Redact PII in any summary posted outside Gmail (names → initials if policy says so).
6) Output markdown table: subject, from, label, draft_id or "no draft", one-line summary.

Constraints:
- No mass unsubscribe or filter creation without approval.
- If uncertain priority, label Review-Human.
- Cite message_id when suggesting follow-up calendar holds.

Deliver: label counts, list of draft IDs, triage-summary.md path.
```

## Workflow

1. Regeln laden: `cat config/inbox-triage-rules.yaml`.
2. Gmail MCP: `search_emails` with `is:unread newer_than:2d -category:promotions`.
3. Threads nach YAML priorisieren; Labels `Action`, `Waiting`, `FYI` setzen.
4. Top-10-`Action`: Thread lesen, `create_draft` with Signatur and Ticket-Referenz.
5. Newsletter: Label `Newsletter` + archivieren (nur nach Policy).
6. `triage-summary.md` with Counts and Draft-IDs schreiben.
7. User reviews drafts; `send email` only after explicit OK per message.

## Definition of done / Definition of Done

- [ ] Alle ungelesenen Threads klassifiziert or in `Review-Human`
- [ ] No sent mail without documented release
Drafts contain correct thread reference/reply-to
- [ ] Summary without unnecessary PII in the agent log

## Security

- Keep OAuth scopes minimal (no vault export of sensitive attachments to public channels).
- MCP-Logs and Chat: no vollen Kundenadressen, wenn Policy Pseudonymisierung verlangt.
- Auto-Forward and filter changes only after release.

## Pitfalls

- Reply-All on internal escalations → CC-Leak; Check drafts on recipient list.
- Promotional query too aggressive → overlook important receipts.
- Halluzinierte Fakten in Antworten → nur Zitate aus gelesenen Messages.
- Time zones in meeting suggestions wrong (always IANA, e.g. Europe/Vienna).
- Doppelte Drafts bei erneutem Lauf without Idempotenz-Check auf `thread_id`.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Morning triage leader inbox.
- **Input:** Query `is:unread -category:promotions`, Regeln `config/inbox-triage-rules.yaml`.
- **Prompt:**

```text
Triage last 48h unread, apply labels, draft replies for P1 Action (max 5), output triage-summary.md.
```

- **Expected result:**

```text
Action: 8 | Waiting: 3 | FYI: 14 | Archived promos: 22
Draft IDs: r-3849201, r-3849202 (customer escalation, board prep)
Review-Human: 1 (legal@...)
```

### Example 2 (Example data (self-written))
- **Task:** Fehlende Regeldatei.
- **Input:** Kein Pfad zu `inbox-triage-rules.yaml`.
- **Prompt:**

```text
Run inbox triage with defaults only.
```

- **Expected result:**

```text
Abbruch: rules_file fehlt.
Demand: Path to priority rules or inline criteria (VIP domains, SLA levels)?
No label or draft actions.
```