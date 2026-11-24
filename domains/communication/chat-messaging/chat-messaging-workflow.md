---
id: chat-messaging-workflow
title: "Chat and messaging"
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
  - name: Hermes skill iMessage
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled."
  - name: ClawHub "Slack" (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "42,838 downloads, 140 registry stars (ClawHub leaderboard 2026-11-23)."
  - name: Grok Bot Slack plugin
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Product documentation."
inputs:
  - "Channel or chat ID"
  - "Time range / last N messages"
  - "Tone and approval for send"
outputs:
  - "Thread summary"
  - "Message draft (optionally sent after OK)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Read Slack, iMessage, and similar channels**, bundle threads, and **post replies only after approval**—including @mentions and channel context.

## When to use

- Team asks for a digest of a channel or DM thread.
- Reply draft for Slack/iMessage; human sends or gives explicit OK.
- Platform skill (Slack OpenClaw, Hermes iMessage on macOS) is available.

**When not to use**

- WhatsApp/Telegram without an official, policy-compliant connector.
- Linux host for **iMessage** (skill is platform-bound; skipped).
- Crisis communications without an agreed messaging playbook.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| OpenClaw Slack skill | Read/post channel | Broad ClawHub usage |
| Hermes iMessage | macOS iMessage/SMS | Native imsg CLI |
| Grok Slack plugin | OAuth as user | Allowed channels only |

## System prompt

```text
You handle team chat for communication/chat-messaging: read threads, summarize, draft replies; post/send only after user approval.

Inputs: platform (slack | imessage), channel_or_chat_id, since (ISO time or "last 24h"), goal (summarize | draft_reply | list_action_items), tone (formal DE default).

Slack flow:
- Fetch channel history with thread replies; note authors and timestamps.
- Summarize decisions, open questions, owners.
- Draft reply in thread or channel; show exact text before postMessage.

iMessage flow (macOS only):
- List recent messages for handle; never send without "SEND to <handle>".

Rules:
- Respect user channel membership (Grok: cannot post where user has no access).
- No secrets, tokens, or attachment exfiltration in summaries.
- Mark uncertain attributions with [?].

Deliver: summary.md, draft message block, list of message IDs referenced.
```

## Workflow

1. Choose platform and verify access (`openclaw skills verify` for ClawHub skills).
2. Slack: set channel ID and `since`; load history including threads.
3. Deduplicate messages; extract decisions and open points.
4. Write reply draft in target tone; fit channel length norms.
5. Show draft to user; wait for `SEND` or edits.
6. On approval: `chat.postMessage` or iMessage send with confirmed text.
7. Archive `output/chat-log.md` with message IDs and timestamps.

## Definition of done

- [ ] Summary references real authors/times
- [ ] No sent message without documented OK
- [ ] Slack replies use correct thread context (thread_ts when needed)
- [ ] Platform limits documented (iMessage on macOS)

## Security

- Do not copy internal strategy chats into public summaries.
- Process screenshots/attachments only with approval.
- OAuth plugins: no tokens in prompts.

## Pitfalls

- Reply in wrong thread → noise.
- @channel without approval → notification storm.
- iMessage skill disabled on Linux → empty output without clear error.
- Grok posts as user → confused with human voice.
- Rate limits on large backfills.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** #product digest 24h.
- **Input:** Slack `#product`, since `2026-11-22T09:00:00+01:00`.
- **Prompt:**

```text
Summarize decisions and action items from #product last 24h; draft one paragraph standup update, do not post.
```

- **Expected result:**

```text
Decisions: Ship v2.1 Friday; defer mobile redesign.
Action items: @maria API spec by Wed; @tom QA checklist.
Draft (not posted): "Good morning — v2.1 stays Friday..."
```

### Example 2 (Example data (self-written))
- **Task:** Missing channel ID.
- **Input:** Name "product" only, no workspace context.
- **Prompt:**

```text
Post update to product channel.
```

- **Expected result:**

```text
Abort: channel_id unknown.
Ask: workspace + channel ID or invite link?
No postMessage executed.
```