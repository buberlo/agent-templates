# Chat and messaging

- **Domain:** `communication`
- **Category:** `chat-messaging`
- **As of:** 2026-11-23

## Summary

Slack, Discord, Telegram, WhatsApp, iMessage – Read and send messages (shared).

## Recommended tool stack

Native platform skills (imessage, Slack) or manufacturer plugin

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill imessage | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | iMessage/SMS ueber imsg CLI auf macOS. | Bundled apple/imessage (plattformgebunden). | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub ‘Slack’ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Slack-Skill. | openclaw skills install (Owner steipete) and openclaw skills verify. | 42,838 downloads, 140 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Grok Bot Slack-Plugin | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp |Post as the Slack user, only in canals that he may enter; does not increase rights.| Connect Apps. | Produktdoku. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

In cross- checks most ports cross- important crosses both Most cross- inter cross cross cross port cross which cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross cross- important cross- important cross- important cross- important cross- important cross cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- cross- important cross- important cross- important cross- important cross- important cross cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross- important cross cross- important cross- important cross- important cross- important cross- important cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross cross-in cross- cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross-in cross cross-in

## Pitfalls

- Hermes skills with platforms: [macos] are skipped silently on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
- imessage-Skill ist macOS-spezifisch.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
