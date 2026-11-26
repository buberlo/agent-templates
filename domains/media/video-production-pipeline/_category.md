# Video Production Pipeline

- **Domain:** `media`
- **Category:** `video-production-pipeline`
- **As of:** 2026-11-23

## Summary

End-to-end pipelines from briefing through editing to rendering and export, including Remotion and studio MCPs.

## Recommended tool stack

- Briefing → Script → Assets → Remotion or FFmpeg-Render → QA der Exporte

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatic videos in React; skills instead of an older MCP path, per standard 2026 recommendations. | Skills from remotion-dev/skills per repo README. | 7,841 stars; upstream Remotion 75,084 stars | https://github.com/remotion-dev/skills | no (as cited) |
| FFmpeg (CLI, often without its own MCP) | CLI | https://ffmpeg.org/ | Editing, conversion, audio normalization, embedding subtitles. Many agents invoke FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear star leader in this research). | OS package; agent requires ffmpeg on PATH. Hermes video analysis docs require ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Remotion skills for data-driven videos; FFmpeg for rough cuts.
- According to third-party documentation, Hermes Desktop video analysis (plugin) exports a Markdown report, SRT, and JSON cues – recorded here without an independent test run.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).
- 2026 secondary sources recommend Remotion skills over an older MCP path.

## Sources

- https://agentos.guide/hermes-agent-video-analysis
- https://github.com/remotion-dev/skills
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
