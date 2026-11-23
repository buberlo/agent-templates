# Technical documentation

- **Domain:** `software-development`
- **Category:** `tech-docs`
- **As of:** 2026-11-23

## Summary

READMEs, API docs, architectural texts; often with Context7 against current library docs.

## Recommended tool stack

Context7 for library docs
DeepWiki for public repos
- MarkItDown

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | no (as cited) |
| MarkItDown | CLI / Bibliothek | https://github.com/microsoft/markitdown |Convert files and Office documents to Markdown – used in Skills and MCP wrappers.| Python-Paket / Repo. | 197.975 Stars | https://github.com/microsoft/markitdown | no (as cited) |
| deepwiki MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki | Oeffentliche GitHub-Repos befragen. | hermes mcp install deepwiki | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

Always drag version-specific docs, not use model for APIs.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/upstash/context7
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/microsoft/markitdown
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/deepwiki
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
