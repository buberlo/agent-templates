# Testing

- **Domain:** `software-development`
- **Category:** `testing`
- **As of:** 2026-11-23

## Summary

Write and run unit, integration and E2E tests (incl. Playwright).

## Recommended tool stack

- Projekt-Testframework + Playwright for E2E

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp | Control and debug live Chrome (Performance, Network, Console) for coding agents. | Via the GitHub repo / MCP client config (stdio), see README. | 58,941 stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | no (as cited) |
| Hermes skill test-driven-development | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | TDD: RED-GREEN-REFACTOR, tests before code. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Have tests written, run locally, only then expand the implementation.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Playwright MCP streamt grosse Snapshots – for reine Extraktion unnoetig teuer.

## Sources

- https://playwright.dev/mcp/introduction
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/microsoft/playwright-mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
