# Web research

- **Domain:** `research-knowledge`
- **Category:** `web-research`
- **As of:** 2026-11-23

## Summary

Live web search, scraping and source verification (Brave, Exa, Tavily, Firecrawl).

## Recommended tool stack

- One search API (Brave/Exa/Tavily) + Firecrawl; browser only if JS/login is required
- Cite sources

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Web search via the Brave Search API. | Official Brave repository. | 1,585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Web search and crawling, designed for agent research. | See the repo (hosted/stdio). | 5,264 stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Real-time search, extract, map, and crawl. | See the repo. | 2,497 stars | https://github.com/tavily-ai/tavily-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping, and crawling as context for agents. | Official MCP repo, typically npx or hosted per the README. | 7,886 Stars; Upstream 207,417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |
| ClawHub "Multi Search Engine" (gpyangyoujun) | Skill | https://clawhubtrends.com/leaderboard.html | Multiple search engines in a single skill. | openclaw skills install (owner gpyangyoujun) and openclaw skills verify. | 138,647 downloads, 672 registry stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Search first, then fetch selectively, then cite. Do not use Playwright as the default scraper (token costs).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/

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
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
