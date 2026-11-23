# Social: X / Twitter

- **Domain:** `content-marketing`
- **Kategorie:** `social-x-twitter`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Recherche, Entwürfe, Threads und Veröffentlichung über xurl, X-MCP oder ähnliche CLIs.

## Empfohlener Tool-Stack

- xurl-Skill (Hermes) oder offizielle X-APIs der jeweiligen Plattform
- Humanizer gegen KI-Ton

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill xurl | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | X/Twitter ueber die xurl-CLI: Suche, Posten, DM, Medien. | Bundled social-media/xurl. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| ClawHub „Humanizer“ (biostartechnology) | Skill | https://clawhubtrends.com/leaderboard.html | Texte weniger schablonig machen; auch in Hermes bundled humanizer. | openclaw skills install (Owner biostartechnology) und openclaw skills verify. | 105.439 Downloads, 601 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Recherche, Entwurf zeigen, erst nach Freigabe posten.

## Fallstricke

- Automatisches Posten ohne Gate verletzt oft den gewuenschten Prozess und Plattformregeln.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
