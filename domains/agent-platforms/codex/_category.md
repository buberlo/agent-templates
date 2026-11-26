# Codex

- **Domain:** `agent-platforms`
- **Category:** `codex`
- **As of:** 2026-11-23

## Summary

OpenAI Codex CLI as a coding agent, often delegated by Hermes, MCP-capable.

## Recommended tool stack

- Codex CLI als Coding-Runtime, MCP wie andere Clients, oft von Hermes delegiert
- OpenClaw can use openclaw mcp serve or openclaw acp toward Codex

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill codex | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Delegiert Features/PRs an OpenAI Codex CLI. | Bundled autonomous-ai-agents/codex. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| OpenClaw MCP serve / ACP | Bridge | https://docs.openclaw.ai/cli/mcp/serve | OpenClaw as an MCP server for clients like Codex or Claude Code, or ACP when OpenClaw hosts the coding runtime. | openclaw mcp serve (stdio) or openclaw acp. | 395,081 stars | https://docs.openclaw.ai/cli/mcp/serve | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Stay in Hermes, use Codex only for the coding loop; bring reviews back into the orchestrator.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Two agents with write access to the same repo without coordination.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/cli/mcp/serve
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
