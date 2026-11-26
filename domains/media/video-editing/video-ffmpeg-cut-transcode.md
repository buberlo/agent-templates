---
id: video-ffmpeg-cut-transcode
title: "Cut, transcode, and subtitle video"
domain: media
category: video-editing
tags:
  - ffmpeg
  - transcode
  - subtitles
  - whisper
target_agents:
  - hermes
  - claude-code
  - cursor
  - generic
required_tools:
  - name: ffmpeg
    install: "OS package: ffmpeg (ffprobe included)"
    version_notes: "FFmpeg 6.x/7.x; libx264 and AAC available"
  - name: ffprobe
    install: "Part of the ffmpeg-Pakets"
    version_notes: "JSON output for automation"
  - name: whisper
    install: "pip: openai-whisper or whisper.cpp CLI"
    version_notes: "large-v3-turbo for DE/EN; GPU optional"
inputs:
  - "Quellvideo (MP4, MOV, MKV)"
  - "Cutfenster (IN/OUT or -ss/-to)"
  - "Target profile (resolution, codec, container)"
  - "Optional: Subtitles (ASR or lieferbare SRT)"
outputs:
  - "Fertiges MP4 with web-tauglichem Profil"
  - "Optional: SRT/VTT and Befehlsprotokoll"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

This template guides agents through **cut**, **transcode**, and optional **subtitle generation** from raw footage—without an NLE, using reproducible FFmpeg commands and traceable quality checks.

## When to use

- Client provides one or a few files; delivery should be a uniform H.264/AAC MP4 plus optional subtitles.
- Cut is linear (ein IN/OUT-Block or wenige Segmente); no Multicam-Sync.
- Agent has Shell-Zugriff on `ffmpeg`/`ffprobe` (no dediziertes Video-MCP required).

**When not to use**

- Color Grading, komplexes Compositing or Frame-genaue Fusion mehrerer Kameras.
- DRM-protected sources or broadcast mezzanines with strict in-house standards without an approved profile.
- Editing into social reels with platform API upload (use dedicated publishing templates for this).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffprobe | Metadaten, Dauer, Codecs | Entscheidung copy vs. re-encode before the Cut |
| ffmpeg | Cut, Skalierung, Encode, mux | De-facto-Standard, scriptbar |
| Whisper | ASR → SRT | Offline-faehig for DE/EN; only at approval |
| sed/awk | SRT-Zeitkorrektur | Kleine Offsets without Re-Encode |

## System prompt

```text
You are a video operations engineer working only via ffmpeg/ffprobe unless the user names another NLE.

Inputs: source path(s), cut window(s), target profile (resolution, fps if fixed, max height, audio layout), subtitle mode (none | soft SRT | burn-in with approval).

Before any destructive step:
- Run ffprobe -v quiet -print_format json -show_format -show_streams on every input.
- Confirm duration, video codec, pixel format, audio sample rate, and rotation metadata.
- If cut end exceeds duration, stop and ask; never guess.

Cut strategy:
- Prefer -ss after -i for frame-accurate re-encode segments; use stream copy (-c copy) only when container, codecs, and timestamps are already deliverable-safe.
- For web: H.264 (libx264 or h264_videotoolbox on Mac), yuv420p, AAC stereo 48 kHz, -movflags +faststart.

Scale: use scale=-2:HEIGHT to keep even dimensions. Preserve SAR/DAR; do not upscale beyond source unless requested.

Subtitles:
- Generate SRT via Whisper only with explicit user consent for voice content.
- Default: soft subtitles (mov_text or separate .srt/.vtt). Burn-in requires written approval (irreversible).

Document every command in order. After encode, ffprobe the output and compare duration to expected (tolerance ±0.5 s).

Output to the user: final paths, probe summary (resolution, bitrate, duration), and any manual QC notes.

Never upload to third-party hosts or publish URLs without approval.
```

## Workflow

1. `ffprobe -v quiet -print_format json -show_format -show_streams input.mov` auswerten; Cutfenster against Dauer verify.
2. Rohschnitt: `ffmpeg -i input.mov -ss 00:01:12.000 -to 00:04:05.000 -c copy cut.mkv` only when Codec/Container passen; sonst Re-Encode-Zweig.
3. Transcode: `ffmpeg -i cut.mkv -vf scale=-2:1080 -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k -movflags +faststart deliver.mp4`.
4. Optional Whisper: `whisper deliver.mp4 --language de --output_format srt --output_dir ./subs/`.
5. Derive VTT from SRT or run `ffmpeg -i deliver.mp4 -i subs.srt -c copy -c:s mov_text deliver_subs.mp4` after approval for softsubs.
6. QA: `ffprobe deliver.mp4`, spot check with `ffplay` or frame grab `ffmpeg -ss 30 -i deliver.mp4 -frames:v 1 qa.jpg`.

## Definition of done

- [ ] Ausgabedauer weicht hoechstens ±0,5 s vom Cutfenster ab
- [ ] Video `yuv420p`, Audio without Clipping; `-movflags +faststart` gesetzt
- [ ] No visible A/V drift in spot checks
- [ ] Subtitles temporally plausible (if generated); proper nouns spot-checked
- [ ] All FFmpeg commands documented in thread or log

## Security

- No uploads to cloud transcoders or video hosting without client approval.
- Transcribe meeting audio, faces, and voices only with GDPR/confidentiality approval.
- Hard-burned subtitles and irreversible deletes only after explicit confirmation.

## Pitfalls

- `-c copy` at Cuten on not-Keyframe-nahen `-ss`-valuesn erzeugt schwarze Frames or Audio-Vorspann—at Unsicherheit re-encoden.
- `-ss` before `-i` is schneller, aber ungenauer; for deliveryen with Frame-Toleranz `<1s` `-ss` after `-i` nutzen.
- Vertikale iPhone-Movies: Rotation-Metadaten vs. tatsaechliche Pixel—`ffprobe` and Testframe verify.
- `loudnorm` zweimal anwenden or on bereits limitiertes Material—Pumping and Verzerrung.
- Whisper hallucinates during music and overlapping speech—manually spot-check SRT against audio.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Firmen-Interview from 4K-MOV on 1080p-Web-MP4 kuerzen.
- **Input:** `interview.mov` (3840×2160, 12:40), Cut `00:00:45`–`00:08:20`, Target 1080p H.264.
- **Prompt:**

```text
Probe interview.mov, cut 45s–8m20s, transcode to 1080p H.264 AAC with faststart. No subtitles. Document commands.
```

- **Expected result:**

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 interview.mov
# → 760.0
ffmpeg -i interview.mov -ss 00:00:45 -to 00:08:20 -vf scale=-2:1080 -c:v libx264 -crf 21 -c:a aac -b:a 160k -movflags +faststart interview_1080p.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 interview_1080p.mp4
# → 455.2
```

### Example 2 (Example data (self-written))
- **Task:** Soft-Subtitles for internes Training (only Intranet).
- **Input:** `training.mp4` (720p), approval for Whisper DE.
- **Prompt:**

```text
Transcribe training.mp4 to German SRT with Whisper, fix obvious proper nouns, mux as soft subtitle track mov_text. No burn-in.
```

- **Expected result:**

```text
1
00:00:01,200 --> 00:00:04,800
Welcome to onboarding module three.

Output: training_de.srt, training_subs.mp4 (video copy + mov_text), ffprobe lists Stream #0:2 subtitle.
```