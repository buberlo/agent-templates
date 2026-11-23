---
id: generic-mcp-agents-workflow
title: "Generische MCP-Agenten"
domain: agent-platforms
category: generic-mcp-agents
tags:
  - generic
  - agent-platforms
  - katalog
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: punkpeye/awesome-mcp-servers
    install: "https://github.com/punkpeye/awesome-mcp-servers"
    version_notes: "98405 GitHub Stars"
  - name: modelcontextprotocol/servers
    install: "https://github.com/modelcontextprotocol/servers"
    version_notes: "92179 GitHub Stars"
inputs:
  - "Kontext/Briefing für Generische MCP-Agenten"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 3
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Gemeinsames Muster: MCP für Zugriff, Tools für Aktionen, Skills für Abläufe.

## Wann nutzen

- Anfragen passen zur Kategorie **Generische MCP-Agenten**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| punkpeye/awesome-mcp-servers | Katalog | Aus Recherche 2026-11-23 |
| modelcontextprotocol/servers | Referenz | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Generische MCP-Agenten (agent-platforms/generic-mcp-agents).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Wenige Server, Filter, Read-only defaults, Skills fuer den Ablauf, menschliche Gates fuer Writes.
```

## Arbeitsablauf

- Wenige Server, Filter, Read-only defaults, Skills fuer den Ablauf, menschliche Gates fuer Writes.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- ClawHub-Skills vor der Nutzung prüfen (`openclaw skills verify`). Im Februar 2026 auditierte Koi Security 2.857 Registry-Skills und bewertete 341 als schadhaft (ca. 12 %). Quellen: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html , https://docs.openclaw.ai/skills/
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Generische MCP-Agenten-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `generic-mcp-agents` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Generische MCP-Agenten. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Generische MCP-Agenten
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
