---
id: imessage-sms-workflow
title: "iMessage and SMS"
domain: communication
category: imessage-sms
tags:
  - imessage
  - communication
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled apple/imessage, macOS."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Optional: Termin-Kontext aus Calendar."
inputs:
  - "the Contact Handle or Chat"
  - "Then-----."
  - "release SEND yes/no"
outputs:
  - "Konversationsauszug"
  - "Sending or submitted SMS/ animals order"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Short messages** via Hermes **imessage** (macOS/imsg CLI) and **only sent after release**; Document SMS/iMessage log for follow-ups.

## When to use

- macOS host with Messages account and Hermes imessage skill.
- a short coordination (only delay, appointment, OTP-note without the OTP itself).
: nonstop-avas : . .  thereof

**When not to use**

- Linux/Windows without macOS Bridge → Skill is skipped.
- Mass SMS/marketing without opt-in and carrier policy.
to, in a spear, to be speared, to be speared, to be speared, to be speared, to be speared.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes imessage | Lesen/Senden | Offizielles bundled Skill |
| gws Calendar (optional) | Context | Schedule time |
| Markdown-Log | Audit | Handle redacted, Zeitstempel |

## System prompt

```text
You operate iMessage/SMS on macOS via Hermes imessage skill (imsg CLI). Read chats, draft short replies; send only on explicit "SEND <handle>".

Inputs: handle (phone or email), action (list | read | draft | send), max_messages, draft_text, language DE.

Read: list recent messages with timestamps; quote last inbound for context.
Draft: <= 320 chars for SMS-safe; mark iMessage vs SMS if known.
Send: echo exact body; require user confirmation string; log message_id if returned.

Do not automate 2FA codes delivery to third parties.
Redact handles in external summaries (show last 2 digits only).
If not on darwin, stop and report platform_unsupported—do not fake send.

Deliver: conversation-excerpt.md, draft block, send receipt or "draft only".

Escalation: if send fails with authorization error, stop; do not retry with alternate handles.
Timezone: stamp all excerpts in Europe/Vienna unless user specifies otherwise.
```

## Workflow

1. `uname -s` — cancel at non-Darwin with clear message.
2. Handle and order clarify (read vs. send).
3. `imsg` about Skill: read last N messages.
4. Antwortentwurf (kurz, klar, without Links wenn SMS-only vermutet).
5. User checks text; at OK: `SEND` repeat with handle.
6. After Send: Verify last line from Chat.
7. `output/imessage-log.md` with time, action, redacted handle.

## Definition of done

- [ ] platform macOS confirmed or cleanly cancelled
- [ ] Sent text byte-identical with approved draft
- [ ] No Secrets im Log
- [ ] Recipient handle documented in internal log

## Security

- Apple ID and device trust are with the user; Agent uses only skill-exposed CLI.
- No forwarding of health or financial PII in SMS, without consent
- Senden gesperrt without zweites explizites Kommando.

## Pitfalls

Commons: Abschaffunga (E.P.A.P.A.A.)
- Falscher Handle → Nachricht an falschen Kontakt (Handle vor Send doppelt zeigen).
- Skill auf Linux still skipped without Agent-Hinweis wenn Prompt schwach.
We terminal we). Which and traders
- Gruppenchats: Reply-Kontext leicht verloren.

## Basic examples

### Example 1 (Example data)

- **Task:** Report delay 15 minutes.
- **Input:** Handle `+43…901`, Draft DE.
- **Prompt:**

```text
Draft SMS: "Bin in 15 Min da, sorry!" — show draft, wait for SEND.
```

- **Expected result:**

```text
Draft: Bin in 15 Min da, sorry!
Status: draft_only (awaiting SEND +43***901)
```

### Example 2 (Example data)

- **Task:** Linux-Server.
- **Input:** `uname` = Linux, imessage angefragt.
- **Prompt:**

```text
Send meeting link via iMessage.
```

- **Expected result:**

```text
Abbruch: platform_unsupported (imessage requires darwin).
Alternative: E-Mail-Entwurf or manuelles Senden vom Mac vorschlagen.
```