# Desktop Automation

- **Domain:** `automation`
- **Category:** `desktop-automation`
- **As of:** 2026-11-23

## Summary

Computer-Use, OS-Automation, kontrollierte GUI-Steuerung.

## Recommended tool stack

- Hermes computer-use Skill
- OS-Automation restriktiv

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes skill computer-use | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Control desktop background-first, escalate on signal. | Bundled autonomous-ai-agents/computer-use. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| ClawHub "Desktop Control" (matagul) | Skill | https://clawhubtrends.com/leaderboard.html | Flagged with a warning on the leaderboard, verify with extra care. Flagged with a warning on the leaderboard – verify before use. | openclaw skills install (owner matagul) and openclaw skills verify. | 53,032 downloads, 335 registry stars (ClawHub leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Small, observable GUI steps; stop if anything is unclear.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Desktop-Control hat weitreichende Rechte.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
