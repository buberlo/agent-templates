# Cron und Routinen

- **Domain:** `automatisierung`
- **Kategorie:** `cron-routines`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Geplante Agent-Jobs, wöchentliche Reviews, Monitoring-Schleifen.

## Empfohlener Tool-Stack

- Hermes Cron/Routines, OpenClaw scheduled jobs, Grok-Bot Routines – mit Nutzungslimit und Pause-Policy

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes Cron (Feature) | Plattform-Feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Im Quickstart als optionales Toolset genannt (nicht Teil von Blank Slate). | Ueber hermes setup / Config aktivieren. | Produktdoku. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | nein (so belegt) |
| ClawHub „Automation Workflows“ (jk-0001) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Skill fuer Automationen. | openclaw skills install (Owner jk-0001) und openclaw skills verify. | 73.666 Downloads, 283 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Idempotente Jobs, klare Quiet Hours, Fehler per Chat eskalieren statt Endlosschleife.

## Fallstricke

- Hintergrundjobs verbrauchen Kontingent; Owner-Pause respektieren.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
