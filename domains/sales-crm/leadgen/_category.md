# Lead generation

- **Domain:** `sales-crm`
- **Category:** `leadgen`
- **As of:** 2026-11-23

## Summary

Research target accounts and contacts, qualify them, and add them to lists or the CRM.

## Recommended tool stack

- Web-Recherche-Stack + CRM-MCP + Outreach-Entwuerfe

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Exa MCP | MCP | https://github.com/exa-labs/exa-mcp-server |Web search and crawling, designed for agent research.| Siehe Repo (hosted/stdio). | 5.264 Stars | https://github.com/exa-labs/exa-mcp-server | no (as cited) |
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server |Web search via the Brave Search API.| Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| attio MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM-Uebernahme. | hermes mcp install attio | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| close MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close | CRM-Uebernahme. | hermes mcp install close | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Define ICP, only public sources, list with origin column.

## Pitfalls

- Scraping in violation of the ToS; do not present fabricated email addresses as verified.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, don't confuse them. Sources: URL0 , URL1
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: URL0 , URL1
- Do not write any tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: URL0
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

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
