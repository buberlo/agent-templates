# Generic MCP agents

1. Metadata from YAML frontmatter + path `domains/<domain>/<category>/`.
2. Canonical prompt assembly:
   - ROLE → Purpose
   - TOOLS → `required_tools` + `_category.md` MCP table
   - WORKFLOW → Workflow
   - EXAMPLES → Basic examples
   - SAFETY → Security
3. Machine-readable: root `catalog.json`; MCP: `mcp/catalog.json`.
4. Before deploy: `python3 scripts/validate_and_index.py`.

See `domains/agent-platforms/generic-mcp-agents/_category.md`.