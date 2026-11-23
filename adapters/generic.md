# Generische MCP-Agenten

1. Metadaten aus YAML-Frontmatter + Pfad `domains/<domain>/<category>/`.
2. Kanonischer Prompt-Bau:
   - ROLE → Zweck
   - TOOLS → `required_tools` + `_category.md` MCP-Tabelle
   - WORKFLOW → Arbeitsablauf
   - EXAMPLES → Grundbeispiele
   - SAFETY → Sicherheit & Freigaben
3. Maschinenlesbar: Root-`catalog.json`, MCP: `mcp/catalog.json`.
4. Vor Deploy: `python3 scripts/validate_and_index.py`.

Siehe `domains/agent-platforms/generic-mcp-agents/_category.md`.