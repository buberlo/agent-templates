# Formulare

- **Domain:** `office-dokumente`
- **Kategorie:** `formulare`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Formulare ausfüllen, Felder mappen und Daten zurückschreiben.

## Empfohlener Tool-Stack

- pdf-Skill fuer Formularfelder
- Mensch reicht ein

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill pdf | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | PDF erzeugen, lesen, mergen, ausfuellen, OCR, Text editieren. | Bundled: productivity/pdf. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Offizielle Agent-Skills zum Erzeugen/Pruefen von Office- und PDF-Dateien; Verify-Schritt (validate.py, Render zu PDF/PNG) ist Teil der Anleitung. | Claude Code: /plugin marketplace add anthropics/skills und /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | nein (so belegt) |

## Typische Workflows

- Felder mappen, Entwurf speichern, Mensch reicht ein.

## Fallstricke

- Keine automatische Behoerden-Einreichung.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://github.com/anthropics/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
