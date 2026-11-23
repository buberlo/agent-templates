# Shopify

- **Domain:** `sales-crm`
- **Category:** `shopify`
- **As of:** 2026-11-23

## Summary

Shopify catalog, orders and store operations for agents.

## Recommended tool stack

- Individually verify Shopify-related MCPs from awesome-mcp (many are unofficial or require payment)

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| forgemeshlabs/shopscout-mcp | MCP | SAVE0 | Listed in awesome-mcp as an official entry: Shopify catalog search, offer ranking, shipping comparison, x402 payment per call. | See repo (hosted, paid calls according to catalog text). | Stars not pulled via API here. | SAVE1 | Yes, marked |

## Typical workflows

- Read catalog, price/stock as a report, changes to the live shop only with approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/forgemeshlabs/shopscout-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
