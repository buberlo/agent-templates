---
id: audio-bearbeitung-workflow
title: "Audio-Bearbeitung"
domain: medien
category: audio-bearbeitung
tags:
  - audio
  - medien
  - cli
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: FFmpeg (CLI, oft ohne eigenes MCP)
    install: "https://ffmpeg.org/"
    version_notes: "Nicht als einzelnes MCP-Star-Signal belegt."
  - name: ClawHub / OpenClaw Skill Openai Whisper (steipete)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "303 GitHub Stars"
inputs:
  - "Kontext/Briefing für Audio-Bearbeitung"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Schneiden, normalisieren, mischen und konvertieren von Audio mit FFmpeg, DAW-nahen CLIs oder MCP-Wrappern.

## Wann nutzen

- Anfragen passen zur Kategorie **Audio-Bearbeitung**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | Aus Recherche 2026-11-23 |
| ClawHub / OpenClaw Skill Openai Whisper  | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Audio-Bearbeitung (medien/audio-bearbeitung).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Audio extrahieren, loudnorm, anschließend transkribieren.
```

## Arbeitsablauf

- Audio extrahieren, loudnorm, anschließend transkribieren.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- STT/TTS-MCPs oft cloud- und kostenpflichtig; lokale Whisper-Skills schonen Daten.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Audio-Bearbeitung-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `audio-bearbeitung` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Audio-Bearbeitung. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Audio-Bearbeitung
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
