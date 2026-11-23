---
id: social-ffmpeg-shorts-repurpose
domain: content-marketing
title: "Longform zu Shorts mit ffmpeg"
category: social-tiktok
tags:
  - ffmpeg
  - shorts
  - repurpose
target_agents:
  - hermes
  - generic
required_tools:
  - name: ffmpeg
    install: "apt: ffmpeg"
    version_notes: "7.x; crop+scale filter"
  - name: yt-dlp
    install: "pip: yt-dlp"
    version_notes: "nur eigene/lizenzierte Quellen"
inputs:
  - "Quellvideo 16:9"
  - "Clip-Marken"
  - "Untertitel SRT optional"
outputs:
  - "9:16 MP4 Clips"
  - "Thumbnail JPG"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Aus Podcasts oder Webinaren vertikale Kurzclips für TikTok/Reels/Shorts schneiden.

## Wann nutzen

- Content-Recycling nach Livestream.
- Nicht ohne Musik-/Bildrechte an Quellmaterial.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | crop 9:16 | Center oder face detect manual |
| drawtext/subtitles | Burn-in | Lesbarkeit mobile |
| ffprobe | Keyframes | Saubere Schnitte |

## System-Prompt / Instruktionen

```text
Cut vertical shorts with ffmpeg crop=ih*9/16,scale=1080:1920.
Max 60s per clip unless specified.
Burn subtitles only with provided SRT and style file.
Name clips: {source}_{start}_{end}.mp4
```

## Arbeitsablauf

1. Highlights aus Transcript wählen.
2. Crop-Fenster festlegen (Gesicht zentriert).
3. Schnitt + Loudnorm für Mobile.
4. Thumbnail aus Frame extrahieren.
5. QC auf 1080×1920 Gerät.

## Qualitätskriterien / Definition of Done

- [ ] Kein Beschnitt wichtiger Grafik
- [ ] Untertitel lesbar (Safe Zone)
- [ ] Länge pro Plattformlimit

## Sicherheit & Freigaben

- Nur Material mit Verwertungsrechten.
- Gesprochene Aussagen kontexttreu (kein Deep-Cut-Missbrauch).

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `webinar.mp4`, 3 Segmente à 45 s
**Erwartetes Ergebnis:** `short_01.mp4` … `short_03.mp4`
