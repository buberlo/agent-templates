# Vulnerability Management

- **Domain:** `security`
- **Category:** `vuln-management`
- **As of:** 2026-11-23

## Summary

Invent and prioritize known vulnerabilities in your own systems and track patches.

## Recommended tool stack

- Semgrep/SAST im CI
- Tickets in Jira/Linear
- Only your own or authorized systems

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| semgrep MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep | Statische Befunde im Agent-Workflow. | hermes mcp install semgrep | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| atlassian MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian | Ticket-Nachverfolgung. | hermes mcp install atlassian | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| linear MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear | Ticket-Nachverfolgung. | hermes mcp install linear | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Inventory findings, prioritize them, open a patch ticket, then rescan.

## Pitfalls

- Scanner output is not automatically complete.
- Defensive, authorized use only; this collection does not include attack methods.
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
