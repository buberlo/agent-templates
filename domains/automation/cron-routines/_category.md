# Cron and Routines

- **Domain:** `automation`
category: Cron-routines `
- **As of:** 2026-11-23

## Summary

Scheduled agent jobs, weekly reviews, monitoring loops.

## Recommended tool stack

Hermes Cron/Routines, OpenClaw scheduled jobs, Grok-Bot Routines – with usage limit and break policy

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Hermes Cron (Feature) | Platform Feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | In Quickstart as an optional toolset (not part of Blank Slate). | Activate via hermes setup / Config. | Product documentary. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |
| ClawHub “Automation Workflows” (jk-0001) | Skill | https://clawhubtrends.com/leaderboard.html | Community skill for automation. | openclaw skills install (Owner jk-0001) and openclaw skills verify. | 73,666 downloads, 283 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

Typical workflows

- Idempotent jobs, clear quiet hours, errors via chat escalate instead of endless loop.

## Pitfalls

- background jobs consume contingent; Respect owner-pause.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
