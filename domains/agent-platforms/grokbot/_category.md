# Grok Bot

- **Domain:** `agent-platforms`
- **Category:** `grokbot`
- **As of:** 2026-11-23

## Summary

Connect Apps, Custom MCP, Skills-Decke, Box-Computer, no localhost-MCPs.

## Recommended tool stack

Connect apps for catalog plugins
- Custom MCP only public HTTPS or Command on the bot box
- Skills-Decke observe
- @-Attach

## MCP Server and Skills

| Name | Type | URL | Usage | Install | Popularity | Source | Unverified |
|------|-------|-----------|
| Grok Bot Plugins / Custom MCP | Product connector | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Connect apps; OAuth tokens stay on the connector backend. Custom MCP: remote HTTPS (streamable HTTP/SSE) or command (`npx`/`uvx`) on the bot machine—not the user laptop localhost or VPN-only. Wiki notes no safe secret-header pattern. | Connect Apps or ask the bot to add the server. Tool policies: always allow, auto-review, needs approval, blocked (wiki, from 0.70.2/1.2.3). | Product docs/wiki (versions 0.75.x–0.77.x, Oct/Nov 2026). | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |
| Grok Bot 101 | Official intro | https://x.ai/bot/guides/grok-bot-101 | Grok Bot supports the same MCP servers, plugins, and skills as Cursor; multiple accounts per service possible. | x.ai/bot app, Connect Apps. | Official guides. | https://x.ai/bot/guides/grok-bot-101 | no (as cited) |

## Typical workflows

- Install plugin, complete Auth in the deadline, hang with @ to the task, block individual tools if necessary.
- If no connector exists: work on the bot computer (CLI, files), do not pretend to be connected to a private laptop MCP.

## Pitfalls

- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skill-Ceiling 200 (seit 0.71.2, Wiki).
Shared Bots: Team can read Command and Args from a Command server.
- Many viral X-threads about N GitHub repos are marketing - not unchecked.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
