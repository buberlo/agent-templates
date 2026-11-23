---
id: mcp-server-bau-mcp-focus
title: "MCP-Server bauen: MCP/Skill-Fokus"
domain: ki-ops
category: mcp-server-bau
tags:
  - mcp
  - ki-ops
  - referenz
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: modelcontextprotocol/servers (Referenzserver)
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "92179 GitHub Stars"
  - name: mcp-builder (in awesome-claude-skills beschrieben)
    install: "https://github.com/ComposioHQ/awesome-claude-skills"
    version_notes: "80108 GitHub Stars"
inputs:
  - "Kontext/Briefing für MCP-Server bauen"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Eigene MCP-Server designen, implementieren und an Clients anbinden.

## Wann nutzen

- Anfragen passen zur Kategorie **MCP-Server bauen**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| modelcontextprotocol/servers (Referenzse | Referenz | Aus Recherche 2026-11-23 |
| mcp-builder (in awesome-claude-skills be | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for MCP-Server bauen (ki-ops/mcp-server-bau).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Enger Tool-Schnitt, gute Beschreibungen, Least Privilege, Tests, dann Katalog/Review (Nous merged MCPs nur per PR).
```

## Arbeitsablauf

- Enger Tool-Schnitt, gute Beschreibungen, Least Privilege, Tests, dann Katalog/Review (Nous merged MCPs nur per PR).

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Zu viele Tools, zu lange Schemas (Token-Overhead). Ungepruefte Community-Server.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-MCP-Server bauen-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `mcp-server-bau` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für MCP-Server bauen. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in MCP-Server bauen
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

### Beispiel 3 (Praxisbeispiel)

- **Aufgabe:** Messen, wie viele Tokens bereits geladene MCP-Server verbrauchen, bevor eine Frage gestellt wird.
- **Input:** Der bestehende MCP-Stack des Autors in Claude. Die genaue Serverliste im First Post konnte in dieser Recherche nicht vollstaendig geladen werden (Reddit-Seite weitgehend ohne Beitragstext).
- **Prompt:**
```text
Mehrere gleichzeitig aktivierte MCP-Server in einem Claude-Setup.
```
- **Erwartetes Ergebnis:**
  Threadtitel und Suche geben die Messung mit 67.000 Tokens Overhead an, bevor die erste Frage eingegeben wurde.
- **Quelle:** https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
