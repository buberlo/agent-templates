# OSINT (openly available sources)

- **Domain:** `security`
- **Category:** `osint`
- **As of:** 2026-11-23

## Summary

Systematically collect public information; no illegal access methods.

## Recommended tool stack

- Oeffentliche Such-MCPs, only offene Sources

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Web search via the Brave Search API. | Official Brave repository. | 1,585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Web search and crawling, designed for agent research. | See the repo (hosted/stdio). | 5,264 stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Real-time search, extract, map, and crawl. | See the repo. | 2,497 stars | https://github.com/tavily-ai/tavily-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping, and crawling as context for agents. | Official MCP repo, typically npx or hosted per the README. | 7,886 Stars; Upstream 207,417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Fragestellung, only oeffentliche Sources, Herkunft dokumentieren.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- No access circumvention, no social engineering.
- These templates do not include attack or bypass instructions.

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://github.com/exa-labs/exa-mcp-server
- https://github.com/tavily-ai/tavily-mcp
- https://github.com/firecrawl/firecrawl-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
