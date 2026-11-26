# Backend and APIs

- **Domain:** `software-development`
- **Category:** `backend-apis`
- **As of:** 2026-11-23

## Summary

Services, APIs, Auth and serverseitige Logik.

## Recommended tool stack

- Repo-Tools + Context7 + DB-MCP im Read-only wo moeglich

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische librarysdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65,314 Stars | https://github.com/upstash/context7 | no (as cited) |
| supabase MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/supabase | Projects/SQL; community recommends read-only mode. Hosted URL in third-party repos mcp.supabase.com – repo supabase/supabase-mcp returned 404 via API. | hermes mcp install supabase | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Produktionsfehler, Issues and Kontext for Coding-Agenten. | Officials getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- API contract first, then implementation and tests.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Destructive SQL via DB MCPs – prefer read-only mode.

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
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
