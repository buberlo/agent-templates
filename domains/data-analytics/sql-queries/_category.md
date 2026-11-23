# SQL queries

- **Domain:** `daten-analytics`
- **Category:** `sql-abfragen`
- **As of:** 2026-11-23

## Summary

-SQL against the use of the -DKD/D extracted from the product or for the use-novanova, or of the resumable range.

## Recommended tool stack

- MotherDuck/Postgres/Supabase Read-only
- Ergebnisse als Tabelle plus Query-Text

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| motherduck MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck | Analytical SQL / DuckDB Cloud. | hermes mcp install motherduck | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| supabase MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase | SQL against Supabase; prefer read-only. | hermes mcp install supabase | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |

## Typical workflows

- Zuerst Schema lesen, dann begrenztes SELECT, no ungebremsten Full Scans auf Prod.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
