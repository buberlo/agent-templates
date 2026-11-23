"Doing" with containers

- **Domain:** `devops-cloud`
- **Category:** `docker-container`
- **As of:** 2026-11-23

## Summary

bbings have been shown to be at least the same.

## Recommended tool stack

- Docker CLI over the agent's terminal tool

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Docker CLI (agent terminal) | CLI | https://docs.docker.com/ | Standard path for build/run/logs in coding and homelab agents. | Docker Engine local / remote host with explicit approval. | Docker itself not measured as MCP star in this list. | https://github.com/punkpeye/awesome-mcp-servers | no (as documented) |

## Typical workflows

- Logs and docker inspect first; No volume releases without an order.

## Pitfalls

- Socket-Zugriff kann Host-weit sehr weitreichende Rechte bedeuten.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.docker.com/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
