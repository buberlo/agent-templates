# Amazon

- **Domain:** `sales-crm`
- **Category:** `amazon`
- **As of:** 2026-11-23

## Summary

Amazon product, order and Seller Central data (often unofficial or Seller APIs).

## Recommended tool stack

- Seller or data servers are often unofficial; be particularly careful with login-in-browser variants

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| HasData/amazon-mcp | MCP | https://github.com/HasData/amazon-mcp | Catalog entry: product data, reviews, and seller as JSON. | See the repo (typically an API-key service). | Stars not pulled here via API. | https://github.com/punkpeye/awesome-mcp-servers | yes, marked |

## Typical workflows

- Only extract data that the account or the API allows.

## Pitfalls

- Unofficial, ToS, credential risk with third-party logins.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, don't confuse them. Sources: URL0 , URL1
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: URL0 , URL1
- Do not write tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: URL0
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/HasData/amazon-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
