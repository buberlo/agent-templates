# YouTube-Content

- **Domain:** `media`
- **Category:** `youtube-content`
- **As of:** 2026-11-23

## Summary

Videos zusammenfassen, Kapitel create, Scripts and Kanal-Content from transcripten ableiten.

## Recommended tool stack

- youtube-content Skill
- Office-Skills when ein Deck/Blog as file gebraucht will

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill youtube-content | Skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | YouTube-transcripte holen and in Kapitel, Summary, Thread, Blog or Zitate verwandeln. | Bundled; Helper fetch_transcript.py over vorbereitetes venv (youtube extra), not rohes pip in the Agent-Env. | Bundled catalog. | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content | no (as cited) |
| ClawHub „YouTube Watcher“ (michaelgathara) | Skill | https://clawhubtrends.com/leaderboard.html | YouTube beobachten or zusammenfassen. | openclaw skills install (Owner michaelgathara) and openclaw skills verify. | 48.111 Downloads, 294 Registry-Stars (ClawHub Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | no (as cited) |

## Typical workflows

- Hermes-Reihenfolge: Transcript with --text-only --timestamps holen, leere Outputs abfangen, at >50k Zeichen chunken, Format waehlen (Default: Summary), Timestamps re-checked.
- Prompt: /youtube-content fasse VIDEO_URL as Kapitel + 8-set-Summary zusammen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content
- https://clawhubtrends.com/leaderboard.html
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
