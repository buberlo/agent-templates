# Image Generation

- **Domain:** `media`
- **Category:** `image-generation`
- **As of:** 2026-11-23

## Summary

Generative Bilder over Modell-APIs, ComfyUI or eingebaute Image-Tools the Agent-Plattform.

## Recommended tool stack

- Plattform-eigene Image-Tools (z. B. Hermes Tool Gateway) or Comfy/Cloud-MCPs

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| comfy-cloud MCP (Hermes-catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud | Comfy-Cloud from the Nous-MCP-catalog. | hermes mcp install comfy-cloud | Nous-approved optional-mcps-catalog entry (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| cloudinary MCP (Hermes-catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudinary | Medien-Assets over Cloudinary. | hermes mcp install cloudinary | Nous-approved optional-mcps-catalog entry (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| ClawHub „Nano Banana Pro“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Bild-/Generative-Skill on ClawHub. | openclaw skills install (Owner steipete) and openclaw skills verify. | 95.115 Downloads, 381 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Prompt + Format + Markenfarben; Ausgabe dateibasiert verify.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/comfy-cloud
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/cloudinary
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
