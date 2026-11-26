# Skills authoring

- **Domain:** `ai-ops`
- **Category:** `skills-authoring`
- **As of:** 2026-11-23

## Summary

Write, test, and publish SKILL.md according to the Agent Skills standard.

## Recommended tool stack

- SKILL.md after Agent-Skills-Standard
- OpenClaw Workshop with Proposal-Review
- Hermes Skill-Dirs

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Agent Skills Standard / Anthropic skills repo | Standard + Beispiele | https://github.com/anthropics/skills | Frontmatter name/description, progressive disclosure, optionale scripts/references. | Marketplace add / Kopie after ~/.claude/skills or ~/.hermes/skills bzw. OpenClaw skills/. | 199,219 Stars | https://code.claude.com/docs/en/skills/ | no (as cited) |
| OpenClaw Skill Workshop | Platform feature | https://docs.openclaw.ai/skills/ | Agent drafts PROPOSAL.md, human reviews and runs openclaw skills workshop apply. | Feature set described in 2026.6.1 guides among others; verify commands in the current CLI. | 395,081 stars | https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1 | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Short description (OpenClaw estimates approx. 24 tokens plus fields per skill). Load body only when needed.
- Workshop: create → evaluate → apply, never allow silent writes to SKILL.md.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Hermes skills with platforms: [macos] are silently skipped on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
- Zu lange Descriptions sprengen das Skills-Prompt-Budget.

## Sources

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/anthropics/skills
- https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://x.com/JayQinQT/status/2120856724668133406
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
