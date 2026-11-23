# Animation und Motion

- **Domain:** `medien`
- **Kategorie:** `animation-motion`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Motion Graphics, Manim, p5.js, Remotion und andere programmatische Animation.

## Empfohlener Tool-Stack

- Remotion-Skills, Hermes manim-video / p5js / ascii-video

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatische Videos in React; Skills statt eines aelteren MCP-Pfads, so die gaengige Empfehlung 2026. | Skills aus remotion-dev/skills laut Repo-README. | 7.841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | nein (so belegt) |
| Hermes-Skills manim-video, p5js, ascii-video | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Manim-CE-Animationen, p5.js-Sketches, ASCII-Video. | Bundled creative/. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Skript oder React-Komponente erzeugen, lokal rendern, Output ansehen.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/remotion-dev/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
