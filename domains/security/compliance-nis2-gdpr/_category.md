# Compliance, NIS2 and GDPR

- **Domain:** `security`
- **Category:** `compliance-nis2-gdpr`
- **As of:** 2026-11-23

## Summary

Structure requirements, TOMs, DPAs and evidence (not legal advice).

## Recommended tool stack

- Dokumenten-Skills for Verzeichnisse and Vorlagen
- Do not pass off output as legal advice

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills for creating/validating Office and PDF files; verification step (validate.py, render to PDF/PNG) is part of the instructions. | Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199,219 stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |
| Hermes skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | Offline docx/pptx/xlsx via Python CLIs (python-docx, python-pptx, openpyxl). Office app not required; PDF rendering only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp | Notion workspace for agents (pages, databases). | Claude Code docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | In the official Hermes MCP catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Ist-Zustand dokumentieren, Luecken als Fragen an Fachleute, Nachweise versionieren.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- An agent is neither a data protection officer nor a law firm.
- These templates do not include attack or bypass instructions.

## Sources

- https://github.com/anthropics/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://code.claude.com/docs/en/mcp
- https://mcp.notion.com/mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
