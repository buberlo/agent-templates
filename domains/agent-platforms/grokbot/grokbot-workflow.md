---
id: grokbot-workflow
title: "Grok Bot"
domain: agent-platforms
category: grokbot
tags:
  - grokbot
  - agent-platforms
  - produktconnector
target_agents:
  - grokbot
  - generic-mcp-agents
required_tools:
  - name: Grok Bot Plugins / Custom MCP
    install: "https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp"
    version_notes: "Produktdoku/Wiki (Angaben zu Versionen 0.75.x–0.77.x, Okt/Nov 2026)."
  - name: Grok Bot 101
    install: "https://x.ai/bot/guides/grok-bot-101"
    version_notes: "Offizielle Guides."
inputs:
  - "Kontext/Briefing für Grok Bot"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Connect Apps, Custom MCP, Skills-Decke, Box-Computer, keine localhost-MCPs.

## Wann nutzen

- Anfragen passen zur Kategorie **Grok Bot**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Grok Bot Plugins / Custom MCP | Produkt-Connector | Aus Recherche 2026-11-23 |
| Grok Bot 101 | Offizielle Einfuehrung | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Grok Bot (agent-platforms/grokbot).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Plugin installieren, Auth in der Frist abschliessen, mit @ an den Task haengen, einzelne Tools blocken wenn noetig.
```

## Arbeitsablauf

- Plugin installieren, Auth in der Frist abschliessen, mit @ an den Task haengen, einzelne Tools blocken wenn noetig.
- Wenn kein Connector existiert: Arbeit auf dem Bot-Computer (CLI, Dateien), nicht so tun als waere ein privates Laptop-MCP verbunden.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skill-Ceiling 200 (seit 0.71.2, Wiki).
- Shared Bots: Team kann Command und Args eines Command-Servers lesen.
- Viele virale X-Threads ueber N GitHub-Repos sind Marketing – nicht ungeprueft uebernehmen.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Grok Bot-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `grokbot` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Grok Bot. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Grok Bot
- **Input:** Unvollständige oder ungültige Eingabe
- **Prompt:**
```text
Erkenne fehlende Pflichtfelder, brich ab und liste konkrete Nachfragen.
```
- **Erwartetes Ergebnis:**
| Feld | Status |
|------|--------|
| input | fehlt |
| Aktion | keine Ausführung |
