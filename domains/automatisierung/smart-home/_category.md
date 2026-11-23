# Smart Home

- **Domain:** `automatisierung`
- **Kategorie:** `smart-home`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Home Assistant und Geräte steuern, Automationen anlegen.

## Empfohlener Tool-Stack

- Home Assistant MCP, Least Privilege, keine Exposition ohne Auth

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| homeassistant-mcp (tevonsb) | MCP | https://github.com/tevonsb/homeassistant-mcp | Home-Assistant-Daten lesen und Geraete (Lichter, Schalter, Thermostate) steuern. | Lokaler MCP, siehe Repo. Eintrag in awesome-mcp-servers, Home-Automation-Sektion. | Star-Zahl in dieser Recherche nicht per API gezogen. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |

## Typische Workflows

- Zustaende lesen, Szenen vorschlagen, Schaltaktionen nach Bestaetigung – besonders bei Tueren, Garagen, Heizungen.

## Fallstricke

- Ein offenes MCP ins Internet ist ein physisches Risiko.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/tevonsb/homeassistant-mcp
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
