# Smart Home

- **Domain:** `automation`
category: Smart-home `
- **As of:** 2026-11-23

## Summary

Control home assistant and devices, create automations.

## Recommended tool stack

- Home Assistant MCP, Least Privilege, no exposure without Auth

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| homeassistant-mcp (tevonsb) | MCP | https://github.com/tevonsb/homeassistant-mcp | Read home assistant data and control devices (lights, switches, thermostats). | Local MCP, see Repo. Entry in awesome-mcp-servers, Home Automation section. | Star number in this research not drawn by API. | https://github.com/punkpeye/awesome-mcp-servers | yes, marked |

Typical workflows

- Reading events, suggesting scenes, switching actions after confirmation - especially in doors, garages, heating systems.

## Pitfalls

- An open MCP on the Internet is a physical risk.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/tevonsb/homeassistant-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
