---
id: audio-ffmpeg-podcast-master
domain: medien
title: "Podcast mastering mit ffmpeg und loudnorm"
category: podcast
tags:
  - ffmpeg
  - loudness
  - podcast
target_agents:
  - hermes
  - grokbot
  - generic
required_tools:
  - name: ffmpeg
    install: "apt/brew: ffmpeg"
    version_notes: "7.x; filter loudnorm, afftdn"
  - name: sox
    install: "apt/brew: sox"
    version_notes: "Optional trimming/silence"
inputs:
  - "Roh-Audio"
  - "Ziel-LUFS (-16/-14)"
  - "Intro/Outro-Stinger"
outputs:
  - "Master MP3"
  - "Wave für Archiv"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Podcast-Folgen auf einheitliche Lautheit bringen, Rauschen reduzieren und für Plattformen exportieren.

## Wann nutzen

- Batch vor Veröffentlichung bei Spotify/Apple.
- Nicht für künstlerisches Mixing mehrspuriger Sessions.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | loudnorm, denoise | EBU R128 approximiert |
| sox | silence trim | Füller am Anfang/Ende |
| ffprobe | LUFS messen | Vorher/Nachher |

## System-Prompt / Instruktionen

```text
Master podcast audio with ffmpeg loudnorm two-pass.
Measure integrated loudness first pass; apply second pass to hit target LUFS.
Apply light afftdn only if noise floor high.
Concat intro/outro with acrossfade when files provided.
Document filter chains and measured LUFS in deliverable notes.
```

## Arbeitsablauf

1. Rohdatei analysieren (Peak, LUFS).
2. Two-pass `loudnorm` auf Zielwert.
3. Optional Stinger einblenden.
4. Export MP3 192k + Archiv-WAV.
5. Stichprobe auf Clipping.

## Qualitätskriterien / Definition of Done

- [ ] Ziel-LUFS ±1 LU
- [ ] True Peak unter -1 dBTP
- [ ] Kein hörbares Pumping durch Denoise

## Sicherheit & Freigaben

- Nur lokal verarbeiten, keine Cloud-Uploads.
- Gaststimmen nur mit Einwilligung veröffentlichen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `ep42_raw.wav`, Ziel -16 LUFS
**Erwartetes Ergebnis:** `ep42_master.mp3`, Messprotokoll
