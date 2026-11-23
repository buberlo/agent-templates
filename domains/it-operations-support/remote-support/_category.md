# Remote support

- **Domain:** `it-operations-support`
- **Category:** `remote-support`
- **As of:** 2026-11-23

## Summary

Remote maintenance with consent, e.g., MeshCentral, plus clear consent and visibility.

## Recommended tool stack

- MeshCentral or a similar remote tool with express consent
- MCP only with scoped, expiring token

## MCP servers and skills

| Name | Typee | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| meshcentral-mcp (EynaExp) | MCP | https://github.com/EynaExp/meshcentral-mcp | Community MCP for MeshCentral: List devices, commands, power actions. Very low star signal – check before production. Only with consent and a scoped token. | See repo. | 5 stars |https://github.com/EynaExp/meshcentral-mcp | no (as cited) |
| Tailscale (Netzwerkpfad) | Netzwerk / Docs | https://tailscale.com/docs/develop-with-ai | Tailscale docs describe AI-assisted doc connections. MeshCentral over Tailscale is described in community discussions. This is a network path, not a hidden remote. | Tailscale on the admin and server side. | meshcentral-mcp only has 5 stars – experimental. |https://tailscale.com/docs/develop-with-ai | no (as cited) |

## Typeical workflows

- Before each session: Inform users, make the session visible, log commands.
- No resetting/updating firmware on third-party devices without an order.

## Pitfalls

- A 5-star Community MCP is not a production standard. Always Consent.
- Remote access only with consent and a visible session.
- Do not write tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not put credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, do not confuse them. Sources:https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources:https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/EynaExp/meshcentral-mcp
- https://tailscale.com/docs/develop-with-ai
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
