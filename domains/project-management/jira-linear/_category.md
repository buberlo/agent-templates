# Jira, Linear, and Tickets

- **Domain:** `project-management`
- **Category:** `jira-linea r `
- **As of:** 2026-11-23

## Summary

Create issues, change status, link sprints and specifications.

## Recommended tool stack

- Linear- or Atlassian-MCP

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| linear MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear | Linear issues/projects; in the Hermes documentation as an OAuth example. | hermes mcp install linear | Nous-approved optional-mcps catalog entry (listing 11/23/2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as assigned) |
| atlassian MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian | Jira/Confluence from the Nous catalog. | hermes mcp install atlassian | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Claude code docs motivate the process feature from issue to implement and open PR (documentary example, no measured case).

## Pitfalls

- Spam an Boards durch zu aggressive Autopiloten.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine the two, don't confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
