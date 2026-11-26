# Notion

- **Domain:** `office-documents`
- **Category:** `notion`
- **As of:** 2026-11-23

## Summary

Seiten and Datenbanken in Notion suchen, anlegen and aktualisieren.

## Recommended tool stack

- Hosted Notion MCP
- Klare Datenbank-Properties im Prompt

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion workspace for agents (pages, databases). | Claude Code docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | In the official Hermes MCP catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |
| ClawHub „Notion“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Skill-Variante neben MCP. | openclaw skills install (Owner steipete) and openclaw skills verify. | 84,423 Downloads, 246 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Claude Code docs cite Notion as a canonical HTTP MCP example.
- Write changes to shared DBs only after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://mcp.notion.com/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
