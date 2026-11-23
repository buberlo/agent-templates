# ETL-Pipelines

- **Domain:** `daten-analytics`
- **Category:** `etl-pipelines`
- **As of:** 2026-11-23

## Summary

According to the company, the “Pick-” and then “】 transforming and orchestrating the data (Airflow-Near, Cloud-ETL, n8n).

## Recommended tool stack

- n8n or existing data-platform MCPs
- Idempotence and logs

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| n8n | Plattform + MCP-catalog entry | https://github.com/n8n-io/n8n |Workflow automation with AI nodes; in Hermes as n8n-official in the optional MCP catalogue.| n8n selbst hosten or Cloud; in Hermes hermes mcp install n8n-official. | 211.894 Stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |
| motherduck MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck | Ziel- or Analyseschicht. | hermes mcp install motherduck | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as documented) |

## Typical workflows

- Extract/Load in the workflow tool, transformation versioned, agent writes or reviewed the jobs.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/n8n-io/n8n
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
