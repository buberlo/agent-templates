# Web-Scraping

- **Domain:** `daten-analytics`
- **Kategorie:** `web-scraping`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Strukturierte Extraktion von Webdaten; Firecrawl, Browser-MCPs, respektiert robots/ToS.

## Empfohlener Tool-Stack

- Firecrawl/Exa/Tavily extract zuerst
- Browser-MCP nur wenn noetig

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Firecrawl MCP | MCP | https://github.com/firecrawl/firecrawl-mcp-server | Websuche, Scraping und Crawling als Kontext fuer Agenten. | Offizielles MCP-Repo, typisch npx oder hosted laut README. | 7.886 Stars; Upstream 207.417 Stars | https://github.com/firecrawl/firecrawl-mcp-server | nein (so belegt) |
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Websuche und Crawling, auf Agenten-Recherche ausgelegt. | Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | nein (so belegt) |
| Tavily MCP | MCP | https://github.com/tavily-ai/tavily-mcp | Echtzeit-Suche, Extract, Map, Crawl. | Siehe Repo. | 2.497 Stars | https://github.com/tavily-ai/tavily-mcp | nein (so belegt) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Lokale Browser-Automation ueber Accessibility-Snapshots, UI-Tests und Interaktion mit Web-Apps. | npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | nein (so belegt) |

## Typische Workflows

- ToS pruefen, rate-limit, strukturiertes Schema vorgeben.

## Fallstricke

- Playwright als Scraper ist token-teuer.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

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
