# Agile and Kanban

- **Domain:** `project-management`
- **Category:** `agile-kanban`
- **As of:** 2026-11-23

## Summary

Board hygiene, handoffs, Definition of Done (e.g. Hermes sdlc-review).

## Recommended tool stack

- Linear/Jira/Todoist MCPs; change status only according to the ruleset

## MCP server and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| linear MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear | Linear from the Nous catalog. | hermes mcp install linear | Nous-approved optional-mcps catalog entry (listing 11/23/2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as assigned) |
| atlassian MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian | Jira/Confluence. | hermes mcp install atlassian | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set order, allowed tools and definition of done.
- First read/research, then draft, then release for effective steps.
- Proofread the output (file, URL, ticket) and specify the source.

- Board spam from overly aggressive autopilots.

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine the two, don't confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
