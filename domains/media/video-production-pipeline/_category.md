# Video Production Pipeline

- **Domain:** `media`
- **Category:** `video-produktion-pipeline`
- **As of:** 2026-11-23

## Summary

Ende-to-Ende-Pipelines of Briefing over Cut bis Render and Export, inkl. Remotion and Studio-MCPs.

## Recommended tool stack

- Briefing → Script → Assets → Remotion or FFmpeg-Render → QA the Exporte

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatische Videos in React; Skills statt eines aelteren MCP-paths, so the gaengige Empfehlung 2026. | Skills from remotion-dev/skills according to Repo-README. | 7.841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | no (as cited) |
| FFmpeg (CLI, often without a dedicated MCP) | CLI | https://ffmpeg.org/ | Cut, convert, normalize audio, embed subtitles. Many agents call FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear leader in this research). | OS package; agent needs ffmpeg on PATH. Hermes video-analysis docs assume ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as documented) |

## Typical workflows

- for datengetriebene Videos Remotion-Skills; for Rohschnitt FFmpeg.
- Hermes Desktop Video-Analyse (Plugin) exportiert according to Drittdoku Markdown-Report, SRT and JSON-Cues – hier without eigenes Lauf-result festgehalten.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://agentos.guide/hermes-agent-video-analysis
- https://github.com/remotion-dev/skills
- https://ffmpeg.org/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
