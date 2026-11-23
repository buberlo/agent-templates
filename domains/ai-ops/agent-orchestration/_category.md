# Agent orchestration

- **Domain:** `ai-ops`
category: Agent Orchestration `
- **As of:** 2026-11-23

## Summary

Delegation to Subagents, Claude Code/Codex, multi-agent teams and Gates.

## Recommended tool stack

- Hermes delegation to Claude Code/Codex
Grok-bot teams/subagents
OpenClaw multi-agent allowlists

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------
| Hermes-Skills claude-code, codex, hermes-agent | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Orchestration and delegation, incl. Skill that configures the agent itself. | Bundled autonomous-ai-agents. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

Typical workflows

- Rough planning in the orchestra, implementation in the coding agent, review separately.

## Pitfalls

- Uncontrolled recursion / cost. Grok Bot: since 0.71.2 up to 200 plugin skills (wiki).
Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine both, not confuse. Sources: https://code.claude.com/docs/en/features-overview.http://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
