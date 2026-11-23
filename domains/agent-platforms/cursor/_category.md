# Cursor

- **Domain:** `agent-platforms`
- **Category:** `cursor`
- **As of:** 2026-11-23

## Summary

IDE agent, MCP plugins, skills; Grok-Bot shares the plugin model.

## Recommended tool stack

- Cursor-MCP-Config, Skills, dieselben Plugin-Muster wie Grok Bot laut offizieller Bot-101-Aussage

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|

| Cursor + MCP/Skills | IDE-Agent | https://x.ai/bot/guides/grok-bot-101 |Grok Bot 101: Grok Bot supports the same MCP servers, plugins, and skills as Cursor.| Cursor-Settings / mcp.json; Plugins analog Connect Apps im Bot-Kosmos. | Produktdoku (no Cursor-Star-Zahl in dieser Recherche). | https://x.ai/bot/guides/grok-bot-101 | no (as cited) |

## Typical workflows

- Version local MCP-Config (without secrets), skills in the repo for the team.

## Pitfalls

- Team Allowlists can block MCPs. Secrets do not commit in mcp.json.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://x.ai/bot/guides/grok-bot-101
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
