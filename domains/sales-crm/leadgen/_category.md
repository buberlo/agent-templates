# Lead generation

- **Domain:** `sales-crm`
- **Category:** `leadgen`
- **As of:** 2026-11-23

## Summary

Research and qualify target accounts and contacts, and import them into lists or CRM.

## Recommended tool stack

- Web research stack + CRM MCP + outreach drafts

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server | Web search and crawling, designed for agent research. | See the repo (hosted/stdio). | 5,264 stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Web search via the Brave Search API. | Official Brave repository. | 1,585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| attio MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM import. | hermes mcp install attio | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| close MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close | CRM import. | hermes mcp install close | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Define ICP, public sources only, list with source column.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Scraping against ToS; do not present invented email addresses as verified.

## Sources

- https://github.com/exa-labs/exa-mcp-server
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/brave/brave-search-mcp-server
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
