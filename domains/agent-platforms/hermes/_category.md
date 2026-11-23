# Hermes Agent (Nous Research)

- **Domain:** `agent-platforms`
- **Category:** Hermes `
- **As of:** 2026-11-23

## Summary

Skills, MCP-catalog, Tool Gateway, Delegation an Claude Code/Codex, lokale Config.

## Recommended tool stack

- hermes setup / --portal
- Skills in ~/.hermes/skills
- MCP nur aus catalog or bewusst selbst
- optional Delegation

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|

| Hermes Agent | Agent-Plattform | https://github.com/NousResearch/hermes-agent | Skills, MCP-catalog (66 optional-mcps-Ordner in dieser Recherche gezaehlt), Tool Gateway, Cron, Memory, Delegation. | Docs Quickstart; Desktop-Installer or CLI. hermes mcp install <name>, hermes skills install, hermes skills browse. | 265.550 Stars, letzter Push am 23.11.2026 (API). | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | no (as cited) |
| Nous-approved MCP-catalog | catalog | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp |Entry under optional mcps/, disabled by default, installation with map for Secrets/OAuth. No community submit tier – only merge via PR.| hermes mcp Picker or hermes mcp install deepwiki\|linear\|…. | 66 Ordner in optional-mcps (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Blank Slate wenn man Least Privilege will. Sonst empfohlene Defaults, dann gezielt MCPs dazu.
- Slash-Commands laut Docs: /github, /youtube-content, /excalidraw.

## Pitfalls

- Hermes skills with platforms: [macos] are skipped silently on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://docs.openclaw.ai/skills/
- Sync respects local deletions; Restore with Hermes Skills reset --restore.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://x.com/JayQinQT/status/2120856724668133406
- https://github.com/NousResearch/hermes-agent
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
