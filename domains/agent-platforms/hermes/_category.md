# Hermes Agent (Nous Research)

- **Domain:** `agent-platforms`
- **Kategorie:** `hermes`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Skills, MCP-Katalog, Tool Gateway, Delegation an Claude Code/Codex, lokale Config.

## Empfohlener Tool-Stack

- hermes setup / --portal
- Skills in ~/.hermes/skills
- MCP nur aus Katalog oder bewusst selbst
- optional Delegation

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Hermes Agent | Agent-Plattform | https://github.com/NousResearch/hermes-agent | Skills, MCP-Katalog (66 optional-mcps-Ordner in dieser Recherche gezaehlt), Tool Gateway, Cron, Memory, Delegation. | Docs Quickstart; Desktop-Installer oder CLI. hermes mcp install <name>, hermes skills install, hermes skills browse. | 265.550 Stars, letzter Push am 23.11.2026 (API). | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | nein (so belegt) |
| Nous-approved MCP-Katalog | Katalog | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | Eintraege unter optional-mcps/, disabled by default, Installation mit Karte fuer Secrets/OAuth. Kein Community-Submit-Tier – nur Merge per PR. | hermes mcp Picker oder hermes mcp install deepwiki\|linear\|…. | 66 Ordner in optional-mcps (Listing 23.11.2026). | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp | nein (so belegt) |

## Typische Workflows

- Blank Slate wenn man Least Privilege will. Sonst empfohlene Defaults, dann gezielt MCPs dazu.
- Slash-Commands laut Docs: /github, /youtube-content, /excalidraw.

## Fallstricke

- Hermes-Skills mit platforms: [macos] werden unter Linux still übersprungen. Quelle: https://x.com/JayQinQT/status/2120856724668133406
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Sync respektiert lokale Loeschungen; Restore mit hermes skills reset --restore.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- https://x.com/JayQinQT/status/2120856724668133406
- https://github.com/NousResearch/hermes-agent
- https://github.com/punkpeye/awesome-mcp-servers
- https://docs.openclaw.ai/skills/
