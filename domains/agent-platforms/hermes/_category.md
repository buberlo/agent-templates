# Hermes Agent (Nous Research)

- **Domain:** `agent-platforms`
- **Category:** `hermes`
- **As of:** 2026-11-23

## Summary

Skills, MCP catalog, Tool Gateway, delegation to Claude Code/Codex, local config.

## Recommended tool stack

- hermes setup / --portal
- Skills in ~/.hermes/skills
- MCP only from catalog or deliberately self-configured
- optional Delegation

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes Agent | Agent platform | https://github.com/NousResearch/hermes-agent | Skills, MCP catalog (66 optional-mcps folders counted in this research), Tool Gateway, cron, memory, delegation. | Docs Quickstart; desktop installer or CLI. hermes mcp install <name>, hermes skills install, hermes skills browse. | 265,550 stars, last push on 23 Nov 2026 (API). | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |
| Nous-approved MCP catalog | Catalog | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | Entries under optional-mcps/, disabled by default, install with card for secrets/OAuth. No community submit tier – merge via PR only. | hermes mcp picker or hermes mcp install deepwiki\ | linear\ | …. | 66 folders in optional-mcps (listing 23 Nov 2026). |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Blank Slate if you want least privilege. Otherwise recommended defaults, then selectively add MCPs.
- Slash commands per docs: /github, /youtube-content, /excalidraw.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Hermes skills with platforms: [macos] are silently skipped on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
- Sync respects local deletions; restore with hermes skills reset --restore.

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://x.com/JayQinQT/status/2120856724668133406
- https://github.com/NousResearch/hermes-agent
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
