# SIEM and SOC

- **Domain:** `security`
- **Category:** `siem-soc`
- **As of:** 2026-11-23

## Summary

Alerts triage, correlation and playbooks in SIEM/SOAR environments (defensive).

## Recommended tool stack

- Existing SIEM APIs/MCPs of the Org, Read-first, Playbooks

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| datadog MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog | Observability-Kontext, soweit berechtigt. | hermes mcp install datadog | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp |Production errors, issues and context for coding agents.| Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | no (as cited) |
| grafana MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/grafana | Dashboards/Alerts lesen. | hermes mcp install grafana | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Alert → Kontext sammeln → dokumentierte Mitigationsvorschlaege. No Offensivmassnahmen.

## Pitfalls

- Write-Zugriff auf Detection-Rules ist hochsensibel.
- Nur defensive, autorisierte Nutzung.
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/getsentry/sentry-mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/datadog
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/grafana
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
