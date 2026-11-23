# Kalender und Scheduling

- **Domain:** `kommunikation`
- **Kategorie:** `kalender-scheduling`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Termine finden, halten, einladen; Calendly, Google Calendar, Outlook.

## Empfohlener Tool-Stack

- Google Calendar ueber Workspace-Skill oder Grok-Bot-Plugin
- Calendly-MCP fuer Buchungslinks

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets ueber gws CLI oder Python. | Bundled productivity/google-workspace. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| calendly MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly | Terminplanung und Einladungslinks. | hermes mcp install calendly | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| Grok Bot Google Calendar | Plugin | https://x.ai/bot/guides/grok-bot-101 | In Grok Bot 101 als typischer Connector genannt. | Connect Apps. | Produktdoku. | https://x.ai/bot/guides/grok-bot-101 | nein (so belegt) |

## Typische Workflows

- Freie Slots vorschlagen, Einladung erst nach Bestaetigung von Teilnehmern und Text.

## Fallstricke

- Zeitzonen (Europe/Vienna deklarieren). Doppelbuchungen bei mehreren Kalendern.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
