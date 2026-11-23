# Incident Response

- **Domain:** `devops-cloud`
- **Category:** `incident-response`
- **As of:** 2026-11-23

## Summary

Incidents triagieren, Timeline bauen, Runbooks abarbeiten (without Offensiv-Schritte).

## Recommended tool stack

- Monitoring-MCPs + Runbook + Chat
- Nur dokumentierte, autorisierte Schritte

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Production errors, issues, and context for coding agents. | Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as documented) |
| datadog MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog | Observability-Kontext. | hermes mcp install datadog | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| ClawHub „Slack“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Slack integration as a skill. | openclaw skills install (Owner steipete) and openclaw skills verify. | 42.838 Downloads, 140 Registry-Stars (ClawHub Leaderboard 2026-11-23). | https://clawhubtrends.com/leaderboard.html | no (as documented) |

## Typical workflows

Timeline,reds, impacts civilians, human release before changes.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/getsentry/sentry-mcp
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
