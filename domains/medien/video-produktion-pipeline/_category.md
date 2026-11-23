# Video-Produktionspipeline

- **Domain:** `medien`
- **Kategorie:** `video-produktion-pipeline`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Ende-zu-Ende-Pipelines von Briefing über Schnitt bis Render und Export, inkl. Remotion und Studio-MCPs.

## Empfohlener Tool-Stack

- Briefing → Script → Assets → Remotion oder FFmpeg-Render → QA der Exporte

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatische Videos in React; Skills statt eines aelteren MCP-Pfads, so die gaengige Empfehlung 2026. | Skills aus remotion-dev/skills laut Repo-README. | 7.841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | nein (so belegt) |
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | https://ffmpeg.org/ | Schnitt, Konvertierung, Audio-Normalize, Untertitel einbetten. Viele Agenten rufen FFmpeg direkt ueber das Terminal-Tool auf. Dedizierte FFmpeg-MCPs sind fragmentiert (kein klarer Star-Leader in dieser Recherche). | OS-Paket; Agent braucht ffmpeg auf PATH. Hermes Video-Analyse-Doku setzt ffmpeg auf PATH voraus. | Nicht als einzelnes MCP-Star-Signal belegt. | https://agentos.guide/hermes-agent-video-analysis | nein (so belegt) |

## Typische Workflows

- Fuer datengetriebene Videos Remotion-Skills; fuer Rohschnitt FFmpeg.
- Hermes Desktop Video-Analyse (Plugin) exportiert laut Drittdoku Markdown-Report, SRT und JSON-Cues – hier ohne eigenes Lauf-Ergebnis festgehalten.

## Fallstricke

- Sekundaerquellen 2026 empfehlen Remotion-Skills gegenueber einem aelteren MCP-Pfad.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://agentos.guide/hermes-agent-video-analysis
- https://github.com/remotion-dev/skills
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
