# KDP / Kindle Direct Publishing

- **Domain:** `sales-crm`
- **Category:** `kdp`
- **As of:** 2026-11-23

## Summary

Manuscript, metadata and listing aids for self-publishing; few sophisticated official agent tools.

## Recommended tool stack

- Research MCP + CRM MCP (Attio/Close or similar)
- Email only as a draft

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| attio MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM Attio. | hermes mcp install attio | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| close MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close | CRM Close. | hermes mcp install close | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Define the task, permitted tools, and Definition of Done.
- First read/research, then draft, then approve for effective steps.
- Proofread the output (file, URL, ticket) and specify the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, don't confuse them. Sources: URL0 , URL1
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: URL0 , URL1
- Do not write tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: URL0
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/close
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
