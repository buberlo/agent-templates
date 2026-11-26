# Agent orchestration

- **Domain:** `ai-ops`
- **Category:** `agent-orchestration`
- **As of:** 2026-11-23

## Summary

Delegation an Subagents, Claude Code/Codex, Multi-Agent-Teams and Gates.

## Recommended tool stack

- Hermes Delegation an Claude Code/Codex
- Grok-Bot Teams/Subagents
- OpenClaw multi-agent allowlists

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skills claude-code, codex, hermes-agent | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Orchestration and Delegation, inkl. Skill der den Agenten selbst konfiguriert. | Bundled autonomous-ai-agents/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Grobe Planung im Orchestrator, Implementation im Coding-Agent, Review getrennt.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Uncontrolled recursion / costs. Grok Bot: up to 200 plugin skills since 0.71.2 (wiki).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
