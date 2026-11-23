# Mobile and Phone Control

- **Domain:** `automation`
category: mobile-phone-control
- **As of:** 2026-11-23

## Summary

Control Android/iOS devices (Mobilerun, mobile-mcp, OpenClaw-Companion).

## Recommended tool stack

Mobile run for real Android devices
Mobile mcp for Sim/Apps
- OpenClaw: Gateway on the computer, app only Companion

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|--------------------------------------------------------------------------------------------------
| Mobilerun (ehem. DroidRun) | CLI + MCP | https://github.com/droidrun/mobilerun | Control Android devices with natural language. Cloud MCP at docs.mobilerun.ai. | mobilerun setup, USB debugging, mobilerun ping. MCP: https://cloud.mobilerun.ai/api/mcp with bearer key according to Docs. | 10.100 Stars | https://docs.mobilerun.ai/mcp-server | no (as cited) |
| Mobile MCP | MCP | https://github.com/mobile-next/mobile-mcp | iOS and Android apps in simulators/gear controlled by agents. | See Repo-README. | 10.819 Stars | https://github.com/mobile-next/mobile-mcp | no (as cited) |
| OpenClaw Android App (Companion) | Companion App | https://docs.openclaw.ai/platforms/android/ | No gateway host. Gateway on macOS/Linux/Windows/WSL2, pairing via QR (openclaw qr). | Official app, Gateway must run. 395,081 Stars. | https://docs.openclaw.ai/platforms/android/ | no (as cited) |

Typical workflows

- Leave Geraet visible, let actions confirm where the platform demands it.

## Pitfalls

Protect cloud MCP keys. Companion is not the agent host.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://docs.mobilerun.ai/mcp server
- https://github.com/mobile-next/mobile-mcp
- https://docs.openclaw.ai/platforms/android/
- https://github.com/droidrun/mobilerun
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
