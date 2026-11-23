# Web-Scraping

- **Domain:** `daten-analytics`
- **Category:** `web-scraping`
- **As of:** 2026-11-23

## Summary

Strukturierte Extraktion von Webdaten; Firecrawl, Browser-MCPs, respektiert robots/ToS.

## Recommended tool stack

- Firecrawl/Exa/Tavily extract zuerst
Browser MCP only if necessary

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping, and crawling as agent context. | Official MCP repo; typically npx or hosted per README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as documented) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Web search and crawling designed for agent research. | See repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | no (as documented) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Real-time search, extract, map, crawl. | See repo. | 2.497 Stars | https://github.com/tavily-ai/tavily-mcp | no (as documented) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and web app interaction. | npx @playwright/mcp@latest (official docs/repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | no (as documented) |

## Typical workflows

- ToS check, rate-limit, strukturiertes Schema vorgeben.

## Pitfalls

- Playwright als Scraper ist token-teuer.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/firecrawl/firecrawl-mcp-server
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://github.com/exa-labs/exa-mcp-server
- https://github.com/tavily-ai/tavily-mcp
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
