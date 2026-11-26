# Photo and Imaging

- **Domain:** `media`
- **Category:** `photo-imaging`
- **As of:** 2026-11-23

## Summary

Edit, convert, batch-process, and caption existing photos and graphics.

## Recommended tool stack

- Local CLIs plus agent vision
- MarkItDown/OCR when text inside the image matters

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| MarkItDown | CLI / library | https://github.com/microsoft/markitdown | Convert files and Office documents to Markdown – used in skills and MCP wrappers. | Python package / repo. | 197,975 stars | https://github.com/microsoft/markitdown | no (as cited) |
| FFmpeg (CLI, often without its own MCP) | CLI | https://ffmpeg.org/ | Editing, conversion, audio normalization, embedding subtitles. Many agents invoke FFmpeg directly via the terminal tool. Dedicated FFmpeg MCPs are fragmented (no clear star leader in this research). | OS package; agent requires ffmpeg on PATH. Hermes video analysis docs require ffmpeg on PATH. | Not evidenced as a single MCP star signal. | https://agentos.guide/hermes-agent-video-analysis | no (as cited) |

## Typical workflows

- Set the task, allowed tools, and definition of done.
- Read or research first, then draft, then request approval for any action that has effects.
- Recheck the output (file, URL, ticket) and cite the source.
- Batch-scale uniformly, then visually inspect output files.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure), MCP are connections and tools. Combine the two, not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/Skills that the task needs. Hermes filters per include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not write tokens or passwords in chat, skill files or command arguments of custom MCPs. Grok Bot wiki: OAuth tokens remain on the connector backend; Command servers must not contain credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy and delete only after explicit approval; good document skills require a verify step (read the file again, render PDF/PNG).

## Sources

- https://github.com/microsoft/markitdown
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
