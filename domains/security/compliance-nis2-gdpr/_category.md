# Compliance, NIS2 and GDPR

- **Domain:** `security`
- **Category:** `compliance-nis2-gdpr`
- **As of:** 2026-11-23

## Summary

Structuring requirements, TOMs, AVVs and evidence (no legal advice).

## Recommended tool stack

- Document skills for directories and templates
- No Rechtsberatung als Output verkaufen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills |Official agent skills for creating/picking Office and PDF files; Verify step (validate.py, render to PDF/PNG) is part of the guide.|Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills.| 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office |docx/pptx/xlsx offline via Python-CLIs (python-docx, python-pptx, openpyxl). Office app not necessary; PDF render only with LibreOffice.| Bundled in Hermes (~/.hermes/skills/), Scripts im Skill-Ordner. | Teil des offiziellen Bundled catalogs. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |
| Notion MCP (hosted) | MCP | https://mcp.notion.com/mcp |Notion workspace for agents (pages, databases).| Claude-Code-Docs: claude mcp add --transport http notion https://mcp.notion.com/mcp. Hermes: hermes mcp install notion. | Im offiziellen Hermes-MCP-catalog (optional-mcps/notion). | https://code.claude.com/docs/en/mcp | no (as cited) |

## Typical workflows

- Ist-Zustand dokumentieren, Luecken als Fragen an Fachleute, evidence versionieren.

## Pitfalls

- An agent is not a data protection officer or a law firm.
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

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
