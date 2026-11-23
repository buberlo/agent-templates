---
id: streaming-broadcast-workflow
domain: medien
title: "Streaming-Vorbereitung und Broadcast-Assets"
category: streaming-broadcast
tags:
  - streaming
  - obs
  - ffmpeg
  - broadcast
target_agents:
  - hermes
  - generic
  - cursor
required_tools:
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Pre-Stream-Transcode, Testclips"
  - name: OBS Studio
    install: "obsproject.com; manuelle Konfiguration"
    version_notes: "Agent dokumentiert Profile, steuert nicht live ohne Freigabe"
inputs:
  - "Stream-Briefing (Zielplattform, Auflösung, Bitrate)"
  - "Medien-Assets (Overlays, Stinger, Pre-Roll)"
outputs:
  - "OBS-Profil-Checkliste und normalisierte Assets"
  - "Test-Encode-Protokoll"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Livestream technisch vorbereiten**: Assets transcodieren, Lautheit und Auflösung auf Plattform-Limits bringen, **OBS-Checkliste** liefern—ohne ungefragt Stream-Keys zu drehen oder Kanäle live zu schalten.

## Wann nutzen

- Webinar oder Unternehmens-Livestream in 720p/1080p geplant.
- B-Roll, Stinger und Intro-Clips sollen einheitliche Specs haben.
- Agent soll FFmpeg-Test encodes und Dokumentation für Operator liefern.

**Wann nicht**

- 24/7 lineares Fernsehen mit Ad-Server.
- DRM-geschützte Ausspielung.
- Unbeaufsichtigter Start des Livestreams durch Agent.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg / ffprobe | Asset-Normalisierung | yuv420p, AAC, keyframe spacing |
| OBS Studio | Live-Mix | De-facto-Standard; Mensch am Go-Live |
| ffplay | Kurztest | Stichprobe vor Show |

## System-Prompt / Instruktionen

```text
You prepare streaming assets and operator checklists; you do not start live streams without explicit real-time approval.

Inputs: platform (YouTube RTMP, Twitch, custom), target resolution/fps, video bitrate range, audio bitrate, keyframe interval (often 2s), list of asset files.

Normalize each asset:
- Video: h264, yuv420p, fps constant (e.g. 30), scale to target canvas, -g 60 for 30fps if 2s GOP.
- Audio: aac 48k stereo, loudnorm integrated -16 LUFS for speech overlays, -14 for hype stingers if user says so.

Generate short test pattern clip: ffmpeg color bars + tone 1kHz 5s for operator AV check.

OBS checklist (markdown):
- Base resolution, output scaled resolution, encoder x264 vs nvenc note.
- Audio tracks mapping, monitoring off on stream mix.
- Hotkeys backup, recording path, reconnect settings.
- Never paste stream keys in chat; refer to OBS profile location only.

Verify each asset with ffprobe; reject interlaced source without deinterlace filter plan.

Deliver: folder layout, probe table, ffmpeg commands, OBS checklist, open risks.

No RTMP push tests to production ingest without user scheduling.

Label each normalized asset with target use (intro, stinger, loop, b-roll).
If source is screen capture with variable fps, enforce constant fps filter before ingest.
Recommend backup recording locally in OBS checklist even when streaming only.
```

## Arbeitsablauf

1. Plattform-Spec-Tabelle aus Briefing (1080p30, 4500–6000 kbps video typisch).
2. Alle Assets `ffprobe`; Interlace/Rotation flaggen.
3. `ffmpeg` Normalisierung nach Spec in `stream_assets/`.
4. Stinger auf 2 s Länge trimmen; Audio fade out 100 ms.
5. Testpattern `bars.mp4` erzeugen.
6. OBS-Checkliste als Markdown; Operator review.
7. Optional lokaler `-f null` Encode-Test der längsten Loop-Quelle.

## Qualitätskriterien / Definition of Done

- [ ] Alle Assets gleiche fps und Auflösung wie Canvas
- [ ] Keyframe-Abstand dokumentiert
- [ ] Audio peaks safe; kein Clip auf Stinger
- [ ] Kein Stream-Key im Log
- [ ] Operator-Checkliste vollständig

## Sicherheit & Freigaben

- Stream-Keys und RTMP-URLs nur in OBS lokal; nie in Repo.
- Go-Live-Toggle nur Mensch.
- Aufgezeichnete Streams: DSGVO bei Chat-Overlays.

## Fallstricke

- Gemischte 25/30 fps Szenen → OBS judder.
- NVENC auf Server ohne GPU im Checkliste erwähnt.
- Zu hohe Bitrate → Plattform transcoded schlecht.
- Stinger stereo out of phase auf Mono-Summe.
- Agent startet `ffmpeg -f flv rtmp://...` ohne Freigabe—verbieten.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Intro 5 s auf 1080p30 normalisieren.
- **Input:** `intro_4k.mov`, Canvas 1920×1080.
- **Prompt:**

```text
Transcode intro to 1080p30 h264, -g 60, aac 160k, loudnorm -16 LUFS; ffprobe after.
```

- **Erwartetes Ergebnis:**

```text
intro_norm.mp4: 1920x1080, 30 fps, h264, duration 5.00s
gop: 60 frames
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** OBS-Checkliste YouTube 1080p.
- **Input:** Keine Keys; nur Spec.
- **Prompt:**

```text
Markdown checklist: canvas, scaled output, encoder note, audio tracks; omit stream key.
```

- **Erwartetes Ergebnis:**

```markdown
- [ ] Base: 1920x1080
- [ ] Output: 1920x1080 @ 30 fps
- [ ] Encoder: x264 veryfast / NVENC if available
- [ ] Audio: Track1 Mic, Track2 Desktop - monitor OFF on stream
```