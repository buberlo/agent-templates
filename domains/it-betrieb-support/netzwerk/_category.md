# Netzwerk

- **Domain:** `it-betrieb-support`
- **Kategorie:** `netzwerk`
- **Stand:** 2026-11-23

## Kurzbeschreibung

Diagnose von Konnektivität, DNS, VPN/Tailscale, Switch/Firewall-Konfiguration auf Beschreibungsebene.

## Empfohlener Tool-Stack

- Diagnose-CLIs (ping, dig, traceroute, curl) im Terminal des Agenten

## MCP-Server und Skills

| Name | Typ | URL | Einsatz | Installation | Popularitaet | Quelle | Unverified? |
|---|---|---|---|---|---|---|---|
| Terminal-Diagnose (Agent Shell) | CLI | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | Standard bei Hermes/Claude Code/Codex: Netzwerk mit Systemtools pruefen. | Im Agent aktiviertes Terminal-Toolset. | n/a | https://hermes-agent.nousresearch.com/docs/getting-started/quickstart | nein (so belegt) |

## Typische Workflows

- Symptom, Scope, Schicht (DNS/TLS/Routing) trennen; Konfigaenderungen nur als Vorschlag.

## Fallstricke

- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- https://github.com/punkpeye/awesome-mcp-servers
- https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
- https://docs.openclaw.ai/skills/
- https://github.com/NousResearch/hermes-agent
