# Notion

- **Domain:** `office-dokumente`
- **Kategorie:** `notion`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Seiten und Datenbanken in Notion suchen, anlegen und aktualisieren.

## Empfohlener Tool-Stack

- Hosted Notion MCP
- Klare Datenbank-Properties im Prompt

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion-Workspace fuer Agenten (Seiten, Datenbanken). | Claude-Code-Docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | Im offiziellen Hermes-MCP-Katalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| ClawHub „Notion“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Skill-Variante neben MCP. | openclaw skills install (Owner steipete) und openclaw skills verify. | 84.423 Downloads, 246 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Claude-Code-Docs nennen Notion als kanonisches HTTP-MCP-Beispiel.
- Schreibende Aenderungen an geteilten DBs nur nach Freigabe.

## Fallstricke

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://mcp.notion.com/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
