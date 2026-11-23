# Audio Editing

- **Domain:** `media`
- **Category:** `audio-editing`
- **As of:** 2026-11-23

## Summary

Cut, normalize, mix, and convert audio with FFmpeg, DAW-style CLIs, or MCP wrappers.

## Recommended tool stack

- FFmpeg for cut/normalize
- Whisper skill for transcripts

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, often without a dedicated MCP) | CLI | https://ffmpeg.org/ | Cut, convert, normalize audio, embed subtitles. Many agents call FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear leader in this research). | OS package; agent needs ffmpeg on PATH. Hermes video-analysis docs assume ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as documented) |
| ClawHub / OpenClaw Skill Openai Whisper (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Transcription via Whisper; according to ClawHub, a frequently installed skill. | openclaw skills install (Owner steipete, Name Openai Whisper). | 77.380 Downloads, 303 Stars on ClawHub (23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Extract audio, loudnorm, then transcribe.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://agentos.guide/hermes-agent-video-analysis
- https://ffmpeg.org/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
