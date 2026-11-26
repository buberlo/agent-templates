---
id: audio-whisper-transcribe-diarize
title: "Transcription and Speaker Segments with Whisper"
domain: media
category: subtitles-translation
tags:
  - whisper
  - transcription
  - diarization
  - srt
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: Whisper
    install: "pip: openai-whisper; optional faster-whisper"
    version_notes: "large-v3-turbo; GPU empfohlen"
  - name: pyannote.audio
    install: "pip: pyannote.audio (HF token for diarization)"
    version_notes: "only with explicit approval and token"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Audio extract, 16 kHz mono for ASR"
inputs:
  - "Audio- or Videodatei"
  - "Language(s) and desired format (SRT, VTT, JSON)"
  - "Optional: speaker count or diarization yes/no"
outputs:
  - "transcript with Timestamps"
  - "Optional: SRT with Sprecher-Praefixen"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Time-aligned transcripts** and optional **speaker segments** for subtitles, translation, and accessibility—locally with Whisper, diarization only with an approved setup.

## When to use

- Internes Training, Podcast or Webinar should untertitelt will.
- Rohmaterial liegt as MP4/MKV/WAV before; Genauigkeit wichtiger as Echtzeit.
- OpenClaw Whisper skill or CLI is available.

**When not to use**

- Broadcast subtitles with strict CEA-608/EBU timing requirements without a human QA reviewer.
- Content subject to law enforcement or attorney-client privilege without legal approval for ML processing.
- Pure translation from an already perfect SRT (use CAT workflow instead of re-ASR).

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg | 16 kHz mono WAV | Whisper-Inboundformat |
| Whisper | Wort-/Segment-Timestamps | Offline, mehrsprachig |
| pyannote | Sprecherlabels | Optional; HF-Token required |
| sed/python | SRT formatieren | Zeilenlaengen, CPS-Limits |

## System prompt

```text
You transcribe audio to timed text for subtitles using Whisper (or faster-whisper) and ffmpeg prep.

Inputs: media path, language code (de, en, auto), output format (srt, vtt, json), diarization (on/off), max chars per line for subs (default 42), reading speed check (optional).

Extract audio: ffmpeg -i input.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio.wav

Transcribe: whisper audio.wav --model large-v3-turbo --language de --output_format all --word_timestamps True
If faster-whisper: use vad_filter true for cleaner segments.

Diarization (only if enabled and HF token present):
- Run pyannote pipeline; merge speaker labels with whisper segment times by overlap.
- Prefix SRT lines with [SPEAKER_00] only if client asked; default use role names from user map.

Subtitle hygiene:
- Split lines >42 chars; min display 1.0s unless natural pause.
- Numbers and product names: flag low-confidence segments (avg_logprob) for human review.

No translation unless second step requested; do not send audio to third-party APIs without approval.

Deliver: srt path, json path, list of low-confidence intervals, and ffmpeg command used.

Strip leading/trailing silence in transcript export only when user requests cleaner SRT.
For code-switching (DE/EN), note language segments in JSON metadata.
When translating later, keep a glossary file of locked terms (product names).
```

## Workflow

1. `ffprobe input.mp4` — Audiospur and Dauer notieren.
2. `ffmpeg -i input.mp4 -vn -ac 1 -ar 16000 audio.wav`.
3. `whisper audio.wav --model large-v3-turbo --language de --output_dir work/`.
4. `audio.srt` on Zeilenlaenge verify; Skript `split_long_lines.py` optional.
5. For diarization: pyannote → `segments.json`; merge with Whisper segments.
6. `ffmpeg -i input.mp4 -i work/audio.srt -c copy -c:s srt -metadata:s:s:0 language=de out_soft.mkv` only after approval.
7. Spot check: verify 3 random intervals in the player against the text.

## Definition of done

- [ ] Timestamps monoton steigend; no Ueberlappung in SRT
- [ ] Sprache korrekt erkannt or explizit gesetzt
- [ ] Eigennamen/Fachbegriffe markiert, when unsicher
- [ ] Diarization only when requested and documented
- [ ] Quellaudio not in fremde Cloud hochgeladen

## Security

- Voice biometrics and personal content: approval and deletion deadline for `work/`.
- Do not commit HF tokens and API keys.
- Public YouTube subtitles: clarify copyright on the source video.

## Pitfalls

- Music under speech → phantom text; use VAD or manual skip.
- Diarization + Whisper offsets merged incorrectly → alternating wrong labels.
- 25 fps vs 30 fps video: SRT from audio often fits, but embedded VTT requires the same timebase.
- Grosse Modelle on CPU: Stunden Laufzeit—Batch nachts plan.
- Automatic translation without review violates brand tone of voice.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** DE-Subtitles for 8-min-Explainer.
- **Input:** `explainer.mp4`, Sprache Deutsch.
- **Prompt:**

```text
Extract audio, whisper large-v3-turbo DE, produce explainer.srt max 42 chars/line, flag low confidence.
```

- **Expected result:**

```text
1
00:00:00,000 --> 00:00:03,400
Today we show the new dashboard.

Low confidence: none above threshold
Duration coverage: 00:07:58.2 / 00:08:00.0
```

### Example 2 (Example data (self-written))
- **Task:** Two speakers, diarization off.
- **Input:** Interview WAV, transcript JSON only for translators.
- **Prompt:**

```text
Whisper JSON only, no diarization, include segment-level timestamps for CAT import.
```

- **Expected result:**

```json
{
  "segments": [
    { "start": 0.0, "end": 4.2, "text": "Guten Tag, willkommen." },
    { "start": 4.5, "end": 9.1, "text": "Thanks, great to be here." }
  ]
}
```