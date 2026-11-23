#RAG and Memory

- **Domain:** `research-knowledge`
- **Category:** `rag-memory`
- **As of:** 2026-11-23

## Summary

Long-term memory, knowledge graphs, vault index and retrieval for agents.

## Recommended tool stack

- Plattform-Memory or mem0/Graphiti
- Obsidian/Vault als sichtbarer Store

## MCP Server and Skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| mem0 | Plattform / Memory-Layer | https://github.com/mem0ai/mem0 |Drop-in long-term memory for agents.| Siehe Repo (SDK; Community-MCPs separat verify). | 69.369 Stars | https://github.com/mem0ai/mem0 | no (as cited) |
| Graphiti | Knowledge Graph | https://github.com/getzep/graphiti |Real-time knowledge graph for agents; Community MCP servers exist (stars significantly smaller than the core repo).| Kernbibliothek laut Repo; MCP-Wrapper separat auf Pflegezustand verify. | 33.021 Stars | https://github.com/getzep/graphiti | no (as cited) |
| Obsidian-Skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Vault lesen, suchen, Notizen anlegen/editieren – haeufiger Memory-/Wissens-Layer. | Hermes bundled /obsidian. OpenClaw: ClawHub-Skill Obsidian (steipete). | ClawHub: 92.458 Downloads, 381 Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub „Memory Setup“ (jrbobbyhansen-pixel) | Skill | https://clawhubtrends.com/leaderboard.html | Community-Memory-Setup-Skill; vor Nutzung verify. |Openclaw Skills Install (Owner Jrbobbyhansen Pixel) and Openclaw Skills Verify.| 40.215 Downloads, 122 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| ClawHub „Elite Longterm Memory“ (nextfrontierbuilds) | Skill | https://clawhubtrends.com/leaderboard.html | Haeufig installiertes Memory-Skill; vor Nutzung verify. |openclaw skills install (Owner nextfrontierbuilds) and openclaw skills verify.| 57.040 Downloads, 205 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Important facts consciously persist; Do not take memory unchecked in instructions.

## Pitfalls

- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- Community Graphiti MCPs are smaller and partly older - state of care check.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/mem0ai/mem0
- https://github.com/getzep/graphiti
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
