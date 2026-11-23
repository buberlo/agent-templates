# E-Mail

- **Domain:** `kommunikation`
- **Kategorie:** `email`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Posteingang triagieren, Entwürfe schreiben, mit Gmail/IMAP/Workspace-Tools arbeiten.

## Empfohlener Tool-Stack

- Triage-Skill + Gmail/Workspace/IMAP
- Default: Entwuerfe, kein Auto-Send

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skills email-inbox-triage und himalaya | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Inbox priorisieren und Entwuerfe sicher vorbereiten; Himalaya fuer IMAP/SMTP im Terminal. | Bundled. ClawHub hat zudem Himalaya (lamelas, 41.823 Downloads) und imap-smtp-email (43.667). | ClawHub-Zahlen: Leaderboard 23.11.2026. | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets ueber gws CLI oder Python. | Bundled productivity/google-workspace. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| Grok Bot Gmail-Plugin | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Offizieller Connector, OAuth im Browser, account-weit. | Connect Apps, Gmail autorisieren, in Chat mit @ anhaengen. | Produktdoku. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |

## Typische Workflows

- Hermes email-inbox-triage: priorisieren, sicher antworten. Himalaya wenn IMAP gewuenscht ist.
- OpenClaw: Himalaya- und imap-smtp-email-Skills (ClawHub).

## Fallstricke

- Senden ohne Freigabe. PII in Logs.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
