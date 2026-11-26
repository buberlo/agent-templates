---
id: chat-messaging-mcp-focus
title: "Chat and messaging: MCP/skill focus"
domain: communication
category: chat-messaging
tags:
  - chat
  - communication
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub "Slack" (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "42,838 downloads, 140 registry stars (ClawHub leaderboard 23 Nov 2026)."
inputs:
  - "Target platform and permitted actions"
  - "Tool policy / MCP include list"
outputs:
  - "Tool matrix and activation log"
  - "Read-only smoke test log (message count)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Activate chat and messaging tools minimally**: separate native skills (Slack, iMessage) from cloud OAuth plugins, enforce a strict tool policy, and verify connectivity with a harmless read-only smoke test.

## When to use

- Setting up a new agent for messaging when deciding between a native skill, an MCP server, or an OAuth plugin.
- Reducing the active tool surface to limit prompt injection risk and context token usage.
- Comparing Hermes `imessage` and OpenClaw `Slack` skills on a specific host operating system.

### When not to use

- Running concrete content tasks such as summarizing threads or drafting replies (use `chat-messaging-workflow` instead).
- Targeting a messaging platform without an installed skill or authorized OAuth plugin.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Hermes `imessage` | macOS SMS/iMessage integration | Bundled platform-specific skill for macOS (`darwin`) |
| OpenClaw `Slack` | Bot or user token Slack integration | Verified registry skill for workspace messaging |
| Grok Slack plugin | Cloud OAuth connector | Operates within connected user permissions without privilege escalation |

## System prompt

```text
You design a minimal chat tooling configuration for communication/chat-messaging: pick ONE primary read path and ONE optional send path.
Work in the user's language.

Inputs:
- Host OS
- Target messaging platforms
- send_allowed (yes/no)
- hermes_include_mcp list
- openclaw tool policy snippet

Produce:
1) tool-matrix.md: platform -> tool -> install command -> required scopes
2) activation steps: hermes mcp include/exclude OR openclaw skills install + verify
3) read smoke test command (list 3 recent messages, redact message bodies in logs)
4) explicit disable list for all send/post tools if send_allowed=no (and require explicit user approval before any external message is sent when send_allowed=yes)

Platform rules:
- Grok plugin: note that posts execute as the connected user and channel ACLs remain unchanged.
- iMessage: requires macOS (darwin); if running on Linux, explicitly state that the skill is skipped and suggest an SMS API alternative only if the user provides an approved MCP.
- Never store tokens or secrets in skill Markdown files. Deliver a verification transcript with timestamps.
```

## Workflow

1. Detect the host operating system (`uname -s` for the `imessage` compatibility check) and confirm target platforms.
2. Populate `tool-matrix.md` with the selected primary read tool, scopes, and installation source.
3. Configure agent policies: exclude unneeded MCP servers in Hermes or run `openclaw skills verify slack` in OpenClaw.
4. Execute a read-only smoke test (e.g., Slack `conversations.history limit=3` or `imessage` chat list) with message bodies redacted.
5. Disable send/post tools in the policy if read-only mode is requested, or gate them behind explicit user approval.
6. Record the verification result and command transcript in `output/messaging-tooling.md`.
7. Obtain user confirmation of the tool matrix before transitioning to production messaging workflows.

## Definition of done

- [ ] Exactly one primary read stack is documented per platform
- [ ] Verification step (`skills verify`) is documented and executed for ClawHub skills
- [ ] Send tools are either disabled or gated behind explicit user approval
- [ ] On Linux hosts, skipping `imessage` is explicitly noted

## Security

- Verify ClawHub skills before production use to mitigate third-party registry risks.
- Never commit bot tokens, signing secrets, or OAuth credentials into repositories or Markdown logs.
- Complete plugin OAuth connections exclusively through official connector flows, and never auto-send messages without explicit approval.

## Pitfalls

- Running two Slack integrations in parallel, resulting in duplicate posts or conflicting rate limits.
- Enabling the `imessage` skill on a non-macOS host, leading to silent runtime failures.
- Invoking the Grok Slack plugin in a channel where the connected user is not a member, causing unclear 404/channel_not_found errors.
- Leaving an overly broad MCP include list active, causing context window overflow.
- Forgetting to disable send/post tools in the policy during a strictly read-only engagement.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Configure a read-only Slack agent (example data).
- **Input:** OpenClaw environment, `send_allowed=no`.
- **Prompt:**
```text
Write the tool matrix, disable all post/send tools, and run a smoke test on #general reading 3 messages with redacted bodies.
```
- **Expected result:**
```text
Primary: openclaw slack (read)
Disabled: chat.postMessage, imessage send
Smoke: 3 messages fetched, bodies redacted in log
File: output/messaging-tooling.md
```

### Example 2 (Example data (self-written))

- **Task:** Prepare macOS iMessage skill activation (example data).
- **Input:** Host OS `darwin`, Hermes bundled `imessage` skill.
- **Prompt:**
```text
Document imessage skill activation on macOS and list the last 2 chats with handles redacted. Gate sending behind explicit confirmation.
```
- **Expected result:**
```text
Platform: darwin — imessage skill active
Chats: +43***01 (2 msgs), team@*** (5 msgs)
Send: gated until user explicitly approves SEND
```
