# Codex

- **Domain:** `agent-platforms`
- **Category:** `codex`
- **As of:** 2026-11-23

## Summary

OpenAI Codex CLI as a coding agent, often delegated by Hermes, MCP-capable.

## Recommended tool stack

- Codex CLI als Coding-Runtime, MCP wie andere Clients, oft von Hermes delegiert
- OpenClaw kann openclaw mcp serve or openclaw acp in Richtung Codex nutzen

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|

| Hermes-Skill codex | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Delegates features/PRs to OpenAI Codex CLI. | Bundled autonomous-ai-agents/codex. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| OpenClaw MCP serve / ACP | Bridge | https://docs.openclaw.ai/cli/mcp/serve |OpenClaw as an MCP server for clients such as Codex or Claude Code, or ACP if OpenClaw hosts the coding runtime.| openclaw mcp serve (stdio) or `openclaw acp`. | 395.081 Stars | https://docs.openclaw.ai/cli/mcp/serve | no (as cited) |

## Typical workflows

- Stay in Hermes, Codex only for the coding loop; Reviews in the Orchestrator.

## Pitfalls

- Two agents with writing rights to the same repo without voting.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/cli/mcp/serve
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
