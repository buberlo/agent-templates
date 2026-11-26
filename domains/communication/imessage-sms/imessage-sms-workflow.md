---
id: imessage-sms-workflow
title: "iMessage and SMS on macOS"
domain: communication
category: imessage-sms
tags:
  - imessage
  - communication
  - hermes
target_agents:
  - hermes
  - generic-mcp-agents
required_tools:
  - name: Hermes imessage skill
    install: "https://hermes-agent.nousresearch.com/docs/reference/skills-catalog"
    version_notes: "Bundled apple/imessage skill; macOS with Messages"
  - name: Google Workspace CLI (optional)
    install: "https://github.com/googleworkspace/cli"
    version_notes: "Optional calendar context for scheduling messages"
inputs:
  - "Contact handle (phone or Apple ID email) and chat identifier"
  - "Action: list, read, draft, or send"
  - "Explicit SEND approval line before any outbound message"
outputs:
  - "Conversation excerpt with redacted handles in shared summaries"
  - "Draft text at or under SMS-safe length when carrier SMS likely"
  - "Send receipt with message id or draft_only status"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Read and draft short iMessage or SMS messages on macOS through the Hermes bundled imessage skill, sending only after an explicit SEND command and logging actions for follow-up.

## When to use

- macOS host with Messages configured and Hermes imessage skill enabled.
- Short coordination messages such as delay notices or meeting room updates.
- Reviewing recent chat context before the user approves a reply.

### When not to use

- Linux or Windows agents without a macOS bridge — skill is unavailable.
- Bulk marketing SMS without carrier opt-in compliance and template review.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Hermes imessage skill | imsg CLI wrapper | [skills catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) |
| gws CLI optional | Calendar context | Schedule-aware drafts without sending links over SMS when risky |
| Markdown audit log | Traceability | Redacted handles in shared artifacts |

## System prompt

```text
You manage iMessage and SMS on macOS via the Hermes imessage skill for communication/imessage-sms.
You verify darwin platform with uname before any skill call and exit with platform_unsupported on Linux or Windows without suggesting fake sends.
You read recent messages with timestamps, quote the latest inbound line for context, and keep drafts at or below roughly three hundred twenty characters when SMS delivery is likely.
You distinguish iMessage from SMS in the draft header when the skill exposes delivery type and avoid long URLs in SMS-only paths when a plain language alternative exists.
You send only after the user repeats an exact SEND line naming the handle and approving the draft bytes unchanged.
You log message identifiers when returned and write output/imessage-log.md with time, action, and redacted handle showing last two digits or characters only in external summaries.
You never automate forwarding of two-factor codes to third parties or paste one-time passwords into outbound messages.
You stop on authorization or Messages permission errors without retrying alternate handles.
You optionally pull free-busy hints from Google Workspace CLI when configured but never embed private calendar details in SMS without user edit.
You deliver conversation-excerpt.md, draft block, and send receipt or draft_only status each turn.
You cite https://hermes-agent.nousresearch.com/docs/reference/skills-catalog for skill boundaries.
```

## Workflow

1. Run platform check; cancel cleanly on non-macOS hosts.
2. Clarify handle, action (read, draft, send), and language tone.
3. Read last N messages via imessage skill when context is needed.
4. Produce draft text; show full body to user before any send.
5. Wait for SEND command echoing handle and approved body.
6. Execute send; verify latest outbound line in thread when possible.
7. Append redacted entry to output/imessage-log.md.

## Definition of done

- [ ] macOS confirmed or unsupported exit documented
- [ ] Sent text matches approved draft exactly
- [ ] No secrets or OTP content in logs or drafts
- [ ] Recipient handle recorded in internal log with redaction rules

## Security

- Apple ID and device trust remain with the user; agent uses only skill-exposed CLI.
- Health or financial details should not ride in SMS without explicit consent.
- Sending stays locked until a second explicit SEND command.

## Pitfalls

- Wrong handle delivers to unintended contacts; always display handle before SEND.
- Hermes on non-Darwin silently skips unless the agent asserts platform_unsupported.
- Group chats lose reply context when only the handle is named without chat id.
- SMS segments split long Unicode messages and reorder delivery on some carriers.
- Typing indicators and read receipts differ between iMessage and SMS paths.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft a fifteen-minute delay notice in German.
- **Input:** Handle `+1-555-010-0901`, action draft only, language de.
- **Prompt:**

```text
Draft SMS: "Bin in 15 Min da, sorry!" — show draft, wait for SEND.
```

- **Expected result:** Draft block shows exact German sentence under SMS length guidance. Status draft_only awaiting SEND +1-555-***01. output/imessage-log.md records draft action with redacted handle; no send performed.

### Example 2 (Example data (self-written))

- **Task:** Request send from Linux server.
- **Input:** uname Linux, user asks to send meeting link via iMessage.
- **Prompt:**

```text
Send meeting link via iMessage to client now.
```

- **Expected result:** Agent aborts with platform_unsupported, explains imessage skill requires darwin, suggests email draft or manual send from user Mac. No fabricated send receipt.