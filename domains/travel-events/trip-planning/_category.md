# Trip planning

- **Domain:** `travel-events`
- **Category:** `trip-planning`
- **As of:** 2026-11-23

## Summary

Itineraries, packing lists, local information, and reservation preparation.

## Recommended tool stack

- Check travel MCPs from catalogs individually; book only with explicit user approval.

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Web search via Brave Search API | Official Brave repo | 1,585 stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Calendly MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly | Dates and booking links | `hermes mcp install calendly` | Nous-approved optional-mcps catalog entry (listing 2026-11-23) | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set task, allowed tools, and definition of done.
- Read and research first, then draft, then release for effective steps.
- Reread output (file, URL, ticket) and specify the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine the two without confusing them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Activate only the MCPs/skills the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files, or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/calendly
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent