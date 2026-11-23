# Agent-Orchestrierung

- **Domain:** `ki-ops`
- **Kategorie:** `agent-orchestration`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Delegation an Subagents, Claude Code/Codex, Multi-Agent-Teams und Gates.

## Empfohlener Tool-Stack

- Hermes Delegation an Claude Code/Codex
- Grok-Bot Teams/Subagents
- OpenClaw multi-agent allowlists

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skills claude-code, codex, hermes-agent | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Orchestration und Delegation, inkl. Skill der den Agenten selbst konfiguriert. | Bundled autonomous-ai-agents/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Grobe Planung im Orchestrator, Implementation im Coding-Agent, Review getrennt.

## Fallstricke

- Unkontrollierte Rekursion / Kosten. Grok Bot: seit 0.71.2 bis zu 200 Plugin-Skills (Wiki).
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
