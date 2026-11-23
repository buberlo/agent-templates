# Design to Code

- **Domain:** `software-development`
- **Category:** `design-to-code`
- **As of:** 2026-11-23

## Summary

Translate Figma/Design systems into executable code or components.

## Recommended tool stack

- Figma MCP
- Danach Tests im Browser

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| figma MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma | Design-to-Code-Kontext. | hermes mcp install figma | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp |Local browser automation with accessibility snapshots, UI tests and interaction with web apps.| npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |

## Typical workflows

- Only selected frames, not load entire files into context at once.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
