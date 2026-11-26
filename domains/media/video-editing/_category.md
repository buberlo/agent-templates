# Video Editing

- **Domain:** `media`
- **Category:** `video-editing`
- **As of:** 2026-11-23

## Summary

Cut, convert, subtitle, and post-process video files, typically with FFmpeg or an agent timeline.

## Recommended tool stack

- FFmpeg on PATH and via the terminal tool
- Use a video MCP or timeline only when needed
- Remotion skills when the video is code/motion graphics

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| FFmpeg (CLI, often without its own MCP) | CLI | https://ffmpeg.org/ | Editing, conversion, audio normalization, embedding subtitles. Many agents invoke FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear star leader in this research). | OS package; agent requires ffmpeg on PATH. Hermes video analysis docs require ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as cited) |
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatic videos in React; skills instead of an older MCP path, per standard 2026 recommendations. | Skills from remotion-dev/skills per repo README. | 7,841 stars; upstream Remotion 75,084 stars | https://github.com/remotion-dev/skills | no (as cited) |
| Hermes skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | Fetch YouTube transcripts and turn them into chapters, summaries, threads, blog posts, or quotes. | Bundled; helper fetch_transcript.py via prepared venv (youtube extra), not raw pip into the agent environment. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as cited) |
| ClawHub "Video Frames" (steipete) | Skill | https://clawhubtrends.com/leaderboard.html | Extract frames from videos. | openclaw skills install (owner steipete) and openclaw skills verify. | 47,716 downloads, 119 registry stars (ClawHub leaderboard 23 Nov 2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Cut local.mp4 from time A to B, normalize audio (loudnorm), write h264+aac, verify with ffprobe.
- No MCP when a single ffmpeg command suffices – saves tokens.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- MCP tool schemas can heavily burden the context even before the first question is asked. In r/ClaudeAI, a user reported 67,000 tokens of overhead. Source: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Many FFmpeg MCP wrappers are small/fragmented; no clear star leader in this research.

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
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
