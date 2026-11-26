# n8n, Make, Zapier

- **Domain:** `automation`
- **Category:** `n8n-make-zapier`
- **As of:** 2026-11-23

## Summary

Visual or API-driven automations, including official n8n MCP entries.

## Recommended tool stack

- n8n (self-hosted or Cloud) plus official MCP catalog entry in Hermes

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| n8n | Platform + MCP catalog entry | https://github.com/n8n-io/n8n | Workflow automation with AI nodes; included in Hermes as n8n-official in the optional MCP catalog. | Self-host n8n or use Cloud; in Hermes: hermes mcp install n8n-official. | 211,894 stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Deterministische Integrationen in n8n, unsichere Urteile im Agenten, klare Schnittstelle dazwischen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Doppelte Automationen. Secrets im n8n-Cred-Store, not im Skill.

## Sources

- https://github.com/n8n-io/n8n
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
