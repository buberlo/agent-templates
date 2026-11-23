# E-Signature

- **Domain:** `office-documents`
- **Category:** `e-signatur`
- **As of:** 2026-11-23

## Summary

Signaturprozesse vorbereiten and Status in Signaturdiensten verfolgen.

## Recommended tool stack

- Anbieterspezifische MCPs einzeln verify, z. B. SignWell-Eintrag in awesome-mcp

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Bidsketch/signwell-mcp | MCP | https://github.com/Bidsketch/signwell-mcp | In awesome-mcp-servers (Workplace) as official Eintrag listed. | Siehe Repo. | Star-Zahl hier not per API pulled. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typical workflows

- only vorbereiten and Status read; Signaturausloesung rechtlich clarify.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/Bidsketch/signwell-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
