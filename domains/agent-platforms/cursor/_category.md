# Cursor

- **Domain:** `agent-platforms`
- **Kategorie:** `cursor`
- **Stand:** 2026-11-23

## Kurzbeschreibung

IDE-Agent, MCP-Plugins, Skills; Grok-Bot teilt das Plugin-Modell.

## Empfohlener Tool-Stack

- Cursor-MCP-Config, Skills, dieselben Plugin-Muster wie Grok Bot laut offizieller Bot-101-Aussage

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Cursor + MCP/Skills | IDE-Agent | https://x.ai/bot/guides/grok-bot-101 | Grok Bot 101: Grok Bot unterstuetzt dieselben MCP-Server, Plugins und Skills wie Cursor. | Cursor-Settings / mcp.json; Plugins analog Connect Apps im Bot-Kosmos. | Produktdoku (keine Cursor-Star-Zahl in dieser Recherche). | https://x.ai/bot/guides/grok-bot-101 | nein (so belegt) |

## Typische Workflows

- Projektlokale MCP-Config versionieren (ohne Secrets), Skills im Repo fuer das Team.

## Fallstricke

- Team-Allowlists koennen MCPs blocken. Secrets nicht in mcp.json committen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://x.ai/bot/guides/grok-bot-101
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
