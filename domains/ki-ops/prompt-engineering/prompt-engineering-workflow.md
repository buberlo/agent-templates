---
id: prompt-engineering-workflow
title: "Prompt Engineering"
domain: ki-ops
category: prompt-engineering
tags:
  - prompt
  - ki-ops
  - muster
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Agent Skills progressive disclosure
    install: "https://code.claude.com/docs/en/skills/"
    version_notes: "199219 GitHub Stars"
inputs:
  - "Kontext/Briefing für Prompt Engineering"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

System-Prompts, Skills und Tool-Beschreibungen schärfen.

## Wann nutzen

- Anfragen passen zur Kategorie **Prompt Engineering**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Agent Skills progressive disclosure | Muster | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Prompt Engineering (ki-ops/prompt-engineering).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Description als Trigger-Text behandeln: wann der Skill feuern soll und wann nicht.
```

## Arbeitsablauf

- Description als Trigger-Text behandeln: wann der Skill feuern soll und wann nicht.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Personality-Instruktionen gehoeren nicht in jedes Skill (OpenClaw-Rat: Prozedur, nicht Persona).
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Prompt Engineering-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `prompt-engineering` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Prompt Engineering. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Prompt Engineering
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
