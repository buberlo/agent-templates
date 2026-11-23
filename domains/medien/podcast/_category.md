# Podcast

- **Domain:** `medien`
- **Kategorie:** `podcast`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Podcast-Workflows: Aufnahme-Vorbereitung, Schnitt, Shownotes, Transkript und Distribution.

## Empfohlener Tool-Stack

- FFmpeg-Schnitt
- Whisper oder youtube-content-aehnlich fuer Shownotes

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | https://ffmpeg.org/ | Schnitt, Konvertierung, Audio-Normalize, Untertitel einbetten. Viele Agenten rufen FFmpeg direkt ueber das Terminal-Tool auf. Dedizierte FFmpeg-MCPs sind fragmentiert (kein klarer Star-Leader in dieser Recherche). | OS-Paket; Agent braucht ffmpeg auf PATH. Hermes Video-Analyse-Doku setzt ffmpeg auf PATH voraus. | Nicht als einzelnes MCP-Star-Signal belegt. | https://agentos.guide/hermes-agent-video-analysis | nein (so belegt) |
| ClawHub / OpenClaw Skill Openai Whisper (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Transkription ueber Whisper, laut ClawHub ein haeufig installiertes Skill. | openclaw skills install (Owner steipete, Name Openai Whisper). | 77.380 Downloads, 303 Stars auf ClawHub (23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | YouTube-Transkripte holen und in Kapitel, Summary, Thread, Blog oder Zitate verwandeln. | Bundled; Helper fetch_transcript.py ueber vorbereitetes venv (youtube extra), nicht rohes pip in die Agent-Env. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | nein (so belegt) |

## Typische Workflows

- Transkript → Kapitelmarken, Shownotes, Clip-Listen mit Timestamps; Veröffentlichung nur nach Freigabe.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://clawhubtrends.com/leaderboard.html
- https://agentos.guide/hermes-agent-video-analysis
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
