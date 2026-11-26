# Calendar and Scheduling

- **Domain:** `communication`
- **Category:** `calendar-scheduling`
- **As of:** 2026-11-23

## Summary

Find, schedule, and send invites for appointments; Calendly, Google Calendar, Outlook.

## Recommended tool stack

- Google Calendar via Workspace skill or Grok Bot plugin
- Calendly-MCP for Buchungslinks

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes skill google-workspace / gws CLI | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. | Bundled productivity/google-workspace. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| calendly MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly | Scheduling and invitation links. | hermes mcp install calendly | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| Grok Bot Google Calendar | Plugin | https://x.ai/bot/guides/grok-bot-101 | Named in Grok Bot 101 as a typical connector. | Connect Apps. | Product docs. | https://x.ai/bot/guides/grok-bot-101 | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Freie Slots vorschlagen, Einladung erst after Bestaetigung von Teilnehmern and Text.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Time zones (declare Europe/Vienna). Double bookings across multiple calendars.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://x.ai/bot/guides/grok-bot-101
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
