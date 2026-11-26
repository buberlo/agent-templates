# Browser Automation

- **Domain:** `automation`
- **Category:** `browser-automation`
- **As of:** 2026-11-23

## Summary

Playwright MCP, Chrome DevTools MCP, cloud browsers; mind the token costs.

## Recommended tool stack

- Playwright MCP for local UI tests
- Chrome DevTools MCP for Debugging
- Firecrawl/search MCP for read-only tasks
- Tokenbudget ueberwachen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Control and debug live Chrome (Performance, Network, Console) for coding agents. | Via the GitHub repo / MCP client config (stdio), see README. | 58,941 stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping, and crawling as context for agents. | Official MCP repo, typically npx or hosted per the README. | 7,886 Stars; Upstream 207,417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Browserbase MCP | MCP | https://github.com/browserbase/mcp-server-browserbase | Cloud browser with Stagehand. | See the repo. | 3,397 stars | https://github.com/browserbase/mcp-server-browserbase | no (as cited) |
| ClawHub „Playwright MCP“ (spiceman161) | Skill | https://clawhubtrends.com/leaderboard.html | Skill-Wrapper um Playwright MCP. | openclaw skills install (Owner spiceman161) and openclaw skills verify. | 39,713 Downloads, 146 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub „Agent Browser“ (matrixy) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Browser-Skill. | openclaw skills install (Owner matrixy) and openclaw skills verify. | 105,425 Downloads, 376 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub "Browser Use" (shawnpana) | Skill | https://clawhubtrends.com/leaderboard.html | Community browser skill. Flagged with a warning on the leaderboard – verify before use. | openclaw skills install (owner shawnpana) and openclaw skills verify. | 40,606 downloads, 101 registry stars (ClawHub leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Your own app's UI: Playwright or DevTools. Reading public websites only: search/Firecrawl. Clearly separate login sessions.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Snapshot-Schwemme. Community-Alternativen werben with kleineren Payloads – unabhaengig benchmerken.

## Sources

- https://playwright.dev/mcp/introduction
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://clawhubtrends.com/leaderboard.html
- https://github.com/microsoft/playwright-mcp
- https://github.com/firecrawl/firecrawl-mcp-server
- https://github.com/browserbase/mcp-server-browserbase
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
