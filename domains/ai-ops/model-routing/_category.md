# Model Routing

- **Domain:** `ai-ops`
category: Model-routing
- **As of:** 2026-11-23

## Summary

Allocate tasks to suitable models/providers, control costs and quality.

## Recommended tool stack

- Hermes hermes model / Smart Routing (Quickstart)

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Hermes model picker / Smart Routing | Platform feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Interactive model selection; Smart routing is disabled in Blank Slate, otherwise part of the recommended defaults. | hermes model or setup modes. | Product documentary. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |

Typical workflows

- Cheaper model for triage, stronger for risky steps.

## Pitfalls

- Weak models call tools unreliable.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Source: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
