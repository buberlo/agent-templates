# Testing

- **Domain:** `software-entwicklung`
- **Kategorie:** `testing`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Unit-, Integrations- und E2E-Tests (inkl. Playwright) schreiben und ausführen.

## Empfohlener Tool-Stack

- Projekt-Testframework + Playwright fuer E2E

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Lokale Browser-Automation ueber Accessibility-Snapshots, UI-Tests und Interaktion mit Web-Apps. | npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | nein (so belegt) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Live-Chrome steuern und debuggen (Performance, Network, Console) fuer Coding-Agenten. | Ueber das GitHub-Repo / MCP-Client-Config (stdio), siehe README. | 58.941 Stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | nein (so belegt) |
| Hermes-Skill test-driven-development | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | TDD: RED-GREEN-REFACTOR, Tests vor Code. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Tests schreiben lassen, lokal ausfuehren, erst dann Implementation verbreitern.

## Fallstricke

- Playwright MCP streamt grosse Snapshots – fuer reine Extraktion unnoetig teuer.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://playwright.dev/mcp/introduction
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/microsoft/playwright-mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
