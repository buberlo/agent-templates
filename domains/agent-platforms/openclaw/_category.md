# OpenClaw

- **Domain:** `agent-platforms`
- **Category:** `openclaw`
- **As of:** 2026-11-23

## Summary

Gateway, ClawHub, Skill Workshop, MCP, Android-Companion, Skill-Verify.

## Recommended tool stack

- Gateway on the computer
- Skills from workspace/ClawHub with verification
- MCP under mcp.servers + tool policy
- Companion-Apps not als Host missverstehen

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| OpenClaw | Agent platform | https://github.com/openclaw/openclaw | Self-hosted gateway, skills, plugins, MCP, channels, Android companion. | Docs at docs.openclaw.ai; CLI openclaw skills\ | mcp\ | plugins. | 395,081 stars (API 23 Nov 2026). |
| ClawHub | Registry | https://github.com/openclaw/clawhub | Public skill and plugin registry, semver, downloads, security scan summaries, openclaw skills verify. | openclaw skills install @owner/skill, openclaw plugins install clawhub:<pkg>, optional npm i -g clawhub for publishing. | 9,559 stars; site clawhub.ai / docs. | https://docs.openclaw.ai/clawhub | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Skill Workshop for neue Prozeduren (Proposal review). MCP add in Settings or CLI. Android per QR an bestehendes Gateway koppeln.
- Prompt budget: OpenClaw truncates skill descriptions when skills.limits.maxSkillsPromptChars is reached.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Loading order can prioritize workspace skills over bundled ones.
- Older .clawdhub metadata is no longer read (renamed to .clawhub).
- Leaderboard-Eintraege with Warnmarkierung and extrem wenigen Registry-Stars trotz hoher Downloads besonders kritisch sehen.

## Sources

- https://docs.openclaw.ai/
- https://docs.openclaw.ai/skills/
- https://docs.openclaw.ai/clawhub
- https://docs.openclaw.ai/tools/mcp
- https://docs.openclaw.ai/platforms/android/
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://www.paloaltonetworks.com/blog/security-operations/clawhavoc-ai-agent-skills-poisoning/
- https://github.com/openclaw/openclaw
- https://github.com/openclaw/clawhub
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
