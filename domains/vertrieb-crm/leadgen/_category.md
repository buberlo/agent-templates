# Leadgenerierung

- **Domain:** `vertrieb-crm`
- **Kategorie:** `leadgen`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Zielaccounts und Kontakte recherchieren, qualifizieren und in Listen oder CRM übernehmen.

## Empfohlener Tool-Stack

- Web-Recherche-Stack + CRM-MCP + Outreach-Entwuerfe

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Websuche und Crawling, auf Agenten-Recherche ausgelegt. | Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | nein (so belegt) |
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche ueber Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | nein (so belegt) |
| attio MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM-Uebernahme. | hermes mcp install attio | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| close MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close | CRM-Uebernahme. | hermes mcp install close | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- ICP festlegen, nur oeffentliche Quellen, Liste mit Herkunftsspalte.

## Fallstricke

- Scraping gegen ToS; keine erfundenen E-Mail-Adressen als verifiziert ausgeben.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/exa-labs/exa-mcp-server
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/brave/brave-search-mcp-server
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
