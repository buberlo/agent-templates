# Video-Bearbeitung

- **Domain:** `medien`
- **Kategorie:** `video-bearbeitung`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Schneiden, konvertieren, untertiteln und nachbearbeiten von Videodateien, typischerweise mit FFmpeg oder einer Agent-Timeline.

## Empfohlener Tool-Stack

- FFmpeg auf PATH und ueber das Terminal-Tool
- Nur bei Bedarf ein Video-MCP oder eine Timeline
- Remotion-Skills wenn das Video Code/Motion Graphics ist

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | https://ffmpeg.org/ | Schnitt, Konvertierung, Audio-Normalize, Untertitel einbetten. Viele Agenten rufen FFmpeg direkt ueber das Terminal-Tool auf. Dedizierte FFmpeg-MCPs sind fragmentiert (kein klarer Star-Leader in dieser Recherche). | OS-Paket; Agent braucht ffmpeg auf PATH. Hermes Video-Analyse-Doku setzt ffmpeg auf PATH voraus. | Nicht als einzelnes MCP-Star-Signal belegt. | https://agentos.guide/hermes-agent-video-analysis | nein (so belegt) |
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatische Videos in React; Skills statt eines aelteren MCP-Pfads, so die gaengige Empfehlung 2026. | Skills aus remotion-dev/skills laut Repo-README. | 7.841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | nein (so belegt) |
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | YouTube-Transkripte holen und in Kapitel, Summary, Thread, Blog oder Zitate verwandeln. | Bundled; Helper fetch_transcript.py ueber vorbereitetes venv (youtube extra), nicht rohes pip in die Agent-Env. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | nein (so belegt) |
| ClawHub „Video Frames“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Frames aus Videos ziehen. | openclaw skills install (Owner steipete) und openclaw skills verify. | 47.716 Downloads, 119 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Schneide local.mp4 von Zeit A bis B, normalisiere Audio (loudnorm), schreibe h264+aac, pruefe mit ffprobe.
- Kein MCP, wenn ein einziges ffmpeg-Kommando reicht – spart Tokens.

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Viele FFmpeg-MCP-Wrapper sind klein/fragmentiert; in dieser Recherche kein klarer Star-Leader.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://agentos.guide/hermes-agent-video-analysis
- https://github.com/remotion-dev/skills
- https://clawhubtrends.com/leaderboard.html
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
