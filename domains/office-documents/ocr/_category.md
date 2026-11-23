# OCR

- **Domain:** `office-documents`
- **Category:** `ocr`
- **As of:** 2026-11-23

## Summary

Text from Scans, Fotos and gescannten PDFs erkennen.

## Recommended tool stack

- pdf-Skill-OCR, MarkItDown

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill pdf | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Create, read, merge, fill, OCR, and edit PDF text. | Bundled: productivity/pdf. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills for creating/checking Office and PDF files; the verify step (validate.py, render to PDF/PNG) is part of the instructions. | Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |
| MarkItDown | CLI / Bibliothek | https://github.com/microsoft/markitdown | files and Office-Dokumente after Markdown wandeln – will in Skills and MCP-Wrappern genutzt. | Python-Paket / Repo. | 197.975 Stars | https://github.com/microsoft/markitdown | no (as cited) |

## Typical workflows

- Scan → OCR → review the image, especially numbers and proper names.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/anthropics/skills
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://github.com/microsoft/markitdown
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
