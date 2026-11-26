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
  - name: Hermes skills email-inbox-triage and himalaya
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "ClawHub figures: leaderboard 23 Nov 2026."
  - name: Hermes skill google-workspace / gws CLI
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled catalog."
inputs:
  - "Context and briefing for email tooling"
  - "Mailbox type, files, URLs, or message IDs per task"
outputs:
  - "Documented tool selection, redacted command log, and saved draft artifacts"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Select and configure targeted email tool stacks**: choose between Hermes `email-inbox-triage` + `himalaya` (IMAP/SMTP) or `gws` / Gmail MCP—using skills for structured triage workflows and MCP connectors for OAuth access while keeping **draft creation (never auto-sending)** as the strict default.

## When to use

- Restricting an agent to activate only the minimum required email tools via MCP include/exclude lists and tool policies.
- Operating across a mix of Google Workspace (`gws`) and third-party IMAP mailboxes.
- Documenting which operational path uses Gmail MCP versus the Himalaya CLI.

### When not to use

- Running a single recurring Gmail triage routine with fixed queries (use `email-gmail-mcp-triage` instead).
- Environments without configured OAuth connectors or secure secret-store handling for IMAP credentials.
- High-risk bulk or mass outbound email campaigns.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| `email-inbox-triage` | Inbox prioritization and reply drafting | Bundled Hermes workflow skill |
| `himalaya` / `imap-smtp-email` | IMAP/SMTP CLI access | Works with standard IMAP servers beyond Google-only setups |
| `gws` CLI | Gmail, Calendar, and Drive CLI | Unified Google Workspace inbox management from one CLI |
| Grok Gmail plugin | Session-bound read/draft access | Official OAuth connector managed by the platform |

## System prompt

```text
You configure and operate email tools for communication/email: Hermes email-inbox-triage, himalaya CLI, gws CLI, or Gmail MCP—activating only the minimum tool set required for the task.
Work in the user's language.

Inputs:
- mailbox_type (gmail_oauth | imap | workspace_gws)
- allowed_actions (read | draft | label | send)
- credential_location (reference to secret store or OAuth profile; never paste raw secrets)

Routing decision:
- Gmail with MCP available -> MCP search + create_draft.
- Generic IMAP -> himalaya envelope list + folder sync; save drafts locally or in Drafts folder, and use SMTP send only after explicit user approval.
- Workspace admin or CLI tasks -> gws gmail users.messages.list.

Mandatory rules:
1) List which tools you enable and explain why; disable unused MCPs to reduce the prompt injection surface.
2) Always read before writing and summarize findings in the user's language (defaulting to English).
3) Default all outbound compositions to create_draft / save to Drafts. Never auto-send; execute a send action only upon explicit user approval ("SEND <message_id>").
4) Verify writes by re-fetching the draft ID or listing the Drafts folder.

Outputs:
- tool-choice.md (one-page decision summary)
- Redacted command log and saved artifact paths
```

## Workflow

1. Clarify the mailbox requirement: Gmail OAuth, generic IMAP, or Google Workspace (`gws`).
2. Configure the Hermes MCP filter or tool policy to include only the chosen backend (`gmail` or `himalaya`).
3. List unread messages via `gws gmail users.messages.list --user me --query "is:unread"` or `himalaya envelope list`.
4. Run the `email-inbox-triage` skill to prioritize threads and prepare reply text.
5. Save replies strictly as drafts (via MCP `create_draft`, local `.eml` files, or the IMAP Drafts folder).
6. Document the active tool path, message counts, and draft locations in `output/email-session.md`.
7. Execute any actual send step only if the user explicitly approves with the target message ID.

## Definition of done

- [ ] Enabled email tools are documented with a clear rationale
- [ ] No credentials or tokens appear in chat logs or Markdown files
- [ ] At least one read operation is verified (unread count or redacted header snippet)
- [ ] Outbound operations are restricted to drafts or gated behind explicit user approval

## Security

- Store IMAP app passwords exclusively in a system secret store, never in command-line arguments (`argv`) or config files committed to git.
- Keep OAuth tokens managed on the official connector backend.
- Minimize PII in agent logs, rotate local Himalaya logs, and require explicit approval before sending any email.

## Pitfalls

- Enabling both a CLI skill and an MCP server in parallel for the same mailbox, causing duplicate drafts or label changes.
- Running Himalaya without TLS enabled, exposing credentials in plaintext.
- Invoking `gws` without a valid `GOOGLE_APPLICATION_CREDENTIALS` setup, resulting in an apparently empty inbox.
- Loading third-party registry skills without running `skills verify` first.
- Leaving the MCP send tool enabled in a draft-only policy, risking accidental transmission.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Triage a company IMAP mailbox and save local reply drafts (example data).
- **Input:** IMAP server `mail.company.example`, Himalaya CLI and `email-inbox-triage` skill enabled.
- **Prompt:**
```text
Enable only himalaya + email-inbox-triage. List unread messages in INBOX, classify them, and save reply drafts locally as .eml files for review without sending.
```
- **Expected result:**
```text
Tools: himalaya, email-inbox-triage (gmail MCP disabled)
Unread: 17 | Drafts saved: output/drafts/re-28401.eml, output/drafts/re-28402.eml
```

### Example 2 (Example data (self-written))

- **Task:** Read a Google Workspace inbox with send tools disabled (example data).
- **Input:** `gws` CLI installed, policy set to `read+draft` only.
- **Prompt:**
```text
Use gws to list the 5 newest unread messages, summarize their subjects, and ensure no send tools are bound in this session.
```
- **Expected result:**
```text
1) Onboarding docs — Alice
2) Invoice #8821 — finance@
...
Send tools: none bound this session
```
