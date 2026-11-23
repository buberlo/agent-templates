---
id: youtube-content-workflow
title: "YouTube-Content"
domain: medien
category: youtube-content
tags:
  - youtube
  - medien
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Hermes-Skill youtube-content
    install: "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/media/media-youtube-content"
    version_notes: "Bundled-Katalog."
  - name: ClawHub „YouTube Watcher“ (michaelgathara)
    install: "https://clawhubtrends.com/leaderboard.html"
    version_notes: "48.111 Downloads, 294 Registry-Stars (ClawHub Leaderboard 23.11.2026)."
inputs:
  - "Kontext/Briefing für YouTube-Content"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Videos zusammenfassen, Kapitel erzeugen, Scripts und Kanal-Content aus Transkripten ableiten.

## Wann nutzen

- Anfragen passen zur Kategorie **YouTube-Content**.
- Nicht nutzen, wenn ein menschlicher Freigabe-Prozess noch nicht geklärt ist (`risk_level: low`).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes-Skill youtube-content | Skill | Aus Recherche 2026-11-23 |
| ClawHub „YouTube Watcher“ (michaelgathar | Skill | Aus Recherche 2026-11-23 |

## System-Prompt / Instruktionen

```text
You are a specialist for YouTube-Content (medien/youtube-content).
Use only tools listed in required_tools. Follow safety gates.
Workflow hint: - Hermes-Reihenfolge: Transcript mit --text-only --timestamps holen, leere Outputs abfangen, bei >50k Zeichen chunken, F
```

## Arbeitsablauf

- Hermes-Reihenfolge: Transcript mit --text-only --timestamps holen, leere Outputs abfangen, bei >50k Zeichen chunken, Format waehlen (Default: Summary), Timestamps gegenlesen.
- Prompt: /youtube-content fasse VIDEO_URL als Kapitel + 8-Satz-Summary zusammen.

## Qualitätskriterien / Definition of Done

- [ ] Eingaben vollständig und dokumentiert
- [ ] Tool-Aufrufe nachvollziehbar (Log/Pfade)
- [ ] Ergebnis entspricht Kategorie-Beschreibung
- [ ] Bei Schreib-/Sendeaktionen: explizite Nutzerfreigabe

## Sicherheit & Freigaben

- Die Formatbeispiele in der Skill-Doku sind Platzhalter, keine realen Video-Ergebnisse. Transkripte koennen deaktiviert sein.
- Skills sind Workflows/Anweisungen (progressive disclosure), MCP sind Verbindungen und Tools. Beides kombinieren, nicht verwechseln. Quellen: https://code.claude.com/docs/en/features-overview , https://github.com/ComposioHQ/awesome-claude-skills
- Nur die MCPs/Skills aktivieren, die die Aufgabe braucht. Hermes filtert per include/exclude; OpenClaw hat Tool-Policy und Prompt-Budgets. Quellen: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp , https://docs.openclaw.ai/skills/
- Keine Tokens oder Passwörter in Chat, Skill-Dateien oder Command-Argumente von Custom-MCPs schreiben. Grok-Bot-Wiki: OAuth-Tokens bleiben auf dem Connector-Backend; Command-Server dürfen keine Credentials in argv enthalten. Quelle: https://www.grokbotwiki.com/guides/grok-bot-plugins-mcp
- Schreiben, Senden, Bezahlen, Deployen und Löschen nur nach expliziter Freigabe; gute Document-Skills verlangen einen Verify-Schritt (Datei erneut lesen, PDF/PNG rendern).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Standard-YouTube-Content-Aufgabe im Agenten-Thread
- **Input:** Parameter-Satz für `youtube-content` (Testdaten)
- **Prompt:**
```text
Nutze den empfohlenen Stack für YouTube-Content. Dokumentiere jeden Tool-Aufruf. Keine Schreibaktion ohne Freigabe.
```
- **Erwartetes Ergebnis:**
```text
Status: OK
Artefakt: output/{slug}-demo.txt
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Fehlerfall / Validierung in YouTube-Content
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
