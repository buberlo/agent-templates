---
id: social-buffer-schedule-campaign
domain: content-marketing
title: "Kampagnenplanung mit Buffer API"
category: social-media-strategie
tags:
  - buffer
  - scheduling
  - social
target_agents:
  - grokbot
  - generic
required_tools:
  - name: buffer
    install: "API: buffer.com"
    version_notes: "Publish API; OAuth"
  - name: canva
    install: "optional Export"
    version_notes: "Assets 1080²"
inputs:
  - "Content-Kalender CSV"
  - "Kanäle"
  - "Zeitzone"
outputs:
  - "Geplante Posts"
  - "Export-IDs"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Social-Media-Posts zeitgesteuert über mehrere Kanäle aus einem Kalender veröffentlichen.

## Wann nutzen

- Produktlaunch, Event-Hype, Evergreen-Serien.
- Nicht für Paid Ads (dafür Meta Ads Manager).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Buffer API | Scheduling | Multi-Channel |
| ffmpeg | Video trim | Unter 60 s Reels |
| Link shortener | Tracking | UTM parametrisieren |

## System-Prompt / Instruktionen

```text
Schedule posts via Buffer API from CSV calendar.
Validate media dimensions per channel before upload.
Attach UTMs to all outbound links.
Queue for human review channel when risk_level medium topics.
```

## Arbeitsablauf

1. CSV validieren (Textlänge, Medienpfade).
2. Medien uploaden; IDs merken.
3. API Batch schedule.
4. Vorschau-Links an Marketing.
5. Nach Publish Metriken notieren.

## Qualitätskriterien / Definition of Done

- [ ] Alle Zeilen scheduled oder Fehler geloggt
- [ ] UTM konsistent
- [ ] Freigabe-Mail archived

## Sicherheit & Freigaben

- OAuth-Token in Secret Store.
- Keine vorzeitigen Leaks unter NDA-Produkte.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `launch_week.csv`, LinkedIn + X
**Erwartetes Ergebnis:** 14 Posts geplant, IDs in `scheduled.json`
