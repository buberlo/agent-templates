# Frontend

- **Domain:** `software-development`
- **Category:** `frontend`
- **As of:** 2026-11-23

## Summary

UI implementation, design-to-code (Figma), components and accessibility.

## Recommended tool stack

- Figma-MCP + Coding-Agent + Browser-MCP zum Sichtverify

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| figma MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma | Design-Kontext; taucht in Community-Tier-Listen neben GitHub/Context7/Playwright auf. | hermes mcp install figma | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| canva MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/canva | Canva aus dem Nous-catalog. | hermes mcp install canva | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp |Local browser automation with accessibility snapshots, UI tests and interaction with web apps.| npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Chrome DevTools MCP | MCP | https://github.com/ChromeDevTools/chrome-devtools-mcp |Live Chrome control and debug (Performance, Network, Console) for coding agents.|About the GitHub repo / MCP client config (stdio), see README.| 58.941 Stars | https://github.com/ChromeDevTools/chrome-devtools-mcp | no (as cited) |

## Typical workflows

- design link + component rules; then in the browser against the running app verify.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://playwright.dev/mcp/introduction
- https://x.com/tooltierai/status/2122012506868584772
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/figma
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/canva
- https://github.com/microsoft/playwright-mcp
- https://github.com/ChromeDevTools/chrome-devtools-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
