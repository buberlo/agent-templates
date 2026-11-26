# Build MCP server

- **Domain:** `ai-ops`
- **Category:** `mcp-server-build`
- **As of:** 2026-11-23

## Summary

Eigene MCP-Server designen, implementieren and an Clients anbinden.

## Recommended tool stack

- MCP spec + official SDKs + mcp-builder skill from Claude skill lists

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| modelcontextprotocol/servers (reference servers) | Reference | https://github.com/modelcontextprotocol/servers | Official/reference MCP servers for learning the patterns. | Clone repo, run individual servers per README. | 92,179 stars | https://github.com/modelcontextprotocol/servers | no (as cited) |
| mcp-builder (described in awesome-claude-skills) | Skill | https://github.com/ComposioHQ/awesome-claude-skills | Guide for building high-quality MCP servers in Python/TypeScript. | Via the respective skill installation method of the platform used. | 80,108 stars (list repo, not the skill alone). | https://github.com/ComposioHQ/awesome-claude-skills | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Narrow tool scope, clear descriptions, least privilege, tests, then catalog/review (Nous merges MCPs only via PR).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Zu viele Tools, zu lange Schemas (Token-Overhead). Ungepruefte Community-Server.

## Sources

- https://github.com/modelcontextprotocol/servers
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
