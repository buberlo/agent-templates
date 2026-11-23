# Testing

- **Domain:** `software-development`
- **Category:** `testing`
- **As of:** 2026-11-23

## Summary

Write and run unit, integration and E2E tests (including Playwright).

## Recommended tool stack

- Project test framework + Playwright for E2E

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp |Local browser automation with accessibility snapshots, UI tests and interaction with web apps.| npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp |Live Chrome control and debug (Performance, Network, Console) for coding agents.|About the GitHub repo / MCP client config (stdio), see README.| 58.941 Stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | no (as cited) |
| Hermes-Skill test-driven-development | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | TDD: RED-GREEN-REFACTOR, Tests vor Code. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Tests schreiben lassen, lokal ausfuehren, erst dann Implementation verbreitern.

## Pitfalls

Playwright MCP streams large snapshots – unnecessarily expensive for pure extraction.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://playwright.dev/mcp/introduction
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/microsoft/playwright-mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
