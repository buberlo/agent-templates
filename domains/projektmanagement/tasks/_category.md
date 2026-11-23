# Tasks

- **Domain:** `projektmanagement`
- **Kategorie:** `tasks`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Aufgaben in Todoist, Issues oder lokalen Task-Systemen führen.

## Empfohlener Tool-Stack

- Todoist-MCP im Hermes-Katalog, oder lokale Markdown-Tasks

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| todoist MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/todoist | Aufgabenverwaltung. | hermes mcp install todoist | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| Hermes-Skills document-to-action-items, weekly-review-planning | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Aufgaben aus Dokumenten; Wochenplanung. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Inbox verarbeiten, Due Dates in Europe/Vienna, keine stillen Completes.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/todoist
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
