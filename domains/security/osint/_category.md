# OSINT (openly available sources)

- **Domain:** `security`
- **Category:** `osint`
- **As of:** 2026-11-23

## Summary

systematically collect public information; No illegal access methods.

## Recommended tool stack

- Oeffentliche Such-MCPs, nur offene Quellen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche ueber Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server |Web search and crawling, designed for agent search.| Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Echtzeit-Suche, Extract, Map, Crawl. | Siehe Repo. | 2.497 Stars | https://github.com/tavily-ai/tavily-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server |Web search, scraping and crawling as context for agents.| Offizielles MCP-Repo, typisch npx or hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |

## Typical workflows

- Fragestellung, nur oeffentliche Quellen, Herkunft dokumentieren.

## Pitfalls

- No Zugangsumgehung, kein Social Engineering.
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://github.com/exa-labs/exa-mcp-server
- https://github.com/tavily-ai/tavily-mcp
- https://github.com/firecrawl/firecrawl-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
