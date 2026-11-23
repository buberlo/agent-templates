# Forensics (authorized only)

- **Domain:** `security`
- **Category:** `forensics`
- **As of:** 2026-11-23

## Summary

high altitude to forensic tool categories; no instructions for circumvention or exploitation.

> No Methodik, no Umgehungsanleitungen.

## Recommended tool stack

- Not subject to detailed procedures in this collection

## MCP servers and skills

In this search, no specific, sufficiently proven tool entry for the category was recorded. See domain stack and source catalogues.  

## Typical workflows

- Nur in autorisierten Verfahren durch zustaendige Stellen; hier no Methodik.

## Pitfalls

- No forensischen Angriffs- or Umgehungsverfahren in dieser Datei.
- No Angriffs- or Umgehungsanleitungen in diesen Templates.
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not pass credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills are workflows/instructions (progressive disclosure); MCP servers are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
