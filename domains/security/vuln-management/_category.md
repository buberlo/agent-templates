# Vulnerability Management

- **Domain:** `security`
- **Kategorie:** `vuln-management`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Bekannte Schwachstellen in eigenen Systemen inventarisieren, priorisieren und Patches nachverfolgen.

## Empfohlener Tool-Stack

- Semgrep/SAST im CI
- Tickets in Jira/Linear
- Nur eigene/autorisierte Systeme

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| semgrep MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep | Statische Befunde im Agent-Workflow. | hermes mcp install semgrep | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| atlassian MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian | Ticket-Nachverfolgung. | hermes mcp install atlassian | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| linear MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear | Ticket-Nachverfolgung. | hermes mcp install linear | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Befunde inventarisieren, priorisieren, Patch-Ticket, Nachscan.

## Fallstricke

- Scanner-Output ist nicht automatisch vollstaendig.
- Nur defensive, autorisierte Nutzung; keine Angriffsverfahren in dieser Sammlung.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/atlassian
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/linear
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
