# Web-Recherche

- **Domain:** `recherche-wissen`
- **Kategorie:** `web-recherche`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Aktuelle Websuche, Scraping und Quellenprüfung (Brave, Exa, Tavily, Firecrawl).

## Empfohlener Tool-Stack

- Eine Such-API (Brave/Exa/Tavily) + Firecrawl; Browser nur wenn JS/Login noetig
- Quellen zitieren

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche ueber Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | nein (so belegt) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Websuche und Crawling, auf Agenten-Recherche ausgelegt. | Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | nein (so belegt) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Echtzeit-Suche, Extract, Map, Crawl. | Siehe Repo. | 2.497 Stars | https://github.com/tavily-ai/tavily-mcp | nein (so belegt) |
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Websuche, Scraping und Crawling als Kontext fuer Agenten. | Offizielles MCP-Repo, typisch npx oder hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | nein (so belegt) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Lokale Browser-Automation ueber Accessibility-Snapshots, UI-Tests und Interaktion mit Web-Apps. | npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | nein (so belegt) |
| ClawHub „Multi Search Engine“ (gpyangyoujun) | Skill | https://clawhubtrends.com/leaderboard.html | Mehrere Suchmaschinen in einem Skill. | openclaw skills install (Owner gpyangyoujun) und openclaw skills verify. | 138.647 Downloads, 672 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Zuerst Suche, dann gezielt fetchen, dann zitieren. Playwright nicht als Default-Scraper (Tokenkosten).

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

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
