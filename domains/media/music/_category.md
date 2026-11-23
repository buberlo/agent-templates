# Music

- **Domain:** `media`
- **Category:** `musik`
- **As of:** 2026-11-23

## Summary

Musikproduktion, Prompting for generative Musik and songwriting-nahe Agent-Skills.

## Recommended tool stack

- Hermes-Skill songwriting-and-ai-music for Craft/Prompts
- Generative Dienste only over erlaubte Cutstellen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill songwriting-and-ai-music | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Songwriting-Handwerk and Suno-AI-Musik-Prompts. | Bundled creative/songwriting-and-ai-music. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Texte lokal write, generative Tools as optionale Stufe, Rechte clarify.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
