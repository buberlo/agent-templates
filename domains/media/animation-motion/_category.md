# Animation and Motion

- **Domain:** `media`
- **Category:** `animation-motion`
- **As of:** 2026-11-23

## Summary

Motion Graphics, Manim, p5.js, Remotion and andere programmatische Animation.

## Recommended tool stack

- Remotion-Skills, Hermes manim-video / p5js / ascii-video

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Remotion Agent Skills | Skill | https://github.com/remotion-dev/skills | Programmatic videos in React; skills instead of an older MCP path, per standard 2026 recommendations. | Skills from remotion-dev/skills per repo README. | 7,841 stars; upstream Remotion 75,084 stars | https://github.com/remotion-dev/skills | no (as cited) |
| Hermes skills manim-video, p5js, ascii-video | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Manim CE animations, p5.js sketches, ASCII video. | Bundled creative/. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Skript or React-Komponente erzeugen, lokal rendern, Output ansehen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/remotion-dev/skills
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
