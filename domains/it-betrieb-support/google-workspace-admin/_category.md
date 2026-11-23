# Google-Workspace-Admin

- **Domain:** `it-betrieb-support`
- **Kategorie:** `google-workspace-admin`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Directory, Gruppen, Richtlinien und Workspace-Admin-Aufgaben.

## Empfohlener Tool-Stack

- gws CLI / google-workspace Skill fuer Inhalte; Admin-APIs getrennt und streng berechtigen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets ueber gws CLI oder Python. | Bundled productivity/google-workspace. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Directory-Aenderungen als Plan ausgeben, nicht ausfuehren ohne Auftrag.

## Fallstricke

- Ein User-OAuth ist kein Super-Admin.
- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
