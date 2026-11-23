# News-Monitoring

- **Domain:** `research-knowledge`
- **Category:** `news-monitoring' `
- **As of:** 2026-11-23

## Summary

Companies, topics or competitors are constantly observing and summarizing them.

## Recommended tool stack

- competitor-news-monitor Skill
- Suche + geplante Routine

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill competitor-news-monitor | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Genannte Unternehmen auf wesentliche News beobachten, zitierte Digests. | Bundled research/competitor-news-monitor. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub „News Summary“ (joargp) | Skill | https://clawhubtrends.com/leaderboard.html | Community-News-Skill. |openclaw skills install (Owner Joargp) and openclaw skills verify.| 40.766 Downloads, 129 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Watchlist, Frequenz, nur verlinkte Funde.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
