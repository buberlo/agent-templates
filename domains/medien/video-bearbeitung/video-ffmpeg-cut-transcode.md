---
id: video-ffmpeg-cut-transcode
domain: medien
title: "Video schneiden, transcodieren und Untertitel"
category: video-bearbeitung
tags:
  - ffmpeg
  - transcode
  - subtitles
target_agents:
  - hermes
  - generic
required_tools:
  - name: ffmpeg
    install: "apt/brew: ffmpeg"
    version_notes: "7.x (libav); ffprobe bundled"
  - name: whisper
    install: "pip: openai-whisper oder CLI whisper.cpp"
    version_notes: "large-v3-turbo für DE/EN"
inputs:
  - "Quellvideo (MP4/MOV)"
  - "Schnittmarken (IN/OUT)"
  - "Zielprofil (z. B. H.264 1080p)"
outputs:
  - "Fertiges MP4"
  - "Optional SRT/VTT"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Videos verlustarm schneiden, für Web transcodieren und optionale Untertitel per ASR erzeugen.

## Wann nutzen

- Kunde liefert Rohtake; Auslieferung soll einheitliches MP4 + Untertitel sein.
- Nicht für komplexes Color Grading oder Multi-Cam-Schnitt (dafür NLE).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | cut, scale, encode | De-facto-Standard, stream copy wo möglich |
| ffprobe | Metadaten | Dauer, Codecs, FPS vor Schnitt |
| Whisper | ASR → SRT | Offline-fähig, gut für DE/EN |

## System-Prompt / Instruktionen

```text
You edit video with ffmpeg only unless user asks otherwise.
1) ffprobe input; confirm codec and duration.
2) Cut with -ss/-to; prefer stream copy only when codecs match deliverable.
3) Transcode: H.264 + AAC, yuv420p, faststart for web.
4) If subtitles requested: whisper → SRT, burn-in only with explicit approval.
Report exact ffmpeg commands and output paths.
```

## Arbeitsablauf

1. `ffprobe` auswerten; Schnittfenster bestätigen.
2. Schnitt (copy oder re-encode je nach Profil).
3. Transcode auf Zielprofil; `+faststart`.
4. Optional Whisper → SRT; VTT aus SRT ableiten.
5. Qualitätscheck: Dauer, Bitrate, Stichprobe abspielen.

## Qualitätskriterien / Definition of Done

- [ ] Zieldauer ±0,5 s
- [ ] Kein A/V-Drift
- [ ] Untertitel zeitlich synchron (falls erstellt)
- [ ] Befehlsprotokoll dokumentiert

## Sicherheit & Freigaben

- Keine Uploads ohne Kundenfreigabe.
- Gesichter/Audio aus Meetings nur mit DSGVO-Freigabe transkribieren.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

_Siehe vorheriger Abschnitt; bei Migration ergänzt._

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Validierung
- **Input:** n/a
- **Prompt:** `validate output`
- **Erwartetes Ergebnis:** OK

## Beispiele (Legacy)

**Eingabe:** `raw.mov`, Schnitt 00:01:12–00:04:05, 1080p MP4
**Erwartetes Ergebnis:** `deliver.mp4`, optional `deliver.srt`
