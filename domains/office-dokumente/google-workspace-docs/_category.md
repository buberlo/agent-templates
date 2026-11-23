# Google Docs / Drive

- **Domain:** `office-dokumente`
- **Kategorie:** `google-workspace-docs`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Docs, Sheets, Slides und Drive-Dateien über Workspace-CLI oder MCP.

## Empfohlener Tool-Stack

- google-workspace / gws CLI oder Workspace-Connectoren (Grok Bot)

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets ueber gws CLI oder Python. | Bundled productivity/google-workspace. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| Grok Bot Google-Connectoren | Plugin/Connector | https://x.ai/bot/guides/grok-bot-101 | Grok Bot 101 nennt Gmail, Calendar, Drive u. a. ueber Connect Apps. | Connect Apps, Provider-Login in der dokumentierten Frist. | Offizielle Produkt-Docs/Wiki. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |

## Typische Workflows

- Lesen und Entwuerfe bevorzugen; Senden nur nach Freigabe.

## Fallstricke

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Grok-Bot-Plugins sind account-weit fuer alle Bots sichtbar.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
