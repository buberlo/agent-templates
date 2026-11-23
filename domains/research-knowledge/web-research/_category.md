# Web research

- **Domain:** `research-knowledge`
- **Category:** `web-research' `
- **As of:** 2026-11-23

## Summary

Current web search, scraping and source verification (Brave, Exa, Tavily, Firecrawl).

## Recommended tool stack

- Eine Such-API (Brave/Exa/Tavily) + Firecrawl; Browser nur wenn JS/Login noetig
- Quellen zitieren

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche via Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server |Web search and crawling, designed for agent research.| Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Echtzeit-Suche, Extract, Map, Crawl. | Siehe Repo. | 2.497 Stars | https://github.com/tavily-ai/tavily-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server |Web search, scraping and crawling as context for agents.| Offizielles MCP-Repo, typisch npx or hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp |Local browser automation with accessibility snapshots, UI tests and interaction with web apps.| npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |
| ClawHub „Multi Search Engine“ (gpyangyoujun) | Skill | https://clawhubtrends.com/leaderboard.html | Mehrere Suchmaschinen in einem Skill. |openclaw skills install (Owner gpyangyoujun) and openclaw skills verify.| 138.647 Downloads, 672 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- First search, then targeted fetching, then citing. Playwright not as a default scraper (token cost).

## Pitfalls

- MCP tool schemas can put a lot of stress on the context even before the first question comes up. In r/ClaudeAI, a user reported on 67.000 Token Overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://github.com/exa-labs/exa-mcp-server
- https://github.com/tavily-ai/tavily-mcp
- https://github.com/firecrawl/firecrawl-mcp-server
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://clawhubtrends.com/leaderboard.html
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
