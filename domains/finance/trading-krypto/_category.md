# Trading and crypto

- **Domain:** `finance`
- **Category:** `trading-krypto`
- **As of:** 2026-11-23

## Summary

Market data and research (Twelve Data, Robinhood catalog entries); trading only with clear limits.

## Recommended tool stack

- Separate data MCPs from order routing

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| robinhood MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/robinhood | Catalog entry—verify write permissions in vendor docs before live use. | hermes mcp install robinhood | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| twelve-data MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twelve-data | Market data from the Nous catalog. | hermes mcp install twelve-data | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| ClawHub "Polymarket" (joelchance) | Skill | https://clawhubtrends.com/leaderboard.html | Very high downloads; not investment advice. | openclaw skills install (Owner joelchance) and openclaw skills verify. | 172,358 Downloads, 112 Registry-Stars (ClawHub Leaderboard 2026-11-23). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub "Stock Analysis" (udiedrichsen) | Skill | https://clawhubtrends.com/leaderboard.html | Warning badge on leaderboard—verify before use. | openclaw skills install (Owner udiedrichsen) and openclaw skills verify. | 48,766 Downloads, 227 Registry-Stars (ClawHub Leaderboard 2026-11-23). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Research and data yes; automated trading only with written limits and separate approval.

## Pitfalls

- Warning-flagged skills. Market skills can mislead.
- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
