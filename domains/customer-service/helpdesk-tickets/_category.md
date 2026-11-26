# Helpdesk and Tickets

- **Domain:** `customer-service`
- **Category:** `helpdesk-tickets`
- **As of:** 2026-11-23

## Summary

Review and prioritize tickets, write drafts, and update them in Zendesk/Intercom/similar tools.

## Recommended tool stack

- Intercom-MCP or andere Helpdesk-MCPs
- Knowledge-Base im Vault

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| intercom MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom | Intercom customer support platform. | hermes mcp install intercom | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| awesome-mcp support section | Catalog | https://github.com/punkpeye/awesome-mcp-servers | Additional support/ITSM servers, verify individually. | Per repo. | Catalog. | https://github.com/punkpeye/awesome-mcp-servers | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Read ticket, macro/draft, internal note, no silent resolves without policy.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- PII in Prompts and Logs minimieren.

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
