---
id: outreach-mcp-focus
title: "Outreach: E-Mail-Skills vs. CRM-MCP"
domain: sales-crm
category: outreach
tags:
  - outreach
  - mcp
  - email
  - hermes
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes skills email-inbox-triage and himalaya
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub figures: Leaderboard 23.11.2026."
  - name: Hermes-Skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled-catalog."
  - name: attio MCP (Hermes-catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio"
    version_notes: "Nous-approved optional-mcps-catalog entry (listing 2026-11-23)."
inputs:
  - "Outreach-Ziel (Draft|Read inbox context|Log activity)"
  - "Active Hermes skills and permitted MCPs"
  - "Sende-Richtlinie (niemals auto-send)"
outputs:
  - "Rationale for tool selection (Skill vs. MCP)"
  - "Executed draft attachment or CRM note"
  - "Token-/Policy-Hinweis"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

For outreach, choose the **smallest working combination of tools**: Gmail via himalaya/gws for drafts, CRM-MCP only for context and activity—no duplicate inboxes, no sending by accident.

## When to use

- The agent should create a draft outreach message and log it in the CRM.
- It is unclear whether the email MCP or the Hermes skill is cheaper.
- OpenClaw/Hermes Tool-Policy begrenzt MCP-Anzahl.

**When not to use**

- Pure copywriting without an email or CRM system.
- Bulk mail via third-party API without compliance review.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| himalaya / gws | Gmail Drafts | Offizieller Workspace-Pfad |
| attio MCP | Person/Deal-Kontext | Strukturierte Felder |
| Email inbox triage skill | Thread context | Reads, does not send |

## System prompt

```text
You route outreach tasks to the smallest tool set (sales-crm/outreach-mcp-focus).

Decision tree:
1) User needs only email draft → gws/himalaya create draft; skip attio unless logging requested.
2) User needs contact context (title, last activity) → attio MCP read first; then draft email.
3) User needs inbox thread summary before reply → email-inbox-triage skill read-only; never send.
4) User asks "log in CRM" → attio draft note or task; do not mark email sent.
5) Close MCP only when user names Close AND sequence content—not default with attio same session.

Never enable a second mailbox MCP alongside himalaya for the same Gmail—duplicate OAuth scopes.

Quote estimated MCP schema tokens if user loads full attio catalog—recommend include filter.

Send policy: hard stop. If tool offers "send", use draft/create only and report draft id.

LinkedIn: no MCP unless user has one approved—output copy for manual paste.

Document: chosen tools, rejected tools, rationale in German one paragraph.

Hermes: respect skill progressive disclosure—load outreach workflow content not entire catalog.

GrokBot: OAuth stays on connector—no refresh tokens in argv.

Verify: after draft create, read-back subject line if API allows.

Parallelism: sequential CRM read then email draft to avoid race on person id.

German outreach copy allowed in draft body; metadata in English ok.

Incident: if draft created wrong recipient, report draft id for user deletion—do not create replacement silently.

Attio rate limits: batch reads ≤20 records.

Close sequences: never enroll contacts in this focus template—refer to outreach-workflow for content only.
```

## Workflow

1. Classify task: Draft / Context / Inbox / CRM log.
2. Check active tools against policy; remove redundancy.
3. CRM read when personalization is missing.
4. Inbox context only for reply tasks.
5. Create draft via gws/Himalaya.
6. Write CRM activity as a draft.
7. Brief report on tool selection + no send confirmation.

## Definition of done

- [ ] Exactly one email path used
- [ ] No URL0 without approval
- [ ] Justification for rejected MCPs
- [ ] Draft or note ID documented

## Security

- Two sending tools running in parallel = highest risk—deactivate.
- Mailbox access only with user OAuth.
- Medium risk of accidental recipient.

## Pitfalls

- Write attio MCP for the email body, even though only a Gmail draft is desired.
- gws Draft in falschem Google-Account.
- The Triage skill also reads private HR emails in the context of Outreach.
- MCP-Token-Overhead frisst Copy-Budget.
- CRM note linked without person ID.

## Basic examples

### Example 1 (Example data)

- **Task:** Draft + CRM log for a contact
- **Input:** attio person_id, Betreffidee
- **Prompt:**

```text
Read person, write DE draft ≤100 words, log draft note in attio—no send.
```

- **Expected result:**

```text
Tools: attio read, gws draft create
draft_id: r-123 | note: "draft created 2026-11-23"
```

### Example 2 (Example data)

- **Task:** Reply context without CRM
- **Input:** Gmail thread id
- **Prompt:**

```text
Summarize thread, propose reply bullets. No MCP except triage skill.
```

- **Expected result:**

```text
3 bullet summary; proposed reply in German; attio not loaded
```