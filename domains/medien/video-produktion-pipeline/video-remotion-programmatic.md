---
id: video-remotion-programmatic
domain: medien
title: "Programmatisches Video mit Remotion"
category: video-produktion-pipeline
tags:
  - remotion
  - react
  - render
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: node
    install: "nvm; Node 20 LTS"
    version_notes: "Remotion 4.x"
  - name: remotion
    install: "npm: @remotion/cli @remotion/renderer"
    version_notes: "latest 4.x; Chrome Headless Shell"
inputs:
  - "Remotion-Projekt oder Template"
  - "Props (JSON)"
  - "Composition-ID"
outputs:
  - "MP4/WebM Render"
  - "Thumbnail PNG"
risk_level: medium
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Motion-Grafiken und Datenvideos aus React-Kompositionen serverseitig rendern.

## Wann nutzen

- Wiederkehrende Reports als Video (KPIs, Text, Logos).
- Nicht für spontanes Schnittmaterial ohne Composition.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Remotion | Composition + Render | TypeScript/React, CI-tauglich |
| @remotion/lambda | optional cloud render | Skalierung für Batch |
| ffmpeg | Nachbearbeitung | Audio-Mux falls nötig |

## System-Prompt / Instruktionen

```text
Render Remotion compositions deterministically.
Validate props against composition schema.
Use: npx remotion render <entry> <composition> out.mp4 --props=props.json
Set concurrency from available CPU; never commit AWS keys.
Deliver output path, duration, and render log excerpt on failure.
```

## Arbeitsablauf

1. `npm ci` im Projekt; Composition und FPS prüfen.
2. Props validieren (Schema/Typescript).
3. Lokales Render oder Lambda-Pipeline anstoßen.
4. ffprobe auf Output; Thumbnail via `npx remotion still`.
5. Artefakte benennen: `{id}_{date}.mp4`.

## Qualitätskriterien / Definition of Done

- [ ] Keine Frame-Drops / komplettes Render
- [ ] Props im Log reproduzierbar
- [ ] Auflösung und Codec wie Spezifikation

## Sicherheit & Freigaben

- Lambda-Rollen least privilege; keine Kundendaten in öffentlichen Buckets.
- Props auf PII prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** Composition `MonthlyKpi`, props `{ "month": "2026-10" }`
**Erwartetes Ergebnis:** `monthly-kpi_2026-10.mp4` (1920×1080, 30 fps)
