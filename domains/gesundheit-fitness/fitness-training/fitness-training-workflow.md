---
id: fitness-training-workflow
title: "Fitness und Training"
domain: gesundheit-fitness
category: fitness-training
tags:
  - fitness
  - gesundheit-fitness
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: strava MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/strava"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Fitness und Training"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Trainingspläne und Tracking (z. B. Strava-Katalog-MCP); keine medizinische Diagnose.

## Wann nutzen

- Anfragen passen zur Kategorie **Fitness und Training**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| strava MCP (Hermes-Katalog) | MCP | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Fitness und Training (gesundheit-fitness/fitness-training).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Trainingstagebuch und oeffentliche Aktivitaetsdaten; Hinweise als allgemeine Fitnessinfo kennzeichnen.
```

## Arbeitsablauf

- Trainingstagebuch und oeffentliche Aktivitaetsdaten; Hinweise als allgemeine Fitnessinfo kennzeichnen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Keine medizinischen Aussagen. OAuth-Daten minimieren.
- Keine medizinische Beratung oder Diagnose.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Fitness und Training-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `fitness-training` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Fitness und Training. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Fitness und Training
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
