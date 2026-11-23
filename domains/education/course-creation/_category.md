# Course creation

- **Domain:** `bildung`
- **Category:** `kurse-erstellen`
- **As of:** 2026-11-23

## Summary

Curriculum, generate lessons, exercises and materials.

## Recommended tool stack

- Document and slide skills
- youtube-content for Source-Material

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills to create/validate Office and PDF files; verify step (validate.py, render to PDF/PNG) is part of the guide. | Claude Code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as documented) |
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline via Python CLIs (python-docx, python-pptx, openpyxl). Office app not required; PDF render only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as documented) |
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | Fetch YouTube transcripts and turn them into chapters, summaries, threads, blog posts, or quotes. | Bundled; helper fetch_transcript.py uses a prepared venv (youtube extra), not raw pip into the agent env. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as documented) |

## Typical workflows

- Learning objectives → outline → lessons → exercises → slides; cite sources.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://github.com/anthropics/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
