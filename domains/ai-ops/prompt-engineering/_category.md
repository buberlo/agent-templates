# Prompt Engineering

- **Domain:** `ai-ops`
- **Category:** `prompt-engineering`
- **As of:** 2026-11-23

## Summary

Refine system prompts, skills, and tool descriptions.

## Recommended tool stack

- Kurze Skill-Descriptions, klare Tool-Beschreibungen, Evaluations

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Agent Skills progressive disclosure | Pattern | https://code.claude.com/docs/en/skills/ | Only name/description (approx. 100 tokens) until the skill triggers, then body, then scripts. | SKILL.md format. | 199,219 stars | https://code.claude.com/docs/en/skills/ | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Treat description as trigger text: when the skill should fire and when it should not.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Personality-Instruktionen gehoeren not in jedes Skill (OpenClaw-Rat: Prozedur, not Persona).

## Sources

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
