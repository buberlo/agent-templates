# Mobile- und Phone-Control

- **Domain:** `automatisierung`
- **Kategorie:** `mobile-phone-control`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Android/iOS-Geräte steuern (Mobilerun, mobile-mcp, OpenClaw-Companion).

## Empfohlener Tool-Stack

- Mobilerun fuer echte Android-Geraete
- mobile-mcp fuer Sim/Apps
- OpenClaw: Gateway am Computer, App nur Companion

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Mobilerun (ehem. DroidRun) | CLI + MCP | https://github.com/droidrun/mobilerun | Android-Geraete mit natuerlicher Sprache steuern. Cloud-MCP unter docs.mobilerun.ai. | mobilerun setup, USB-Debugging, mobilerun ping. MCP: https://cloud.mobilerun.ai/api/mcp mit Bearer-Key laut Docs. | 10.100 Stars | https://docs.mobilerun.ai/mcp-server | nein (so belegt) |
| Mobile MCP | MCP | https://github.com/mobile-next/mobile-mcp | iOS- und Android-Apps in Simulatoren/Geraeten durch Agenten steuern. | Siehe Repo-README. | 10.819 Stars | https://github.com/mobile-next/mobile-mcp | nein (so belegt) |
| OpenClaw Android App (Companion) | Companion-App | https://docs.openclaw.ai/platforms/android/ | Kein Gateway-Host. Gateway auf macOS/Linux/Windows/WSL2, Pairing per QR (openclaw qr). | Offizielle App, Gateway muss laufen. | 395.081 Stars. | https://docs.openclaw.ai/platforms/android/ | nein (so belegt) |

## Typische Workflows

- Geraet sichtbar lassen, Aktionen bestaetigen lassen wo die Plattform das verlangt.

## Fallstricke

- Cloud-MCP-Keys schuetzen. Companion ist nicht der Agent-Host.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://docs.mobilerun.ai/mcp-server
- https://github.com/mobile-next/mobile-mcp
- https://docs.openclaw.ai/platforms/android/
- https://github.com/droidrun/mobilerun
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
