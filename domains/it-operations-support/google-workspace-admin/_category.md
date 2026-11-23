# Google Workspace admin

- **Domain:** `it-operations-support`
- **Category:** `google-workspace-admin`
- **As of:** 2026-11-23

## Summary

Directory, groups, policies and workspace admin tasks.

## Recommended tool stack

- gws CLI/Google Workspace skill for content; admin APIs separated and strictly authorised

## MCP servers and skills

| Name | Typee | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. | Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typeical workflows

- Output directory changes as a plan; do not execute without an order.

## Pitfalls

- A user OAuth is not a super admin.
- Remote access only with consent and a visible session.
- Do not write any tokens or passwords in chats, skill files or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain any credentials in argv. Source:https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, do not confuse them. Sources:https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources:https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
