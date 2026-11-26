---
id: grokbot-scheduled-x-research-brief-v1
title: "Grok Bot scheduled X research brief"
domain: agent-platforms
category: grokbot
tags:
  - grokbot
  - x-api
  - scheduled
  - research
target_agents:
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Grok Bot 101
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Connect Apps and Custom MCP; scheduled task patterns."
  - name: X MCP (Grok Bot)
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Public post reads via Connect Apps when enabled; follow X API terms."
inputs:
  - "Research topic and neutral search keywords (no harassment targets)"
  - "Schedule cadence the user configures in Grok Bot (e.g. weekly)"
  - "Output format: bullet brief, max length, citation style for X posts"
outputs:
  - "Recurring brief template with sourced post URLs only from tool results"
  - "Tool policy table: allowed X reads, blocked post/create tools"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-26"
---

## Purpose

Configure **Grok Bot** to produce a **scheduled public X research brief** using **Connect Apps** read tools, with **create_posts** and other write tools blocked unless explicitly approved ([Grok Bot 101](https://x.ai/bot/guides/grok-bot-101)). For unofficial connector notes, label community guides separately from xAI docs.

## When to use

- A founder wants a weekly roundup of discourse on a product category from public posts only.
- Compliance requires human-readable citations (post URLs) and no automated posting.
- The bot runs on xAI-hosted infrastructure and OAuth stays on connectors, not in prompts.

### When not to use

- Targeting private individuals, non-public accounts, or coordinated harassment.
- Campaigns that require automated posting without human review—use separate approval workflow.
- Tasks needing localhost MCP on a developer laptop without bot-box command or public HTTPS.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Grok Bot Connect Apps (X) | Read public posts | Curated plugin with tool policies |
| Custom MCP (optional) | Enrichment | Only HTTPS or bot-box command per Grok Bot model |
| Scheduled Grok Bot task | Cadence | User sets schedule in product UI |
| Notion or email (optional) | Delivery | Human pastes brief; no auto-DM without approval |

## System prompt

```text
You design Grok Bot scheduled research briefs for agent-platforms/grokbot using official guidance at https://x.ai/bot/guides/grok-bot-101.
You configure tool policies so X read and search tools are allowed or need approval while create_posts, delete, and mass-DM tools remain blocked unless the user explicitly enables them for a different workflow.
You write briefing prompts that demand neutral tone, public-source-only claims, and full https://x.com/... citations copied from tool output rather than invented.
You refuse to schedule briefs focused on private individuals, leaked data, or non-public content.
You document Connect Apps OAuth boundaries: the bot does not receive raw user X tokens in chat according to the connector model described in Grok Bot guides.
You cap brief length and section count so scheduled runs stay within typical context limits and user reading time.
You include a pitfall note that unofficial wiki guides are not xAI documentation and should be labeled when cited for MCP wiring tips.
You recommend a human review step before forwarding the brief to executives or clients.
You never store X API keys or bot admin tokens in the scheduled prompt text.
You deliver the scheduled task prompt text, tool policy table, and an example brief block with fictional but realistic structure.
```

## Workflow

1. Confirm research topic, keyword list, and blocked behaviors with the user.
2. Enable X Connect App; set tool policy: allow read/search, block create_posts.
3. Draft scheduled prompt requiring citations and uncertainty labels for unverified rumors.
4. Run one manual test execution; capture tool call list and resulting brief.
5. User reviews test brief for tone and compliance; adjusts keywords.
6. Activate schedule in Grok Bot UI; note timezone and recipient channel.
7. Log each run's post URLs in a shared doc optionally via human paste (no automated exfiltration).
8. Quarterly review: rotate keywords, re-check tool policies after plugin updates.

## Definition of done

- [ ] Tool policy blocks write/post tools by default
- [ ] Test brief includes only URLs returned by X read tools
- [ ] Schedule documented with owner and review step
- [ ] No private or non-public targeting in prompt

## Security

- Public X data still contains PII; redact handles when sharing externally if policy requires.
- Custom MCP URLs must be TLS and reviewed—shared bot teams may see command args.
- Do not embed secrets in scheduled prompts visible to bot admins.

## Pitfalls

- Models may invent posts if tools fail—require "no tool results → say unavailable" instruction.
- Skill ceilings on Grok Bot limit very large skill bundles; keep prompt focused.
- Scheduled tasks cannot reach developer laptop MCP without bot-box hosting.
- Community wiki install steps may lag product UI—prefer x.ai bot guides for policies.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Weekly brief on "MCP server security" discourse for product marketing (internal only).
- **Input:** Keywords: MCP security, model context protocol, OAuth; Fridays 09:00 UTC; max 12 bullets.
- **Prompt:**

```text
Draft Grok Bot scheduled prompt and tool policy. Manual test run once. No posting.
```

- **Expected result:**

```text
Tool policy: search_posts allow; create_posts block.
Test brief: 8 bullets, each with one https://x.com/... link from tool output, plus 2 labeled "unverified rumor" items downgraded with no recommendation.
Closing line: not financial or legal advice; human editor Jane Doe before exec forward.
Schedule metadata recorded for user to enter in Grok Bot UI (not automated by agent).
```

### Example 2 (Example data (self-written))

- **Task:** Block brief when X tools return rate limit errors.
- **Input:** Fictional rate limit response on test run.
- **Prompt:**

```text
Update prompt to handle empty/rate-limited X results without fabrication.
```

- **Expected result:**

```text
Brief body: "X read tools unavailable (rate limit). No posts cited this run."
Zero fabricated URLs; log shows error from connector.
User notified to retry later; schedule not disabled.
Reminder to check X developer terms for search automation limits.
```