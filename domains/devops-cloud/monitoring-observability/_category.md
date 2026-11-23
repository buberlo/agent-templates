# Monitoring and Observability

- **Domain:** `devops-cloud`
- **Category:** `monitoring-observability`
- **As of:** 2026-11-23

## Summary

Metrics, Traces, Dashboards in Grafana, Datadog, Sentry, Prometheus.

## Recommended tool stack

- Sentry for App-Errors, Grafana/Datadog for Infra, Read-only

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Production errors, issues, and context for coding agents. | Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as documented) |
| grafana MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/grafana | Grafana aus dem Nous-catalog. | hermes mcp install grafana | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| datadog MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog | Datadog aus dem Nous-catalog. | hermes mcp install datadog | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| betterstack MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/betterstack | Better Stack aus dem Nous-catalog. | hermes mcp install betterstack | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |

## Typical workflows

Community posts pair coding agents with Sentry plus browser MCP to see Prod errors.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/getsentry/sentry-mcp
- https://x.com/loudernet/status/2119104655061823561
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/grafana
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/betterstack
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
