# Wikis and Dokumentation

- **Domain:** `research-knowledge`
- **Category:** `wikis-documentation`
- **As of:** 2026-11-23

## Summary

Maintain and query internal wikis, DeepWiki, docs sites and knowledge spaces.

## Recommended tool stack

- DeepWiki-MCP for oeffentliche Repos
- Notion/Obsidian intern

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| deepwiki MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki | Questions about public GitHub repos; used as a catalog example in Hermes docs. | hermes mcp install deepwiki | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion workspace for agents (pages, databases). | Claude Code docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | In the official Hermes MCP catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |
| Obsidian skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Read and search vault, create/edit notes – common memory/knowledge layer. | Hermes bundled /obsidian. OpenClaw: ClawHub skill Obsidian (steipete). | ClawHub: 92,458 downloads, 381 stars (leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Repo questions via DeepWiki, internal docs via vault/Notion.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

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
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
