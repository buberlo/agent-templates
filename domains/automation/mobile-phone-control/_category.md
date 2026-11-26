# Mobile and Phone Control

- **Domain:** `automation`
- **Category:** `mobile-phone-control`
- **As of:** 2026-11-23

## Summary

Control Android/iOS devices (Mobilerun, mobile-mcp, OpenClaw companion).

## Recommended tool stack

- Mobilerun for echte Android-Geraete
- mobile-mcp for Sim/Apps
- OpenClaw: Gateway am Computer, App only Companion

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Mobilerun (formerly DroidRun) | CLI + MCP | https://github.com/droidrun/mobilerun | Control Android devices using natural language. Cloud MCP at docs.mobilerun.ai. | mobilerun setup, USB debugging, mobilerun ping. MCP: https://cloud.mobilerun.ai/api/mcp with Bearer key per docs. | 10,100 stars | https://docs.mobilerun.ai/mcp-server | no (as cited) |
| Mobile MCP | MCP | https://github.com/mobile-next/mobile-mcp | Control iOS and Android apps in simulators/devices via agents. | See repo README. | 10,819 stars | https://github.com/mobile-next/mobile-mcp | no (as cited) |
| OpenClaw Android App (Companion) | Companion app | https://docs.openclaw.ai/platforms/android/ | Not a gateway host. Gateway on macOS/Linux/Windows/WSL2, pairing via QR (openclaw qr). | Official app, gateway must be running. | 395,081 stars. | https://docs.openclaw.ai/platforms/android/ | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Geraet sichtbar lassen, Aktionen bestaetigen lassen wo die Plattform das verlangt.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Cloud-MCP-Keys schuetzen. Companion ist not der Agent-Host.

## Sources

- https://docs.mobilerun.ai/mcp-server
- https://github.com/mobile-next/mobile-mcp
- https://docs.openclaw.ai/platforms/android/
- https://github.com/droidrun/mobilerun
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://cloud.mobilerun.ai/api/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
