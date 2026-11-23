# Browser-Automation

- **Domain:** `automatisierung`
- **Kategorie:** `browser-automation`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Playwright MCP, Chrome DevTools MCP, Cloud-Browser; Tokenkosten beachten.

## Empfohlener Tool-Stack

- Playwright MCP fuer lokale UI-Tests
- Chrome DevTools MCP fuer Debugging
- Firecrawl/Such-MCP fuer reines Lesen
- Tokenbudget ueberwachen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Lokale Browser-Automation ueber Accessibility-Snapshots, UI-Tests und Interaktion mit Web-Apps. | npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | nein (so belegt) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Live-Chrome steuern und debuggen (Performance, Network, Console) fuer Coding-Agenten. | Ueber das GitHub-Repo / MCP-Client-Config (stdio), siehe README. | 58.941 Stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | nein (so belegt) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Websuche, Scraping und Crawling als Kontext fuer Agenten. | Offizielles MCP-Repo, typisch npx oder hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | nein (so belegt) |
| Browserbase MCP | MCP | https://github.com/browserbase/mcp-server-browserbase | Cloud-Browser mit Stagehand. | Siehe Repo. | 3.397 Stars | https://github.com/browserbase/mcp-server-browserbase | nein (so belegt) |
| ClawHub „Playwright MCP“ (spiceman161) | Skill | https://clawhubtrends.com/leaderboard.html | Skill-Wrapper um Playwright MCP. | openclaw skills install (Owner spiceman161) und openclaw skills verify. | 39.713 Downloads, 146 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| ClawHub „Agent Browser“ (matrixy) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Browser-Skill. | openclaw skills install (Owner matrixy) und openclaw skills verify. | 105.425 Downloads, 376 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| ClawHub „Browser Use“ (shawnpana) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Browser-Skill. Im Leaderboard mit Warnmarkierung – vor Nutzung verifizieren. | openclaw skills install (Owner shawnpana) und openclaw skills verify. | 40.606 Downloads, 101 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- UI der eigenen App: Playwright oder DevTools. Offene Webseite nur lesen: Search/Firecrawl. Login-Sessions klar trennen.

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Snapshot-Schwemme. Community-Alternativen werben mit kleineren Payloads – unabhaengig benchmerken.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

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
