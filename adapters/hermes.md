# Hermes Agent

1. Template aus `domains/<domain>/<category>/` wählen; Metadaten in `domains/<domain>/<category>/_category.md` und optional `domains/<domain>/_domain.md`.
2. **Skill:** Abschnitt **System-Prompt / Instruktionen** + **Arbeitsablauf** als `SKILL.md`; Frontmatter nicht kopieren.
3. **MCP:** `required_tools` und MCP-Tabelle in `_category.md` auf `optional-mcps/` mappen (`hermes mcp install <name>`, OAuth laut Setup-Karte).
4. **Filter:** MCP include/exclude nutzen; Skills mit `platforms: [macos]` erscheinen unter Linux nicht — prüfen.
5. **Risiko:** Bei `risk_level: high` Human-in-the-loop aus **Sicherheit & Freigaben** verbindlich machen.

Plattform-Details: `domains/agent-platforms/hermes/_category.md`.