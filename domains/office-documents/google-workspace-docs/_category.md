# Google Docs / Drive

- **Domain:** `office-documents`
- **Category:** `google-workspace-docs`
- **As of:** 2026-11-23

## Summary

Docs, Sheets, Slides and Drive-files over Workspace-CLI or MCP.

## Recommended tool stack

- google-workspace / gws CLI or Workspace-Connectoren (Grok Bot)

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets over gws CLI or Python. | Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| Grok Bot Google-Connectoren | Plugin/Connector | https://x.ai/bot/guides/grok-bot-101 | Grok Bot 101 nennt Gmail, Calendar, Drive u. a. over Connect Apps. | Connect Apps, Provider-Login in the documentedn Frist. | Official Produkt-Docs/Wiki. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

- Lesen and Entwuerfe bevorzugen; Senden only after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
