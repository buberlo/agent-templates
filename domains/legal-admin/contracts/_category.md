# Contracts

- **Domain:** `legal-admin`
- **Category:** `contracts`
- **As of:** 2026-11-23

## Summary

Structuring contracts, highlighting clauses, comparison tables – no legal advice.

## Recommended tool stack

- Document skills for drafts; human legal review required

## MCP servers and skills

| Name | Typee | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Official agent skills for creating/checking Office and PDF files; the verify step (validate.py, render to PDF/PNG) is part of the instructions. | Claude code: /plugin marketplace add anthropics/skills and /plugin install document-skills@anthropic-agent-skills. | 199,219 stars |https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | no (as cited) |

## Typeical workflows

- Define the task, allowed tools, and definition of done.
- Read and research first, then draft, then approval for actions that take effect.
- Review output (file, URL, ticket) and cite the source.

## Pitfalls

- No legal advice; drafts must be reviewed by experts.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both, do not confuse them. Sources:https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills that the task needs. Hermes filters by include/exclude; OpenClaw has tool policies and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write any tokens or passwords in chats, skill files or command arguments of custom MCPs. Grok Bot Wiki: OAuth tokens remain on the connector backend; command servers must not contain any credentials in argv. Source:https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://github.com/anthropics/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
