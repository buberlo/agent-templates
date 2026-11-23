#n8n, Make, Zapier

- **Domain:** `automation`
- Category: `n8n-make-zapier`
- **As of:** 2026-11-23

## Summary

Visual or API-based automations, including official n8n MCP entries.

## Recommended tool stack

- n8n (self-host or cloud) plus official MCP catalog entry in Hermes

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| n8n | Platform + MCP catalog entry | https://github.com/n8n-io/n8n | Workflow automation with AI nodes; in Hermes as n8n-official in the optional MCP catalog. | n8n itself host or cloud; in Hermes hermes mcp install n8n-official. | 211.894 Stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

Typical workflows

- Deterministic integrations in n8n, uncertain judgments in the agent, clear interface between them.

## Pitfalls

Double automation. Secrets in the n8n cred store, not in the skill.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/n8n-io/n8n
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
