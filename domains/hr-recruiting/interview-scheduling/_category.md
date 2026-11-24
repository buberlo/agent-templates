# Interview scheduling

- **Domain:** `hr-recruiting`
- **Category:** `interview-scheduling`
- **As of:** 2026-11-24

## Summary

Coordinate panel and candidate availability, propose interview slots, and prepare invite copy. Calendar invites are sent by humans after approval.

## Recommended tool stack

- Google Calendar or Google Workspace MCP (read availability)
- Document skills for recap emails and interview packets

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| google_workspace_mcp | MCP | https://github.com/taylorwilsdon/google_workspace_mcp | Calendar free-busy and event draft | User OAuth via MCP server | Active community server (listing 2026-11-24). | https://github.com/taylorwilsdon/google_workspace_mcp | no (as cited) |
| calendly MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly | External scheduling links when policy allows | hermes mcp install calendly | Nous optional MCP entry | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Define participants, time zones, duration, and interview loop stages.
- Read calendars; propose slots; human sends invites.
- Capture proposed slots in a table with backup options.

## Pitfalls

- Creating calendar events without candidate consent leaks internal attendee lists.
- Ignoring holidays in panel members' locales produces impossible slots.
- Do not share one scheduling link that exposes all internal calendar details.

## Sources

- https://github.com/taylorwilsdon/google_workspace_mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly