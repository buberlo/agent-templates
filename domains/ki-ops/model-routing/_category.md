# Model Routing

- **Domain:** `ki-ops`
- **Kategorie:** `model-routing`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Aufgaben auf passende Modelle/Provider verteilen, Kosten und Qualität steuern.

## Empfohlener Tool-Stack

- Hermes hermes model / Smart Routing (Quickstart)

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes model picker / Smart Routing | Plattform-Feature | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Interaktive Modellwahl; Smart Routing ist in Blank Slate deaktiviert, sonst Teil der empfohlenen Defaults. | hermes model bzw. Setup-Modi. | Produktdoku. | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | nein (so belegt) |

## Typische Workflows

- Guenstigeres Modell fuer Triage, staerkeres fuer riskante Schritte.

## Fallstricke

- Schwache Modelle rufen Tools unzuverlaessig.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
