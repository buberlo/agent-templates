---
id: mobile-phone-control-mcp-focus
title: "Mobile- und Phone-Control: MCP/Skill-Fokus"
domain: automatisierung
category: mobile-phone-control
tags:
  - mobile
  - automatisierung
  - climcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Mobilerun (ehem. DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "10100 GitHub Stars"
  - name: Mobile MCP
    install: "https://github.com/mobile-next/mobile-mcp"
    version_notes: "10819 GitHub Stars"
inputs:
  - "Kontext/Briefing für Mobile- und Phone-Control"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Android/iOS-Geräte steuern (Mobilerun, mobile-mcp, OpenClaw-Companion).

## Wann nutzen

- Anfragen passen zur Kategorie **Mobile- und Phone-Control**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Mobilerun (ehem. DroidRun) | CLI + MCP | Aus Recherche 2026-11-23 |
| Mobile MCP | MCP | Aus Recherche 2026-11-23 |
| OpenClaw Android App (Companion) | Companion-App | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Mobile- und Phone-Control (automatisierung/mobile-phone-control).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Geraet sichtbar lassen, Aktionen bestaetigen lassen wo die Plattform das verlangt.
```

## Arbeitsablauf

- Geraet sichtbar lassen, Aktionen bestaetigen lassen wo die Plattform das verlangt.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Cloud-MCP-Keys schuetzen. Companion ist nicht der Agent-Host.
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Mobile- und Phone-Control-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `mobile-phone-control` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Mobile- und Phone-Control. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Mobile- und Phone-Control
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
