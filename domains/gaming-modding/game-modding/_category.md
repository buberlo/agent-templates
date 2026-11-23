# Game modding

- **Domain:** `gaming-modding`
- **Category:** `game-modding`
- **As of:** 2026-11-23

## Summary

Develop or configure mods where legal for owned/permitted games.

## Recommended tool stack

- Legal owned/permitted content only; no piracy tools

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| unreal-engine MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine | Unreal Engine from the Nous catalog when relevant. | hermes mcp install unreal-engine | Nous-approved optional-mcps catalog entry (listing 2026-11-23). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Define scope, allowed tools, and definition of done.
- Read and research first, then draft, then approval before impactful steps.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine
