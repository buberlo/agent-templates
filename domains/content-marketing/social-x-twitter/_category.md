# Social: X / Twitter

- **Domain:** `content-marketing`
- **Category:** `social-x-twitter`
- **As of:** 2026-11-23

## Summary

Research, drafts, threads, and publishing via xurl, X MCP, or similar CLIs.

## Recommended tool stack

- xurl skill (Hermes) or official X APIs of the respective platform
- Humanizer to avoid an AI tone

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes skill xurl | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | X/Twitter via the xurl CLI: search, posting, DMs, media. | Bundled social-media/xurl. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub "Humanizer" (biostartechnology) | Skill | https://clawhubtrends.com/leaderboard.html | Make texts less formulaic; also bundled in Hermes as humanizer. | openclaw skills install (owner biostartechnology) and openclaw skills verify. | 105,439 downloads, 601 registry stars (ClawHub leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Research, show draft, post only after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Automatic posting without a gate often violates the intended process and platform rules.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
