# Quality and CSAT

- **Domain:** `customer-service`
- **Category:** `qos-csat`
- **As of:** 2026-11-23

## Summary

Evaluous discussion quality, CS/NPS and escalation patterns.

## Recommended tool stack

- Helpdesk-MCP (z. B. Intercom) + interne Knowledge-Base
- No stillen Closes

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| intercom MCP (Hermes-catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom | Intercom aus dem Nous-catalog. | hermes mcp install intercom | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Establish.es, set, permitted tools and related definition,
- First read/research, then draft, then release for working steps.
re-intelligence and re-intelligence. God of the re-intelling and re- right.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine both, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policies and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok-bot-wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/intercom
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
