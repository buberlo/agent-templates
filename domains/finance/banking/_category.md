# Banking

- **Domain:** `finance`
- **Category:** `banking`
- **As of:** 2026-11-23

## Summary

Read transactions via banking/open-banking MCPs (Plaid etc.); no secrets in chat.

## Recommended tool stack

- Plaid catalog MCP, read-only, strong auth

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| plaid MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/plaid | Open-banking/account data when the user authorizes Plaid. | hermes mcp install plaid | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Categorize transactions; no transfers without a separate system and explicit task.

## Pitfalls

- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
