# Homelab

- **Domain:** `it-operations-support`
- **Category:** `homelab`
- **As of:** 2026-11-23

## Summary

Self-hosted labs: Proxmox, Docker, home server, documentation of your own infrastructure.

## Recommended tool stack

- SSH/Terminal, Docker, optional Home Assistant, Documentation im Vault

## MCP servers and skills

| Name | Typee | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| homeassistant-mcp (tevonsb) | MCP | https://github.com/tevonsb/homeassistant-mcp | Read Home Assistant data and control devices (lights, switches, thermostats). | Local MCP, see repo. Entry in awesome-mcp-servers, Home Automation section. | Star count not retrieved via API in this search. |https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |
| Obsidian skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Read vault, search, create/edit notes—common memory/knowledge layer. | Hermes bundled /obsidian. OpenClaw: ClawHub skill Obsidian (steipete). | ClawHub: 92,458 downloads, 381 stars (leaderboard 2026-11-23). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typeical workflows

- Inventory and runbooks first, changes small and reversible.

## Pitfalls

- Remote access only with consent and a visible session.
- Do not write any tokens or passwords in chats, skill files or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain any credentials in argv. Source:https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, do not confuse them. Sources:https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources:https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/tevonsb/homeassistant-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://clawhubtrends.com/leaderboard.html
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
