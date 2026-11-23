# Git und GitHub

- **Domain:** `software-entwicklung`
- **Kategorie:** `git-github`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Commits, Branches, PRs, Issues über gh CLI oder offiziellen GitHub-MCP.

## Empfohlener Tool-Stack

- gh CLI (Skill) und/oder Official GitHub MCP
- Read-only wo moeglich

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ mit PAT-Header (Claude-Code-Docs) oder lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| Hermes-Skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | GitHub ueber die gh-CLI: PRs, Issues, Reviews, Repos, Auth. Auf ClawHub ist Github (steipete) eines der meistinstallierten Skills. | Hermes: bundled (/github). OpenClaw: openclaw skills install aus ClawHub (Owner steipete). | ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Auth einmalig (gh auth login), dann PRs/Issues ueber das Skill. Community-Tipp: Read-only-URLs des GitHub-Servers nutzen.

## Fallstricke

- Fine-grained PAT nur auf noetige Repos. Kein Token in argv bei Grok-Bot-Command-MCPs.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/mcp
- https://github.com/github/github-mcp-server
- https://x.com/tooltierai/status/2122012506868584772
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
