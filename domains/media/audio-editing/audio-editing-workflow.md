---
id: audio-editing-workflow
title: "Cut, normalize, and convert audio"
domain: media
category: audio-editing
tags:
  - audio
  - ffmpeg
  - normalize
target_agents:
  - hermes
  - generic
  - cursor
required_tools:
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "afilter, codec conversion"
  - name: Whisper Skill
    install: "ClawHub Openai Whisper optional"
    version_notes: "only for transcript after Audio-Prep"
inputs:
  - "Quellaudio (beliebiges Format)"
  - "Target (Format, loudness, Cut)"
outputs:
  - "Bearbeitete Audiodatei"
  - "Optional transcript"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

General **audio post-production** with FFmpeg: extract, cut, loudnorm, format conversion—optional handoff to Whisper for transcripts, no DAW required.

## When to use

- Sprachmemos, Sessions or Extrakte from Video sollen hoerbar and einheitlich will.
- Batch conversion WAV→FLAC/MP3 with identical parameters.
- Agent should command chain document.

**When not to use**

- MIDI/virtuelle Instrumente mixen.
- Autotune and Melodie-Korrektur on Takes.
- Surround-5.1-Mastering for Kino.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg | Cut, Filter, Encode | Ein Werkzeug for the meisten Jobs |
| ffprobe | Analyse | Codec, layout, duration |
| Whisper Skill | transcript | Optional zweiter step |

## System prompt

```text
You edit and convert audio using ffmpeg/ffprobe as the primary toolchain.

Inputs: source path, operations list (trim, denoise light, loudness target, format), output path, whether to preserve sample rate.

Probe first: ffprobe -show_streams -show_format.

Trim: use -ss after -i for sample-accurate on re-encode; -c copy only for simple container trims on codecs that support it.

Loudness: two-pass loudnorm for speech; state integrated LUFS and true peak in summary.

Convert: explicit codec (pcm_s16le wav, flac, libmp3lame q:a 2, aac b:a 192k).
Resample only when required; prefer aresample=resampler=soxr at 48k for video handoff.

Light denoise: afftdn nr<=15 for speech room tone; skip for music.

Extract from video: -vn -map 0:a:0.

After work, run volumedetect or loudnorm summary on output.

Optional whisper: only on user's request after final WAV exists.

No sending audio to unknown APIs. Document commands in order.

If multiple inputs differ in sample rate, resample to a single rate before concat.
Report input/output duration delta after trim; flag if >0.2 s unexplained.
For phone recordings, apply optional highpass at 80 Hz only when hum is reported.
Keep intermediate WAV until user confirms final codec; delete only after approval.
```

## Workflow

1. `ffprobe input` — channels, rate, duration.
2. from Video: `ffmpeg -i clip.mp4 -vn -map 0:a:0 -c:a pcm_s16le audio.wav`.
3. Cut: `ffmpeg -i audio.wav -ss 5 -to 120 -c copy trimmed.wav` or re-encode at MP3.
4. loudnorm two-pass on `trimmed.wav`.
5. Export MP3/FLAC je Briefing.
6. Optional Whisper on WAV.
7. Summary: Peak, LUFS, path.

## Definition of done

- [ ] Ausgabeformat and -rate wie spezifiziert
- [ ] no Clipping (true peak ≤ -1 dBTP when normalisiert)
- [ ] Cut an richtigen Zeitmarken ±0,1 s
- [ ] Command log complete

## Security

- Vertrauliche Gespraeche lokal halten; Cloud-Transcription only with approval.

## Pitfalls

- MP3-Cut with `-c copy` an Frame-Grenzen unsauber.
- Stereo to Mono without `-ac 1` kann Phasen-Mono-Effekt ignorieren—`-pan` only deliberately.
- loudnorm on Musik-Mix verfaelscht Dynamik.
- Multiple transcoding MP3→AAC→MP3: generation loss.
- Whisper on 8 kHz Telefon-Audio without Upsample.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Audio from Zoom-MP4, -24 LUFS rough normalisieren.
- **Input:** `meeting.mp4`, 62 min.
- **Prompt:**

```text
Extract audio to 48k wav, two-pass loudnorm -24 LUFS for archive, log commands.
```

- **Expected result:**

```bash
ffmpeg -i meeting.mp4 -vn -ar 48000 meeting.wav
# loudnorm two-pass → meeting_norm.wav, integrated ≈ -24 LUFS
```

### Example 2 (Example data (self-written))
- **Task:** 3 Voice-Memos to a FLAC.
- **Input:** `memo1.m4a`, `memo2.m4a`, `memo3.m4a`.
- **Prompt:**

```text
Concat to single FLAC 48k stereo; resample each input first.
```

- **Expected result:**

```
concat_list.txt → combined.flac
ffprobe: 1 stream, flac, 48000 Hz, stereo, duration sum ±0.1s
```