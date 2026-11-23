# Hermes Agent — Template einbinden

1. **Skill oder System-Prompt:** YAML-Frontmatter nicht übernehmen. Abschnitt **System-Prompt / Instruktionen** als Skill-Body (`SKILL.md`) oder Erweiterung der Hermes-Systemnachricht.
2. **Tools:** `required_tools` in Hermes-Tool-Registry / MCP-Connectors mappen; `install` und `version_notes` vor Aktivierung prüfen.
3. **Metadaten:** `id`, `version`, `risk_level` in Skill-Metadaten oder internes Manifest für Updates.
4. **Freigaben:** Abschnitt **Sicherheit & Freigaben** als verbindliche Guardrails im Skill-Kopf (kurz, imperativ).
5. **Validierung:** Repository-Root: `python3 scripts/validate_and_index.py` — nur validierte Templates deployen.

**Pfad-Konvention:** `categories/<category>/<id>.md` → Skill-Name: `<category>/<id>`.