# Prompt Engineering

- **Domain:** `ai-ops `
category: Prompt-engineering g'
- **As of:** 2026-11-23

## Summary

Sharpen system prompts, skills and tool descriptions.

## Recommended tool stack

Short skill descriptions, clear tool descriptions, evaluations

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Agent Skills progressive disclosure | pattern | https://code.claude.com/docs/en/skills/ | Only name/description (about 100 tokens) until the skill reaches, then body, then scripts. | SKILL.md format. | 199.219 Stars | https://code.claude.com/docs/en/skills/ | no (as cited) |

Typical workflows

- Treat description as trigger text: when the skill should fire and when not.

## Pitfalls

- Personality instructions do not belong in every skill (OpenClaw advice: procedure, not persona).
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
