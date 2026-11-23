# PDF

- **Domain:** `office-dokumente`
- **Kategorie:** `pdf`
- **Stand:** 2026-11-23

## Kurzbeschreibung

PDFs lesen, mergen, ausfüllen, OCR und gezielt editieren.

## Empfohlener Tool-Stack

- Anthropic pdf-Skill und/oder Hermes pdf-Skill
- pypdf, OCR-Pfad fuer Scans
- MarkItDown als Alternative

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Offizielle Agent-Skills zum Erzeugen/Pruefen von Office- und PDF-Dateien; Verify-Schritt (validate.py, Render zu PDF/PNG) ist Teil der Anleitung. | Claude Code: /plugin marketplace add anthropics/skills und /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | nein (so belegt) |
| Hermes-Skill pdf | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | PDF erzeugen, lesen, mergen, ausfuellen, OCR, Text editieren. | Bundled: productivity/pdf. | Bundled-Katalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| MarkItDown | CLI / Bibliothek | https://github.com/microsoft/markitdown | Dateien und Office-Dokumente nach Markdown wandeln – wird in Skills und MCP-Wrappern genutzt. | Python-Paket / Repo. | 197.975 Stars | https://github.com/microsoft/markitdown | nein (so belegt) |
| ClawHub „Nano Pdf“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Sehr haeufig installiertes PDF-Skill auf ClawHub. | openclaw skills install (Owner steipete) und openclaw skills verify. | 102.189 Downloads, 245 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Lesen/Mergen/Formularfuellung mit pypdf; visuell per Render pruefen.

## Fallstricke

- OCR-Fehler in Zahlen und Aktenzeichen; keine finale Einreichung ohne Sichtpruefung.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/microsoft/markitdown
- https://github.com/anthropics/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
