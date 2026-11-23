# Payments (Stripe etc.)

- **Domain:** `finance`
- **Category:** `payments-stripe`
- **As of:** 2026-11-23

## Summary

Payment provider, customers, products, and subscriptions via official toolkits/MCPs.

## Recommended tool stack

- Official Stripe Agent Toolkit / Hermes stripe catalog
- No live charges without approval

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Stripe Agent Toolkit | Toolkit / MCP-capable | https://github.com/Stripe/agent-toolkit | Official tools to integrate Stripe into AI products and agents. | See repo; Hermes optional-mcps: stripe. | 2,083 Stars | https://github.com/Stripe/agent-toolkit | no (as cited) |
| paypal MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/paypal | PayPal from the Nous catalog. | hermes mcp install paypal | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| square MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/square | Square from the Nous catalog. | hermes mcp install square | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Use sandbox/test data first; live only with explicit scope and limits.

## Pitfalls

- Refunds and payouts are irreversibly visible.
- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/Stripe/agent-toolkit
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
