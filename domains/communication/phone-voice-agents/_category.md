# Telefon and Voice-Agents

- **Domain:** `communication`
- **Category:** `phone-voice-agents`
- **As of:** 2026-11-23

## Summary

Outbound/inbound calls via voice agent platforms, transcripts, and post-processing.

## Recommended tool stack

- Evaluate specialized platforms separately
- Twilio docs MCP in the Hermes catalog is documentation, not automatically a dialer

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| twilio-docs MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs | Twilio documentation, not to be implicitly equated with a production calling agent. | hermes mcp install twilio-docs | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |
| ClawHub "Agent Phone Call" (mrsz) | Skill | https://clawhubtrends.com/leaderboard.html | Flagged with a warning on the leaderboard, only 8 registry stars despite high downloads. Flagged with a warning on the leaderboard – verify before use. | openclaw skills install (owner mrsz) and openclaw skills verify. | 72,476 downloads, 8 registry stars (ClawHub leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Clarify call content and consent; comply with recording regulations.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Verify ClawHub skills before use (`openclaw skills verify`). In February 2026, Koi Security audited 2,857 registry skills and classified 341 as malicious (approx. 12%). Sources: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Warnmarkierte ClawHub-Skills not ungeprueft laden.

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/twilio-docs
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
