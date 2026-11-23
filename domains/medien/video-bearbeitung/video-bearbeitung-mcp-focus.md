---
id: video-bearbeitung-mcp-focus
title: "Video-Bearbeitung: MCP/Skill-Fokus"
domain: medien
category: video-bearbeitung
tags:
  - video
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
  - name: Remotion Agent Skills
    install: "https://github.com/remotion-dev/skills"
    version_notes: "7841 GitHub Stars"
inputs:
  - "Kontext/Briefing für Video-Bearbeitung"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Schneiden, konvertieren, untertiteln und nachbearbeiten von Videodateien, typischerweise mit FFmpeg oder einer Agent-Timeline.

## Wann nutzen

- Anfragen passen zur Kategorie **Video-Bearbeitung**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| FFmpeg (CLI, oft ohne eigenes MCP) | CLI | Aus Recherche 2026-11-23 |
| Remotion Agent Skills | Skill | Aus Recherche 2026-11-23 |
| Hermes-Skill youtube-content | Skill | Aus Recherche 2026-11-23 |
| ClawHub „Video Frames“ (steipete) | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for Video-Bearbeitung (medien/video-bearbeitung).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Schneide local.mp4 von Zeit A bis B, normalisiere Audio (loudnorm), schreibe h264+aac, pruefe mit ffprobe.
```

## Arbeitsablauf

- Schneide local.mp4 von Zeit A bis B, normalisiere Audio (loudnorm), schreibe h264+aac, pruefe mit ffprobe.
- Kein MCP, wenn ein einziges ffmpeg-Kommando reicht – spart Tokens.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- MCP-Toolschemas können den Kontext stark belasten, noch bevor die erste Frage kommt. In r/ClaudeAI berichtete ein Nutzer von 67.000 Token Overhead. Quelle: https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/
- Viele FFmpeg-MCP-Wrapper sind klein/fragmentiert; in dieser Recherche kein klarer Star-Leader.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach 

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-Video-Bearbeitung-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `video-bearbeitung` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für Video-Bearbeitung. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in Video-Bearbeitung
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
