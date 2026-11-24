---
id: email-mcp-focus
title: "Email: MCP/skill focus"
domain: communication
category: email
tags:
  - email
  - communication
  - skillcli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: primary-tool
    install: "see category"
    version_notes: "as of 2026-11-23"
inputs:
  - "Context/briefing for E-Mail"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report, or ticket update)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Select targeted email stacks**: Hermes Triage + Himalaya (IMAP) or **gws*rate / Gmail-MCP—Skills for workflow, MCP for OAuth connection; Standard remains **design, no sending**.

## When to use

Agent should only activate the appropriate e-mail tools (include/exclude, tool policy).
- Mix of workspace (gws) and third-party IMAP.
Documentation of which path Gmail MCP vs. It is the Himalayas.

**When not to use**

- A single, recurring, scripted im particular nomination  introduction ? mail-Gmail-mcp-triage ?
- No set up OAuth or IMAP password handling.
- Hochriskante Massenkommunikation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
shops, turneds, turneds, turneds and turneds,
| Himalaya / imap-smtp-email | IMAP/SMTP CLI | OpenClaw/ClawHub, kein Google-only |
| gws CLI | Gmail, Calendar, Drive | Workspace-Inbox in einem CLI |
| Grok Gmail-Plugin | Chat-gebundenes Lesen/Schreiben | Offizieller OAuth-Connector |

## System prompt

```text
You configure and use email tools for communication/email: Hermes email-inbox-triage, himalaya CLI, gws, or Gmail MCP—pick the minimum set for the task.

Inputs: mailbox type (gmail_oauth | imap | workspace_gws), allowed actions (read | draft | label | send), credential location (never paste secrets).

Decision:
- Gmail with MCP available → MCP search + create_draft.
- Generic IMAP → himalaya envelope list + folder sync; draft via SMTP only after approval.
- Workspace admin tasks → gws gmail users.messages.list.

Always:
1) List which tools you enable and why.
2) Read before write; summarize in German if user writes German.
3) create_draft / save to Drafts; send only on explicit "SEND message_id".

Output: tool-choice.md (one page), command log redacted, artifact paths.
Disable unused MCPs to reduce prompt injection surface.
Verify: re-fetch draft or list folder after write.
```

## Workflow

1. Clarify request: Gmail-OAuth, IMAP or gws.
2. Hermes MCP set: only "gmail" or "himalaya" included.
3. `gws gmail users.messages.list --user me --query "is:unread"" or "himalaya envelope list".
profits from the raising Skill **email-inbox-triage** for prioritization and draft text concerned.
PT-Corory, or/thory, or yet ororteed or in third or yet yet, or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet or yet
6. Document result list `output/email-session.md` with tool path.
7. Send step only after user sharing with message ID.

## Definition of done

the feedback the the on the the formula, – the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the on the the the aboves pull the once: the the the the the extract referred or the the and exercise referred traderslam the the the fort the or the the the the the the the treat treat the down or the the hit the the to theor or the the the take the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the thespar the tap to just the the the the and the quarter.” the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the
does not  into the presence of a then-migrant.
Re morning (WW ,  (ww) rushing upwards ( second benefiting in and ing in (ww) and (ww)
- [ ] Writing actions only as a drafts or with release

## Security

- IMAP app passwords only in Secret Store, not in argv.
- Grok/OAuth-Tokens bleiben auf Connector-Backend.
- PII in Agent-Logs minimieren; Himalaya-Logs rotieren.

## Pitfalls

- Skill and MCP in parallel for the same account → double actions.
- Himalaya without TLS → Credentials im Klartext.
- gws without richtiges `GOOGLE_APPLICATION_CREDENTIALS` → scheinbar leere Inbox.
- OpenClaw-ClawHub-Skills without `skills verify` laden.
- Send by mistake if MCP send tool is not removed from policy.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** IMAP-Firmenpostfach triagieren.
- **Input:** Server `mail.firma.example`, Skill Himalaya aktiv.
- **Prompt:**

```text
Enable only himalaya + email-inbox-triage. List unread INBOX, classify, save reply drafts locally as .eml for review.
```

- **Expected result:**

```text
Tools: himalaya, email-inbox-triage (gmail MCP disabled)
Unread: 17 | Drafts saved: output/drafts/re-28401.eml, re-28402.eml
```

### Example 2 (Example data (self-written))
- **Task:** Workspace-Inbox lesen without Send-Tool.
- **Input:** gws installiert, Policy: read+draft only.
- **Prompt:**

```text
gws list 5 newest unread, summarize subjects in German, no send tools in session.
```

- **Expected result:**

```text
1) Onboarding docs — Alice
2) Invoice #8821 — finance@
...
Send tools: none bound this session
```