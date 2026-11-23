# E-Mail

- **Domain:** `communication`
- **Category:** `email`
- **As of:** 2026-11-23

## Summary

Employees working with Gmail/IMAP/Workspace tools.

## Recommended tool stack

- Triage-Skill + Gmail/Workspace/IMAP
- Default: Entwuerfe, kein Auto-Send

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skills email-inbox-triage and himalaya | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Prioritize inbox and safely prepare design; Himalaya for IMAP/SMTP in the terminal. | Bundled. ClawHub also has Himalaya (lamelas, 41,823 downloads) and imap-smtp-email (43,667). | ClawHub figures: leaderboard 2026-11-23. | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes-Skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs-reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets about gws CLI or inter Python. Bundled productivity/google-workspace. Bundled catalog. pays to voicing to the accounting firm for the use of the accounting system.
| Grok Bot Gmail plugin | plugin | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | Official connector, OAuth in browser, account-wide. | Connect Apps, authorize Gmail, in chat with @ hook up. | Product documentary. | https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp | no (as cited) |

## Typical workflows

- Hermes email-inbox-triage: priorisieren, sicher antworten. Himalaya wenn IMAP gewuenscht ist.
That is held in the next part of the next part.

## Pitfalls

- Send without release. PII in logs.
- Skills are workflows/instructions (progressive disclosure), MCPs are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filtersses per include/exclude; OpenClaw hass tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Don’t write any of your own or any of your own passwords in your own MCPs, Skill files, or Command arguments. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; Good document skills require a Verify step (read file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
