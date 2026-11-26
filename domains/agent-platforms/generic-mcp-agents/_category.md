# Generic MCP agents

- **Domain:** `agent-platforms`
- **Category:** `generic-mcp-agents`
- **As of:** 2026-11-23

## Summary

Common pattern: MCP for access, tools for actions, skills for workflows.

## Recommended tool stack

- MCP for Zugang, Tools for Aktionen, Skills for Verhalten
- Kuratierte Listen: awesome-mcp-servers, Referenzserver

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| punkpeye/awesome-mcp-servers | Catalog | https://github.com/punkpeye/awesome-mcp-servers | Large curated list, last active Nov 2026, web directory glama.ai. | Use only as a directory, do not install as a server. | 98,405 stars | https://github.com/punkpeye/awesome-mcp-servers | no (as cited) |
| modelcontextprotocol/servers | Referenz | https://github.com/modelcontextprotocol/servers | Referenzimplementierungen. | Repo. | 92,179 Stars | https://github.com/modelcontextprotocol/servers | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Wenige Server, Filter, Read-only defaults, Skills for den Ablauf, menschliche Gates for Writes.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/modelcontextprotocol/servers
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
