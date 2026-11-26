# Cron and Routines

- **Domain:** `automation`
- **Category:** `cron-routines`
- **As of:** 2026-11-23

## Summary

Scheduled agent jobs, weekly reviews, monitoring loops.

## Recommended tool stack

- Hermes Cron/Routines, OpenClaw scheduled jobs, Grok-Bot Routines – with Nutzungslimit and Pause-Policy

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes Cron (Feature) | Platform feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Mentioned in the Quickstart as an optional toolset (not part of Blank Slate). | Enable via hermes setup / config. | Product docs. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |
| ClawHub „Automation Workflows“ (jk-0001) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Skill for Automationen. | openclaw skills install (Owner jk-0001) and openclaw skills verify. | 73,666 Downloads, 283 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Idempotent jobs, clear quiet hours, escalate errors via chat instead of endless loops.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Hintergrundjobs verbrauchen Kontingent; Owner-Pause respektieren.

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
