# Generische MCP-Agenten

- **Domain:** `agent-platforms`
- **Kategorie:** `generic-mcp-agents`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Gemeinsames Muster: MCP für Zugriff, Tools für Aktionen, Skills für Abläufe.

## Empfohlener Tool-Stack

- MCP fuer Zugang, Tools fuer Aktionen, Skills fuer Verhalten
- Kuratierte Listen: awesome-mcp-servers, Referenzserver

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| punkpeye/awesome-mcp-servers | Katalog | https://github.com/punkpeye/awesome-mcp-servers | Grosse kuratierte Liste, zuletzt aktiv Nov 2026, Web-Directory glama.ai. | Nur als Directory nutzen, nicht als Server installieren. | 98.405 Stars | https://github.com/punkpeye/awesome-mcp-servers | nein (so belegt) |
| modelcontextprotocol/servers | Referenz | https://github.com/modelcontextprotocol/servers | Referenzimplementierungen. | Repo. | 92.179 Stars | https://github.com/modelcontextprotocol/servers | nein (so belegt) |

## Typische Workflows

- Wenige Server, Filter, Read-only defaults, Skills fuer den Ablauf, menschliche Gates fuer Writes.

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://github.com/modelcontextprotocol/servers
- https://code.claude.com/docs/en/features-overview
- https://github.com/ComposioHQ/awesome-claude-skills
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
