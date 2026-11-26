---
id: streaming-broadcast-workflow
title: "Streaming Preparation and Broadcast Assets"
domain: media
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
    version_notes: "Agent documents profiles, does not control live without approval"
inputs:
  - "Stream briefing (target platform, resolution, bitrate)"
  - "Medien-Assets (Overlays, Stinger, Pre-Roll)"
outputs:
  - "OBS profile checklist and normalized assets"
  - "Test-encode log"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Technically prepare livestream**: transcode assets, bring loudness and resolution to platform limits, provide **OBS checklist**—without rotating stream keys or taking channels live unprompted.

## When to use

- Webinar or Unternehmens-Livestream in 720p/1080p geplant.
- B-roll, stinger, and intro clips should have uniform specs.
- Agent should deliver FFmpeg test encodes and documentation for the operator.

**When not to use**

- 24/7 lineares Fernsehen with Ad-Server.
- DRM-protected playback.
- Unattended start of the livestream by the agent.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg / ffprobe | Asset-Normalisierung | yuv420p, AAC, keyframe spacing |
| OBS Studio | Live mix | De facto standard; human at go-live |
| ffplay | Quick test | Spot check before show |

## System prompt

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

## Workflow

1. Plattform-Spec-Tabelle from Briefing (1080p30, 4500–6000 kbps video typisch).
2. all Assets `ffprobe`; Interlace/Rotation flaggen.
3. `ffmpeg` Normalisierung after Spec in `stream_assets/`.
4. Stinger on 2 s Laenge trimmen; Audio fade out 100 ms.
5. Testpattern `bars.mp4` create.
6. OBS checklist as Markdown; operator review.
7. Optional local `-f null` encode test the longest loop source.

## Definition of done

- [ ] All assets match canvas fps and resolution
- [ ] Keyframe interval documented
- [ ] Audio peaks safe; no Clip on Stinger
- [ ] no Stream-Key im Log
- [ ] Operator checklist complete

## Security

- Stream-Keys and RTMP-URLs only in OBS lokal; nie in Repo.
- Go-live toggle by human only.
- Aufgezeichnete Streams: DSGVO at Chat-Overlays.

## Pitfalls

- Gemischte 25/30 fps Szenen → OBS judder.
- NVENC on server without GPU mentioned in the checklist.
- to hohe Bitrate → Plattform transcoded schlecht.
- Stinger stereo out of phase on Mono-Summe.
- Agent startet `ffmpeg -f flv rtmp://...` without approval—verbieten.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Intro 5 s on 1080p30 normalisieren.
- **Input:** `intro_4k.mov`, Canvas 1920×1080.
- **Prompt:**

```text
Transcode intro to 1080p30 h264, -g 60, aac 160k, loudnorm -16 LUFS; ffprobe after.
```

- **Expected result:**

```text
intro_norm.mp4: 1920x1080, 30 fps, h264, duration 5.00s
gop: 60 frames
```

### Example 2 (Example data (self-written))
- **Task:** OBS checklist YouTube 1080p.
- **Input:** no Keys; only Spec.
- **Prompt:**

```text
Markdown checklist: canvas, scaled output, encoder note, audio tracks; omit stream key.
```

- **Expected result:**

```markdown
- [ ] Base: 1920x1080
- [ ] Output: 1920x1080 @ 30 fps
- [ ] Encoder: x264 veryfast / NVENC if available
- [ ] Audio: Track1 Mic, Track2 Desktop - monitor OFF on stream
```