# Grok Bot — Template einbinden

1. **Bot-Beschreibung:** Aus **Zweck**, **Wann nutzen** und **Tool-Stack** eine kompakte Bot-Bio (Deutsch, max. ~500 Zeichen).
2. **Skill / Custom Instructions:** Vollständiger Abschnitt **System-Prompt / Instruktionen** plus **Arbeitsablauf** als Skill oder feste Bot-Instruktion.
3. **Tools:** Pro Eintrag in `required_tools` den passenden X-/MCP-/Plugin-Connector aktivieren; bei `target_agents` ohne `grokbot` Template nicht blind übernehmen.
4. **Risiko:** Bei `risk_level: high` Human-Approval-Schritt aus **Sicherheit & Freigaben** explizit in den Skill.
5. **Sync:** `version` und `updated` im internen Changelog des Bots pflegen.

**Export-Hinweis:** Abschnitte ab `## Zweck` können 1:1 in Grok-Bot-Skill-Editor eingefügt werden.