# Outreach

- **Domain:** `sales-crm`
- **Category:** `outreach`
- **As of:** 2026-11-23

## Summary

Draft personalized 1:1 messages via email, LinkedIn or Sequencer and send them once approved.

## Recommended tool stack

- E-Mail-Draft-Tools + CRM
- No bulk mailing from the agent without a policy

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
|Hermes skills: email inbox triage and Himalaya| Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |Prioritize your inbox and prepare drafts securely; Himalaya for IMAP/SMTP in the terminal.|Bundled. ClawHub also has Himalaya (lamelas, 41,823 downloads) and imap-smtp-email (43,667).| ClawHub figures: Leaderboard 23.11.2026. | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.| Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| attio MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio | CRM-Kontext. | hermes mcp install attio | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Personalization based on established facts, draft in CRM/Gmail Draft, human sends.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, don't confuse them. Sources: URL0 , URL1
- Only activate the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: URL0 , URL1
- Do not write any tokens or passwords in chats, skill files, or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: URL0
- Writing, sending, paying, deploying and deleting only after explicit approval; good document skills require a verification step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/attio
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
