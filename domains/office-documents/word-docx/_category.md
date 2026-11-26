# Word / DOCX

- **Domain:** `office-documents`
- **Category:** `word-docx`
- **As of:** 2026-11-23

## Summary

Generate and verify reports, letters and templates as .docx.

## Recommended tool stack

- Anthropic docx-Skill or Hermes microsoft-office
- Immer validieren and after PDF/JPEG rendern

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills for creating/validating Office and PDF files; verification step (validate.py, render to PDF/PNG) is part of the instructions. | Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199,219 stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |
| Hermes skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | Offline docx/pptx/xlsx via Python CLIs (python-docx, python-pptx, openpyxl). Office app not required; PDF rendering only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as cited) |
| MarkItDown | CLI / library | https://github.com/microsoft/markitdown | Convert files and Office documents to Markdown – used in skills and MCP wrappers. | Python package / repo. | 197,975 stars | https://github.com/microsoft/markitdown | no (as cited) |
| ClawHub „Word / DOCX“ (ivangdavila) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Skill for Word. | openclaw skills install (Owner ivangdavila) and openclaw skills verify. | 72,207 Downloads, 322 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Explicitly load skill. After writing: validate.py / docx_validate.py, soffice to PDF, pdftoppm, inspect images.
- Do not sum table widths (DXA) beyond the text area.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Default page size A4 in the docx skill. A green validation is not visual proof.

## Sources

- https://github.com/anthropics/skills
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://clawhubtrends.com/leaderboard.html
- https://github.com/microsoft/markitdown
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
