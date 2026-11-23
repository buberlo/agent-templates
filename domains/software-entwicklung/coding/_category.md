# Coding

- **Domain:** `software-entwicklung`
- **Kategorie:** `coding`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Features implementieren, Bugs fixen, Code in Repositories ändern.

## Empfohlener Tool-Stack

- Agent-native Edit/Terminal + Context7 + GitHub MCP + Tests
- Delegation an Claude Code/Codex wo vorgesehen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | nein (so belegt) |
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ mit PAT-Header (Claude-Code-Docs) oder lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| Hermes-Skill github / ClawHub Github | Skill + CLI | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | GitHub ueber die gh-CLI: PRs, Issues, Reviews, Repos, Auth. Auf ClawHub ist Github (steipete) eines der meistinstallierten Skills. | Hermes: bundled (/github). OpenClaw: openclaw skills install aus ClawHub (Owner steipete). | ClawHub-Downloads Github (steipete): 174.624, 585 Registry-Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |
| Hermes-Skills claude-code und codex | Skill (Delegation) | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Coding-Aufgaben an Claude Code CLI bzw. OpenAI Codex CLI delegieren. | Bundled autonomous-ai-agents/. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- Community-Default-Stack in Posts: Context7, GitHub MCP, Playwright MCP, Chrome DevTools MCP, oft plus Sentry.
- Feature, Akzeptanzkriterien, Testdatei zuerst (Hermes TDD-Skill).

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Veraltete APIs ohne Context7/Docs-MCP.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/upstash/context7
- https://code.claude.com/docs/en/mcp
- https://x.com/tooltierai/status/2122012506868584772
- https://x.com/AnylancerInc/status/2116384700449149180
- https://github.com/github/github-mcp-server
- https://clawhubtrends.com/leaderboard.html
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
