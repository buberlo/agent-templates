# Diagrams and Whiteboards

- **Domain:** `office-documents`
- **Category:** `diagramme-whiteboard`
- **As of:** 2026-11-23

## Summary

Architekturdiagramme, Excalidraw, Miro, Mermaid and Infografiken.

## Recommended tool stack

- Hermes architecture-diagram, Miro-MCP, Excalidraw when installiert

## MCP servers and skills

| Name | Type | URL | Use | Install | Popularity | Source | Unverified |
|---|---|---|---|---|---|---|---|
| Hermes-Skill architecture-diagram | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Dunkle SVG-Architektur-/Cloud-Diagramme as HTML. | Bundled creative/architecture-diagram. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | no (as cited) |
| miro MCP (Hermes-catalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/miro | Whiteboard-Kollaboration. | hermes mcp install miro | Nous-approved optional-mcps-catalog entry (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | no (as cited) |

## Typical workflows

- /architecture-diagram or vergleichbaren Slash-Command according to Hermes-Docs nutzen, HTML/SVG oeffnen.

## Pitfalls

- Skills are workflows/instructions (progressive disclosure); MCPs are connections and tools. Combine both; do not confuse them. Sources: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Enable only the MCPs/skills the task needs. Hermes filters via include/exclude; OpenClaw has tool policy and prompt budgets. Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Do not put tokens or passwords in chat, skill files, or custom MCP command arguments. Grok Bot wiki: OAuth tokens stay on the connector backend; command servers must not include credentials in argv. Source: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Write, send, pay, deploy, and delete only after explicit approval; good document skills require a verify step (re-read the file, render PDF/PNG).

## Sources

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/miro
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
