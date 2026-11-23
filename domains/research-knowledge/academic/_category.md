# Academic research

- **Domain:** `research-knowledge`
- **Category:** `Academic' `
- **As of:** 2026-11-23

## Summary

Search and develop papers (arXiv, Semantic Scholar, Zotero).

## Recommended tool stack

- Hermes arxiv-Skill
- grounded-citations

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill arxiv | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog |search arXiv by keyword, author, category, ID.| Bundled research/arxiv. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| Hermes-Skill grounded-citations | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Antworten auf pruefbare Quellen stuetzen. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Paper-ID or Suchanfrage → Abstract/PDF → zitierfaehige Notizen, no invented DOI.

## Pitfalls

Hallucinated citations; Open every source.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
