# Arduino and ESP32

- **Domain:** `hardware-embedded`
- **Category:** `arduino-esp32`
- **As of:** 2026-11-23

## Summary

Sketches, pinouts, flash workflows, and serial logs.

## Recommended tool stack

- Vendor CLIs, serial logs, repo files; cautious with flash/hardware

## MCP servers and skills

_No sufficiently cited category-specific tool was recorded in this research. See domain stack and source catalogs._

## Typical workflows

- Define scope, allowed tools, and definition of done.
- Read and research first, then draft, then approval before impactful steps.
- Review output (file, URL, ticket) and cite sources.

## Pitfalls

- Do not put tokens or passwords in chat, skill files, or custom MCP command argv. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not embed credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- No silent payments, trades, or transfers.
- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not conflate them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
