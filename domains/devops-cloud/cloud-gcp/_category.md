# Cloud: GCP

- **Domain:** `devops-cloud`
- **Kategorie:** `cloud-gcp`
- **Stand:** 2026-11-23

## Kurzbeschreibung

GCP/GKE-Ressourcen, inkl. verwalteter MCP-Endpunkte wo angeboten.

## Empfohlener Tool-Stack

- CLI (kubectl/terraform/docker) oder offizielle Cloud-MCPs, default read-only

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ mit PAT-Header (Claude-Code-Docs) oder lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| Sentry MCP | MCP | https://github.com/getsentry/sentry-mcp | Produktionsfehler, Issues und Kontext fuer Coding-Agenten. | Offizielles getsentry/sentry-mcp Repo. | 973 Stars | https://github.com/getsentry/sentry-mcp | nein (so belegt) |

## Typische Workflows

- Auftrag, erlaubte Tools und Definition of Done festlegen.
- Zuerst lesen/recherchieren, dann Entwurf, dann Freigabe fuer wirkende Schritte.
- Output gegenlesen (Datei, URL, Ticket) und Quelle angeben.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://github.com/getsentry/sentry-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
