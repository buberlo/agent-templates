# Musik

- **Domain:** `medien`
- **Kategorie:** `musik`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Musikproduktion, Prompting für generative Musik und songwriting-nahe Agent-Skills.

## Empfohlener Tool-Stack

- Hermes-Skill songwriting-and-ai-music fuer Craft/Prompts
- Generative Dienste nur ueber erlaubte Schnittstellen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill songwriting-and-ai-music | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Songwriting-Handwerk und Suno-AI-Musik-Prompts. | Bundled creative/songwriting-and-ai-music. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Texte lokal schreiben, generative Tools als optionale Stufe, Rechte klaeren.

## Fallstricke

- Output-Rechte und Modell-ToS variieren.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
