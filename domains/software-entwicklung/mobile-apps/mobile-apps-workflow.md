---
id: mobile-apps-workflow
title: "Mobile Apps"
domain: software-entwicklung
category: mobile-apps
tags:
  - mobile
  - software-entwicklung
  - mcp
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Mobile MCP
    install: "https://github.com/mobile-next/mobile-mcp"
    version_notes: "10819 GitHub Stars"
  - name: Mobilerun (ehem. DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "10100 GitHub Stars"
inputs:
  - "Kontext/Briefing für Mobile Apps"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

iOS/Android-Entwicklung, Device-Tests über Mobile-MCP oder Simulatoren.

## Wann nutzen

- Anfragen passen zur Kategorie **Mobile Apps**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Mobile MCP | MCP | Aus Recherche 2026-11-23 |
| Mobilerun (ehem. DroidRun) | CLI + MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Mobile Apps (software-entwicklung/mobile-apps).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - UI-Flows auf Simulator/Geraet ausfuehren, Screenshots/UI-State zurueckgeben, dann Code aendern.
```

## Arbeitsablauf

- UI-Flows auf Simulator/Geraet ausfuehren, Screenshots/UI-State zurueckgeben, dann Code aendern.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- USB-Debugging und Zustimmungen. Cloud-MCP-Keys nicht in git.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Mobile Apps-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `mobile-apps` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Mobile Apps. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Mobile Apps
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
