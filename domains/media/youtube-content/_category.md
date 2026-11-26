# YouTube-Content

- **Domain:** `media`
- **Category:** `youtube-content`
- **As of:** 2026-11-23

## Summary

Summarize videos, generate chapters, and derive scripts and channel content from transcripts.

## Recommended tool stack

- youtube-content Skill
- Office skills when a deck/blog is needed as a file

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | Fetch YouTube transcripts and turn them into chapters, summaries, threads, blog posts, or quotes. | Bundled; helper fetch_transcript.py via prepared venv (youtube extra), not raw pip into the agent environment. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as cited) |
| ClawHub „YouTube Watcher“ (michaelgathara) | Skill | https://clawhubtrends.com/leaderboard.html | YouTube beobachten or zusammenfassen. | openclaw skills install (Owner michaelgathara) and openclaw skills verify. | 48,111 Downloads, 294 Registry-Stars (ClawHub Leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Hermes workflow: fetch transcript with --text-only --timestamps, catch empty outputs, chunk if >50k characters, choose format (default: Summary), proofread timestamps.
- Prompt: /youtube-content fasse VIDEO_URL als Kapitel + 8-Satz-Summary zusammen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- The format examples in the skill documentation are placeholders, not real video results. Transcripts may be disabled.

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
