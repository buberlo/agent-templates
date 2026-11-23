# Homelab

- **Domain:** `it-betrieb-support`
- **Kategorie:** `homelab`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Selbst gehostete Labs: Proxmox, Docker, Home-Server, Dokumentation der eigenen Infrastruktur.

## Empfohlener Tool-Stack

- SSH/Terminal, Docker, optional Home Assistant, Dokumentation im Vault

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| homeassistant-mcp (tevonsb) | MCP | https://github.com/tevonsb/homeassistant-mcp | Home-Assistant-Daten lesen und Geraete (Lichter, Schalter, Thermostate) steuern. | Lokaler MCP, siehe Repo. Eintrag in awesome-mcp-servers, Home-Automation-Sektion. | Star-Zahl in dieser Recherche nicht per API gezogen. | https://github.com/punkpeye/awesome-mcp-servers | ja, markiert |
| Obsidian-Skills (Hermes bundled, ClawHub steipete) | Skill | https://hermes-agent.nousresearch.com/docs/reference/skills-catalog | Vault lesen, suchen, Notizen anlegen/editieren – haeufiger Memory-/Wissens-Layer. | Hermes bundled /obsidian. OpenClaw: ClawHub-Skill Obsidian (steipete). | ClawHub: 92.458 Downloads, 381 Stars (Leaderboard 23.11.2026). | https://clawhubtrends.com/leaderboard.html | nein (so belegt) |

## Typische Workflows

- Inventar und Runbooks zuerst, Aenderungen klein und reversibel.

## Fallstricke

- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://github.com/tevonsb/homeassistant-mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://github.com/punkpeye/awesome-mcp-servers
- https://clawhubtrends.com/leaderboard.html
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
