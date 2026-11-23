# Docker und Container

- **Domain:** `devops-cloud`
- **Kategorie:** `docker-container`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Images, Compose, Registries und Laufzeitprobleme.

## Empfohlener Tool-Stack

- Docker CLI ueber das Terminal-Tool des Agenten

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Docker CLI (agent terminal) | CLI | https://docs.docker.com/ | Standardweg fuer Build/Run/Logs in Coding- und Homelab-Agenten. | Docker Engine lokal / Remote-Host mit klarer Freigabe. | Docker selbst nicht als MCP-Star in dieser Liste gemessen. | https://github.com/punkpeye/awesome-mcp-servers | nein (so belegt) |

## Typische Workflows

- Logs und docker inspect zuerst; keine Volume-Loeschungen ohne Auftrag.

## Fallstricke

- Socket-Zugriff kann Host-weit sehr weitreichende Rechte bedeuten.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.docker.com/
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
