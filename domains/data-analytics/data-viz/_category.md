# Data visualization

- **Domain:** `data-analytics`
- **Category:** `data-viz`
- **As of:** 2026-11-23

## Summary

Charts, Infografiken and interaktive HTML-Reports.

## Recommended tool stack

- Read-only SQL + notebooks/sheets + Firecrawl only when web data is needed

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| motherduck MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck | Analytical SQL. | hermes mcp install motherduck | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| MarkItDown | CLI / library | https://github.com/microsoft/markitdown | Convert files and Office documents to Markdown – used in skills and MCP wrappers. | Python package / repo. | 197,975 stars | https://github.com/microsoft/markitdown | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck
- https://github.com/microsoft/markitdown
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
