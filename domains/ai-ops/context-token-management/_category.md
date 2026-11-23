# Context and token management

- **Domain:** `ai-ops`
category: Context token management `
- **As of:** 2026-11-23

## Summary

Tool scheme overhead, lazy loading, CLI instead of fat MCPs, prompt budgets.

## Recommended tool stack

- Few MCPs, tool filters, skills instead of always-on tools, CLI instead of bold browser MCP

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation over accessibility snapshots, UI testing and interaction with web apps. | npx @playwright/mcp@latest (official Docs/Repo). | 40,040 Stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Context7 | MCP / Platform | https://github.com/upstash/context7 | Get current version-specific library documentation into the agent context. | package @upstash/context7-mcp or Docs in the repo. | 65.314 Stars | https://github.com/upstash/context7 | no (as cited) |
| Hermes tools.include / exclude and MCP filters | Config | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | Per server export only the necessary tools. | ~/.hermes/config.yaml or hermes mcp status. | Product documentary. | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

Typical workflows

- Measure baseline token consumption without question, then turn off servers until the stack is portable.

## Pitfalls

- MCP tool schemas can put a lot of stress on the context even before the first question comes up. In r/ClaudeAI, a user reported 67,000 token overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft recommends cli over mcp for playwright/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://docs.openclaw.ai/skills/
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/upstash/context7
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
