# Telefon und Voice-Agents

- **Domain:** `kommunikation`
- **Kategorie:** `telefon-voice-agents`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Outbound/Inbound-Calls über Voice-Agent-Plattformen, Transkripte und Nachbearbeitung.

## Empfohlener Tool-Stack

- Spezialplattformen separat pruefen
- Twilio-Docs-MCP im Hermes-Katalog ist Dokumentation, nicht automatisch ein Dialer

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| twilio-docs MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs | Dokumentation zu Twilio, nicht stillschweigend gleichzusetzen mit einem produktiven Anruf-Agenten. | hermes mcp install twilio-docs | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| ClawHub „Agent Phone Call“ (mrsz) | Skill | https://clawhubtrends.com/leaderboard.html | Im Leaderboard mit Warnmarkierung, nur 8 Registry-Stars bei hohen Downloads. Im Leaderboard mit Warnmarkierung – vor Nutzung verifizieren. | openclaw skills install (Owner mrsz) und openclaw skills verify. | 72.476 Downloads, 8 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Anrufinhalte und Einwilligung klaeren; Aufzeichnungsregeln beachten.

## Fallstricke

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Warnmarkierte ClawHub-Skills nicht ungeprueft laden.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
