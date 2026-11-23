# Desktop Automation

- **Domain:** `automation`
category: Desktop Automation `
- **As of:** 2026-11-23

## Summary

Computer use, OS automation, controlled GUI control.

## Recommended tool stack

Hermes computer-use skill
OS automation restrictive

MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Hermes-Skill computer-use | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Desktop background-first control, escalate at signal. Bundled autonomous-ai-agents/computer-use. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub “Desktop Control” (matagul) | Skill | https://clawhubtrends.com/leaderboard.html | Verify in the leaderboard with warning marking, especially carefully. In the leaderboard with warning marking – verify before use. | openclaw skills install (Owner matagul) and openclaw skills verify. | 53,032 downloads, 335 registry stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

Typical workflows

- Small, observable GUI steps; stop in case of uncertainty.

## Pitfalls

- Check ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and rated 341 as defective (about 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
Desktop control has extensive rights.
Activate only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a Verify step (re-read file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
