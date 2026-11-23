# ETL-Pipelines

- **Domain:** `daten-analytics`
- **Kategorie:** `etl-pipelines`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Daten laden, transformieren und orchestrieren (Airflow-nahe, Cloud-ETL, n8n).

## Empfohlener Tool-Stack

- n8n oder vorhandene Data-Platform-MCPs
- Idempotenz und Logs

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| n8n | Plattform + MCP-Katalogeintrag | https://github.com/n8n-io/n8n | Workflow-Automation mit AI-Nodes; in Hermes als n8n-official im optionalen MCP-Katalog. | n8n selbst hosten oder Cloud; in Hermes hermes mcp install n8n-official. | 211.894 Stars | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| motherduck MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck | Ziel- oder Analyseschicht. | hermes mcp install motherduck | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Extract/Load im Workflow-Tool, Transformation versioniert, Agent schreibt oder reviewed die Jobs.

## Fallstricke

- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/n8n-io/n8n
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/motherduck
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
