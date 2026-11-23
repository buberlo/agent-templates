# MCP-Server bauen

- **Domain:** `ki-ops`
- **Kategorie:** `mcp-server-bau`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Eigene MCP-Server designen, implementieren und an Clients anbinden.

## Empfohlener Tool-Stack

- MCP-Spec + offizielle SDKs + mcp-builder-Skill aus Claude-Skill-Listen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| modelcontextprotocol/servers (Referenzserver) | Referenz | https://github.com/modelcontextprotocol/servers | Offizielle/Referenz-MCP-Server zum Lernen der Muster. | Repo klonen, einzelne Server laut README. | 92.179 Stars | https://github.com/modelcontextprotocol/servers | nein (so belegt) |
| mcp-builder (in awesome-claude-skills beschrieben) | Skill | https://github.com/ComposioHQ/awesome-claude-skills | Anleitung zum Bau hochwertiger MCP-Server in Python/TypeScript. | Ueber die jeweilige Skill-Installation der genutzten Plattform. | 80.108 Stars (Listen-Repo, nicht der Skill allein). | https://github.com/ComposioHQ/awesome-claude-skills | nein (so belegt) |

## Typische Workflows

- Enger Tool-Schnitt, gute Beschreibungen, Least Privilege, Tests, dann Katalog/Review (Nous merged MCPs nur per PR).

## Fallstricke

- Zu viele Tools, zu lange Schemas (Token-Overhead). Ungepruefte Community-Server.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/modelcontextprotocol/servers
- https://github.com/ComposioHQ/awesome-claude-skills
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
