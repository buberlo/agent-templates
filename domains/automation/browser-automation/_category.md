# Browser Automation

- **Domain:** `automation`
category: browser automation `
- **As of:** 2026-11-23

## Summary

Playwright MCP, Chrome DevTools MCP, Cloud Browser; Consider token costs.

## Recommended tool stack

Playwright MCP for local UI tests
Chrome DevTools MCP for Debugging
Firecrawl/Search MCP for pure reading
- Monitor token budget

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation over accessibility snapshots, UI testing and interaction with web apps. | npx @playwright/mcp@latest (official Docs/Repo). | 40,040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Live Chrome Control and Debug (Performance, Network, Console) for coding agents. | About the GitHub repo / MCP client config (stdio), see README. | 58.941 Stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | no (as cited) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Web search, scraping and crawling as context for agents. | Official MCP repo, typically npx or hosted according to README. | 7,886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | no (as cited) |
| Browserbase MCP | MCP | https://github.com/browserbase/mcp-server-browserbase | Stagehand cloud browser. | See Repo. | 3.397 Stars | https://github.com/browserbase/mcp-server-browserbase | no (as cited) |
| ClawHub “Playwright MCP” (spiceman161) | Skill | https://clawhubtrends.com/leaderboard.html | Skill wrapper around Playwright MCP. | openclaw skills install (Owner spiceman161) and openclaw skills verify. | 39,713 downloads, 146 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub Agent Browser (matrixy) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installed browser skill. | openclaw skills install (Owner matrixy) and openclaw skills verify. | 105,425 downloads, 376 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub “Browser Use” (shawnpana) | Skill | https://clawhubtrends.com/leaderboard.html | Community Browser Skill. In the leaderboard with warning marking – verify before use. | openclaw skills install (Owner shawnpana) and openclaw skills verify. | 40,606 downloads, 101 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

Typical workflows

- UI of your own app: Playwright or DevTools. Read open website only: Search/Firecrawl. Clearly separate login sessions.

## Pitfalls

- MCP tool schemas can put a lot of stress on the context even before the first question comes up. In r/ClaudeAI, a user reported 67,000 token overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- Snapshot swim. Community alternatives advertise with smaller payloads – independently notice.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine both, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

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
