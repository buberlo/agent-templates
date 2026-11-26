# Local models / Ollama

- **Domain:** `ai-ops`
- **Category:** `local-models-ollama`
- **As of:** 2026-11-23

## Summary

Run local LLMs, quantize models, configure context and persistence.

## Recommended tool stack

- Ollama or a comparable runtime, sufficient context, custom evals before swapping models

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Ollama (local, typically via CLI instead of MCP) | CLI / Runtime | https://ollama.com | Serve local LLMs, often directly from the agent or as an OpenAI-compatible endpoint. No star-verified official Ollama MCP recorded in this research. | Installer from ollama.com; point the agent provider to the local endpoint (Hermes: hermes model). | Popularity of Ollama itself not re-measured via API here. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | yes, flagged |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Choose appropriate hardware, set context limit and persistence, measure quality with custom verification.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://ollama.com
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
