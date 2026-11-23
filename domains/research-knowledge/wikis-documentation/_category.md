#Wikis and documentation

- **Domain:** `research-knowledge`
- **Category:** wikis documentation `
- **As of:** 2026-11-23

## Summary

Maintain and query internal wikis, DeepWiki, docs sites and knowledge spaces.

## Recommended tool stack

- DeepWiki-MCP for public repos
- Notion/Obsidian intern

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| deepwiki MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki | Fragen zu oeffentlichen GitHub-Repos; in Hermes-Docs als Katalogbeispiel. | hermes mcp install deepwiki | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp |Notion workspace for agents (pages, databases).| Claude-Code-Docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | Im offiziellen Hermes-MCP-catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |
| Obsidian-Skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Vault lesen, suchen, Notizen anlegen/editieren – haeufiger Memory-/Wissens-Layer. | Hermes bundled /obsidian. OpenClaw: ClawHub-Skill Obsidian (steipete). | ClawHub: 92.458 Downloads, 381 Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Repo-Fragen via DeepWiki, interne Docs via Vault/Notion.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki
- https://code.claude.com/docs/en/mcp
- https://mcp.notion.com/mcp
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
