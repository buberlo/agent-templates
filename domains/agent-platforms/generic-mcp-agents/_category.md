# Generic MCP agents

- **Domain:** `agent-platforms`
- **Category:** `generic-mcp-agents`
- **As of:** 2026-11-23

## Summary

Common pattern: MCP for access, tools for actions, skills for operations.

## Recommended tool stack

- MCP for access, tools for actions, skills for behavior
- Kuratierte Listen: awesome-mcp-servers, Referenzserver

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|

| punkpeye/awesome-mcp-servers | catalog | https://github.com/punkpeye/awesome-mcp-servers | Grosse kuratierte Liste, zuletzt aktiv Nov 2026, Web-Directory glama.ai. |Only use as a directory, not install as a server.| 98.405 Stars | https://github.com/punkpeye/awesome-mcp-servers | no (as cited) |
| modelcontextprotocol/servers | Referenz | https://github.com/modelcontextprotocol/servers | Referenzimplementierungen. | Repo. | 92.179 Stars | https://github.com/modelcontextprotocol/servers | no (as cited) |

## Typical workflows

- Few servers, filters, read-only defaults, skills for the process, human gates for writes.

## Pitfalls

- MCP tool schemas can put a lot of stress on the context even before the first question comes up. In r/ClaudeAI, a user reported 67,000 token overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i measured my mcp token overhead 67k tokens/
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/modelcontextprotocol/servers
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
