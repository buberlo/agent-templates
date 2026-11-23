# Languages

- **Domain:** `bildung`
- **Category:** `sprachen`
- **As of:** 2026-11-23

## Summary

Language learning, translation, corrections and practice dialogues.

## Recommended tool stack

- Office-/Video-Skills, Quellenpflicht

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill microsoft-office | Skill + CLI | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | docx/pptx/xlsx offline via Python CLIs (python-docx, python-pptx, openpyxl). Office app not required; PDF render only with LibreOffice. | Bundled in Hermes (~/.hermes/skills/), scripts in the skill folder. | Part of the official bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office | no (as documented) |
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | Fetch YouTube transcripts and turn them into chapters, summaries, threads, blog posts, or quotes. | Bundled; helper fetch_transcript.py uses a prepared venv (youtube extra), not raw pip into the agent env. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as documented) |

## Typical workflows

- Confirm the task, allowed tools, and definition of done.
- Read/research first, then draft, then approval for consequential steps.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-microsoft-office
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
