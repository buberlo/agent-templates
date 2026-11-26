# Secrets Management

- **Domain:** `security`
- **Category:** `secrets-management`
- **As of:** 2026-11-23

## Summary

Recognize secrets, rotate, stay out of chats and keep them in vaults.

## Recommended tool stack

- Secret-Scanner, Vault, nie Chat als Speicher

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Policy: no secrets in the prompt | Practice rule | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Grok Bot wiki: no keys in custom MCP arguments; tokens stay on the connector backend. | Process, no install. | n/a | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

- Leak gefunden → rotieren, aus Git entfernen, Scanner in CI.

## Pitfalls

- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
