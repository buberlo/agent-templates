# Mental health organization

- **Domain:** `health-fitness`
- **Category:** `mental-health-organisation`
- **As of:** 2026-11-23

## Summary

Appointments, reminders, journaling structure—not therapy or crisis replacement.

## Recommended tool stack

- Strava or health APIs only with user OAuth; no clinical advice

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| strava MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava | Activity data when user authorizes Strava. | hermes mcp install strava | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Define scope, allowed tools, and definition of done.
- Read and research first, then draft, then approval before impactful steps.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- No medical diagnosis, therapy, or emergency control—acute symptoms: call emergency services.
- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava
