# Chat und Messaging

- **Domain:** `kommunikation`
- **Kategorie:** `chat-messaging`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Slack, Discord, Telegram, WhatsApp, iMessage – Nachrichten lesen und (freigegeben) senden.

## Empfohlener Tool-Stack

- Native Plattform-Skills (imessage, Slack) oder Hersteller-Plugin

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill imessage | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | iMessage/SMS ueber imsg CLI auf macOS. | Bundled apple/imessage (plattformgebunden). | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| ClawHub „Slack“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Slack-Skill. | openclaw skills install (Owner steipete) und openclaw skills verify. | 42.838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| Grok Bot Slack-Plugin | Plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Postet als der Slack-User, nur in Kanaelen die dieser betreten darf; erhoeht keine Rechte. | Connect Apps. | Produktdoku. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | nein (so belegt) |

## Typische Workflows

- Lesen und Entwurf, Senden nach Freigabe.

## Fallstricke

- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- imessage-Skill ist macOS-spezifisch.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
