# CI/CD

- **Domain:** `devops-cloud`
- **Kategorie:** `cicd`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Pipelines (GitHub Actions, GitLab CI, CircleCI, Buildkite) lesen, anpassen und Fehler analysieren.

## Empfohlener Tool-Stack

- GitHub MCP/Actions, CircleCI/Buildkite aus Hermes-Katalog

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ mit PAT-Header (Claude-Code-Docs) oder lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| circleci MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/circleci | CircleCI aus dem Nous-Katalog. | hermes mcp install circleci | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| buildkite MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/buildkite | Buildkite aus dem Nous-Katalog. | hermes mcp install buildkite | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Log der failed Jobs holen, lokal reproduzieren, Fix als PR.

## Fallstricke

- Pipeline-Secrets nie in den Chat spiegeln.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/mcp
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/github/github-mcp-server
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/circleci
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/buildkite
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
