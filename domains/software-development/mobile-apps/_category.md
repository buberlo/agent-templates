# Mobile Apps

- **Domain:** `software-development`
- **Category:** `mobile-apps`
- **As of:** 2026-11-23

## Summary

iOS/Android development, device tests via mobile MCP or simulators.

## Recommended tool stack

- Device-MCP (mobile-mcp or Mobilerun) zusaetzlich zum SDK/Build

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Mobile MCP | MCP | https://github.com/mobile-next/mobile-mcp |Control iOS and Android apps in simulators/gear through agents.| Siehe Repo-README. | 10.819 Stars | https://github.com/mobile-next/mobile-mcp | no (as cited) |
| Mobilerun (ehem. DroidRun) | CLI + MCP | https://github.com/droidrun/mobilerun |Control Android devices with natural language. Cloud MCP at docs.mobilerun.ai.|mobilerun setup, USB debugging, mobilerun ping. MCP: https://cloud.mobilerun.ai/api/mcp with bearer key according to Docs.| 10.100 Stars | https://docs.mobilerun.ai/mcp-server | no (as cited) |

## Typical workflows

- UI-Flows auf Simulator/Geraet ausfuehren, Screenshots/UI-State zurueckgeben, dann Code aendern.

## Pitfalls

- USB debugging and consents. Cloud MCP keys not in git.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/mobile-next/mobile-mcp
- https://docs.mobilerun.ai/mcp-server
- https://github.com/droidrun/mobilerun
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
