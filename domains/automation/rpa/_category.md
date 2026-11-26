# RPA

- **Domain:** `automation`
- **Category:** `rpa`
- **As of:** 2026-11-23

## Summary

UI robotics on desktop and legacy applications when no API exists.

## Recommended tool stack

- n8n for deterministic workflows, browser/mobile MCP only selectively, gates for impactful actions

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| n8n | Platform + MCP catalog entry | https://github.com/n8n-io/n8n | Workflow automation with AI nodes; included in Hermes as n8n-official in the optional MCP catalog. | Self-host n8n or use Cloud; in Hermes: hermes mcp install n8n-official. | 211,894 stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/n8n-io/n8n
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
