# Property listings

- **Domain:** `real-estate`
- **Category:** `exposes `
- **As of:** 2026-11-23

## Summary

Create exposés and short object profiles or extract from sources.

## Recommended tool stack

- Search and document tools, no automatic binding offers

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Brave Search MCP | MCP | https://github.com/brave/brave-search-mcp-server | Websuche via Brave Search API. | Offizielles Brave-Repo. | 1.585 Stars | https://github.com/brave/brave-search-mcp-server | no (as cited) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office |docx/pptx/xlsx offline via Python-CLIs (python-docx, python-pptx, openpyxl). Office app not necessary; PDF render only with LibreOffice.| Bundled in Hermes (~/.hermes/skills/), Scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |

## Typical workflows

- Set task, allowed tools and definition of done.
- First read/research, then draft, then release for effective steps.
- Reread output (file, URL, ticket) and specify source.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/brave/brave-search-mcp-server
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
