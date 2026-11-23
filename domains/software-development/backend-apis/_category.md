# Backend and APIs

- **Domain:** `software-development`
- **Category:** `backend-apis`
- **As of:** 2026-11-23

## Summary

Services, APIs, Authentic, and Server-side Logic

## Recommended tool stack

- Repo-Tools + Context7 + DB-MCP im Read-only wo moeglich

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | no (as cited) |
| supabase MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase | Projekte/SQL; Community empfiehlt Read-only-Mode. Hosted-URL in Drittrepos mcp.supabase.com – Repo supabase/supabase-mcp war per API 404. | hermes mcp install supabase | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp |Production errors, issues and context for coding agents.| Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as cited) |

## Typical workflows

- API contract first, then implementation and testing.

## Pitfalls

- Destructive SQL durch DB-MCPs – Read-only-Mode bevorzugen.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine both, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://x.com/tooltierai/status/2122012506868584772
- https://github.com/upstash/context7
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase
- https://github.com/getsentry/sentry-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
