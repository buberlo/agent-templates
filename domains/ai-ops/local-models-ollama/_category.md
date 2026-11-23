# Local models / Ollama

- **Domain:** `ai-ops`
- **Category:** `local-models-ollam a’
- **As of:** 2026-11-23

## Summary

Operating, quantizing, configuring context and persistence local LLMs.

## Recommended tool stack

- Ollama or comparable runtime, sufficient context, own Evals before models are exchanged

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|------------------------------------------------------
| Ollama (local, typically via CLI instead of MCP) | CLI / Runtime | https://ollama.com | Local LLMs serve, often directly from the agent or as an OpenAI-compatible endpoint. No star-populated official Ollama MCP captured in this research. | Installer from ollama.com; Show agent providers on local endpoint (Hermes: hermes model). | Popularity of Ollama even here not newly measured by API. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | yes, marked |

Typical workflows

- Select hardware appropriately, set context limit and persistence, measure quality with your own assessment.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://ollama.com
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
