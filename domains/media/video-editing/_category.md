# Video Editing

- **Domain:** `media`
- **Category:** `video-editing`
- **As of:** 2026-11-23

## Summary

Cut, convert, subtitle, and post-process video files, typically with FFmpeg or an agent timeline.

## Recommended tool stack

- FFmpeg on PATH and over the Terminal-Tool
- only at Bedarf ein Video-MCP or eine Timeline
- Remotion-Skills when the Video Code/Motion Graphics is

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, often without a dedicated MCP) | CLI | https://ffmpeg.org/ | Cut, convert, normalize audio, embed subtitles. Many agents call FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear leader in this research). | OS package; agent needs ffmpeg on PATH. Hermes video-analysis docs assume ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as documented) |
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatische Videos in React; Skills statt eines aelteren MCP-paths, so the gaengige Empfehlung 2026. | Skills from remotion-dev/skills according to Repo-README. | 7.841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | no (as cited) |
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | YouTube-transcripte holen and in Kapitel, Summary, Thread, Blog or Zitate verwandeln. | Bundled; Helper fetch_transcript.py over vorbereitetes venv (youtube extra), not rohes pip in the Agent-Env. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as cited) |
| ClawHub „Video Frames“ (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Frames from Videos ziehen. | openclaw skills install (Owner steipete) and openclaw skills verify. | 47.716 Downloads, 119 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Schneide local.mp4 of Zeit A bis B, normalisiere Audio (loudnorm), schreibe h264+aac, pruefe with ffprobe.
- no MCP, when ein einziges ffmpeg-Kommando reicht – spart Tokens.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://agentos.guide/hermes-agent-video-analysis
- https://github.com/remotion-dev/skills
- https://clawhubtrends.com/leaderboard.html
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
