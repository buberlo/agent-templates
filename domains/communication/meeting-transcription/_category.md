# Meetings and Transcription

- **Domain:** `communication`
- **Category:** `meeting-transcription`
- **As of:** 2026-11-23

## Summary

Transcribe meetings, extract decisions and action items, draft follow-ups.

## Recommended tool stack

- Fireflies catalog MCP or Whisper
- Hermes meeting-action-items / teams-meeting-pipeline

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| ClawHub / OpenClaw Skill Openai Whisper (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Transcription via Whisper, a frequently installed skill according to ClawHub. | openclaw skills install (owner steipete, name Openai Whisper). | 77,380 downloads, 303 stars on ClawHub (23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes-Skills meeting-action-items, teams-meeting-pipeline | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Action items with owner/quote; Teams meeting summaries. | Bundled productivity/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| fireflies MCP (Hermes catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies | Meeting transcripts via Fireflies. | hermes mcp install fireflies | Nous-approved optional-mcps catalog entry (listing 23 Nov 2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Transkript → Entscheidungen, Owner, Deadlines, zitiert; Mails only als Draft.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- Aufzeichnungseinwilligung. Halluzinierte Beschluesse.

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://clawhubtrends.com/leaderboard.html
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/fireflies
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
