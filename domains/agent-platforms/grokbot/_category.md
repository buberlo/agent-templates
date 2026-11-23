# Grok Bot

- **Domain:** `agent-platforms`
- **Kategorie:** `grokbot`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Connect Apps, Custom MCP, Skills-Decke, Box-Computer, keine localhost-MCPs.

## Empfohlener Tool-Stack

- Connect Apps fuer Katalog-Plugins
- Custom MCP nur public HTTPS oder Command auf der Bot-Box
- Skills-Decke beachten
- @-Attach

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Grok Bot Plugins / Custom MCP | Produkt-Connector | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Connect Apps, OAuth-Tokens auf Cursor-Connector-Backend, Bots bekommen keine Tokens. Custom: Remote HTTPS (streamable HTTP/SSE) oder Command (npx/uvx) auf dem Bot-Computer – nicht localhost des User-Laptops, nicht VPN-only. Kein sicherer Secret-Header-Weg laut Staff-Zitaten im Wiki. | Connect Apps oder den Bot bitten, den Server hinzuzufuegen. Tool-Policies: Always allow, Auto-review, Needs approval, Blocked (Wiki, ab 0.70.2/1.2.3). | Produktdoku/Wiki (Angaben zu Versionen 0.75.x–0.77.x, Okt/Nov 2026). | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |
| Grok Bot 101 | Offizielle Einfuehrung | https://x.ai/bot/guides/grok-bot-101 | Grok Bot unterstuetzt dieselben MCP-Server, Plugins und Skills wie Cursor. Mehrere Accounts pro Dienst moeglich. | App von x.ai/bot, Connect Apps. | Offizielle Guides. | https://x.ai/bot/guides/grok-bot-101 | nein (so belegt) |

## Typische Workflows

- Plugin installieren, Auth in der Frist abschliessen, mit @ an den Task haengen, einzelne Tools blocken wenn noetig.
- Wenn kein Connector existiert: Arbeit auf dem Bot-Computer (CLI, Dateien), nicht so tun als waere ein privates Laptop-MCP verbunden.

## Fallstricke

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skill-Ceiling 200 (seit 0.71.2, Wiki).
- Shared Bots: Team kann Command und Args eines Command-Servers lesen.
- Viele virale X-Threads ueber N GitHub-Repos sind Marketing – nicht ungeprueft uebernehmen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
