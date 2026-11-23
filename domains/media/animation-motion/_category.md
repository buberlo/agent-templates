# Animation and Motion

- **Domain:** `media`
- **Category:** `animation-motion`
- **As of:** 2026-11-23

## Summary

Motion Graphics, Manim, p5.js, Remotion and other programmatic animation.

## Recommended tool stack

- Remotion-Skills, Hermes manim-video / p5js / ascii-video

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatic videos in React; Skills instead of an older MCP path, according to the common recommendation 2026. | Skills from remotion-dev/skills according to Repo-README. | 7,841 Stars; Upstream Remotion 75.084 Stars | https://github.com/remotion-dev/skills | no (as cited) |
| Hermes-Skills manim-video, p5js, ascii-video | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Manim-CE-Animationen, p5.js-Sketches, ASCII-Video. | Bundled creative/. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

Create script or React component, render locally, view output.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/remotion-dev/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
