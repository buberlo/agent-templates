# Evals and Benchmarks

- **Domain:** `ai-ops`
- **Category:** `evals-benchmarks `
- **As of:** 2026-11-23

## Summary

Measure the quality of agents and models, detect regressions.

## Recommended tool stack

- Own task sets, not just marketing leaderboards

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| hugoles/langfuse-mcp (Community) | MCP | https://github.com/hugoles/langfuse-mcp | Listed in awesome-mcp as a Langfuse API read access (Traces, Scores, Prompts). | See Repo. | Stars not pulled by API here. | https://github.com/punkpeye/awesome-mcp-servers | yes, marked |

Typical workflows

- Create goldens, regress after prompt/skill changes.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/hugoles/langfuse-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
