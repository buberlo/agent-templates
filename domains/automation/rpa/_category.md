# RPA

- **Domain:** `automation`
- **Category:**r pa’
- **As of:** 2026-11-23

## Summary

UI robotics on desktop and older applications if no API exists.

## Recommended tool stack

- n8n for deterministics, browser/mobile MCP only targeted, gates for effective actions

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| n8n | Platform + MCP catalog entry | https://github.com/n8n-io/n8n | Workflow automation with AI nodes; in Hermes as n8n-official in the optional MCP catalog. | n8n itself host or cloud; in Hermes hermes mcp install n8n-official. | 211.894 Stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation over accessibility snapshots, UI testing and interaction with web apps. | npx @playwright/mcp@latest (official Docs/Repo). | 40,040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |

Typical workflows

- Set task, allowed tools and definition of done.
- First read/research, then draft, then release for effective steps.
- Re-read output (file, URL, ticket) and specify source.

## Pitfalls

Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok-bot-wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/n8n-io/n8n
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
