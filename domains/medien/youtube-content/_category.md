# YouTube-Content

- **Domain:** `medien`
- **Kategorie:** `youtube-content`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Videos zusammenfassen, Kapitel erzeugen, Scripts und Kanal-Content aus Transkripten ableiten.

## Empfohlener Tool-Stack

- youtube-content Skill
- Office-Skills wenn ein Deck/Blog als Datei gebraucht wird

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | YouTube-Transkripte holen und in Kapitel, Summary, Thread, Blog oder Zitate verwandeln. | Bundled; Helper fetch_transcript.py ueber vorbereitetes venv (youtube extra), nicht rohes pip in die Agent-Env. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | nein (so belegt) |
| ClawHub „YouTube Watcher“ (michaelgathara) | Skill | https://clawhubtrends.com/leaderboard.html | YouTube beobachten oder zusammenfassen. | openclaw skills install (Owner michaelgathara) und openclaw skills verify. | 48.111 Downloads, 294 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Hermes-Reihenfolge: Transcript mit --text-only --timestamps holen, leere Outputs abfangen, bei >50k Zeichen chunken, Format waehlen (Default: Summary), Timestamps gegenlesen.
- Prompt: /youtube-content fasse VIDEO_URL als Kapitel + 8-Satz-Summary zusammen.

## Fallstricke

- Die Formatbeispiele in der Skill-Doku sind Platzhalter, keine realen Video-Ergebnisse. Transkripte koennen deaktiviert sein.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
