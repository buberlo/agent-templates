# Hermes Agent

1. Pick a template under `domains/<domain>/<category>/`; read `domains/<domain>/<category>/_category.md` and optional `domains/<domain>/_domain.md`.
2. **Skill:** Copy **System prompt** and **Workflow** into `SKILL.md`; do not copy YAML frontmatter.
3. **MCP:** Map `required_tools` and the MCP table in `_category.md` to `optional-mcps/` (`hermes mcp install <name>`, OAuth per setup card).
4. **Filter:** Use MCP include/exclude; skills with `platforms: [macos]` are hidden on Linux — verify.
5. **Risk:** For `risk_level: high`, enforce human-in-the-loop steps from **Security** in the runbook.

Platform details: `domains/agent-platforms/hermes/_category.md`.