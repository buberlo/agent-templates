# Chat and messaging

- **Domain:** `communication`
- **Category:** `chat-messaging`
- **As of:** 2026-11-23

## Summary

Slack, Discord, Telegram, WhatsApp, iMessage – read and (with approval) send messages.

## Recommended tool stack

- Native Plattform-Skills (imessage, Slack) or Hersteller-Plugin

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes skill imessage | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | iMessage/SMS via imsg CLI on macOS. | Bundled apple/imessage (platform-specific). | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub „Slack“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Slack-Skill. | openclaw skills install (Owner steipete) and openclaw skills verify. | 42,838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Grok Bot Slack plugin | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Posts as the Slack user, only in channels that user is allowed to access; does not elevate permissions. | Connect Apps. | Product documentation. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Read and draft; send after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Hermes skills with platforms: [macos] are silently skipped on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
- imessage skill is macOS-specific.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://x.com/JayQinQT/status/2120856724668133406
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
