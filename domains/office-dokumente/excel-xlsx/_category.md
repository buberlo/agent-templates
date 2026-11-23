# Excel / XLSX

- **Domain:** `office-dokumente`
- **Kategorie:** `excel-xlsx`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Tabellen, Formeln, Charts und Datenbereinigung in Arbeitsmappen.

## Empfohlener Tool-Stack

- Anthropic xlsx-Skill oder Hermes xlsx-CLIs
- Formeln nach Open oder xlsx_recalc pruefen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Offizielle Agent-Skills zum Erzeugen/Pruefen von Office- und PDF-Dateien; Verify-Schritt (validate.py, Render zu PDF/PNG) ist Teil der Anleitung. | Claude Code: /plugin marketplace add anthropics/skills und /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | nein (so belegt) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline ueber Python-CLIs (python-docx, python-pptx, openpyxl). Office-App nicht noetig; PDF-Render nur mit LibreOffice. | Bundled in Hermes (~/.hermes/skills/), Scripts im Skill-Ordner. | Teil des offiziellen Bundled-Katalogs. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | nein (so belegt) |
| ClawHub „Excel / XLSX“ (ivangdavila) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Skill fuer Excel. | openclaw skills install (Owner ivangdavila) und openclaw skills verify. | 65.403 Downloads, 259 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Daten und Formeln trennen; nach dem Schreiben Sheets gegenlesen (xlsx_read.py).

## Fallstricke

- Hermes-Doku: Formeln werden oft erst von der Office-App oder xlsx_recalc.py berechnet.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://github.com/anthropics/skills
- https://clawhubtrends.com/leaderboard.html
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
