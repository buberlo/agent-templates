---
id: netzwerk-workflow
title: "Netzwerk"
domain: it-betrieb-support
category: netzwerk
tags:
  - netzwerk
  - it-betrieb-support
  - cli
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic-mcp-agents
required_tools:
  - name: Terminal-Diagnose (Agent Shell)
    install: "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart"
    version_notes: "n/a"
inputs:
  - "Kontext/Briefing für Netzwerk"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Diagnose von Konnektivität, DNS, VPN/Tailscale, Switch/Firewall-Konfiguration auf Beschreibungsebene.

## Wann nutzen

- Anfragen passen zur Kategorie **Netzwerk**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Terminal-Diagnose (Agent Shell) | CLI | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Netzwerk (it-betrieb-support/netzwerk).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Symptom, Scope, Schicht (DNS/TLS/Routing) trennen; Konfigaenderungen nur als Vorschlag.
```

## Arbeitsablauf

- Symptom, Scope, Schicht (DNS/TLS/Routing) trennen; Konfigaenderungen nur als Vorschlag.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Remote nur mit Einwilligung und sichtbarer Sitzung.
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Netzwerk-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `netzwerk` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Netzwerk. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Netzwerk
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
