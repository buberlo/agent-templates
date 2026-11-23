# OpenClaw

- **Domain:** `agent-platforms`
- **Kategorie:** `openclaw`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Gateway, ClawHub, Skill Workshop, MCP, Android-Companion, Skill-Verify.

## Empfohlener Tool-Stack

- Gateway auf dem Computer
- Skills aus Workspace/ClawHub mit Verify
- MCP unter mcp.servers + Tool-Policy
- Companion-Apps nicht als Host missverstehen

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| OpenClaw | Agent-Plattform | https://github.com/openclaw/openclaw | Self-hosted Gateway, Skills, Plugins, MCP, Kanaele, Android-Companion. | Docs auf docs.openclaw.ai; CLI openclaw skills\|mcp\|plugins. | 395.081 Stars (API 23.11.2026). | https://docs.openclaw.ai/ | nein (so belegt) |
| ClawHub | Registry | https://github.com/openclaw/clawhub | Oeffentliche Skill- und Plugin-Registry, Semver, Downloads, Security-Scan-Summaries, openclaw skills verify. | openclaw skills install @owner/skill, openclaw plugins install clawhub:<pkg>, optional npm i -g clawhub zum Publizieren. | 9.559 Stars; Site clawhub.ai / docs. | https://docs.openclaw.ai/clawhub | nein (so belegt) |

## Typische Workflows

- Skill Workshop fuer neue Prozeduren (Proposal review). MCP add in Settings oder CLI. Android per QR an bestehendes Gateway koppeln.
- Prompt-Budget: OpenClaw kuerzt Skill-Beschreibungen, wenn skills.limits.maxSkillsPromptChars greift.

## Fallstricke

- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Loading-Order kann Workspace-Skills ueber Bundled legen.
- Aeltere .clawdhub-Metadaten werden nicht mehr gelesen (Rename auf .clawhub).
- Leaderboard-Eintraege mit Warnmarkierung und extrem wenigen Registry-Stars trotz hoher Downloads besonders kritisch sehen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://docs.openclaw.ai/
- https://docs.openclaw.ai/skills/
- https://docs.openclaw.ai/clawhub
- https://docs.openclaw.ai/tools/mcp
- https://docs.openclaw.ai/platforms/android/
- https://clawhubtrends.com/leaderboard.html
- https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
- https://www.paloaltonetworks.com/blog/security-operations/clawhavoc-ai-agent-skills-poisoning/
- https://github.com/openclaw/openclaw
- https://github.com/openclaw/clawhub
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent
