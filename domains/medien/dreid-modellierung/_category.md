# 3D-Modellierung

- **Domain:** `medien`
- **Kategorie:** `dreid-modellierung`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Erzeugen und prüfen von 3D-Assets, Szenen und Exporten (Blender, CAD-nahe Tools).

## Empfohlener Tool-Stack

- FFmpeg/CLI wo Dateien transformiert werden
- Plattform-Skills (Hermes media/creative, ClawHub Whisper/Video)
- Output immer gegenpruefen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | https://ffmpeg.org/ | Schnitt, Konvertierung, Audio-Normalize, Untertitel einbetten. Viele Agenten rufen FFmpeg direkt ueber das Terminal-Tool auf. Dedizierte FFmpeg-MCPs sind fragmentiert (kein klarer Star-Leader in dieser Recherche). | OS-Paket; Agent braucht ffmpeg auf PATH. Hermes Video-Analyse-Doku setzt ffmpeg auf PATH voraus. | Nicht als einzelnes MCP-Star-Signal belegt. | https://agentos.guide/hermes-agent-video-analysis | nein (so belegt) |

## Typische Workflows

- Auftrag, erlaubte Tools und Definition of Done festlegen.
- Zuerst lesen/recherchieren, dann Entwurf, dann Freigabe fuer wirkende Schritte.
- Output gegenlesen (Datei, URL, Ticket) und Quelle angeben.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://agentos.guide/hermes-agent-video-analysis
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
