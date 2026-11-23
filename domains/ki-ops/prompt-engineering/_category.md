# Prompt Engineering

- **Domain:** `ki-ops`
- **Kategorie:** `prompt-engineering`
- **Stand:** 2026-11-23

## Kurzbeschreibung

System-Prompts, Skills und Tool-Beschreibungen schärfen.

## Empfohlener Tool-Stack

- Kurze Skill-Descriptions, klare Tool-Beschreibungen, Evaluations

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Agent Skills progressive disclosure | Muster | https://code.claude.com/docs/en/skills/ | Nur Name/Description (ca. 100 Tokens) bis der Skill greift, dann Body, dann Scripts. | SKILL.md-Format. | 199.219 Stars | https://code.claude.com/docs/en/skills/ | nein (so belegt) |

## Typische Workflows

- Description als Trigger-Text behandeln: wann der Skill feuern soll und wann nicht.

## Fallstricke

- Personality-Instruktionen gehoeren nicht in jedes Skill (OpenClaw-Rat: Prozedur, nicht Persona).
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
