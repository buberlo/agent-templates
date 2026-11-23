# Excel / XLSX

- **Domain:** `office-documents`
- **Category:** `excel-xlsx`
- **As of:** 2026-11-23

## Summary

Tabellen, Formeln, Charts and Datenbereinigung in Arbeitsmappen.

## Recommended tool stack

- Anthropic xlsx-Skill or Hermes xlsx-CLIs
- Formeln after Open or xlsx_recalc verify

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills for creating/checking Office and PDF files; the verify step (validate.py, render to PDF/PNG) is part of the instructions. | Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline over Python-CLIs (python-docx, python-pptx, openpyxl). Office-App not required; PDF-Render only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), Scripts in the skill folder. | Part of the official Bundled-Katalogs. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |
| ClawHub „Excel / XLSX“ (ivangdavila) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Skill for Excel. | openclaw skills install (Owner ivangdavila) and openclaw skills verify. | 65.403 Downloads, 259 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Daten and Formeln trennen; after the Write Sheets re-checked (xlsx_read.py).

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://github.com/anthropics/skills
- https://clawhubtrends.com/leaderboard.html
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
