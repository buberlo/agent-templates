# Library management

- **Domain:** `research-knowledge`
- **Category:** `library-zotero`
- **As of:** 2026-11-23

## Summary

Zotero and comparable libraries for sources, PDFs and citations.

## Recommended tool stack

- Search-MCP + Fetch/Firecrawl + Zitations-Skill

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche via Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server |Web search and crawling, designed for agent research.| Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server |Web search, scraping and crawling as context for agents.| Offizielles MCP-Repo, typisch npx or hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |

## Typical workflows

- Set task, allowed tools and definition of done.
- First read/research, then draft, then release for effective steps.
- Reread output (file, URL, ticket) and specify source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://github.com/exa-labs/exa-mcp-server
- https://github.com/firecrawl/firecrawl-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
