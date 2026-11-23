# Helpdesk und Tickets

- **Domain:** `kundenservice`
- **Kategorie:** `helpdesk-tickets`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Tickets sichten, priorisieren, Entwürfe schreiben und in Zendesk/Intercom/ähnlichen Tools aktualisieren.

## Empfohlener Tool-Stack

- Intercom-MCP oder andere Helpdesk-MCPs
- Knowledge-Base im Vault

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| intercom MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom | Customer-Support-Plattform Intercom. | hermes mcp install intercom | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| awesome-mcp Support-Sektion | Katalog | https://github.com/punkpeye/awesome-mcp-servers | Weitere Support-/ITSM-Server, einzeln pruefen. | Je Repo. | Katalog. | https://github.com/punkpeye/awesome-mcp-servers | nein (so belegt) |

## Typische Workflows

- Ticket lesen, Makro/Entwurf, interne Notiz, keine stillen Resolves ohne Policy.

## Fallstricke

- PII in Prompts und Logs minimieren.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
