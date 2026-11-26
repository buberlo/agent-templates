# Outreach

- **Domain:** `sales-crm`
- **Category:** `outreach`
- **As of:** 2026-11-23

## Summary

Draft personalized 1:1 outreach via email, LinkedIn or sequencer and send after approval.

## Recommended tool stack

- E-Mail-Draft-Tools + CRM
- No bulk sending from the agent without policy

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skills email-inbox-triage and himalaya | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Prioritize the inbox and prepare drafts safely; Himalaya for IMAP/SMTP in the terminal. | Bundled. ClawHub also lists Himalaya (lamelas, 41,823 downloads) and imap-smtp-email (43,667). | ClawHub figures: leaderboard 23 Nov 2026. | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. | Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| attio MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM context. | hermes mcp install attio | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Personalization based on verified facts, draft in CRM/Gmail draft, human sends.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
