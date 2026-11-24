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
  - name: Hermes-Skill imessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub „Slack“ (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "42.838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "target platform and permitted actions"
  - "Tool-Policy / MCP-Include-Liste"
outputs:
  - "Tool matrix and activation protocol"
  - "Test-Lesezugriff (Nachrichtenanzahl)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

************************************************************************************************************************************************************************************************************/ * between**** minimum* concerned. lettra- sames- 8- same benchmarks for the family

## When to use

- New agent setup for messaging; Insecurity Skill vs. MCP vs. Plugin.
- Reduction of the tool surface (prompt injection, budget).
- Vergleich Hermes imessage vs. OpenClaw Slack auf einem Host.

**When not to use**

- Konkrete Inhaltsaufgabe (Thread zusammenfassen) → `chat-messaging-workflow`.
Platform without installed skill and without plugin OAuth.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes imessage | macOS SMS/iMessage | Plattform skill, bundled |
| OpenClaw Slack | Bot/User-Token je Setup | Verifizierte Registry-Skills |
| Grok Slack plugin | Cloud OAuth | No rights increase over users |

## System prompt

```text
You design minimal chat tooling for communication/chat-messaging: pick ONE primary read path and ONE optional send path.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: host OS, platforms needed, send_allowed (yes/no), hermes_include_mcp list, openclaw tool policy snippet.
Produce:
1) tool-matrix.md: platform → tool → install command → scopes
2) activation steps: hermes mcp include/exclude OR openclaw skills install + verify
3) read smoke test command (list 3 recent messages, redact bodies in log)
4) explicit disable list for send tools if send_allowed=no
Grok plugin: note posts as connected user, channel ACL unchanged.
iMessage: require darwin; if linux, state skill skipped and suggest SMS API alternative only if user provides approved MCP.
Never store tokens in skill markdown. Deliver verification transcript with timestamps.```

## Workflow

1. The con retailings to be consuming, conning the singles consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming consuming
2 2 `tool-matrix.md` from category research.
3. Hermes: exclude unnecessary MCPs; OpenClaw: ‘openclaw skills verify slack’.
4. Slack `conversations.history limit=3` or imessage list.
ly.ly to be able to withstand.
6. Result and command protocol in `output/messaging-tooling.md`.
7. User confirms Matrix before productive workflow.

## Definition of done

- [ ] Exactly one primary reading stack documented
- [ ] Verify step mentioned/executed for ClawHub skills
- [ ] Send tools disabled or marked with release gate
- [ ] Linux + imessage: expliziter Hinweis auf Skip

## Security

- ClawHub-Skills vor Produktion verifizieren (bekannte Registry-Risiken).
- No Bot-Tokens in Repos.
- Plugin OAuth only via official connect flows.

## Pitfalls

- Zwei Slack-Integrationen parallel → doppelte Posts.
- imessage without macOS → stilles Fehlschlagen.
- Grok in Kanal without User-Mitgliedschaft → 404 without klare Ursache.
- Zu breite MCP-Include-Liste → Kontext-Overflow.
the ‘forget to use’ sets of tests

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Slack read-only Agent.
- **Input:** OpenClaw, `send_allowed=no`.
- **Prompt:**

```text
Write tool-matrix and disable all post/send tools; smoke test #general read 3 messages.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Primary: openclaw slack (read)
Disabled: chat.postMessage, imessage send
Smoke: 3 messages fetched, subjects redacted in log
File: output/messaging-tooling.md
```

### Example 2 (Example data (self-written))
- **Task:** macOS iMessage vorbereiten.
- **Input:** Darwin, Hermes bundled imessage.
- **Prompt:**

```text
Document imessage skill activation and list last 2 chats (handles redacted).
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Platform: darwin — imessage skill active
Chats: +43***01 (2 msgs), team@*** (5 msgs)
Send: gated until user types SEND
```