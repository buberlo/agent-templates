# Smart Home

- **Domain:** `automation`
- **Category:** `smart-home`
- **As of:** 2026-11-23

## Summary

Control Home Assistant and devices, create automations.

## Recommended tool stack

- Home Assistant MCP, least privilege, no exposure without auth

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| homeassistant-mcp (tevonsb) | MCP | https://github.com/tevonsb/homeassistant-mcp | Read Home Assistant data and control devices (lights, switches, thermostats). | Local MCP, see repo. Listed in awesome-mcp-servers, home automation section. | Star count not fetched via API in this research. | https://github.com/punkpeye/awesome-mcp-servers | yes, marked |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Read states, suggest scenes, execute switching actions after confirmation – especially for doors, garages, and heaters.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- An MCP exposed to the internet is a physical risk.

## Sources

- https://github.com/tevonsb/homeassistant-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
