# Context and token management

- **Domain:** `ai-ops`
- **Category:** `context-token-management`
- **As of:** 2026-11-23

## Summary

Tool-Schema-Overhead, Lazy Loading, CLI statt fetter MCPs, Prompt-Budgets.

## Recommended tool stack

- Wenige MCPs, Tool-Filter, Skills statt immer-on Tools, ggf. CLI statt fetter Browser-MCP

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Local browser automation via accessibility snapshots, UI tests, and interaction with web apps. | npx @playwright/mcp@latest (official docs/repo). | 40,040 stars | https://playwright.dev/mcp/introduction | no (as cited) |
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische librarysdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65,314 Stars | https://github.com/upstash/context7 | no (as cited) |
| Hermes tools.include / exclude and MCP filter | Config | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | Export only the tools each server needs. | ~/.hermes/config.yaml or hermes mcp status. | Product docs. | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Measure baseline token consumption without a query, then disable servers until the stack is sustainable.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/

## Sources

- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://www.reddit.com/r/mcp/comments/1spvkrz/microsoft_recommends_cli_over_mcp_for_playwright/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://docs.openclaw.ai/skills/
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://github.com/upstash/context7
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
