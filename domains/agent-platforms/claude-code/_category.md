# Claude Code

- **Domain:** `agent-platforms`
- **Kategorie:** `claude-code`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Skills, MCP, Slash-Commands, Delegation und offizielle Anthropic-Dokument-Skills.

## Empfohlener Tool-Stack

- eingebaute Repo-Tools + Skills + MCP ueber claude mcp add
- document-skills fuer Office

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Claude Code | CLI-Agent | https://github.com/anthropics/claude-code | Terminal-Coding-Agent, Skills, MCP, Slash-Commands. | Offizielle Install-Docs; claude mcp add --transport http <name> <url>. | 156.765 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| Anthropic document skills (docx, pptx, xlsx, pdf) | Skill | https://github.com/anthropics/skills | Offizielle Agent-Skills zum Erzeugen/Pruefen von Office- und PDF-Dateien; Verify-Schritt (validate.py, Render zu PDF/PNG) ist Teil der Anleitung. | Claude Code: /plugin marketplace add anthropics/skills und /plugin install document-skills@anthropic-agent-skills. | 199.219 Stars | https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/ | nein (so belegt) |
| GitHub Official MCP | MCP | https://github.com/github/github-mcp-server | Repos, Issues, PRs, Code Search, Actions. | Remote z. B. claude mcp add --transport http github https://api.githubcopilot.com/mcp/ mit PAT-Header (Claude-Code-Docs) oder lokaler Server aus dem Repo. | 34.686 Stars | https://code.claude.com/docs/en/mcp | nein (so belegt) |
| Context7 | MCP / Plattform | https://github.com/upstash/context7 | Aktuelle, versionsspezifische Bibliotheksdokumentation in den Agent-Kontext holen. | Paket @upstash/context7-mcp bzw. Docs im Repo. | 65.314 Stars | https://github.com/upstash/context7 | nein (so belegt) |
| Playwright MCP | MCP | https://github.com/microsoft/playwright-mcp | Lokale Browser-Automation ueber Accessibility-Snapshots, UI-Tests und Interaktion mit Web-Apps. | npx @playwright/mcp@latest (offizielle Docs/Repo). | 40.040 Stars | https://playwright.dev/mcp/introduction | nein (so belegt) |

## Typische Workflows

- Skill liegt in ~/.claude/skills oder Projekt-.claude/skills bzw. Plugin-Marketplace.
- MCP nur wenn sonst Daten aus anderen Tools kopiert wuerden (offizielle Empfehlungslogik).

## Fallstricke

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- MCP-Server mit externem Content: Prompt-Injection-Risiko (Claude-Code-Docs-Warnung).
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/skills/
- https://code.claude.com/docs/en/features-overview
- https://aifrontierpost.com/articles/anthropic-official-agent-skills-tutorial/
- https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- https://github.com/anthropics/claude-code
- https://github.com/anthropics/skills
- https://github.com/github/github-mcp-server
- https://github.com/upstash/context7
- https://playwright.dev/mcp/introduction
- https://github.com/microsoft/playwright-mcp
- https://agentspulse.github.io/tutorials/claude-powerpoint-skill/
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
