# Persoenliche Termine

- **Domain:** `personal-lifestyle`
- **Category:** `personal-appointments`
- **As of:** 2026-11-23

## Summary

Doctor, Government, private Kalender – with reminders and Unterlagen.

## Recommended tool stack

- Kalender, listn, lokale files; Einkaeufe not still ausloesen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets over gws CLI or Python. | Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Define assignment, allowed tools, and definition of done.
- Read/research first, then draft, then approval for actions with side effects.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
