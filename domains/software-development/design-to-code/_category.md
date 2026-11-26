# Design to Code

- **Domain:** `software-development`
- **Category:** `design-to-code`
- **As of:** 2026-11-23

## Summary

Translate Figma/design systems into working code or components.

## Recommended tool stack

- Figma MCP
- Danach Tests im Browser

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| figma MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma | Design-to-code context. | hermes mcp install figma | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Load only selected frames into context, not entire files at once.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

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
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
