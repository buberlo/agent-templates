# Notion

- **Domain:** `office-documents`
- **Category:** `notion`
- **As of:** 2026-11-23

## Summary

pages and databases in Notion suchen, anlegen and aktualisieren.

## Recommended tool stack

- Hosted Notion MCP
- Klare Datenbank-Properties im Prompt

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion-Workspace for agents (pages, databases). | Claude-Code-Docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | Im official Hermes-MCP-catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |
| ClawHub „Notion“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Skill-Variante neben MCP. | openclaw skills install (Owner steipete) and openclaw skills verify. | 84.423 Downloads, 246 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Claude-Code-Docs nennen Notion as kanonisches HTTP-MCP-Example.
- Writede changes an geteilten DBs only after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://mcp.notion.com/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
