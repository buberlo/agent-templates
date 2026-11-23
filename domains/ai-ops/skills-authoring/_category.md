# Skills authoring

- **Domain:** `ai-ops`
category: skills-authoring
- **As of:** 2026-11-23

## Summary

Write, test and publish SKILL.md according to Agent Skills standard.

## Recommended tool stack

- SKILL.md according to agent skills standard
OpenClaw Workshop with Proposal Review
Hermes Skill-Dirs

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
--------------------------------------------------------------------------------------------------------------------------------------------------
| Agent Skills Standard / Anthropic skills repo | Standard + Examples | https://github.com/anthropics/skills | Frontmatter name/description, progressive disclosure, optional scripts/references. | Marketplace add / Copy to ~/.claude/skills or ~/.hermes/skills or OpenClaw skills. | 199.219 Stars | https://code.claude.com/docs/en/skills/ | no (as cited) |
| OpenClaw Skill Workshop | Platform Feature | https://docs.openclaw.ai/skills/ | Agent designs PROPOSAL.md, human reviewed and openclaw skills workshop apply. | Feature set described among others in 2026.6.1 guides; Check commands in the current CLI. | 395.081 Stars | https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1 | no (as cited) |

Typical workflows

- Short description (OpenClaw calculates about 24 tokens plus fields per skill). Body load only when necessary.
- Workshop: create → evaluate → apply, never write silently on SKILL.md.

## Pitfalls

- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html https://docs.openclaw.ai/skills/
- Hermes skills with platforms: [macos] are skipped silently on Linux. Source: https://x.com/JayQinQT/status/2120856724668133406
- Too long descriptions blow the skills prompt budget.
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine both, not confuse. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://code.claude.com/docs/en/skills/
- https://docs.openclaw.ai/skills/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://github.com/anthropics/skills
- https://www.elegantsoftwaresolutions.com/blog/openclaw-skill-workshop-power-user-guide-2026-6-1
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
