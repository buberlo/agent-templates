# Codex

- **Domain:** `agent-platforms`
- **Kategorie:** `codex`
- **Stand:** 2026-11-23

## Kurzbeschreibung

OpenAI-Codex-CLI als Coding-Agent, oft von Hermes delegiert, MCP-fähig.

## Empfohlener Tool-Stack

- Codex CLI als Coding-Runtime, MCP wie andere Clients, oft von Hermes delegiert
- OpenClaw kann openclaw mcp serve oder openclaw acp in Richtung Codex nutzen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes-Skill codex | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Delegiert Features/PRs an OpenAI Codex CLI. | Bundled autonomous-ai-agents/codex. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |
| OpenClaw MCP serve / ACP | Bruecke | https://docs.openclaw.ai/cli/mcp/serve | OpenClaw als MCP-Server fuer Clients wie Codex oder Claude Code, bzw. ACP wenn OpenClaw den Coding-Runtime hostet. | openclaw mcp serve (stdio) bzw. openclaw acp. | 395.081 Stars | https://docs.openclaw.ai/cli/mcp/serve | nein (so belegt) |

## Typische Workflows

- In Hermes bleiben, Codex nur fuer die Coding-Schleife; Reviews zurueck im Orchestrator.

## Fallstricke

- Zwei Agenten mit Schreibrecht auf dasselbe Repo ohne Abstimmung.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/cli/mcp/serve
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
