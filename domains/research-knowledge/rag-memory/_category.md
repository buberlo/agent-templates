# RAG and Memory

- **Domain:** `research-knowledge`
- **Category:** `rag-memory`
- **As of:** 2026-11-23

## Summary

Long-term memory, knowledge graphs, vault index and retrieval for agents.

## Recommended tool stack

- Plattform-Memory or mem0/Graphiti
- Obsidian/Vault als sichtbarer Store

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| mem0 | Platform / Memory Layer | https://github.com/mem0ai/mem0 | Drop-in long-term memory for agents. | See repo (SDK; verify community MCPs separately). | 69,369 stars | https://github.com/mem0ai/mem0 | no (as cited) |
| Graphiti | Knowledge Graph | https://github.com/getzep/graphiti | Real-time knowledge graph for agents; community MCP servers exist (stars significantly lower than the core repo). | Core library per repo; check maintenance status of MCP wrappers separately. | 33,021 stars | https://github.com/getzep/graphiti | no (as cited) |
| Obsidian skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Read and search vault, create/edit notes – common memory/knowledge layer. | Hermes bundled /obsidian. OpenClaw: ClawHub skill Obsidian (steipete). | ClawHub: 92,458 downloads, 381 stars (leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub "Memory Setup" (jrbobbyhansen-pixel) | Skill | https://clawhubtrends.com/leaderboard.html | Community memory setup skill; verify before use. | openclaw skills install (owner jrbobbyhansen-pixel) and openclaw skills verify. | 40,215 downloads, 122 registry stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub "Elite Longterm Memory" (nextfrontierbuilds) | Skill | https://clawhubtrends.com/leaderboard.html | Frequently installed memory skill; verify before use. | openclaw skills install (owner nextfrontierbuilds) and openclaw skills verify. | 57,040 downloads, 205 registry stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Wichtige Fakten bewusst persistieren; Memory not ungeprueft in Anweisungen uebernehmen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Community Graphiti MCPs are smaller and sometimes older – verify maintenance status.

## Sources

- https://github.com/mem0ai/mem0
- https://github.com/getzep/graphiti
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
