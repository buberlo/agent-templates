# Landingpages

- **Domain:** `content-marketing`
- **Category:** `landing-pages`
- **As of:** 2026-11-23

## Summary

Drawings from landing pages and marketing sites as HTML/Coin or in Webflow/CMS.

## Recommended tool stack

- Schreibende Skills + Humanizer
Search/crawl for facts
Channel APIs only with release

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche ueber Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server |Web search, scraping and crawling as context for agents. specialised MCP-Repo, typically npoma or hosted according to README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl satisfying/fitrecrawl-mcp server | no (as cited) |

## Typical workflows

- Set task, allowed tools and definition of done.
- First read/research, then draft, then release for effective steps.
- Reread output (file, URL, ticket) and specify source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policies and prompt budgets. Sources: https://urners-agent.nousnesssearch.com/docs/user guide no into , https://doc respects.
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://github.com/firecrawl/firecrawl-mcp-server
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
