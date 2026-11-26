# ETL-Pipelines

- **Domain:** `data-analytics`
- **Category:** `etl-pipelines`
- **As of:** 2026-11-23

## Summary

Daten laden, transformieren and orchestrieren (Airflow-nahe, Cloud-ETL, n8n).

## Recommended tool stack

- n8n or vorhandene Data-Platform-MCPs
- Idempotenz and Logs

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| n8n | Platform + MCP catalog entry | https://github.com/n8n-io/n8n | Workflow automation with AI nodes; included in Hermes as n8n-official in the optional MCP catalog. | Self-host n8n or use Cloud; in Hermes: hermes mcp install n8n-official. | 211,894 stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| motherduck MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck | Target or analytics layer. | hermes mcp install motherduck | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Extract/Load im Workflow-Tool, Transformation versioniert, Agent schreibt or reviewed die Jobs.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://github.com/n8n-io/n8n
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
