# Obsidian

- **Domain:** `office-documents`
- **Category:** `obsidian`
- **As of:** 2026-11-23

## Summary

Lokale Vaults read, verlinken, notieren – oft as Memory-Layer.

## Recommended tool stack

- Obsidian-Skill on the lokalen Vault

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Obsidian-Skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Vault read, suchen, Notizen anlegen/edit – frequentlyer Memory-/Wissens-Layer. | Hermes bundled /obsidian. OpenClaw: ClawHub-Skill Obsidian (steipete). | ClawHub: 92.458 Downloads, 381 Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Neue Notizen with Quellenangaben; bestehende files not still viawrite.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://docs.openclaw.ai/skills/
- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/NousResearch/hermes-agent
