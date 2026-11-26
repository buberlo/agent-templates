# Model Routing

- **Domain:** `ai-ops`
- **Category:** `model-routing`
- **As of:** 2026-11-23

## Summary

Route tasks to suitable models/providers, manage cost and quality.

## Recommended tool stack

- Hermes hermes model / Smart Routing (Quickstart)

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes model picker / Smart Routing | Platform feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Interactive model selection; Smart Routing is disabled in Blank Slate, otherwise part of the recommended defaults. | hermes model or setup modes. | Product documentation. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Cheaper model for triage, stronger model for high-risk steps.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Schwache Modelle rufen Tools unzuverlaessig.

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
