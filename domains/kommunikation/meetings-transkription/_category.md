# Meetings und Transkription

- **Domain:** `kommunikation`
- **Kategorie:** `meetings-transkription`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Meetings transkribieren, Decisions und Action Items extrahieren, Follow-ups entwerfen.

## Empfohlener Tool-Stack

- Fireflies-Katalog-MCP oder Whisper
- Hermes meeting-action-items / teams-meeting-pipeline

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| ClawHub / OpenClaw Skill Openai Whisper (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Transkription ueber Whisper, laut ClawHub ein haeufig installiertes Skill. | openclaw skills install (Owner steipete, Name Openai Whisper). | 77.380 Downloads, 303 Stars auf ClawHub (23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| Hermes-Skills meeting-action-items, teams-meeting-pipeline | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Action Items mit Owner/Zitat; Teams-Meeting-Zusammenfassungen. | Bundled productivity/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| fireflies MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies | Meeting-Transcripts ueber Fireflies. | hermes mcp install fireflies | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Transkript → Entscheidungen, Owner, Deadlines, zitiert; Mails nur als Draft.

## Fallstricke

- Aufzeichnungseinwilligung. Halluzinierte Beschluesse.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
