# Podcast

- **Domain:** `media`
- **Category:** `podcast`
- **As of:** 2026-11-23

## Summary

Podcast-Workflows: Aufnahme-Vorbereitung, Schnitt, Shownotes, Transkript and Distribution.

## Recommended tool stack

- FFmpeg-Schnitt
- Whisper or youtube-content-aehnlich for Shownotes

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, often without its own MCP) | CLI | https://ffmpeg.org/ | Editing, conversion, audio normalization, embedding subtitles. Many agents invoke FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear star leader in this research). | OS package; agent requires ffmpeg on PATH. Hermes video analysis docs require ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as cited) |
| ClawHub / OpenClaw Skill Openai Whisper (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Transcription via Whisper, a frequently installed skill according to ClawHub. | openclaw skills install (owner steipete, name Openai Whisper). | 77,380 downloads, 303 stars on ClawHub (23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |
| Hermes skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | Fetch YouTube transcripts and turn them into chapters, summaries, threads, blog posts, or quotes. | Bundled; helper fetch_transcript.py via prepared venv (youtube extra), not raw pip into the agent environment. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Transcript → chapter markers, show notes, clip lists with timestamps; publication only after approval.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://clawhubtrends.com/leaderboard.html
- https://agentos.guide/hermes-agent-video-analysis
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
