# Compliance, NIS2 und DSGVO

- **Domain:** `security`
- **Kategorie:** `compliance-nis2-dsgvo`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Anforderungen, TOMs, AVVs und Nachweise strukturieren (keine Rechtsberatung).

## Empfohlener Tool-Stack

- Dokumenten-Skills fuer Verzeichnisse und Vorlagen
- Keine Rechtsberatung als Output verkaufen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Offizielle Agent-Skills zum Erzeugen/Pruefen von Office- und PDF-Dateien; Verify-Schritt (validate.py, Render zu PDF/PNG) ist Teil der Anleitung. | Claude Code: /plugin marketplace add anthropics/skills und /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | nein (so belegt) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline ueber Python-CLIs (python-docx, python-pptx, openpyxl). Office-App nicht noetig; PDF-Render nur mit LibreOffice. | Bundled in Hermes (~/.hermes/skills/), Scripts im Skill-Ordner. | Teil des offiziellen Bundled-Katalogs. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | nein (so belegt) |
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion-Workspace fuer Agenten (Seiten, Datenbanken). | Claude-Code-Docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | Im offiziellen Hermes-MCP-Katalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | nein (so belegt) |

## Typische Workflows

- Ist-Zustand dokumentieren, Luecken als Fragen an Fachleute, Nachweise versionieren.

## Fallstricke

- Ein Agent ist kein Datenschutzbeauftragter und keine Kanzlei.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/anthropics/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://code.claude.com/docs/en/mcp
- https://mcp.notion.com/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
