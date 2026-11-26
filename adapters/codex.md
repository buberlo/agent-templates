# OpenAI Codex

1. Pick a template under `domains/<domain>/<category>/`; read `domains/<domain>/<category>/_category.md`.
2. Put **System prompt** and **Workflow** into `AGENTS.md` (and nested `AGENTS.md` files where a subtree needs a tighter policy). Do not copy YAML frontmatter.
3. Map `required_tools` and the MCP table in `_category.md` to Codex MCP config. Do not put secrets in the repo or in command arguments.
4. Prioritize templates whose `target_agents` include `codex`.
5. For `risk_level: high`, keep human-in-the-loop steps from **Security** in the runbook.

Platform details: `domains/agent-platforms/codex/_category.md`.
