# AppSec und SAST

- **Domain:** `security`
- **Kategorie:** `appsec-sast`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Statische Checks (z. B. Semgrep) und sichere Review-Muster im eigenen Code.

## Empfohlener Tool-Stack

- Semgrep-MCP oder CLI
- Review-Skills

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| semgrep MCP (Hermes-Katalog) | MCP | https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep | SAST-Befunde. | hermes mcp install semgrep | Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |
| Hermes-Skill requesting-code-review | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Enthaelt einen Security-Scan-Schritt im Review-Workflow. | Bundled. | Bundled. | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | nein (so belegt) |

## Typische Workflows

- CI bricht bei festgelegten Regeln, Agent erklaert Befund und schlaegt Fix im eigenen Code vor.

## Fallstricke

- Nur defensive, autorisierte Nutzung.
- Keine Angriffs- oder Umgehungsanleitungen in diesen Templates.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/semgrep
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
